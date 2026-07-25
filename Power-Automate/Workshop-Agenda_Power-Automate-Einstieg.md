# Workshop: Einstieg in Microsoft Power Automate
### Citizen Developer Programm – 2-stündiger interaktiver Praxis-Workshop

**Zielgruppe:** Citizen Developer ohne oder mit sehr wenig Vorerfahrung in Power Automate bzw. Prozessautomatisierung.
**Format:** Präsenz/Remote, hoher Interaktionsanteil, Live-Demo + gemeinsamer Flow-Bau, laufende Fragerunde statt reinem Frontalvortrag.
**Gesamtdauer:** 120 Minuten (inkl. 1 Pause à 10 Min.)

> **Hinweis zur Nutzung dieses Dokuments:** Dies ist als **Skript** für den Vortrag gedacht – jeder Block enthält Talking Points (was wörtlich/sinngemäß gesagt werden kann), konkrete Klickpfade für die Live-Demo sowie Caveats/Zahlen direkt aus der Microsoft-Dokumentation. Wörtliche Zitate sind mit *„…"* gekennzeichnet und stammen aus der lokal abgelegten Volldokumentation ([power-automate.md](power-automate.md), ~97.800 Zeilen), durchsucht über [search_docs.py](search_docs.py).

---

## 1. Lernziele

Am Ende des Workshops können die Teilnehmenden:

1. Die Grundbegriffe von Power Automate (Trigger, Aktion, Konnektor, Cloud Flow) erklären und voneinander abgrenzen.
2. Die drei Cloud-Flow-Typen (Automated, Instant, Scheduled) unterscheiden und wissen, wann sie welchen einsetzen.
3. Einen eigenen Cloud Flow von Grund auf im Designer erstellen, testen und veröffentlichen (aktivieren).
4. Eine einfache Bedingung (Condition) sowie eine Genehmigung (Approval) in einen Flow einbauen.
5. Den Unterschied zwischen Standard- und Premium-Konnektoren benennen und einordnen, wofür Desktop Flows/RPA, Umgebungen, Solutions und DLP-Richtlinien da sind – auch wenn diese im Workshop nicht vertieft gebaut werden.
6. Wissen, wo sie im Alltag weiterlernen und sich Hilfe holen können (Templates, Community, IT/Center of Excellence).

---

## 2. Vorbereitung (vor dem Workshop, nicht Teil der 120 Min.)

