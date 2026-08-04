# Power Platform: DEV- und PROD-Umgebung mit Entra-ID-Gruppen einrichten

**Ziel dieses Dokuments:** Ende-zu-Ende-Anleitung, um zwei Power-Platform-Umgebungen (**DEV** und **PROD**) sauber und governance-konform aufzusetzen — von der Microsoft-Entra-ID-Sicherheitsgruppe bis zur konkreten Rollenzuweisung im Power Platform Admin Center.

> **Annahmen dieses Dokuments** (bitte gegenprüfen, ob das zu eurem Setup passt):
> 1. Beide Umgebungen werden **mit Dataverse-Datenbank** angelegt (empfohlener Standardweg von Microsoft für eine echte DEV/PROD-Trennung mit sauberem Rollenmodell; ermöglicht später auch Power Apps, Managed Environments, Solutions/ALM).
> 2. Der Fokus liegt bewusst auf **Umgebungen + Entra-Gruppen + Rollenzuweisung**. Data-Loss-Prevention-Richtlinien (DLP) und Managed Environments sind bewusst **nicht** Teil dieser Anleitung (siehe Abschnitt 11 „Was dieser Guide bewusst nicht abdeckt").
> 3. Alle Namen (Umgebungen, Gruppen, Teams) sind **Platzhalter** im Schema `PP-…` / `Contoso – …` — bitte per Suchen-und-Ersetzen an eure Unternehmens-Namenskonvention anpassen.
>
> **Quellenlage:** Die lokal abgelegte Power-Automate-Dokumentation ([power-automate.md](power-automate.md), durchsucht über [search_docs.py](search_docs.py)) liefert das Governance-*Konzept* (Umgebungsrollen, Sicherheitsgruppen, Makers-vs-Runners-Modell). Die konkreten, aktuellen Klickpfade im Power Platform Admin Center und im Microsoft-Entra-Admin-Center stammen aus den unten verlinkten Microsoft-Learn-Quellen (Stand der Recherche: **04.08.2026**) — vor dem produktiven Einsatz kurz prüfen, ob sich UI-Bezeichnungen zwischenzeitlich geändert haben.

---

## 1. Zielbild auf einen Blick

Am Ende dieser Anleitung existieren:

| Baustein | Anzahl | Zweck |
|---|---|---|
| **Power-Platform-Umgebung DEV** | 1 (Typ *Sandbox*, mit Dataverse) | Entwicklungs-/Testumgebung, nur für Admins zugänglich |
| **Power-Platform-Umgebung PROD** | 1 (Typ *Production*, mit Dataverse) | Produktivumgebung, für Admins **und** Anwender:innen zugänglich |
| **Entra-ID-Sicherheitsgruppe `PP-Admins-AllEnv`** | 1 | Enthält alle Power-Platform-Admins → Nutzungs- **und** Adminrechte in **DEV und PROD** |
| **Entra-ID-Sicherheitsgruppe `PP-Users-PROD`** | 1 | Enthält alle reinen Anwender:innen → **nur Nutzungsrechte in PROD**, kein Zugriff auf DEV |
| **Entra-ID-„Gate"-Gruppe `PP-EnvAccess-PROD`** | 1 | Technische Sammelgruppe, die `PP-Admins-AllEnv` und `PP-Users-PROD` verschachtelt und als Zugriffs-Torwächter der PROD-Umgebung dient (Begründung siehe Abschnitt 3.3) |
| **Dataverse-Gruppenteams (Group Teams)** | 3 | Verknüpfen die Entra-Gruppen mit den passenden Dataverse-Sicherheitsrollen je Umgebung |

**Rollen-Matrix (Ergebnis):**

| Gruppe | DEV-Zugriff | DEV-Rolle | PROD-Zugriff | PROD-Rolle |
|---|---|---|---|---|
| `PP-Admins-AllEnv` | ✅ Ja | **System Administrator** (voller Admin- und Nutzungszugriff) | ✅ Ja | **System Administrator** (voller Admin- und Nutzungszugriff) |
| `PP-Users-PROD` | ❌ Nein | – | ✅ Ja | **Basic User** (reine Nutzung: Flows/Apps ausführen, keine Design-/Adminrechte) |

Das Bindeglied zwischen „wer darf überhaupt in die Umgebung" (Sicherheitsgruppe der Umgebung) und „was darf die Person dort tun" (Dataverse-Sicherheitsrolle) sind die **Dataverse-Gruppenteams** — dazu mehr in Abschnitt 8.

---

## 2. Voraussetzungen

### 2.1 Berechtigungen, die ausführende Person(en) benötigen

| Aufgabe | Benötigte Rolle |
|---|---|
| Entra-ID-Sicherheitsgruppen anlegen/bearbeiten | Mind. **Groups Administrator** oder **User Administrator** in Microsoft Entra ID (Global Administrator geht auch) |
| Power-Platform-Umgebungen anlegen, Sicherheitsgruppe zuweisen | **Power Platform Administrator**, **Dynamics 365 Administrator** oder **Global Administrator** (Entra-Rolle) |
| Dataverse-Gruppenteams anlegen, Sicherheitsrollen zuweisen | **System Administrator** in der jeweiligen Umgebung |

> **Wichtig zur Selbstberechtigung:** Verlasst euch **nicht** darauf, dass die Person, die eine Umgebung anlegt, automatisch als System Administrator in dieser Umgebung eingetragen wird — Microsoft hat die automatische Rollenvergabe an Tenant-Admins zuletzt bewusst eingeschränkt (*„Previously, Microsoft Entra ID admins … were automatically assigned the System Administrator role in Dataverse. This is no longer the case."*, [Assign security roles](https://learn.microsoft.com/en-us/power-platform/admin/assign-security-roles)). Prüft nach dem Anlegen jeder Umgebung explizit unter **Settings → Users + permissions → Users**, ob eure ausführende Person bereits die Rolle *System Administrator* hat; falls nicht, kann sich eine Person mit der tenant-weiten Rolle **Power Platform Administrator** selbst die Rolle zuweisen (bzw. ein:e bestehende:r System Administrator vergibt sie manuell).
>
> Die tenant-weiten Entra-Rollen **Global Administrator**, **Power Platform Administrator** und **Dynamics 365 Administrator** müssen laut Microsoft-Doku *direkt* an einzelne Benutzer:innen vergeben werden — **nicht** über eine Sicherheitsgruppe. Das betrifft nur diese drei tenant-weiten Admin-Rollen, nicht die umgebungsbezogene Dataverse-Rolle *System Administrator*, die wir weiter unten sehr wohl per Gruppe vergeben. Mehr dazu in Abschnitt 9 (optional).

### 2.2 Lizenzierung (kurzer Überblick, keine Tiefenprüfung)

Damit Mitglieder einer Sicherheitsgruppe überhaupt als Benutzer:in in einer Dataverse-gesicherten Umgebung angelegt werden, brauchen sie eine passende Lizenz:

> *„If a security group is associated with an environment, only users with Dataverse licenses or per app plan that are members of the environment security group are created as users in the environment."* — [Control user access to environments](https://learn.microsoft.com/en-us/power-platform/admin/control-user-access)

- **Admins (`PP-Admins-AllEnv`):** benötigen eine Lizenz mit Dataverse-Zugriff, üblicherweise **Power Apps per user plan** oder **Power Automate per user plan** (oder eine Dynamics-365-Lizenz).
- **Anwender:innen (`PP-Users-PROD`):** je nachdem, was sie nutzen sollen, reicht ggf. die in Microsoft 365 „seeded" enthaltene Power-Automate-Berechtigung für Standard-Konnektoren; für Dataverse-/App-Zugriff braucht es mindestens einen **Power Apps per-app plan** (pro Umgebung zubuchbar) oder eine entsprechende per-user-Lizenz.

> Lizenzprüfung/-zuweisung erfolgt im [Microsoft 365 Admin Center](https://admin.microsoft.com) unter **Benutzer → Aktive Benutzer**. Diese Anleitung geht davon aus, dass Lizenzen bereits vorhanden sind bzw. parallel beschafft werden — Details zur Lizenzmodell-Auswahl sind bewusst nicht Teil dieses Dokuments.

### 2.3 Kapazität

Für jede Umgebung mit Dataverse-Datenbank wird mind. **1 GB freie Dataverse-Datenbankkapazität** benötigt (für DEV + PROD zusammen also mind. 2 GB im Tenant verfügbar).

### 2.4 Namenskonventionen dieser Anleitung (bitte anpassen)

| Platzhalter | Bedeutung | Beispiel-Ersetzung |
|---|---|---|
| `Contoso – Power Platform (DEV)` | Name der DEV-Umgebung | `Musterfirma GmbH – Power Platform (DEV)` |
| `Contoso – Power Platform (PROD)` | Name der PROD-Umgebung | `Musterfirma GmbH – Power Platform (PROD)` |
| `PP-Admins-AllEnv` | Entra-Gruppe für Admins | `SG-PowerPlatform-Admins` |
| `PP-Users-PROD` | Entra-Gruppe für PROD-Anwender:innen | `SG-PowerPlatform-Users-Prod` |
| `PP-EnvAccess-PROD` | Technische Gate-Gruppe für PROD | `SG-PowerPlatform-EnvAccess-Prod` |
| `GT-DEV-Admins`, `GT-PROD-Admins`, `GT-PROD-Users` | Namen der Dataverse-Gruppenteams | frei wählbar, siehe Abschnitt 8 |

---

## 3. Schritt 1 — Microsoft-Entra-ID-Sicherheitsgruppen anlegen

Wir legen **drei** Sicherheitsgruppen an: die zwei fachlichen Gruppen (Admins, PROD-Anwender:innen) sowie eine technische „Gate"-Gruppe, die beide für den Zugriff auf PROD verschachtelt (Begründung in 3.3).

### 3.1 Gruppe `PP-Admins-AllEnv` anlegen

1. Im [Microsoft Entra Admin Center](https://entra.microsoft.com) anmelden (mind. Rolle **Groups Administrator**).
2. Navigieren zu **Entra ID → Groups → All groups**.
3. **+ New group** wählen.
4. Felder ausfüllen:
   - **Group type:** `Security`
   - **Group name:** `PP-Admins-AllEnv`
   - **Group description:** z. B. „Power-Platform-Admins mit Nutzungs- und Verwaltungsrechten in DEV und PROD"
   - **Membership type:** `Assigned` (empfohlen — feste, bewusst gepflegte Mitgliederliste statt dynamischer Regel, da diese Gruppe sicherheitskritisch ist)
   - **Owners:** mind. eine verantwortliche Person (z. B. CoE-/IT-Verantwortliche:r) hinterlegen
   - **Members:** alle Personen, die volle Admin-Rechte in DEV und PROD erhalten sollen, direkt hinzufügen
5. **Create** klicken.

### 3.2 Gruppe `PP-Users-PROD` anlegen

Gleiches Vorgehen wie 3.1, mit:
- **Group name:** `PP-Users-PROD`
- **Group description:** z. B. „Reine Anwender:innen mit Nutzungsrechten ausschließlich in der PROD-Umgebung"
- **Membership type:** `Assigned`
- **Members:** alle Personen, die Flows/Apps in PROD nur *ausführen*, aber nicht bauen oder administrieren sollen

### 3.3 Gruppe `PP-EnvAccess-PROD` anlegen — und warum sie nötig ist

Im Power Platform Admin Center kann pro Umgebung **genau eine** Sicherheitsgruppe als Zugriffs-„Torwächter" hinterlegt werden. Da PROD aber **zwei** unterschiedliche Zielgruppen (Admins *und* Anwender:innen) bedienen soll, brauchen wir eine übergeordnete Gruppe, die beide fachlichen Gruppen als **verschachtelte Mitglieder (nested groups)** enthält. Das ist ein offiziell dokumentiertes Muster:

> *„You create a security group in Microsoft Entra ID … You then add this security group as a child of the environment security group, create a Dataverse group team, and assign a security role to the group team. Your managers can now access Dataverse immediately."* — [Control user access to environments](https://learn.microsoft.com/en-us/power-platform/admin/control-user-access)

Für **DEV** brauchen wir das nicht: Dort ist die einzige Zielgruppe `PP-Admins-AllEnv`, die kann direkt als Umgebungs-Sicherheitsgruppe hinterlegt werden (siehe Schritt 3 der Umgebungserstellung in Abschnitt 5).

**Vorgehen:**

1. Gruppe wie in 3.1 anlegen:
   - **Group type:** `Security`
   - **Group name:** `PP-EnvAccess-PROD`
   - **Group description:** „Technische Zugriffsgruppe der PROD-Umgebung — verschachtelt Admins und PROD-Anwender:innen"
   - **Membership type:** `Assigned`
   - Keine direkten Members hinzufügen — diese Gruppe bezieht ihre „Mitglieder" ausschließlich über die zwei verschachtelten Gruppen.
2. `PP-Admins-AllEnv` als Mitglied von `PP-EnvAccess-PROD` verschachteln:
   1. In **Entra ID → Groups → All groups** die Gruppe **`PP-Admins-AllEnv`** öffnen (nicht die Gate-Gruppe — die Verschachtelung wird von der *Kind*-Gruppe aus angelegt).
   2. Im Seitenmenü **Group memberships** wählen.
   3. **+ Add memberships** wählen.
   4. Nach `PP-EnvAccess-PROD` suchen, auswählen, **Select** klicken.
3. Gleiches für `PP-Users-PROD` wiederholen: `PP-Users-PROD` öffnen → **Group memberships** → **+ Add memberships** → `PP-EnvAccess-PROD` auswählen.

Ergebnis: `PP-EnvAccess-PROD` enthält jetzt (indirekt, über Verschachtelung) alle Admins und alle PROD-Anwender:innen — das ist die Gruppe, die wir gleich als Sicherheitsgruppe der PROD-Umgebung hinterlegen.

> **Hinweis zu verschachtelten Gruppen:** Mitglieder einer verschachtelten Gruppe werden **nicht automatisch vorab** in die Umgebung provisioniert. Sie werden erst zur Umgebung hinzugefügt, sobald (a) ein passendes Dataverse-Gruppenteam für die verschachtelte Gruppe existiert (siehe Schritt 8) und/oder (b) das Mitglied sich zum ersten Mal in der Umgebung anmeldet. Das ist gewolltes Verhalten und kein Fehler.
>
> **Wichtige Einschränkung:** Nicht unterstützt werden u. a. das Verschachteln von Gruppen, die mit lokalem Active Directory synchronisiert sind, sowie das Mischen von Sicherheits- und Microsoft-365-Gruppentypen beim Verschachteln. Reine, cloud-native Security-Gruppen (wie hier verwendet) funktionieren problemlos.

---

## 4. Architekturüberblick (Gruppen-Verschachtelung PROD)

```
PP-EnvAccess-PROD   ← als "Sicherheitsgruppe" an der PROD-Umgebung hinterlegt
 ├── PP-Admins-AllEnv     (verschachtelt)  → Rolle in PROD: System Administrator
 └── PP-Users-PROD        (verschachtelt)  → Rolle in PROD: Basic User

PP-Admins-AllEnv     ← als "Sicherheitsgruppe" DIREKT an der DEV-Umgebung hinterlegt
                                            → Rolle in DEV: System Administrator
```

---

## 5. Schritt 2 — DEV-Umgebung anlegen

1. Im [Power Platform Admin Center](https://admin.powerplatform.microsoft.com) anmelden (als Power Platform Administrator, Dynamics 365 Administrator oder Global Administrator).
2. Im Navigationsbereich **Manage** wählen, dann im **Manage**-Bereich **Environments**.
3. Auf der **Environments**-Seite in der Befehlsleiste **New** wählen.
4. Erste Seite ausfüllen:

   | Feld | Wert für DEV |
   |---|---|
   | Name | `Contoso – Power Platform (DEV)` |
   | Region | passende Region eures Tenants |
   | Get new features early | nach Präferenz (für DEV oft sinnvoll: `Yes`, um neue Features früh zu testen) |
   | Type | **Sandbox** (empfohlen für DEV — nichtproduktive Umgebungen mit Reset- und Copy-Funktion, getrennt von der Produktivumgebung; Backup/Restore steht in beiden Typen zur Verfügung, i. d. R. mit kürzerer Aufbewahrung als bei Production) |
   | Purpose | z. B. „Entwicklungs- und Testumgebung für Power-Automate-/Power-Apps-Lösungen" |
   | Add a Dataverse data store | **Yes** (diese Einstellung ist unumkehrbar) |
   | Pay-as-you-go with Azure | nur falls ihr Pay-as-you-go nutzt, sonst `No` |

5. **Next** klicken.
6. Zweite Seite ausfüllen:

   | Feld | Wert für DEV |
   |---|---|
   | Language | Standardsprache der Umgebung |
   | URL | z. B. `contoso-dev` (muss tenant-weit eindeutig sein) |
   | Currency | Basiswährung für Reporting |
   | Enable Dynamics 365 apps | i. d. R. `No`, außer ihr braucht explizit Dynamics-365-Apps (ebenfalls unumkehrbar) |
   | Deploy sample apps and data | optional, für DEV ggf. hilfreich zum Ausprobieren |
   | **Security group** | **`PP-Admins-AllEnv`** auswählen (nur Admins sollen DEV überhaupt sehen können) |

7. **Save** klicken.

> **Hinweis:** Das Feld *Security group* ist in aktuellen Admin-Center-Versionen ein Pflichtfeld geworden. Solltet ihr bewusst offenen Zugriff wollen, wählt explizit `None` — für DEV empfehlen wir aber ausdrücklich die Einschränkung auf `PP-Admins-AllEnv`.

---

## 6. Schritt 3 — PROD-Umgebung anlegen

Gleiches Vorgehen wie in Abschnitt 5, mit folgenden Abweichungen:

| Feld | Wert für PROD |
|---|---|
| Name | `Contoso – Power Platform (PROD)` |
| Type | **Production** |
| Purpose | z. B. „Produktivumgebung für unternehmensweit genutzte Flows und Apps" |
| Get new features early | i. d. R. `No` (Produktivumgebungen bekommen Updates erst nach dem regulären Rollout-Zyklus — mehr Stabilität) |
| **Security group** | **`PP-EnvAccess-PROD`** auswählen (die Gate-Gruppe aus Abschnitt 3.3, die Admins und PROD-Anwender:innen verschachtelt) |

Alle übrigen Felder analog zu DEV befüllen (Dataverse: **Yes**, Dynamics-365-Apps i. d. R. **No**, ggf. keine Beispiel-Apps/-Daten in PROD).

---

## 7. Nachbereitung an der Umgebungsliste prüfen

Nach dem Speichern beider Umgebungen solltet ihr in **Environments** zwei neue Einträge sehen (Status kann kurz „Provisioning" anzeigen, bis Dataverse fertig eingerichtet ist — das dauert üblicherweise wenige Minuten). Öffnet zur Kontrolle jede Umgebung → **Edit** → prüft, dass unter **Security group** die korrekte Gruppe hinterlegt ist (`PP-Admins-AllEnv` bei DEV, `PP-EnvAccess-PROD` bei PROD).

---

## 8. Schritt 4 — Rollen zuweisen über Dataverse-Gruppenteams (Group Teams)

Die Sicherheitsgruppe an der Umgebung entscheidet nur, **wer überhaupt hinein darf**. **Was** die Person dort tun darf, wird über eine **Dataverse-Sicherheitsrolle** gesteuert. Der skalierbare, empfohlene Weg, eine Rolle an *alle Mitglieder einer Entra-Gruppe* zu vergeben (statt Person für Person), ist ein **Dataverse-Gruppenteam (Group Team)**:

> *„Using groups lets administrators assign a security role with its respective privileges to all the members of the group, instead of having to provide the access rights to an individual team member."* — [Manage group teams](https://learn.microsoft.com/en-us/power-platform/admin/manage-group-teams)

Wir legen **drei Gruppenteams** an — eines pro Zeile der Rollen-Matrix aus Abschnitt 1.

### 8.1 Vorbereitung: ObjectID der Entra-Gruppen notieren

Für jede der drei Entra-Gruppen (`PP-Admins-AllEnv`, `PP-Users-PROD`, `PP-EnvAccess-PROD` wird hier nicht gebraucht) im [Azure Portal](https://portal.azure.com) bzw. Entra Admin Center die **Object ID** notieren (Gruppe öffnen → **Overview** → Object ID kopieren). Das erleichtert die eindeutige Auswahl im nächsten Schritt.

### 8.2 Gruppenteam `GT-DEV-Admins` in der DEV-Umgebung anlegen

1. [Power Platform Admin Center](https://admin.powerplatform.microsoft.com) → **Manage** → **Environments** → Umgebung **`Contoso – Power Platform (DEV)`** auswählen.
2. **Settings** → **Users + permissions** → **Teams**.
3. **+ Create team** wählen.
4. Felder ausfüllen:
   - **Team name:** `GT-DEV-Admins`
   - **Description:** „Verknüpft Entra-Gruppe PP-Admins-AllEnv mit der Rolle System Administrator in DEV"
   - **Business unit:** Standard-Business-Unit (Root) auswählen, sofern keine eigene BU-Struktur existiert
   - **Administrator:** verantwortliche Person eintragen
   - **Team type:** **Microsoft Entra Security group**
   - **Group name:** `PP-Admins-AllEnv` auswählen
   - **Membership type:** **Members** (bezieht sich auf die regulären Mitglieder der Entra-Gruppe, siehe Tabelle unten)
5. Team speichern.
6. Neu angelegtes Team auswählen (Checkbox) → **Manage security roles** → Rolle **System Administrator** auswählen → **Save**.

> **Membership-Type-Optionen** (Auszug aus [Manage group teams](https://learn.microsoft.com/en-us/power-platform/admin/manage-group-teams)):
>
> | Dataverse-Gruppenteam-Mitgliedstyp | Ergebnis |
> |---|---|
> | **Members** | Nur reguläre Mitglieder (keine Gäste) der Entra-Gruppe |
> | **Members and guests** | Reguläre Mitglieder + Gastnutzer:innen der Entra-Gruppe |
> | **Owners** | Nur die Owner der Entra-Gruppe |
> | **Guests** | Nur Gastnutzer:innen der Entra-Gruppe |
>
> Für unsere internen Admin-/Anwender:innen-Gruppen ist **Members** in der Regel die richtige Wahl.

### 8.3 Gruppenteam `GT-PROD-Admins` in der PROD-Umgebung anlegen

Gleiches Vorgehen wie 8.2, aber in der Umgebung **`Contoso – Power Platform (PROD)`**:
- **Team name:** `GT-PROD-Admins`
- **Team type:** Microsoft Entra Security group
- **Group name:** `PP-Admins-AllEnv`
- **Membership type:** Members
- Zugewiesene Sicherheitsrolle: **System Administrator**

### 8.4 Gruppenteam `GT-PROD-Users` in der PROD-Umgebung anlegen

Gleiches Vorgehen, ebenfalls in **`Contoso – Power Platform (PROD)`**:
- **Team name:** `GT-PROD-Users`
- **Team type:** Microsoft Entra Security group
- **Group name:** `PP-Users-PROD`
- **Membership type:** Members
- Zugewiesene Sicherheitsrolle: **Basic User** (teils noch als „Common Data Service User" bezeichnet — reine Nutzungsrechte: Apps/Flows ausführen, keine Design- oder Adminrechte)

> **Wichtiger Hinweis zur Verschachtelung:** Damit Mitglieder eines Gruppenteams tatsächlich Zugriff auf die Umgebung erhalten, muss die zugehörige Entra-Gruppe (direkt oder verschachtelt) Mitglied der an der Umgebung hinterlegten Sicherheitsgruppe sein:
> *„If your environment has a security group, you need to add the group team's Microsoft Entra group as a member of that security group in order for the group team's users to be able to access the environment."* — [Manage group teams](https://learn.microsoft.com/en-us/power-platform/admin/manage-group-teams)
>
> Das haben wir in Abschnitt 3.3 bereits erledigt (`PP-Admins-AllEnv` und `PP-Users-PROD` sind Mitglieder von `PP-EnvAccess-PROD`, welche wiederum als Sicherheitsgruppe an PROD hängt). Bei DEV ist die Bedingung trivial erfüllt, da `PP-Admins-AllEnv` selbst direkt die Sicherheitsgruppe der Umgebung ist.

### 8.5 Warum genügt „System Administrator" für „Nutzungs- und Adminrechte"?

Die Dataverse-Rolle **System Administrator** ist die höchste vordefinierte Sicherheitsrolle und umfasst **alle** Privilegien — inklusive aller Nutzungsrechte, die auch die Rolle *Basic User* hätte, plus vollständiger Verwaltungsrechte (Sicherheitsrollen vergeben, Umgebungseinstellungen ändern, alle Datensätze sehen/bearbeiten, Solutions importieren, etc.). Eine separate Zuweisung von *Basic User* zusätzlich zu *System Administrator* ist daher nicht nötig.

---

## 9. (Optional) Tenant-weite Power-Platform-Admin-Rechte für die Admin-Gruppe

Was wir bisher eingerichtet haben, gibt der Admins-Gruppe **volle Kontrolle innerhalb von DEV und PROD** (Dataverse-Rolle *System Administrator*, zugewiesen über die Gruppenteams aus Schritt 8). Das ist eine bewusst andere, engere Berechtigungsebene als die tenant-weite Entra-Rolle **Power Platform Administrator**, die zusätzlich erlaubt:

- neue Umgebungen im gesamten Tenant anzulegen, zu löschen, zu sichern/wiederherzustellen oder zu kopieren,
- tenant-weite und umgebungsbezogene Daten-/DLP-Richtlinien zu verwalten,
- **jede** Umgebung im Tenant zu verwalten — Power-Platform-Administrator:innen sind laut Microsoft von der Sicherheitsgruppen-Einschränkung einer Umgebung ausdrücklich **nicht betroffen** und können Umgebungen auch verwalten, ohne Mitglied der jeweiligen Sicherheitsgruppe zu sein.

Diese drei tenant-weiten Rollen (**Global Administrator**, **Power Platform Administrator**, **Dynamics 365 Administrator**) unterscheiden sich technisch von der umgebungsbezogenen Dataverse-Rolle *System Administrator* aus Schritt 8 und müssen laut Microsoft **zwingend direkt an einzelne Benutzerkonten** vergeben werden — eine Vergabe über eine Sicherheitsgruppe wird nicht unterstützt:

> *„Global admin, Power Platform admin, and the Dynamics 365 admin roles must be directly assigned for a user. Role association through security groups is not supported."* — [Use service admin roles to manage your tenant](https://learn.microsoft.com/en-us/power-platform/admin/use-service-admin-role-manage-tenant)

**Wichtige Ergänzung, die leicht übersehen wird:** Das Zuweisen einer dieser drei tenant-weiten Rollen ersetzt **nicht** die Dataverse-Rolle *System Administrator* aus Schritt 8. Beide Ebenen sind unabhängig voneinander:

> *„When the Dynamics 365 administrator, Power Platform administrator, or Global administrator role is assigned to a user in Microsoft Entra ID, the user is no longer automatically assigned to the system administrator role in environments."* — [Use service admin roles to manage your tenant](https://learn.microsoft.com/en-us/power-platform/admin/use-service-admin-role-manage-tenant)

Mit anderen Worten: Auch wenn ihr diesen optionalen Schritt zusätzlich ausführt, bleibt Schritt 8 (Gruppenteams mit Rolle *System Administrator* in DEV und PROD) die Grundlage dafür, dass eure Admins-Gruppe tatsächlich mit den Daten in beiden Umgebungen arbeiten kann.

**Vorgehen (dokumentierter Weg über das Microsoft 365 Admin Center):**

1. Im [Microsoft 365 Admin Center](https://admin.microsoft.com) anmelden (mind. Rolle **Privileged Role Administrator**).
2. **Users → Active users** öffnen, betreffende Person auswählen.
3. Unter **Account → Roles** auf **Manage roles** klicken.
4. **Show all by category** ausklappen.
5. Unter der Kategorie **Collaboration** die Rolle **Power Platform administrator** (oder **Dynamics 365 administrator**) auswählen.
6. **Save changes** klicken.

Dieser Vorgang muss für **jede einzelne Person** wiederholt werden, die diese tenant-weite Rolle erhalten soll — es gibt keinen Gruppen-Automatismus. Deshalb bleibt dieser Schritt bewusst optional und außerhalb des Kern-Setups.

---

## 10. Verifizierung / Testcheckliste

- [ ] Beide Umgebungen erscheinen im Power Platform Admin Center mit Status „Ready".
- [ ] `Contoso – Power Platform (DEV)` → **Edit** zeigt Sicherheitsgruppe `PP-Admins-AllEnv`.
- [ ] `Contoso – Power Platform (PROD)` → **Edit** zeigt Sicherheitsgruppe `PP-EnvAccess-PROD`.
- [ ] `PP-EnvAccess-PROD` enthält (unter **Group memberships**/Verschachtelung, geprüft über die beiden Kind-Gruppen) `PP-Admins-AllEnv` und `PP-Users-PROD`.
- [ ] In DEV existiert Team `GT-DEV-Admins` mit Rolle **System Administrator**.
- [ ] In PROD existieren Teams `GT-PROD-Admins` (Rolle **System Administrator**) und `GT-PROD-Users` (Rolle **Basic User**).
- [ ] Eine Testperson aus `PP-Admins-AllEnv` meldet sich in [make.powerautomate.com](https://make.powerautomate.com) an, wählt oben rechts **Environments** und sieht **beide** Umgebungen (DEV und PROD).
- [ ] Eine Testperson aus `PP-Users-PROD` meldet sich an und sieht **nur PROD** in der Umgebungsauswahl, nicht DEV.
- [ ] Eine Testperson aus `PP-Users-PROD` kann in PROD einen ihr freigegebenen Flow/eine App **ausführen**, aber **nicht** den Designer öffnen bzw. keine neue Ressource anlegen (kein Environment-Maker-Recht, nur Basic User).

> **Hinweis zur Wartezeit:** Neu hinzugefügte Gruppenmitglieder werden nicht zwingend sofort synchronisiert. Die tatsächliche Berechtigung eines Gruppenmitglieds wird beim jeweiligen Anmeldevorgang zur Laufzeit ausgewertet und laut Doku bis zu **8 Stunden** zwischengespeichert (Cache), bevor Änderungen an der Gruppenmitgliedschaft vollständig durchschlagen. Bei Tests also ggf. Neuanmeldung/etwas Wartezeit einplanen.

---

## 11. Was dieser Guide bewusst nicht abdeckt (Ausblick)

Für den vollständigen Governance-Ausbau nach diesem Kern-Setup, aber außerhalb des Umfangs dieser Anleitung:

- **Data-Loss-Prevention-(DLP)-Richtlinien** je Umgebung (z. B. PROD strenger als DEV klassifizieren, Business-/Non-Business-Konnektoren trennen).
- **Managed Environments** (erweiterte Governance-Features wie Sharing-Limits, Maker-Wellcome-Content, Solution-Checker-Enforcement — Voraussetzung: Umgebung mit Dataverse, was hier bereits erfüllt ist).
- **Solutions / ALM-Pipeline** DEV → PROD (Flows/Apps als Solution verpacken und zwischen den beiden hier angelegten Umgebungen automatisiert bewegen).
- **Business Units** innerhalb von Dataverse für feingranularere Datentrennung.

Diese Themen bauen direkt auf dem hier geschaffenen Fundament auf und lassen sich bei Bedarf in einem eigenen Folgedokument vertiefen.

> **Klarstellung zur bereits existierenden Default-Umgebung:** Jeder Tenant hat automatisch eine **Default-Umgebung**, die von allen lizenzierten Nutzer:innen gemeinsam verwendet wird. Diese Anleitung fasst die Default-Umgebung bewusst nicht an — sie bleibt von `PP-Admins-AllEnv`/`PP-Users-PROD` komplett unberührt. Das ist auch technisch gar nicht anders möglich: *„Security groups can't be assigned to default and developer environment types."* ([Control user access to environments](https://learn.microsoft.com/en-us/power-platform/admin/control-user-access)) Wer die Default-Umgebung zusätzlich absichern will (z. B. für Citizen-Development-Zwecke), braucht dafür einen separaten Ansatz — siehe [Secure the default environment](https://learn.microsoft.com/en-us/power-platform/guidance/adoption/secure-default-environment).

---

## 12. Quellen

**Microsoft Learn (aktuelle Admin-Center-Klickpfade, abgerufen 04.08.2026):**

- [Create and manage environments in the Power Platform admin center](https://learn.microsoft.com/en-us/power-platform/admin/create-environment)
- [Control user access to environments with security groups and licenses](https://learn.microsoft.com/en-us/power-platform/admin/control-user-access)
- [Manage group teams](https://learn.microsoft.com/en-us/power-platform/admin/manage-group-teams)
- [Assign security roles](https://learn.microsoft.com/en-us/power-platform/admin/assign-security-roles)
- [How to manage groups (Microsoft Entra)](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-manage-groups)
- [Power Platform environments overview](https://learn.microsoft.com/en-us/power-platform/admin/environments-overview)
- [Role-based security roles for Dataverse](https://learn.microsoft.com/en-us/power-platform/admin/database-security)
- [Use service admin roles to manage your tenant](https://learn.microsoft.com/en-us/power-platform/admin/use-service-admin-role-manage-tenant)
- [The admin center — Power Automate](https://learn.microsoft.com/en-us/power-automate/admin-center)

**Lokale Projektdokumentation (Governance-Konzepte):**

- [power-automate.md](power-automate.md) — Abschnitte „Manage permissions and roles in Power Automate environments" (Umgebungsrollen, Dataverse-Sicherheitsrollen, Flow-Sharing), „Use security roles and groups: Manage makers versus run-only users" (Makers-vs-Runners-Governance-Muster), durchsucht über [search_docs.py](search_docs.py).
- [Workshop-Agenda_Power-Automate-Einstieg.md](Workshop-Agenda_Power-Automate-Einstieg.md) — als Referenz für Grundbegriffe (Environment, Solution, DLP), falls Einsteiger:innen im Team diesen Guide lesen.

*Hinweis: Power Platform entwickelt sich fortlaufend weiter — vor einem produktiven Rollout kurz gegenprüfen, ob sich Feldnamen oder Klickpfade im Admin Center zwischenzeitlich geändert haben.*
