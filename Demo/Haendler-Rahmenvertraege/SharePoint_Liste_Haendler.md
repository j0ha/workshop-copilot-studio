# MS-Lists-Struktur: "Dienstwagen-Händlernetzwerk"

Diese Liste bildet die Vertragspartner (Autohäuser/Leasinggesellschaften) ab, über die Fahrzeuge gemäß Dienstwagenrichtlinie (§16, §17) beschafft werden dürfen. Sie dient im Demo-Setup später als mögliche Knowledge-Quelle (SharePoint) für den Copilot-Studio-Agent.

## Spaltenstruktur (zum Anlegen in MS Lists)

| Spaltenname | Spaltentyp in MS Lists | Hinweise |
|---|---|---|
| **Händlername** | Einzeiliger Text | Titel-Spalte (Standard "Title" umbenennen) |
| **Hersteller/Marken** | Einzeiliger Text | Kommagetrennt, z. B. "Volkswagen, Audi, Škoda" |
| **Nutzfahrzeuge im Sortiment** | Wahl (Ja / Nein) | Für Anfragen zu leichten Nutzfahrzeugen relevant (§3, §11) |
| **Standort** | Einzeiliger Text | Stadt |
| **Rahmenvertragsnummer** | Einzeiliger Text | Referenz auf das jeweilige Vertragsdokument |
| **Vertragslaufzeit bis** | Datum | Enddatum des Rahmenvertrags |
| **Ansprechpartner** | Einzeiliger Text | Name + E-Mail |
| **Abgedeckte Berechtigungsstufen** | Einzeiliger Text | Aus Ziffer 5 (Modellportfolio) des jeweiligen Rahmenvertrags, z. B. "C, D, E, P" |
| **Flottenrabatt-Spanne** | Einzeiliger Text | Aus Ziffer 6.1 (Leasingkonditionen) des jeweiligen Rahmenvertrags, niedrigster bis höchster Rabattsatz über alle Stufen |
| **Vollwartungsvertrag** | Wahl (Inklusive / Optional / Pflicht je Stufe) | Aus dem Wartungs-Abschnitt (Ziffer 9) des jeweiligen Rahmenvertrags |
| **Kürzeste Lieferzeit im Portfolio** | Einzeiliger Text | Aus der Lieferzeiten-Tabelle des jeweiligen Rahmenvertrags, schnellstes gelistetes Modell |
| **Partnerwerkstätten im Netz** | Zahl | Aus dem Werkstattnetz-Abschnitt des jeweiligen Rahmenvertrags; bei ElectroDrive Mobility zusätzlich markenweites Servicenetz nutzbar (siehe Hinweis unten) |

*(12 Spalten – die ursprünglichen 7 plus 5 weitere, die direkt aus den Rahmenverträgen der Händler stammen und für Konditionsvergleiche nützlich sind.)*

## Dateninhalt (5 Einträge)

| Händlername | Hersteller/Marken | Nutzfahrzeuge im Sortiment | Standort | Rahmenvertragsnummer | Vertragslaufzeit bis | Ansprechpartner | Abgedeckte Berechtigungsstufen | Flottenrabatt-Spanne | Vollwartungsvertrag | Kürzeste Lieferzeit im Portfolio | Partnerwerkstätten im Netz |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AutoWelt Nord GmbH | Volkswagen, Audi, Škoda | Nein | Hamburg | RV-2025-014 | 31.12.2027 | Jens Brammer, j.brammer@autowelt-nord.de | C, D, E, P | 14–16 % | Optional (34 EUR/Monat) | 6–8 Wochen (Fabia, Golf) | 12 |
| Süddeutsche Fahrzeugleasing AG | BMW, Mercedes-Benz | Nein | Stuttgart | RV-2025-021 | 30.06.2028 | Melanie Wachter, m.wachter@sfl-ag.de | A, B, C | 10–13 % | Pflicht für A/B, optional für C (42 EUR/Monat) | 4–6 Monate (X3, GLC) | 9 |
| ElectroDrive Mobility GmbH | Tesla, Hyundai, Kia | Nein | München | RV-2025-033 | 31.03.2027 | Kaan Yildirim, k.yildirim@electrodrive-mobility.de | B, C, D, E, P | 15–20 % | Inklusive (kein Aufpreis) | 2–4 Wochen (Model 3, Model Y) | 2 (zzgl. markenweites Servicenetz) |
| Rhein-Ruhr Nutzfahrzeuge & Fuhrpark Service GmbH | Ford, Mercedes-Benz | Ja | Duisburg | RV-2025-040 | 31.12.2026 | Sabine Kortmann, s.kortmann@rr-nfz.de | E, P, Nutzfahrzeug | 10–12 % | Pflicht für Nutzfahrzeuge, optional für E/P (30 EUR/Monat) | 3–4 Monate (Citan Kombi) | 6 |
| Ostdeutsche Fuhrparkpartner GmbH | Škoda, Opel | Nein | Leipzig | RV-2025-047 | 31.12.2029 | Thomas Lindner, t.lindner@ofp-leipzig.de | E, P | 21–22 % | Optional (22 EUR/Monat) | 6–8 Wochen (Fabia, Astra, Scala) | 4 |

**Hinweis zu den 5 neuen Spalten:** Alle Werte sind 1:1 aus dem jeweiligen Rahmenvertrag übernommen (Modellportfolio, Leasingkonditionen, Wartungs- und Lieferzeiten-Abschnitte) und eignen sich gut für Vergleichsfragen an den Agent, z. B. „Welcher Händler hat den höchsten Flottenrabatt?“ (Ostdeutsche Fuhrparkpartner, 21–22 %) oder „Bei welchem Händler ist die Vollwartung im Preis inklusive?“ (ElectroDrive Mobility). Ändert sich ein Rahmenvertrag, müssen diese Spalten entsprechend nachgepflegt werden – die Liste ist keine automatische Ableitung aus den Vertragsdokumenten.

## Kurzprofil je Händler (zur Einordnung, nicht Teil der Liste selbst)

- **AutoWelt Nord** – Volumenmarken-Generalist, deckt Berechtigungsstufen C–P ab, mittlere Konditionen.
- **Süddeutsche Fahrzeugleasing** – Premiumsegment, deckt Stufen A–C ab, längere Lieferzeiten, dafür Vollservice-Standard.
- **ElectroDrive Mobility** – reiner Elektrofahrzeug-Händler, deckt Stufen B–P ab, kürzeste Lieferzeiten, höchster Flottenrabatt (Nachhaltigkeitsfokus, passt zu §12 der Richtlinie).
- **Rhein-Ruhr Nutzfahrzeuge & Fuhrpark Service** – einziger Händler mit echten Nutzfahrzeugen (Transporter/Vans), deckt Stufe E/P sowie Nutzfahrzeug-Bedarf gemäß §11 ab.
- **Ostdeutsche Fuhrparkpartner** – günstigster Anbieter, Fokus auf Poolfahrzeuge (Stufe P/E), schnellste Standardlieferzeiten, kein Vollservice inklusive.

Zugehörige Rahmenverträge: siehe die 5 Dokumente `Rahmenvertrag_0X_*.md` in diesem Ordner.
