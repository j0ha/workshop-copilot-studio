# Skill "Schadenmeldung vorbereiten" – Übersicht & Packaging

Der eigentliche, portable Skill liegt im Standardformat unter [`schadenmeldung-vorbereiten/`](schadenmeldung-vorbereiten/):

```
Skills/
└── schadenmeldung-vorbereiten/
    ├── SKILL.md                              ← YAML-Frontmatter (name, description) + Markdown-Instructions
    └── templates/
        └── schadenmeldung-vorlage.md          ← unterstützende Datei: Ausgabeformat für die Zusammenfassung
```

Dieses README ist **nicht** Teil des Skill-Pakets selbst, sondern eine Zusatzerklärung fürs Team.

## 1. Zwei Wege, den Skill in Copilot Studio anzulegen

**Option A – Direkt in Copilot Studio bauen:**
Im Build-Tab unter **Skills** → **Create from blank** → Name (`schadenmeldung-vorbereiten`), Beschreibung und den Markdown-Inhalt aus `SKILL.md` eintragen. Unterstützende Dateien wie die Vorlage lassen sich dabei nicht mit hochladen – für dieses Detail eignet sich Option B besser.

**Option B – Als ZIP-Paket hochladen (empfohlen, da portabel):**
1. Ordner `schadenmeldung-vorbereiten/` (inkl. `SKILL.md` und `templates/`) als ZIP packen, z. B.:
   ```bash
   cd Demo/Skills
   zip -r schadenmeldung-vorbereiten.zip schadenmeldung-vorbereiten/
   ```
2. Im Build-Tab unter **Skills** die Option zum Hochladen eines bestehenden Skill-Pakets wählen und die ZIP-Datei auswählen.
3. Copilot Studio liest Name und Beschreibung automatisch aus dem YAML-Frontmatter der `SKILL.md`.

## 2. Warum eine unterstützende Datei (Template)?

Die Ausgabevorlage liegt bewusst **getrennt** von der eigentlichen Skill-Logik in `templates/schadenmeldung-vorlage.md`. Das zeigt gut, wofür "optionale unterstützende Dateien" in einem Skill-Paket gedacht sind: Wiederverwendbare Bausteine (hier: ein festes Ausgabeformat), auf die die Instructions in `SKILL.md` nur verweisen, statt sie inline zu wiederholen. Bei Bedarf ließe sich der Ordner künftig z. B. um eine Referenzliste der Fleet-Management-Kontakte je Standort erweitern, ohne `SKILL.md` selbst anzufassen.

## 3. Beispiel-Dialog (zum Testen im Preview-Tab)

**Nutzer:** Ich hatte gerade einen Unfall mit meinem Dienstwagen, Kennzeichen B-FP 4471. Niemand verletzt, aber die Stoßstange ist eingedrückt. War auf dem Parkplatz vom Kunden, Gegenseite ist auch da.

**Agent (Skill aktiv):**
> Gut, dass niemand verletzt wurde. Um die Meldung für das Fuhrparkmanagement vorzubereiten, brauche ich noch ein paar Angaben: Ihren Namen und Ihre Personalnummer, den genauen Ort und die Uhrzeit, ob das Fahrzeug noch fahrbereit ist, die Kontakt- und Versicherungsdaten der Gegenseite, ob die Polizei verständigt wurde, und ob Sie Fotos gemacht haben.

**Nutzer:** Julia Sommer, PN 55210. Heute 14:15 Uhr, Kundenparkplatz ABC GmbH in Köln. Fahrzeug ist fahrbereit. Polizei war nicht da, Fotos habe ich gemacht. Versicherungsdaten der Gegenseite habe ich noch nicht.

**Agent:**
> Danke, hier ist der Entwurf für die Schadenmeldung:
>
> ```
> BETREFF: Schadenmeldung Dienstwagen – B-FP 4471 – [heutiges Datum]
>
> Meldende Person: Julia Sommer, PN 55210
> Fahrzeug: B-FP 4471
> Datum/Uhrzeit: [heutiges Datum], 14:15 Uhr
> Ort: Kundenparkplatz ABC GmbH, Köln
> Hergang: Kollision auf dem Kundenparkplatz, Stoßstange eingedrückt
> Fahrzeug fahrbereit: ja
> Beteiligte: Gegenseite vor Ort, Daten noch offen
> Versicherungsdaten Gegenseite: fehlend
> Zeuginnen/Zeugen: fehlend
> Polizei verständigt: nein
> Fotos vorhanden: ja
>
> Fehlende Angaben: Versicherungsdaten Gegenseite, ggf. Zeugenkontakte
> ```
>
> Das ist ein Entwurf – bitte ergänzen Sie die fehlenden Versicherungsdaten der Gegenseite, sobald Sie sie haben, und senden Sie die Meldung ans Fuhrparkmanagement. Die 24-Stunden-Frist zur Meldung gilt weiterhin.

## 4. Einordnung für den Workshop

Dieser Skill **ersetzt nicht** die Handoff-Regel aus den Agent-Instructions (Übergabe bei akutem Unfall) – er ergänzt sie um eine strukturierte Vorbereitung, bevor bzw. während an das Fuhrparkmanagement übergeben wird. Gut geeignet, um live den Unterschied zwischen **Instructions** (allgemeines Verhalten, ein Feld) und **Skill** (fester, portabler, wiederverwendbarer Ablauf für eine konkrete Aufgabe, eigenes SKILL.md + ZIP) zu zeigen.