- [ ] Zugang zu Power Automate ([make.powerautomate.com](https://make.powerautomate.com)) für alle Teilnehmenden testen (Lizenz vorhanden? richtiges Environment?). Hinweis aus der Doku: *„Every member in an organization can access the **default environment**."* – als Fallback, falls jemand kein eigenes zugewiesenes Environment hat.
- [ ] Eine SharePoint-Testbibliothek/-liste mit zwei Ordnern ("Eingang" / "Geprüft") für die Live-Demo anlegen
- [ ] Eigenen Laptop/Beamer-Setup mit Power-Automate-Designer testen
- [ ] Foliensatz mit den 4 Kernbegriffen (Trigger, Aktion, Konnektor, Flow) als visuelle Anker vorbereiten
- [ ] Miro/Whiteboard oder Chat für Fragen währenddessen vorbereiten (parkende Fragen sammeln)
- [ ] Prüfen, welche Lizenz die Teilnehmenden haben: Mit einer reinen Microsoft-365-Lizenz stehen **nur Standard-Konnektoren** zur Verfügung (siehe Block 4) – falls die Hands-on-Übung (Block 6) einen Premium-Konnektor bräuchte, vorher gegenprüfen, ob alle TN das können

---

## 3. Agenda-Übersicht (Timeboxing)

| # | Block | Dauer | Kumuliert |
|---|-------|-------|-----------|
| 1 | Begrüßung, Ziele, Kontext des Citizen-Developer-Programms | 10 Min. | 0:10 |
| 2 | Grundlagen: Was ist Power Automate? | 15 Min. | 0:25 |
| 3 | Live-Tour: Der Flow-Designer | 10 Min. | 0:35 |
| 4 | Kernbausteine: Trigger, Aktionen, Konnektoren (direkt im Designer gezeigt) | 15 Min. | 0:50 |
| 5 | **Pause** | 10 Min. | 1:00 |
| 6 | Gemeinsamer Hands-on: Ersten Flow bauen (Scheduled Flow + E-Mail) | 25 Min. | 1:25 |
| 7 | Flow erweitern: Bedingungen (Conditions) | 10 Min. | 1:35 |
| 8 | Approvals: Genehmigungsprozesse automatisieren | 10 Min. | 1:45 |
| 9 | Ausblick: Desktop Flows/RPA, Umgebungen, Solutions, DLP, AI Builder | 10 Min. | 1:55 |
| 10 | Offene Fragerunde, nächste Schritte, Abschluss | 5 Min. | 2:00 |

---

## 4. Detaillierte Ablaufplanung

### Block 1 – Begrüßung, Ziele, Kontext (0:00–0:10 | 10 Min.)

**Was:** Vorstellung, Einordnung des Workshops im Citizen-Developer-Programm, Erwartungsabgleich.

**Wie:**
- Kurze Vorstellungsrunde (Name, Abteilung, "Ein Prozess, den ich gerne automatisiert hätte")
- Ziele des Citizen-Developer-Programms in 2–3 Sätzen einordnen: Warum macht die Firma das? Welche Rolle spielt Power Automate darin?
- Agenda und Lernziele zeigen, Erwartungen abfragen ("Was soll am Ende dieses Workshops für Sie möglich sein?")
- Spielregeln für Interaktion klären: Fragen jederzeit erlaubt, "Parkplatz" für tiefergehende/Spezialfragen

**Talking Point:** Betonen, dass Power Automate bewusst als Low-Code/No-Code-Werkzeug für genau diese Zielgruppe gebaut ist – man muss laut Microsoft *„little to no knowledge of coding"* mitbringen, um produktiv zu werden.

**Interaktionselement:** Kurze Blitzumfrage ("Wer hat schon einmal einen Flow gebaut?" per Handzeichen oder Chat-Emoji) – gibt Kalibrierung fürs Tempo.

---

### Block 2 – Grundlagen: Was ist Power Automate? (0:10–0:25 | 15 Min.)

*Quelle: [Overview of cloud flows](https://learn.microsoft.com/en-us/power-automate/overview-cloud), [What is Power Automate?](https://learn.microsoft.com/en-us/power-automate/flow-types)*

**Was:** Einordnung von Power Automate als Low-Code-Automatisierungswerkzeug innerhalb der Power Platform.

**Kernzitat zum Einstieg (wörtlich vorlesen oder sinngemäß wiedergeben):**
> *„With its automation capabilities, Power Automate helps you streamline your business processes and automate repetitive tasks. Its intuitive interface and many connectors allow you to create workflows with little to no knowledge of coding."*

- Power Automate verbindet Apps und Dienste, um Aufgaben/Prozesse zu automatisieren – ausgelöst durch Ereignisse (z. B. E-Mail-Eingang) oder Zeitpunkte.
- Analogie für Einsteiger: "Wenn-Dann"-Regeln, wie ein digitaler Assistent, der repetitive Aufgaben übernimmt.
- **Wichtige Einordnung, die oft übersehen wird:** Power Automate ist mehr als nur Cloud Flows. Laut Doku gibt es **drei Typen von Flows**:
  - **Cloud flows** – *„Create a cloud flow when you want your automation to be triggered either automatically, instantly, or via a schedule."* → das ist der Fokus dieses Workshops.
  - **Desktop flows** – *„Use desktop flows to automate tasks on the web or the desktop."* → RPA, wird in Block 9 kurz eingeordnet.
  - **Generative actions (preview)** – man beschreibt nur die *Absicht*, die KI wählt die passenden Aktionen selbst. Nur als Ausblick erwähnen, nicht vertiefen.
- Zwei Wege, einen Cloud Flow zu bauen: **mit Copilot** (Beschreibung in natürlicher Sprache, Copilot schlägt Trigger und Aktionen vor) oder **from scratch/ohne Copilot** (manuell im Designer, in beiden Designer-Varianten verfügbar). Für den Workshop: Fokus auf "ohne Copilot", damit die Teilnehmenden die Mechanik wirklich verstehen – Copilot kurz als späteren Beschleuniger erwähnen.
- **Die drei Cloud-Flow-Typen** (zentrale Tabelle, ausführlich erklären – das ist DAS Basiswissen):

  | Typ | Wann nutzen? | Beispiel | Nutzen laut Doku |
  |---|---|---|---|
  | **Automated Flow** | Wird durch ein Ereignis ausgelöst | Neue Datei in SharePoint, neue E-Mail | Konnektoren verbinden Cloud-/On-Premises-Dienste automatisch |
  | **Instant Flow** | Wird manuell per Knopfdruck gestartet | "Erinnerung an Team senden"-Button | Läuft sofort bei Auswahl eines Buttons/einer Steuerung |
  | **Scheduled Flow** | Läuft zeitgesteuert/wiederkehrend | Wöchentlicher Report, monatlicher Datenupload | Vorhersehbare Aufgaben müssen nur einmal automatisiert werden |

- Kurzer Hinweis: Es gibt auch die Power-Automate-Mobile-App (iOS & Android) zum Erstellen/Nutzen von Flows unterwegs.
- **Voraussetzung, die viele überraschen könnte:** Man braucht eine Microsoft-Work-/School-E-Mail-Adresse zur Registrierung – ein reiner privater Microsoft-Account reicht nicht.

**Interaktionselement:** Für jeden der 3 Flow-Typen ein Alltagsbeispiel aus dem Unternehmen der Teilnehmenden gemeinsam sammeln (Zuruf/Chat) – z. B. "Was bei uns könnte ein Scheduled Flow sein?"

---

### Block 3 – Live-Tour: Der Flow-Designer (0:25–0:35 | 10 Min.)

*Quelle: [Explore the cloud flows designer](https://learn.microsoft.com/en-us/power-automate/flows-designer)*

**Was:** Orientierung im Designer, bevor die Kernbausteine und später der eigene Flow darin gebaut werden.

**Live am Beamer zeigen** (Teilnehmende schauen zu, das eigene Nachklicken kommt in Block 6):

- **Canvas** (Arbeitsfläche): Hier wird der Flow zusammengeklickt; blaue gestrichelte Linien ("Drop Zones") zeigen an, wo man Aktionen per Drag-&-Drop einfügen kann.
- **Flow-Name, Speichern-Button, Test-Button, Flow-Checker** (prüft den Flow auf Fehler, bevor man testet).
- **Konfigurationsbereich (Parameters-Tab):** Über das **Blitz-Symbol** fügt man *Dynamic Content* ein (Werte aus vorherigen Schritten), über das ***fx***-Symbol eine *Expression*. Praktischer Shortcut: einfach `/` im Eingabefeld tippen, um direkt "Insert dynamic content" oder "Insert expression" zu öffnen.
- **Save-Button-Verhalten:** Nach erfolgreichem Speichern erscheint laut Doku die Meldung *„Your flow is ready to go. We recommend you test it"* mit grünem Haken. Bei einem Fehler erscheint ein rotes X mit Fehlerbeschreibung direkt an der betroffenen Karte.
- **Test-Button:** Manuelles Testen eines Flows (**Test → Manually → Test**); nach Abschluss erscheint pro Schritt ein grüner Haken plus Laufzeit in Sekunden.
- **Praktischer Sicherheits-Tipp für die Hands-on-Phase:** Der neue Designer speichert bei einem fehlgeschlagenen Save-Vorgang automatisch eine Kopie im Browser-Speicher – auch wenn der Flow noch Fehler enthält. So geht bei einem Verbindungsabbruch nichts verloren; über den Button **Recover flow** lässt sich diese Kopie später wiederherstellen.
- Kurzer Hinweis auf **"Code View"** für technisch Interessierte (zeigt den zugrunde liegenden JSON-Code einer Aktion) – optional, nicht vertiefen.
- Kurzer Hinweis auf nützliche Canvas-Werkzeuge unten links: **Zoom in/out, Fit view, Minimap** (Navigation in großen Flows) und **Layout-Umschalter** (inline vs. Panel-Ansicht).

**Caveat für Fortgeschrittene (nur bei Nachfrage erwähnen):** Es gibt aktuell noch einen **neuen** und einen **klassischen Designer** parallel. Der neue Designer ist Standard, kann aber laut Doku noch nicht alle Flow-Arten öffnen (z. B. bestimmte Business-Process-Flow-Trigger oder sehr alte, nicht-OpenAPI-basierte Verbindungen) – dann springt Power Automate automatisch in den klassischen Designer. Für den Workshop nicht relevant, aber gut zu wissen, falls TN später eine abweichende Oberfläche sehen.

**Didaktischer Tipp:** Bewusst als reine Demo halten (keine Interaktion nötig) – dient als "Landkarte" bzw. Bühne, auf der im nächsten Block die Kernbegriffe direkt gezeigt werden, statt sie nur abstrakt auf einer Folie zu erklären.

---

### Block 4 – Kernbausteine: Trigger, Aktionen, Konnektoren (0:35–0:50 | 15 Min.)

*Quellen: [Triggers](https://learn.microsoft.com/en-us/power-automate/triggers-introduction), [Actions](https://learn.microsoft.com/en-us/power-automate/actions-introduction)*

**Was:** Die drei Bausteine, aus denen jeder Flow besteht – jetzt direkt am gerade gezeigten Designer verankert.

**Trigger:**
- Ein Trigger ist das Ereignis, das den Flow **startet** (z. B. "Wenn eine neue E-Mail eintrifft").
- Trigger-Arten passend zu den 3 Flow-Typen: automatisch (Event), instant/manuell (Knopfdruck), geplant (Recurrence).
- Konnektoren (z. B. Outlook, SharePoint) bringen vorgefertigte Trigger mit – Outlook allein liefert bereits eine ganze Liste (z. B. *„When a new email arrives (V3)"*, *„When an email is flagged (V3)"*).
- Am Designer zeigen: Wo im Trigger-Auswahlbildschirm findet man welche Trigger-Art?

**Aktionen:**
- Aktionen sind das, was der Flow **tut**, nachdem der Trigger ausgelöst hat (E-Mail senden, Datensatz aktualisieren, Nachricht posten).
- Ein Flow braucht meist mehrere Aktionen (sequentiell oder parallel), z. B.: neues SharePoint-Element → E-Mail senden + Planner-Task erstellen + Datenbank aktualisieren.
- Kategorien im Aktionsbereich des Designers (live zeigen, da aus Block 3 bereits bekannt): **Favoriten, KI-Funktionen (AI Capabilities), Built-in Tools** (Variablen, Schleifen, Bedingungen – die "Werkzeugkiste") und **By Connector** (alle verfügbaren Dienste, die 20 meistgenutzten Konnektoren stehen oben).
- Unterscheidung: einfache/atomare Aktionen (z. B. `Compose`, `Get items`, `Create item`) vs. Container-Aktionen (`Condition`, `Switch`, `Apply to each`, `Scope`).
- **Nützlicher Praxis-Tipp (Copy & Paste):** Aktionen lassen sich per Rechtsklick → **Copy Action** kopieren und in einen anderen Teil desselben oder eines anderen Flows einfügen (**Paste an action**) – spart bei ähnlichen Schritten viel Zeit. Tastenkürzel: `Strg+C` / `Strg+V`.

**Konnektoren:**
- Ein Konnektor repräsentiert einen Dienst (SharePoint, Outlook, Teams, Excel, …) und stellt dessen Trigger und Aktionen bereit.
- **Standard- vs. Premium-Konnektoren – das ist für Citizen Developer lizenzrelevant und sollte klar benannt werden:**
  > *„You need a Power Automate license to access all Power Automate connectors, including the premium connectors. Users with a Microsoft 365 license can use all standard connectors."*
  - Standard-Konnektoren (z. B. SharePoint, Outlook, Teams, Excel) sind mit der normalen M365-Lizenz nutzbar.
  - Premium-Konnektoren (z. B. HTTP-Request, SQL Server, Dataverse, benutzerdefinierte Konnektoren) benötigen eine zusätzliche Power-Automate-Lizenz.
  - **Praxis-Konsequenz:** Wenn ein Flow "auf einmal nicht mehr läuft" oder beim Erstellen ein Lizenzhinweis erscheint, ist das oft genau dieser Unterschied – kein Bug, sondern Lizenzsteuerung.
- Im **"By Connector"**-Bereich der Aktionsauswahl (aus Block 3 bekannt) live nach 2–3 bekannten Diensten suchen lassen.

**Merksatz für die Folie:**
> **Trigger = Auslöser ("Wenn…") → Aktion(en) = Was passiert ("Dann…") → Konnektor = Verbindung zum jeweiligen Dienst**

**Interaktionselement:** Kurzes Quiz (mündlich/Chat): 3 Alltagssituationen vorlesen, Teilnehmende rufen "Trigger oder Aktion?" – ggf. Antwort direkt live im Designer verifizieren (Suchfeld nutzen).

---

## ☕ Pause (0:50–1:00 | 10 Min.)

---

### Block 6 – Gemeinsamer Hands-on: Ersten Flow bauen (1:00–1:25 | 25 Min.)

*Quelle: [Create your first cloud flow without Copilot](https://learn.microsoft.com/en-us/power-automate/create-cloud-flow-without-copilot)*

**Was:** Alle Teilnehmenden bauen live mit – Schritt für Schritt, synchron zum Trainer.

**Ziel-Flow:** Ein **Scheduled Cloud Flow**, der eine E-Mail versendet (angelehnt an das offizielle Tutorial). Da Designer, Trigger, Aktionen und Konnektoren aus den Blöcken 3 und 4 bereits bekannt sind, wird hier direkt produktiv gearbeitet statt neu orientiert.

**Schritt-für-Schritt (jeder Schritt wird vom Trainer vorgemacht, dann von den TN nachgebaut):**

1. Anmeldung bei [make.powerautomate.com](https://make.powerautomate.com) (2 Min.)
2. **Create → Start from blank → Scheduled cloud flow** (2 Min.)
3. Flow benennen (z. B. "Mein erster Flow – Wochenreminder"), im Feld **Starting** Datum/Uhrzeit wählen, im Feld **Repeat every** z. B. "1" + "Week" wählen (3 Min.)
4. **Create** klicken → Designer öffnet sich mit **Recurrence-Trigger** (bereits gesetzt) (2 Min.)
5. Aktion hinzufügen: **+ → "Send an email (V2)"** unter **Microsoft 365 Outlook** suchen und auswählen (3 Min.)
6. Felder befüllen: **To** (eigene E-Mail-Adresse, ggf. mehrere durch Komma getrennt), **Subject**, **Body** (5 Min.)
7. **Save** klicken, Erfolgsmeldung *„Your flow is ready to go. We recommend you test it"* einordnen bzw. Fehler gemeinsam lösen (3 Min.)
8. **Test → Manually → Test** – Flow manuell auslösen und Ergebnis (grüne Haken, E-Mail-Eingang) gemeinsam prüfen (5 Min.)

**Wichtig für Trainer:**
- Bewusst langsames Tempo, nach jedem Schritt kurz Rundumblick ("Alle so weit? Fragen?")
- Typische Stolpersteine vorher kennen:
  - Fehlende Lizenz/Konnektor-Berechtigung (siehe Standard-/Premium-Unterschied aus Block 4)
  - Falsches Environment aktiv – Erinnerung an den Hinweis aus der Doku: *„Make sure that you're in the correct environment before you create a flow… You can't easily move components from one environment to another."*
  - Verbindung (Connection) muss ggf. neu autorisiert werden (grünes Häkchen bei den Connections prüfen)
- Diesen Block als **Kern des Workshops** behandeln – hier entsteht der "erste Erfolg", den der Workshop laut Zielsetzung vermitteln soll
- **Falls Zeit übrig bleibt:** Als Alternativ-/Erweiterungsbeispiel kann erwähnt werden, dass sich derselbe Trigger-Aktion-Aufbau z. B. auch mit einer SharePoint-Liste statt Recurrence umsetzen lässt (Trigger **When an item is created**) – das baut die Brücke zu Block 8 (Approvals mit SharePoint).

**Interaktionselement:** Durchgehend offene Fragerunde – Trainer geht aktiv herum (bzw. schaut in Video-Kacheln/Chat) und hilft bei individuellen Problemen.

---

### Block 7 – Flow erweitern: Bedingungen (Conditions) (1:25–1:35 | 10 Min.)

*Quellen: [Add a condition](https://learn.microsoft.com/en-us/power-automate/add-condition), [Use expressions in conditions to check multiple values](https://learn.microsoft.com/en-us/power-automate/use-expressions-in-conditions), [Customize your triggers with conditions](https://learn.microsoft.com/en-us/power-automate/customize-triggers)*

**Was:** Einführung von Entscheidungslogik im Flow.

**Grundprinzip:**
- Eine **Condition**-Aktion prüft, ob eine Bedingung wahr oder falsch ist, und verzweigt den Flow entsprechend in **"Ja" (If yes)**- und **"Nein" (If no)**-Zweige.
- Prinzip im Designer: linke Box = Wert/Dynamic Content, mittlere Box = Vergleichsoperator (z. B. "ist größer oder gleich"), rechte Box = Vergleichswert.
- Am Beispiel des eigenen Flows demonstrieren (Live-Ergänzung durch Trainer, TN schauen zu oder bauen optional mit, je nach Zeitpuffer).

**Für komplexere Fälle – mehrere Werte gleichzeitig prüfen:**
Die einfache Condition-Karte vergleicht nur *einen* Wert. Für mehrere Werte (z. B. "Status = fertig ODER Status = nicht nötig") nutzt man **Expressions**. Kompakte Cheat-Sheet-Tabelle, die sich gut als Live-Referenz eignet:

| Ausdruck | Bedeutung | Beispiel |
|---|---|---|
| `and(...)` | Beide Argumente müssen wahr sein | `and(greater(1,10),equals(0,0))` → `false` |
| `or(...)` | Mindestens ein Argument muss wahr sein | `or(greater(1,10),equals(0,0))` → `true` |
| `equals(...)` | Prüft Gleichheit | `equals(parameters('Status'),'Fertig')` |
| `greater(...)` / `greaterOrEquals(...)` | Größer(-gleich) | `greater(10,10)` → `false` |
| `less(...)` / `lessOrEquals(...)` | Kleiner(-gleich) | `less(10,100)` → `true` |
| `empty(...)` | Prüft, ob Wert/Array/String leer ist | `empty('')` → `true` |
| `not(...)` | Kehrt einen Boolean um | `not(contains('200 Success','Fail'))` → `true` |

**Praxisbeispiel zum Live-Zeigen:** "Lösche alle Zeilen, bei denen Status = 'blockiert' UND Zuständig = 'Herr Müller' ist" → `@and(equals(item()?['Status'], 'blockiert'), equals(item()?['Zuständig'], 'Herr Müller'))`.

**Profi-Tipp mit direktem Kosten-/Praxisbezug (unbedingt erwähnen, macht großen Eindruck):** Es gibt neben der Condition-*Aktion* auch **Trigger Conditions** – ein Filter direkt am Trigger, *bevor* der Flow überhaupt zu laufen beginnt.
> *„Without trigger conditions, your flow would trigger every time an invoice email is received, even if the invoice isn't approved. This can result in the flow running 1,000 times for 1,000 invoices, even though only 50 of them are approved. By adding a trigger condition to trigger only when an invoice is approved, the flow runs only 50 times."*

Das ist besonders in **Pay-as-you-go-Umgebungen** relevant, wo laut Doku *jeder* Flow-Lauf abgerechnet wird. Praktisch: Trigger Conditions liegen unter **Trigger auswählen → Settings → Trigger conditions → + Add**; jede Bedingung muss mit `@` beginnen, mehrere Bedingungen werden per Default per UND verknüpft (für ODER: `@or(test1, test2, test3)`).

**Interaktionselement:** Gemeinsam an der Tafel/im Chat ein Bedingungsbeispiel aus dem eigenen Arbeitsalltag der TN entwickeln ("Wenn Rechnung > 1.000 € ist, dann…") – und kurz diskutieren, ob das eher eine Condition-Aktion oder (bei häufigen Events) eine Trigger Condition wäre.

---

### Block 8 – Approvals: Genehmigungsprozesse automatisieren (1:35–1:45 | 10 Min.)

*Quellen: [Get started with approvals](https://learn.microsoft.com/en-us/power-automate/get-started-approvals), [Trigger approvals from a SharePoint document library](https://learn.microsoft.com/en-us/power-automate/trigger-sharepoint-library), [Create and test an approval workflow](https://learn.microsoft.com/en-us/power-automate/modern-approvals)*

**Was:** Einführung in Freigabe-/Genehmigungsworkflows – ein Klassiker für Citizen-Developer-Use-Cases.

- Approvals ermöglichen es, menschliche Entscheidungen (Freigaben) in einen automatisierten Flow einzubinden. Laut Doku unterstützt Power Automate Genehmigungen über mehrere Dienste hinweg, u. a. *„SharePoint, Dynamics 365, Salesforce, OneDrive for work or school, Zendesk, or WordPress"* – z. B. Urlaubsanträge, Rechnungsfreigaben, Dokumentenprüfung.
- Zentrale Aktion: **"Start and wait for an approval"** – der Flow pausiert, bis der/die Genehmiger:in reagiert hat. Es gibt daneben auch **"Create an approval"** und **"Wait for an approval"** als getrennte Bausteine, falls man den Prozess feiner steuern will.
- Die 4 Genehmigungstypen kurz zeigen (Tabelle):

  | Typ | Verhalten |
  |---|---|
  | Alle müssen genehmigen | Jede:r Genehmiger:in muss antworten; die Flow-Fortsetzung läuft erst nach allen Antworten oder bei einer einzelnen Ablehnung |
  | Erste:r Antwortende:r entscheidet | Erste Antwort (egal wer) schließt den Request ab |
  | Individuelle Antworten – alle | Eigene Antwortoptionen definierbar, alle müssen antworten |
  | Individuelle Antworten – eine | Eigene Antwortoptionen definierbar, eine Antwort reicht |
  | Sequenziell | Genehmiger:innen antworten nacheinander in fester Reihenfolge – typisches Beispiel laut Doku: *Vor-Genehmigung nötig, bevor Rechnungen über 1.000 $ final von der Finanzabteilung freigegeben werden* |

- Genehmiger:innen können direkt aus **Outlook-E-Mail, Microsoft-Teams-Adaptive-Card, dem Power-Automate-Action-Center** oder der **mobilen App** reagieren.
- Voraussetzung: Dataverse-Datenbank (wird bei Erstnutzung im Default-Environment automatisch angelegt, in anderen Environments braucht die erstmalige Ausführung Admin-Rechte) + gültige Power-Automate-/M365-Lizenz (die Approvals-Aktion ist ein **Standard**-Konnektor, siehe Block 4 – jede Lizenz mit Standard-Konnektor-Zugriff reicht).
- **Praxis-Tipps für später (kurz erwähnen):**
  - Eine offene Genehmigung lässt sich unter **Approvals → Sent-Tab → Cancel** vom Flow-Ersteller zurückziehen.
  - Genehmigungen können auch an **Gastnutzer:innen** vergeben werden – wichtig: nur, wenn diese die B2B-Tenant-Einladung angenommen haben, sonst werden sie automatisch aus der Liste entfernt.

**Live-Demo (nur zeigen, kein Nachbauen wegen Zeit):** Anhand des SharePoint-Beispiels visualisieren: Neue Datei in Bibliothek → **Get file content** → **Start and wait for an approval** → **Apply to each** (Antworten durchlaufen) → **Condition** (Approver Response = "Approve"?) → bei Ja: Datei in anderen Ordner verschieben + Original löschen; bei Nein: keine weitere Aktion.

> Wichtiger Sicherheitshinweis aus der Doku, den man als Trainer ernst nehmen sollte: *„Always follow the best practices for SharePoint security and your organization's best practices to ensure your environment is secure."* – ein guter Anknüpfungspunkt, um auf das Citizen-Developer-Programm bzw. die IT/Governance-Ansprechpartner zu verweisen.

**Interaktionselement:** Frage in die Runde: "Welcher Genehmigungsprozess bei uns im Unternehmen wäre ein gutes erstes Automatisierungsprojekt?" – Antworten sammeln, ggf. als Grundlage für Folgeprojekte im Citizen-Developer-Programm notieren.

---

### Block 9 – Ausblick: Weitere Power-Automate-Bausteine (1:45–1:55 | 10 Min.)

**Was:** Kompakter Überblick über Konzepte, die für den Einstieg *nicht* zwingend gebraucht werden, aber jede:r Citizen Developer kennen sollte, um sie später einzuordnen bzw. um zu wissen, wann IT/CoE einzubeziehen ist. Bewusst knapp halten – kein Deep-Dive.

- **Desktop Flows / RPA** *(Quelle: [Introduction to desktop flows](https://learn.microsoft.com/en-us/power-automate/desktop-flows/introduction))*
  > *„Desktop flows broaden the existing robotic process automation (RPA) capabilities in Power Automate and enable you to automate all repetitive desktop processes."*
  Im Unterschied zu Cloud Flows (die über APIs/Konnektoren arbeiten) steuert ein Desktop Flow die Oberfläche direkt – über *„application UI elements, images, or coordinates"*. Einsatz, wenn kein Konnektor existiert, z. B. bei alten Terminal-Anwendungen oder Systemen ohne API. Wichtig: Für **Premium**-Konnektoren in Desktop Flows braucht man eine **Attended-RPA-Lizenz**; mit einer kostenlosen Work-/School-Lizenz sind nur Standard-Konnektoren nutzbar.

- **Umgebungen (Environments)**
  > *„Environments create boundaries between different types of work. For example, an organization might have separate environments for different departments. Many organizations use environments to separate flows that are still being developed from those that are ready for widespread use."*
  Wichtiger, sehr praktischer Warnhinweis aus der Doku direkt an Citizen Developer: *„Make sure that you're in the correct environment before you create a flow, an app, or a similar component. You can't easily move components from one environment to another."* Für Governance i. d. R. vom CoE/IT vorgegeben.

- **Solutions**
  > *„When you host your flows in a solution, they become portable, making it effortless to move them and all their components from one environment to another."*
  Typisches Beispiel aus der Doku: Ein Flow wird in einer Sandbox entwickelt, in eine Testumgebung verschoben und nach dem Testen in die Produktivumgebung übernommen (Dev → Test → Prod). Relevant, sobald ein Flow "produktiv" gehen soll – Voraussetzung ist eine Dataverse-Umgebung.

- **DLP-Richtlinien (Data Loss Prevention)**
  DLP-Richtlinien klassifizieren Konnektoren in **Business** vs. **Non-Business** und verhindern, dass beide Kategorien in einem Flow kombiniert werden. Kernaussage aus der Doku, gut als Merksatz für die Teilnehmenden:
  > *„DLP policies don't directly stop sharing flows, but they mitigate risks if flows are broadly shared. By classifying connectors into Business versus Non-Business and creating DLP rules, you prevent flows … from using connectors that could exfiltrate data."*
  Für Citizen Developer wichtig zu wissen: *Wenn eine Konnektor-Kombination im Flow blockiert wird, ist das Absicht der IT/des CoE – nicht selbst versuchen zu umgehen, sondern beim CoE nachfragen.* DLP-Richtlinien gibt es übrigens auch separat für **Desktop Flows** (dort werden ganze Aktionsgruppen als business/non-business markiert).

- **AI Builder** *(Quelle: [Use AI Builder](https://learn.microsoft.com/en-us/power-automate/use-ai-builder))*
  > *„AI Builder is a Microsoft Power Platform capability that enables you to add intelligence to your automated processes, predict outcomes, and help improve business performance. AI Builder is a turnkey solution that brings the power of Microsoft AI through a point-and-click experience."*
  Praktisches Beispiel: die Aktion **"Create text with GPT (preview)"**, mit der man z. B. Texte zusammenfassen oder Antwort-Entwürfe generieren lassen kann, direkt als Schritt im Flow. Lizenzhinweis: AI Builder ist ein **Add-on**; im Power-Automate-Premium-Plan sind bereits einige AI-Builder-Credits enthalten.

**Format:** Als kompakte Übersichtsfolie mit 5 Kacheln präsentieren, pro Punkt 1–2 Sätze plus ein Praxisbeispiel – bewusst als "das gibt's auch noch" positionieren, nicht als Pflichtstoff für heute.

**Interaktionselement:** Kurze Abfrage, ob einer dieser Begriffe im Unternehmenskontext schon gefallen ist (z. B. "Hat jemand von euch schon von unseren DLP-Richtlinien gehört?") – schafft Bezug zur Unternehmensrealität.

---

### Block 10 – Offene Fragerunde, nächste Schritte, Abschluss (1:55–2:00 | 5 Min.)

**Was:** Konsolidierung, offene Fragen aus dem "Parkplatz" klären, konkrete nächste Schritte mitgeben.

**Inhalt:**
- Rückblick auf Lernziele: Kurzer Check "Was war heute neu für euch?"
- Parkplatz-Fragen (aus dem Chat/Board gesammelt) beantworten oder Nachbereitung ankündigen
- Konkrete nächste Schritte für die Teilnehmenden:
  - Templates-Bibliothek in Power Automate erkunden (schneller Einstieg für eigene Use Cases) – allein für SharePoint gibt es laut Doku bereits *„more than 100 SharePoint templates"*
  - Eigenen kleinen Prozess identifizieren und bis zum nächsten Termin/Community-Call einen ersten Flow-Entwurf bauen
  - Kontaktweg für Support nennen (CoE-Kontakt, interner Kanal, ggf. Community-Forum)
- Feedback einholen (kurze mündliche Runde oder Link zu Umfrage)

---

## 5. Didaktische Hinweise für den Trainer

- **Sprache:** Durchgehend "Wenn…Dann…"-Sprache statt technischer Begriffe verwenden, um die Grundmechanik zu verankern – Fachbegriffe (Trigger/Aktion/Konnektor) erst *nach* dem intuitiven Verständnis einführen.
- **Fehlerkultur:** Im Hands-on-Teil (Block 6) werden mit hoher Wahrscheinlichkeit Verbindungsprobleme/Lizenzthemen auftreten – das offen als "normalen Teil des Lernens" einordnen, nicht überspielen.
- **Tempo-Puffer:** Block 6 (Hands-on) ist der zeitkritischste Block. Falls Verzögerung entsteht, kann Block 9 (Ausblick) auf 5 Minuten gekürzt und als Nachbereitungs-Handout mitgegeben werden.
- **Fragerunde statt Frontalvortrag:** In jedem Block ist mindestens ein Interaktionselement eingeplant (siehe oben) – bewusst nutzen, um Verständnislücken früh zu erkennen, statt am Ende zu sammeln.
- **Parkplatz-Prinzip:** Tiefergehende oder Spezialfragen (z. B. zu Lizenzierung, komplexen Expressions, Governance-Details) auf einem sichtbaren "Parkplatz" (Whiteboard/Chat-Thread) sammeln und in Block 10 oder per Follow-up klären, um den Fluss nicht zu stören.
- **Zitate dosiert einsetzen:** Die wörtlichen Doku-Zitate in diesem Skript sind als Absicherung/Beleg gedacht, nicht zum Ablesen – am wirkungsvollsten ist es, sie sinngemäß in eigenen Worten wiederzugeben und nur bei besonders prägnanten Sätzen (z. B. den Trigger-Condition-Zahlen in Block 7) wörtlich zu zitieren.

---

## 6. Glossar (als Handout/Cheat-Sheet nutzbar)

| Begriff | Kurzerklärung |
|---|---|
| **Cloud Flow** | In der Cloud laufender, über Trigger/Aktionen/Konnektoren gebauter Automatisierungs-Workflow |
| **Desktop Flow / RPA** | Automatisierung auf Desktop-/Web-Oberflächenebene (UI-Elemente, Bilder, Koordinaten) statt über APIs |
| **Trigger** | Das Ereignis, das einen Flow startet (automatisch, instant/manuell, geplant) |
| **Aktion** | Ein Schritt, den der Flow nach dem Trigger ausführt (E-Mail senden, Datensatz anlegen, …) |
| **Konnektor** | Anbindung an einen Dienst (SharePoint, Outlook, …), stellt dessen Trigger/Aktionen bereit; Standard oder Premium |
| **Standard-/Premium-Konnektor** | Standard mit jeder M365-Lizenz nutzbar; Premium (z. B. HTTP, SQL, Dataverse) benötigt Power-Automate-Lizenz |
| **Designer (neu/klassisch)** | Grafische Oberfläche zum Bauen von Flows; neuer Designer ist Standard, klassischer für Spezialfälle weiter verfügbar |
| **Dynamic Content** | Werte aus vorherigen Schritten, per Blitz-Symbol in ein Feld einfügbar |
| **Expression** | Formel/Funktion (z. B. `and()`, `or()`, `equals()`) zur Verarbeitung von Werten, per *fx*-Symbol einfügbar |
| **Condition (Aktion)** | Verzweigt den Flow anhand einer Bedingung in "Ja"/"Nein"-Zweige |
| **Trigger Condition** | Filter direkt am Trigger, verhindert unnötige Flow-Läufe (und deren Kosten/Kontingent-Verbrauch) |
| **Scope / Switch / Apply to each** | Container-Aktionen zur Strukturierung, Verzweigung bzw. Schleifenbildung im Flow |
| **Approval** | Genehmigungsprozess, der menschliche Entscheidungen in den Flow einbindet (5 Ablauftypen) |
| **Environment** | Abgegrenzter Arbeitsbereich (z. B. Sandbox/Dev/Prod), trennt Flows/Daten/Ressourcen |
| **Solution** | Verpackungsmechanismus, um Flows (und andere Power-Platform-Komponenten) portabel zwischen Environments zu bewegen |
| **DLP-Richtlinie (Data Loss Prevention)** | Regel, die Konnektoren in Business/Non-Business einteilt und unzulässige Kombinationen blockiert |
| **AI Builder** | Point-and-Click-KI-Funktionen (z. B. Textgenerierung mit GPT) als Aktion im Flow nutzbar; lizenzpflichtiges Add-on |

---

## 7. Referenzen (verwendete Microsoft-Learn-Quellen)

- [Overview of cloud flows](https://learn.microsoft.com/en-us/power-automate/overview-cloud)
- [What is Power Automate?](https://learn.microsoft.com/en-us/power-automate/flow-types)
- [Triggers – Power Automate](https://learn.microsoft.com/en-us/power-automate/triggers-introduction)
- [Actions – Power Automate](https://learn.microsoft.com/en-us/power-automate/actions-introduction)
- [Explore the cloud flows designer](https://learn.microsoft.com/en-us/power-automate/flows-designer)
- [Create your first cloud flow without Copilot](https://learn.microsoft.com/en-us/power-automate/create-cloud-flow-without-copilot)
- [Add a condition to a cloud flow](https://learn.microsoft.com/en-us/power-automate/add-condition)
- [Use expressions in conditions to check multiple values](https://learn.microsoft.com/en-us/power-automate/use-expressions-in-conditions)
- [Customize your triggers with conditions](https://learn.microsoft.com/en-us/power-automate/customize-triggers)
- [Get started with Power Automate approvals](https://learn.microsoft.com/en-us/power-automate/get-started-approvals)
- [Trigger approvals from a SharePoint document library](https://learn.microsoft.com/en-us/power-automate/trigger-sharepoint-library)
- [Create and test an approval workflow with Power Automate](https://learn.microsoft.com/en-us/power-automate/modern-approvals)
- [Use SharePoint and Power Automate to build workflows](https://learn.microsoft.com/en-us/power-automate/sharepoint-overview)
- [Overview of using Outlook and Power Automate](https://learn.microsoft.com/en-us/power-automate/email-overview)
- [Introduction to desktop flows](https://learn.microsoft.com/en-us/power-automate/desktop-flows/introduction)
- [Overview of solution-aware flows](https://learn.microsoft.com/en-us/power-automate/overview-solution-flows)
- [Data loss prevention (DLP) policies (desktop flows)](https://learn.microsoft.com/en-us/power-automate/desktop-flows/data-loss-prevention)
- [Use AI Builder in Power Automate](https://learn.microsoft.com/en-us/power-automate/use-ai-builder)
- Ergänzend ausgewertet: die vollständige, lokal abgelegte Power-Automate-Dokumentation (`power-automate.md`, ~97.800 Zeilen), durchsucht über das mitgelieferte [search_docs.py](search_docs.py) – u. a. für die konkreten Zahlen zu Trigger-Conditions/Flow-Läufen, Standard-/Premium-Lizenzierung, Environment- und Solution-Verhalten sowie die DLP- und AI-Builder-Details.

*Hinweis: Vor dem Workshop empfiehlt es sich, kurz zu prüfen, ob sich UI-Bezeichnungen oder Lizenzdetails zwischenzeitlich geändert haben, da Power Automate sich stetig weiterentwickelt.*
