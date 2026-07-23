---
name: schadenmeldung-vorbereiten
description: Bereitet bei einem gemeldeten Unfall, Schaden, Diebstahl oder einer Panne mit dem Dienstwagen eine strukturierte Schadenmeldung vor und erstellt daraus einen Entwurfstext für die Übergabe ans Fuhrparkmanagement. Auslöser sind Formulierungen wie "Ich hatte einen Unfall", "mein Auto wurde beschädigt/aufgebrochen", "ich hatte eine Panne" oder "hilf mir, den Schaden zu melden".
---

# Schadenmeldung vorbereiten

Dieser Skill unterstützt dabei, eine strukturierte Schadenmeldung für das Fuhrparkmanagement vorzubereiten, wenn eine Person einen Unfall, Schaden, Diebstahl oder eine Panne mit ihrem Dienstwagen meldet. Er ergänzt die allgemeine Handoff-Regel des Agents um einen festen, wiederholbaren Ablauf – Fehlende Angaben werden gezielt nachgefragt statt geraten.

## Schritt 0 – Sicherheit zuerst

Wenn Personen verletzt sind oder eine akute Gefahrenlage besteht, unterbrich diesen Skill sofort und weise darauf hin, umgehend den Notruf 112 zu verständigen, bevor irgendetwas anderes erfolgt. Erst wenn die Situation sicher ist, mit Schritt 1 fortfahren.

## Schritt 1 – Fehlende Angaben erfragen

Sammle in einer einzigen, kompakten Rückfrage die folgenden Angaben, sofern sie nicht bereits im Gespräch genannt wurden. Bereits genannte Punkte nicht erneut abfragen:

- Name und Personalnummer der meldenden Person
- Kennzeichen des Dienstwagens
- Ort und genauer Zeitpunkt des Vorfalls
- kurze Beschreibung des Hergangs
- ob das Fahrzeug fahrbereit ist (ja/nein)
- beteiligte Personen/Fahrzeuge und deren Kennzeichen (falls vorhanden)
- Kontakt- und Versicherungsdaten der Gegenseite (falls vorhanden)
- Kontaktdaten von Zeuginnen/Zeugen (falls vorhanden)
- ob die Polizei verständigt wurde; falls ja, das polizeiliche Aktenzeichen
- ob Fotos der Unfallstelle/Schäden vorliegen (ja/nein)

## Schritt 2 – Zusammenfassung erzeugen

Fasse die verfügbaren Angaben – auch wenn einzelne Punkte fehlen – exakt im Format der Vorlage `templates/schadenmeldung-vorlage.md` zusammen. Felder, zu denen keine Angabe vorliegt, werden dort als "fehlend" markiert, niemals erfunden oder plausibel geraten.

## Schritt 3 – Übergabe

Weise darauf hin, dass die erzeugte Zusammenfassung ein Entwurf ist, den die meldende Person prüfen und selbst an das Fuhrparkmanagement senden kann, und dass die 24-Stunden-Meldefrist der Dienstwagenrichtlinie unabhängig davon weiterhin gilt. Beschreibe den Kontaktweg inhaltlich (z. B. "an die hinterlegte Fuhrparkmanagement-Adresse bzw. Notfallhotline"), ohne interne Datei- oder Systemnamen zu nennen. Dieser Skill versendet nichts automatisch.

## Leitplanken

- Fehlende Angaben niemals erfinden, sondern explizit als "fehlend" kennzeichnen.
- Keine Aussage zu Haftung, Schuldfrage oder Kostenübernahme treffen – das bleibt dem Fuhrparkmanagement und der Versicherung vorbehalten.
- Sprache und Tonalität folgen den allgemeinen Agent-Instructions (professionell, Sie-Form, sachlich, keine Wertung).
