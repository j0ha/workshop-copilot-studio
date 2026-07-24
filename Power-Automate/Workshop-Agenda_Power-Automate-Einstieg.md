# Workshop: Einstieg in Microsoft Power Automate
### Citizen Developer Programm – 2-stündiger interaktiver Praxis-Workshop

**Zielgruppe:** Citizen Developer ohne oder mit sehr wenig Vorerfahrung in Power Automate bzw. Prozessautomatisierung.
**Format:** Präsenz/Remote, hoher Interaktionsanteil, Live-Demo + gemeinsamer Flow-Bau, laufende Fragerunde statt reinem Frontalvortrag.
**Gesamtdauer:** 120 Minuten (inkl. 1 Pause à 10 Min.)

---

## 1. Lernziele

Am Ende des Workshops können die Teilnehmenden:

1. Die Grundbegriffe von Power Automate (Trigger, Aktion, Konnektor, Cloud Flow) erklären und voneinander abgrenzen.
2. Die drei Cloud-Flow-Typen (Automated, Instant, Scheduled) unterscheiden und wissen, wann sie welchen einsetzen.
3. Einen eigenen Cloud Flow von Grund auf im Designer erstellen, testen und veröffentlichen (aktivieren).
4. Eine einfache Bedingung (Condition) sowie eine Genehmigung (Approval) in einen Flow einbauen.
5. Einordnen, wofür Desktop Flows/RPA, Umgebungen, Solutions und DLP-Richtlinien da sind – auch wenn diese im Workshop nicht vertieft gebaut werden.
6. Wissen, wo sie im Alltag weiterlernen und sich Hilfe holen können (Templates, Community, IT/Center of Excellence).

---

## 2. Vorbereitung (vor dem Workshop, nicht Teil der 120 Min.)

- [ ] Zugang zu Power Automate (make.powerautomate.com) für alle Teilnehmenden testen (Lizenz vorhanden? Environment korrekt?)
- [ ] Eine SharePoint-Testbibliothek/-liste mit zwei Ordnern ("Eingang" / "Geprüft") für die Live-Demo anlegen
- [ ] Eigenen Laptop/Beamer-Setup mit Power-Automate-Designer testen
- [ ] Foliensatz mit den 4 Kernbegriffen (Trigger, Aktion, Konnektor, Flow) als visuelle Anker vorbereiten
- [ ] Miro/Whiteboard oder Chat für Fragen währenddessen vorbereiten (parkende Fragen sammeln)

---

## 3. Agenda-Übersicht (Timeboxing)

| # | Block | Dauer | Kumuliert |
|---|-------|-------|-----------|
| 1 | Begrüßung, Ziele, Kontext des Citizen-Developer-Programms | 10 Min. | 0:10 |
| 2 | Grundlagen: Was ist Power Automate? | 15 Min. | 0:25 |
| 3 | Kernbausteine: Trigger, Aktionen, Konnektoren | 15 Min. | 0:40 |
| 4 | Live-Tour: Der Flow-Designer | 10 Min. | 0:50 |
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

**Interaktionselement:** Kurze Blitzumfrage ("Wer hat schon einmal einen Flow gebaut?" per Handzeichen oder Chat-Emoji) – gibt Kalibrierung fürs Tempo.

---

### Block 2 – Grundlagen: Was ist Power Automate? (0:10–0:25 | 15 Min.)

**Was:** Einordnung von Power Automate als Low-Code-Automatisierungswerkzeug innerhalb der Power Platform.

