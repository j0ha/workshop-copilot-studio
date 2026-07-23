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

*(7 Spalten – "circa 5" plus zwei ergänzende Verwaltungsfelder, die für die Praxis sinnvoll sind; bei Bedarf Ansprechpartner/Vertragsnummer weglassen, um exakt bei 5 zu bleiben.)*

## Dateninhalt (5 Einträge)

| Händlername | Hersteller/Marken | Nutzfahrzeuge im Sortiment | Standort | Rahmenvertragsnummer | Vertragslaufzeit bis | Ansprechpartner |
|---|---|---|---|---|---|---|
| AutoWelt Nord GmbH | Volkswagen, Audi, Škoda | Nein | Hamburg | RV-2025-014 | 31.12.2027 | Jens Brammer, j.brammer@autowelt-nord.de |
| Süddeutsche Fahrzeugleasing AG | BMW, Mercedes-Benz | Nein | Stuttgart | RV-2025-021 | 30.06.2028 | Melanie Wachter, m.wachter@sfl-ag.de |
| ElectroDrive Mobility GmbH | Tesla, Hyundai, Kia | Nein | München | RV-2025-033 | 31.03.2027 | Kaan Yildirim, k.yildirim@electrodrive-mobility.de |
| Rhein-Ruhr Nutzfahrzeuge & Fuhrpark Service GmbH | Ford, Mercedes-Benz | Ja | Duisburg | RV-2025-040 | 31.12.2026 | Sabine Kortmann, s.kortmann@rr-nfz.de |
| Ostdeutsche Fuhrparkpartner GmbH | Škoda, Opel | Nein | Leipzig | RV-2025-047 | 31.12.2029 | Thomas Lindner, t.lindner@ofp-leipzig.de |

## Kurzprofil je Händler (zur Einordnung, nicht Teil der Liste selbst)

- **AutoWelt Nord** – Volumenmarken-Generalist, deckt Berechtigungsstufen C–P ab, mittlere Konditionen.
- **Süddeutsche Fahrzeugleasing** – Premiumsegment, deckt Stufen A–C ab, längere Lieferzeiten, dafür Vollservice-Standard.
- **ElectroDrive Mobility** – reiner Elektrofahrzeug-Händler, deckt Stufen B–P ab, kürzeste Lieferzeiten, höchster Flottenrabatt (Nachhaltigkeitsfokus, passt zu §12 der Richtlinie).
- **Rhein-Ruhr Nutzfahrzeuge & Fuhrpark Service** – einziger Händler mit echten Nutzfahrzeugen (Transporter/Vans), deckt Stufe E/P sowie Nutzfahrzeug-Bedarf gemäß §11 ab.
- **Ostdeutsche Fuhrparkpartner** – günstigster Anbieter, Fokus auf Poolfahrzeuge (Stufe P/E), schnellste Standardlieferzeiten, kein Vollservice inklusive.

Zugehörige Rahmenverträge: siehe die 5 Dokumente `Rahmenvertrag_0X_*.md` in diesem Ordner.