**Inhalt (Quelle: [Overview of cloud flows](https://learn.microsoft.com/en-us/power-automate/overview-cloud)):**
- Power Automate verbindet Apps und Dienste, um Aufgaben/Prozesse zu automatisieren – ausgelöst durch Ereignisse (z. B. E-Mail-Eingang) oder Zeitpunkte.
- Analogie für Einsteiger: "Wenn-Dann"-Regeln, wie ein digitaler Assistent, der repetitive Aufgaben übernimmt.
- Zwei Wege, einen Flow zu bauen: **mit Copilot** (Beschreibung in natürlicher Sprache) oder **from scratch/ohne Copilot** (manuell im Designer). Für den Workshop: Fokus auf "ohne Copilot", damit die Teilnehmenden die Mechanik wirklich verstehen – Copilot kurz erwähnen als späteren Beschleuniger.
- **Die drei Cloud-Flow-Typen** (zentrale Tabelle, ausführlich erklären – das ist DAS Basiswissen):

  | Typ | Wann nutzen? | Beispiel |
  |---|---|---|
  | **Automated Flow** | Wird durch ein Ereignis ausgelöst | Neue Datei in SharePoint, neue E-Mail |
  | **Instant Flow** | Wird manuell per Knopfdruck gestartet | "Erinnerung an Team senden"-Button |
  | **Scheduled Flow** | Läuft zeitgesteuert/wiederkehrend | Wöchentlicher Report, monatlicher Datenupload |

- Kurzer Hinweis: Es gibt auch die Power-Automate-Mobile-App zum Erstellen/Nutzen von Flows unterwegs.

**Interaktionselement:** Für jeden der 3 Flow-Typen ein Alltagsbeispiel aus dem Unternehmen der Teilnehmenden gemeinsam sammeln (Zuruf/Chat) – z. B. "Was bei uns könnte ein Scheduled Flow sein?"

---

### Block 3 – Kernbausteine: Trigger, Aktionen, Konnektoren (0:25–0:40 | 15 Min.)

**Was:** Die drei Bausteine, aus denen jeder Flow besteht.

**Inhalt Trigger (Quelle: [Triggers](https://learn.microsoft.com/en-us/power-automate/triggers-introduction)):**
- Ein Trigger ist das Ereignis, das den Flow **startet** (z. B. "Wenn eine neue E-Mail eintrifft").
- Trigger-Arten passend zu den 3 Flow-Typen: automatisch (Event), instant/manuell (Knopfdruck), geplant (Recurrence).
- Konnektoren (z. B. Outlook, SharePoint) bringen vorgefertigte Trigger mit.

**Inhalt Aktionen (Quelle: [Actions](https://learn.microsoft.com/en-us/power-automate/actions-introduction)):**
- Aktionen sind das, was der Flow **tut**, nachdem der Trigger ausgelöst hat (E-Mail senden, Datensatz aktualisieren, Nachricht posten).
- Ein Flow braucht meist mehrere Aktionen (sequentiell oder parallel), z. B.: neues SharePoint-Element → E-Mail senden + Planner-Task erstellen + Datenbank aktualisieren.
- Kategorien im Aktionsbereich des Designers: **Favoriten, KI-Funktionen (AI Capabilities), Built-in Tools** (Variablen, Schleifen, Bedingungen – die "Werkzeugkiste") und **By Connector** (alle verfügbaren Dienste).
- Unterscheidung: einfache/atomare Aktionen (z. B. `Compose`, `Get items`) vs. Container-Aktionen (`Condition`, `Switch`, `Apply to each`, `Scope`).

**Inhalt Konnektoren:**
- Ein Konnektor repräsentiert einen Dienst (SharePoint, Outlook, Teams, Excel, …) und stellt dessen Trigger und Aktionen bereit.
- Für Unternehmenskontext relevant: Standard- vs. Premium-Konnektoren (kurz erwähnen, da lizenzrelevant – Details im Ausblicksblock/DLP).

**Merksatz für die Folie:**
> **Trigger = Auslöser ("Wenn…") → Aktion(en) = Was passiert ("Dann…") → Konnektor = Verbindung zum jeweiligen Dienst**

**Interaktionselement:** Kurzes Quiz (mündlich/Chat): 3 Alltagssituationen vorlesen, Teilnehmende rufen "Trigger oder Aktion?"

---

### Block 4 – Live-Tour: Der Flow-Designer (0:40–0:50 | 10 Min.)

**Was:** Orientierung im Designer, bevor die Teilnehmenden selbst Hand anlegen.

**Inhalt (Quelle: [Explore the cloud flows designer](https://learn.microsoft.com/en-us/power-automate/flows-designer)):**
Live am Beamer zeigen, ohne dass die Teilnehmenden selbst schon mitklicken (das kommt in Block 6):
- Canvas (Arbeitsfläche), Flow-Name, Speichern-Button, Test-Button, Flow-Checker
- Konfigurationsbereich (Parameters-Tab), Dynamic Content (Blitz-Symbol) und Expressions (*fx*)
- Save-Button-Verhalten: grüner Haken = "bereit zum Testen"; roter Fehler = Ursache anzeigen und korrigieren
- Test-Button: manuelles Testen eines Flows, Ergebnis pro Schritt (grüner Haken + Laufzeit)
- Kurzer Hinweis auf "Code View" für technisch Interessierte (optional, nicht vertiefen)

**Didaktischer Tipp:** Bewusst als reine Demo halten (keine Interaktion nötig) – dient als "Landkarte", damit im Hands-on-Teil niemand verloren geht.

---

## ☕ Pause (0:50–1:00 | 10 Min.)

---

### Block 6 – Gemeinsamer Hands-on: Ersten Flow bauen (1:00–1:25 | 25 Min.)

**Was:** Alle Teilnehmenden bauen live mit – Schritt für Schritt, synchron zum Trainer.

**Ziel-Flow:** Ein **Scheduled Cloud Flow**, der eine E-Mail versendet (angelehnt an das offizielle Tutorial, Quelle: [Create your first cloud flow without Copilot](https://learn.microsoft.com/en-us/power-automate/create-cloud-flow-without-copilot)).

**Schritt-für-Schritt (jeder Schritt wird vom Trainer vorgemacht, dann von den TN nachgebaut):**

1. Anmeldung bei [make.powerautomate.com](https://make.powerautomate.com) (2 Min.)
2. **Create → Start from blank → Scheduled cloud flow** (2 Min.)
3. Flow benennen (z. B. "Mein erster Flow – Wochenreminder"), Startzeitpunkt und Wiederholung festlegen (z. B. wöchentlich) (3 Min.)
4. **Create** klicken → Designer öffnet sich mit **Recurrence-Trigger** (bereits gesetzt) (2 Min.)
5. Aktion hinzufügen: **+ → "Send an email (V2)"** (Office 365 Outlook) suchen und auswählen (3 Min.)
6. Felder befüllen: An (eigene E-Mail-Adresse), Betreff, Nachrichtentext (5 Min.)
7. **Save** klicken, Erfolgsmeldung ("Ihr Flow ist startklar") einordnen bzw. Fehler gemeinsam lösen (3 Min.)
8. **Test → Manually → Test** – Flow manuell auslösen und Ergebnis (grüne Haken, E-Mail-Eingang) gemeinsam prüfen (5 Min.)

**Wichtig für Trainer:**
- Bewusst langsames Tempo, nach jedem Schritt kurz Rundumblick ("Alle so weit? Fragen?")
- Typische Stolpersteine vorher kennen: fehlende Lizenz/Konnektor-Berechtigung, falsches Environment, Verbindung (Connection) muss ggf. neu autorisiert werden
- Diesen Block als **Kern des Workshops** behandeln – hier entsteht der "erste Erfolg", den der Workshop laut Zielsetzung vermitteln soll

**Interaktionselement:** Durchgehend offene Fragerunde – Trainer geht aktiv herum (bzw. schaut in Video-Kacheln/Chat) und hilft bei individuellen Problemen.

---

### Block 7 – Flow erweitern: Bedingungen (Conditions) (1:25–1:35 | 10 Min.)

**Was:** Einführung von Entscheidungslogik im Flow.

**Inhalt (Quelle: [Add a condition](https://learn.microsoft.com/en-us/power-automate/add-condition)):**
- Eine **Condition** prüft, ob eine Bedingung wahr oder falsch ist, und verzweigt den Flow entsprechend in **"Ja"**- und **"Nein"**-Zweige.
- Prinzip: linke Box = Wert/Dynamic Content, mittlere Box = Vergleichsoperator (z. B. "ist größer oder gleich"), rechte Box = Vergleichswert.
- Am Beispiel des eigenen Flows demonstrieren (Live-Ergänzung durch Trainer, TN schauen zu oder bauen optional mit, je nach Zeitpuffer): z. B. "Wochentag = Montag? Dann andere Nachricht senden."
- Hinweis: Komplexere Bedingungen (UND/ODER) lassen sich über den **Add**-Button verschachteln.

**Interaktionselement:** Gemeinsam an der Tafel/im Chat ein Bedingungsbeispiel aus dem eigenen Arbeitsalltag der TN entwickeln ("Wenn Rechnung > 1.000 € ist, dann…").

---

### Block 8 – Approvals: Genehmigungsprozesse automatisieren (1:35–1:45 | 10 Min.)

**Was:** Einführung in Freigabe-/Genehmigungsworkflows – ein Klassiker für Citizen-Developer-Use-Cases.

**Inhalt (Quellen: [Get started with approvals](https://learn.microsoft.com/en-us/power-automate/get-started-approvals), [Trigger approvals from SharePoint library](https://learn.microsoft.com/en-us/power-automate/trigger-sharepoint-library)):**
- Approvals ermöglichen es, menschliche Entscheidungen (Freigaben) in einen automatisierten Flow einzubinden – z. B. Urlaubsanträge, Rechnungsfreigaben, Dokumentenprüfung.
- Zentrale Aktion: **"Start and wait for an approval"** – der Flow pausiert, bis der/die Genehmiger:in reagiert hat.
- Die 4 Genehmigungstypen kurz zeigen (Tabelle):

  | Typ | Verhalten |
  |---|---|
  | Alle müssen genehmigen | Jede:r Genehmiger:in muss antworten |
  | Erste:r Antwortende:r entscheidet | Erste Antwort zählt |
  | Individuelle Antworten – alle | Eigene Antwortoptionen, alle müssen antworten |
  | Individuelle Antworten – eine | Eigene Antwortoptionen, eine Antwort reicht |
  | Sequenziell | Genehmiger:innen antworten nacheinander in fester Reihenfolge |

- Genehmiger:innen können direkt aus **Outlook-E-Mail, Teams-Karte oder Power-Automate-Action-Center** reagieren.
- Voraussetzung: Dataverse-Datenbank (wird bei Erstnutzung automatisch angelegt) + gültige Power-Automate-/M365-Lizenz.
- **Live-Demo (nur zeigen, kein Nachbauen wegen Zeit):** Anhand des SharePoint-Beispiels kurz visualisieren: Neue Datei in Bibliothek → Genehmigungsanfrage → bei "Approve" wird Datei in anderen Ordner verschoben.

**Interaktionselement:** Frage in die Runde: "Welcher Genehmigungsprozess bei uns im Unternehmen wäre ein gutes erstes Automatisierungsprojekt?" – Antworten sammeln, ggf. als Grundlage für Folgeprojekte im Citizen-Developer-Programm notieren.

---

### Block 9 – Ausblick: Weitere Power-Automate-Bausteine (1:45–1:55 | 10 Min.)

**Was:** Kompakter Überblick über Konzepte, die für den Einstieg *nicht* zwingend gebraucht werden, aber jede:r Citizen Developer kennen sollte, um sie später einzuordnen bzw. um zu wissen, wann IT/CoE einzubeziehen ist. Bewusst knapp halten – kein Deep-Dive.

- **Desktop Flows / RPA:** Automatisierung von Desktop-Anwendungen und Legacy-Systemen (Klicks, Tastatureingaben) – im Unterschied zu Cloud Flows, die über APIs/Konnektoren arbeiten. Einsatz, wenn kein Konnektor existiert.
- **Umgebungen (Environments):** Container zur Trennung von Daten, Flows und Ressourcen (z. B. Dev/Test/Prod, Abteilungen). Wichtig für Governance – als Citizen Developer i. d. R. vom CoE/IT vorgegeben.
- **Solutions:** Verpackungsmechanismus, um Flows (und andere Power-Platform-Komponenten) strukturiert zu entwickeln, zu versionieren und zwischen Umgebungen zu transportieren (z. B. Dev → Prod). Relevant, sobald ein Flow "produktiv" gehen soll.
- **DLP-Richtlinien (Data Loss Prevention):** Regeln der IT/des CoE, die festlegen, welche Konnektoren miteinander kombiniert werden dürfen (z. B. Trennung Business- vs. Non-Business-Datenkonnektoren). Für Citizen Developer wichtig zu wissen: *Wenn eine Kombination blockiert wird, ist das Absicht – nicht mit Support klären, sondern beim CoE nachfragen.*
- **AI Builder (Quelle: [Use AI Builder](https://learn.microsoft.com/en-us/power-automate/use-ai-builder)):** Point-and-Click-KI-Funktionen (z. B. Texterkennung, Vorhersagemodelle), die direkt als Aktion in einen Flow eingebaut werden können – ideal für spätere, fortgeschrittenere Use Cases.

**Format:** Als kompakte Übersichtsfolie mit 5 Kacheln präsentieren, pro Punkt 1–2 Sätze plus ein Praxisbeispiel – bewusst als "das gibt's auch noch" positionieren, nicht als Pflichtstoff für heute.

**Interaktionselement:** Kurze Abfrage, ob einer dieser Begriffe im Unternehmenskontext schon gefallen ist (z. B. "Hat jemand von euch schon von unseren DLP-Richtlinien gehört?") – schafft Bezug zur Unternehmensrealität.

---

### Block 10 – Offene Fragerunde, nächste Schritte, Abschluss (1:55–2:00 | 5 Min.)

**Was:** Konsolidierung, offene Fragen aus dem "Parkplatz" klären, konkrete nächste Schritte mitgeben.

**Inhalt:**
- Rückblick auf Lernziele: Kurzer Check "Was war heute neu für euch?"
- Parkplatz-Fragen (aus dem Chat/Board gesammelt) beantworten oder Nachbereitung ankündigen
- Konkrete nächste Schritte für die Teilnehmenden:
  - Templates-Bibliothek in Power Automate erkunden (schneller Einstieg für eigene Use Cases)
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

---

## 6. Quellenverzeichnis

- [Overview of cloud flows](https://learn.microsoft.com/en-us/power-automate/overview-cloud)
- [Triggers – Power Automate](https://learn.microsoft.com/en-us/power-automate/triggers-introduction)
- [Actions – Power Automate](https://learn.microsoft.com/en-us/power-automate/actions-introduction)
- [Explore the cloud flows designer](https://learn.microsoft.com/en-us/power-automate/flows-designer)
- [Create your first cloud flow without Copilot](https://learn.microsoft.com/en-us/power-automate/create-cloud-flow-without-copilot)
- [Add a condition to a cloud flow](https://learn.microsoft.com/en-us/power-automate/add-condition)
- [Get started with Power Automate approvals](https://learn.microsoft.com/en-us/power-automate/get-started-approvals)
- [Trigger approvals from a SharePoint document library](https://learn.microsoft.com/en-us/power-automate/trigger-sharepoint-library)
- [Overview of using Outlook and Power Automate](https://learn.microsoft.com/en-us/power-automate/email-overview)
- [Use AI Builder in Power Automate](https://learn.microsoft.com/en-us/power-automate/use-ai-builder)
