# Workshop: Microsoft Copilot Studio für Citizen Developer

**Format:** Interaktiver Präsenz-/Remote-Workshop — **keine Folien/Slides**. Alles, was gezeigt wird, passiert live in der Power Platform / in Copilot Studio selbst.
**Dauer:** 120 Minuten
**Zielgruppe:** Citizen Developer im Rahmen des Citizen Developer Programms (keine/wenig Vorerfahrung mit Copilot Studio)
**Ziel des Workshops:** Teilnehmende verstehen die Grundkonzepte von Copilot Studio, kennen die zentralen Bausteine eines Agents und haben gemeinsam mit dem Trainer einen eigenen Agent erstellt, getestet und veröffentlicht.

> Hinweis zur Aktualität: Copilot Studio befindet sich aktuell im Übergang von der *klassischen* Experience (Topics/Trigger-basiert) zur *neuen* Experience (natural-language-first, "Build"-Tab). Dieser Workshop nutzt primär die **neue Experience**, da sie der einfachere Einstieg für Citizen Developer ist. Ein kurzer Hinweis auf die klassische Experience gehört in die Grundlagen, damit Teilnehmende nicht verwirrt sind, falls sie in ihrer Umgebung noch die klassische Oberfläche sehen.

### Didaktisches Grundprinzip: "Show, don't slide"

Da keine Folien genutzt werden, brauchen alle theoretischen Blöcke einen **konkreten Live-Ankerpunkt im Tool**. Dafür empfiehlt sich folgende Vorbereitung:

- **Referenz-Agent vorbereiten:** Vor dem Workshop einen bereits fertig konfigurierten Beispiel-Agent anlegen (z. B. "IT-Helpdesk-FAQ-Assistent" mit Instructions, einer Knowledge-Quelle, einem Tool und einer Skill). Dieser dient als lebendiges Anschauungsobjekt für die Konzeptblöcke (2, 3, 5), bevor die Teilnehmenden im Hands-on-Block ihren eigenen, leeren Agent bauen.
- **Zwei Browser-Tabs/Fenster parallel offen halten:** einen mit dem Referenz-Agent (zum Zeigen von Konzepten), einen leeren für den späteren Live-Aufbau des gemeinsamen Workshop-Agents.
- Jede Erklärung folgt dem Muster: *kurz sprechen → sofort im Tool anklicken/zeigen → Teilnehmende schauen mit, keine Slide nötig.*
- Bildschirmfreigabe/Beamer ist durchgehend auf Copilot Studio (nicht auf einer Präsentation).

---

## Lernziele

Am Ende des Workshops können die Teilnehmenden:

1. Erklären, was ein Agent in Copilot Studio ist und aus welchen Bausteinen er besteht (Instructions, Knowledge, Tools, Skills, Model).
2. In eigenen Worten beschreiben, wie ein LLM grundsätzlich funktioniert (statistische Vorhersage des nächsten Wortes) und warum daraus ein grundsätzliches Restrisiko für die Korrektheit von Antworten folgt.
3. Einen Agent selbstständig anlegen und über natürlichsprachige Instructions konfigurieren.
4. Eine Wissensquelle (Knowledge Source) und mindestens ein Tool/Skill hinzufügen.
5. Einen Agent im Preview-Tab testen und über einen Kanal (Demo-Website) veröffentlichen.
6. Die zentralen Risiken beim Bauen und Veröffentlichen eigener Agents benennen (Halluzinationsrisiko, Authentifizierung, Tool-Credentials, Reichweite bei Freigabe/Veröffentlichung, öffentliche Knowledge-Quellen) und wissen, worauf sie als Citizen Developer selbst achten müssen.

---

## Vorbereitung / Setup-Checkliste (vor dem Workshop an Teilnehmende kommunizieren)

- [ ] Zugang zu [copilotstudio.microsoft.com](https://copilotstudio.microsoft.com) mit gültiger Lizenz (Trial reicht zum Bauen/Testen, aber **nicht** zum Publizieren – das vorab klären, siehe unten)
- [ ] Zugewiesenes Environment bekannt (Sandbox/Dev-Umgebung des Citizen Developer Programms)
- [ ] Browser + stabile Internetverbindung
- [ ] Eine konkrete, kleine Idee für einen eigenen Agent mitbringen (z. B. FAQ-Bot zu einem Thema, kleiner Prozess-Assistent) – wird als Basis für individuelle Nachahmung nach dem Workshop genutzt
- [ ] Optional: Ein Beispieldokument (PDF/Word) oder eine SharePoint-Seite als potenzielle Wissensquelle

**Trainer-seitige Vorbereitung (zusätzlich, da ohne Folien gearbeitet wird):**
- [ ] Referenz-Agent vorab bauen und konfigurieren (Instructions, 1 Knowledge-Quelle, 1 Tool, 1 Skill) – dient als Live-Anschauungsobjekt in den Blöcken 2, 3 und 5
- [ ] Zweiten, leeren Agent-Slot/Environment für den gemeinsamen Hands-on-Aufbau vorbereiten
- [ ] Bildschirmfreigabe/Beamer-Setup vorab testen, da durchgehend im Live-Tool gearbeitet wird (kein Fallback über Folien)

**Wichtig:** Mit einer Trial-Lizenz kann man einen Agent bauen und im Preview-Chat testen, aber **nicht veröffentlichen**. Für den gemeinsamen Hands-on-Teil sollte daher mindestens der Trainer (besser: alle Teilnehmenden) über eine volle Lizenz/Environment-Zugang verfügen, damit der Publish-Schritt live gezeigt werden kann.

---

## Agenda-Übersicht

| # | Zeit | Dauer | Block | Format |
|---|------|-------|-------|--------|
| 1 | 00:00–00:05 | 5 Min | Begrüßung, Vorstellung, Ziele & Ablauf | Gespräch (kein Tool nötig) |
| 2 | 00:05–00:30 | 25 Min | Grundlagen & Risikobewusstsein: Was ist ein Agent, was steckt dahinter – und wo liegen die Risiken? | Live-Rundgang durch Copilot-Studio-Startseite & Referenz-Agent + Exkurs LLM-Funktionsweise + Risikodiskussion |
| 3 | 00:30–00:40 | 10 Min | Anatomie eines Agents: Der Build-Tab im Überblick | Live-Klick-Tour durch den Build-Tab des Referenz-Agents |
| 4 | 00:40–00:50 | 10 Min | Instructions vertieft: Wie schreibe ich gute Anweisungen? | Live-Bearbeitung der Instructions + Preview-Chat-Test |
| 5 | 00:50–01:05 | 15 Min | Knowledge, Tools & Skills – Konzepte und Unterschiede | Live am Referenz-Agent: Knowledge-, Tools-, Skills-Bereich zeigen |
| 6 | 01:05–01:10 | 5 Min | **Pause** | – |
| 7 | 01:10–01:40 | 30 Min | **Hands-on: Gemeinsam einen Agent bauen** | Alle bauen live und parallel in Copilot Studio |
| 8 | 01:40–01:50 | 10 Min | Testen im Preview-Tab & Veröffentlichen | Live-Demo Publish-Dialog + gemeinsames Testen |
| 9 | 01:50–02:00 | 10 Min | Offene Fragen, Wrap-up, nächste Schritte | Moderierte Fragerunde |

---

## Detaillierter Ablaufplan

### 1. Begrüßung, Ziele & Ablauf (5 Min)

- Kurze persönliche Vorstellung, Rolle im Citizen Developer Programm
- Erwartungsabfrage: "Wer hat schon einmal mit Copilot Studio gearbeitet?" (Handzeichen/Chat-Poll)
- Ablauf des Workshops erklären: Theorie-Blöcke wechseln sich mit Hands-on ab, am Ende steht ein gemeinsam gebauter Agent
- Spielregeln für Interaktivität festlegen: Fragen jederzeit möglich (nicht bis zum Schluss warten), Fragerunde-Segmente explizit ankündigen

**Talking Point:** Betonen, dass der Workshop bewusst niedrigschwellig ist – Copilot Studio ist als No-Code/Low-Code-Werkzeug für genau diese Zielgruppe gebaut.

---

### 2. Grundlagen & Risikobewusstsein: Was ist ein Agent, was steckt dahinter – und wo liegen die Risiken? (25 Min)

*Quelle: [Agents overview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/overview)*

**Live im Tool:** Bildschirm auf [copilotstudio.microsoft.com](https://copilotstudio.microsoft.com) einloggen und gemeinsam durch die **Home**-Seite navigieren, bevor irgendetwas erklärt wird.

#### Teil A – Was ist eigentlich ein Agent, und was ist der Nutzen davon? (8 Min)

1. Auf der **Home**-Seite zeigen: Eingabefeld für natürlichsprachige Beschreibung ("Automate our…"), Kacheln **Agent** und **Workflow**
2. Zum vorbereiteten **Referenz-Agent** wechseln, **Preview**-Tab öffnen und live eine Testfrage stellen – die Antwort erscheint in einem ganz normalen Chatfenster

**Kernerklärung (am laufenden Chat entlang):** Was wir hier gerade gesehen haben, ist im Kern ein interaktiver Chat. Dahinter sitzt ein **LLM (Large Language Model)** – dasselbe Grundprinzip wie bei ChatGPT. Das Modell liest, was ich ihm gebe (meine Frage, den bisherigen Gesprächsverlauf, die hinterlegten Instructions und ggf. Wissen), und generiert daraufhin Runde für Runde eine Antwort. Ich kann so ganz natürlich, konversationell mit ihm chatten und über die Zeit hinweg ganz bestimmte, spezialisierte Aufgaben erledigen.

**Vergleich, der beim Einordnen hilft:** Man kann sich das vorstellen, als würde man ein ganz normales ChatGPT nehmen und es gezielt auf ein bestimmtes Thema "tunen": Man gibt ihm klare Anweisungen, was es tun soll und was nicht (**Instructions**), Zugriff auf bestimmte Informationen (**Knowledge**) und Werkzeuge, mit denen es tatsächlich etwas für mich erledigen kann (**Tools**). Aus einem universellen Chatbot wird so ein spezialisierter Assistent für einen ganz bestimmten Zweck – genau das ermöglicht Copilot Studio, ohne dass man dafür programmieren können muss.

**Kurzer historischer Einordnungspunkt:** Chatbots gab es auch schon vorher – die **klassische Experience** in Copilot Studio arbeitet mit fest definierten Topics, Triggern und Gesprächsflüssen ("wenn die Frage X enthält, antworte mit Y"). Mit LLMs kommt jetzt die Fähigkeit dazu, auch auf unvorhergesehene Formulierungen sinnvoll zu reagieren, ohne dass man jeden Fall einzeln vorprogrammieren muss. Das ist der große Gewinn an Flexibilität – bringt aber, wie wir gleich sehen, auch eine neue Art von Unsicherheit mit sich, die es bei fest programmierten Flows so nicht gab.

**Wichtiger Praxis-Hinweis (falls jemand schon die klassische Experience kennt):** Wer schon einmal mit der klassischen Experience gearbeitet hat, wird in der neuen Experience bewusst weniger **deterministische** Kontrollmöglichkeiten finden – z. B. keinen festen "Escalate"-System-Topic mit Transfer-Node mehr, keine Node-basierten Gesprächsflüsse, keine separaten Einstellungs-Panels. Laut Doku ist das ein bekannter, aktueller Unterschied: *"The classic experience has a broader set of configurable features than the new experience."* Alles, was früher über feste Regeln/Nodes lief, läuft in der neuen Experience nur noch über natürlichsprachige Instructions – dazu gleich mehr in Block 3 und 4.

**Nutzen für euch als Citizen Developer:** Wiederkehrende, oft manuelle Aufgaben – Fragen beantworten, Informationen zusammensuchen, kleine Prozesse anstoßen – lassen sich so konversationell und ohne Code unterstützen oder automatisieren.

**Interaktion:** Kurze Frage in die Runde: "Was stellt ihr euch unter einem 'Agent' vor – ein Chatbot, ein Workflow, oder beides?" → Überleitung: "Es kann beides sein, und Copilot Studio entscheidet das teilweise automatisch."

#### Teil B – Exkurs: Wie "denkt" das Modell dahinter eigentlich? (7 Min)

Dieser Exkurs ist die fachliche Grundlage für die Risiken, die direkt im Anschluss kommen – deshalb bewusst vor Teil C platziert, nicht danach.

**Kernidee (einfach und bildhaft erklären):** Ein LLM ist im Grunde ein sehr großes **statistisches Modell**. Es liest den gesamten Input – meine Frage, den Gesprächsverlauf, die Instructions, das angebundene Wissen – und sagt Wort für Wort vorher, welches Wort statistisch am wahrscheinlichsten als Nächstes folgt. Man kann es sich wie eine extrem leistungsfähige Autovervollständigung vorstellen.

**Der entscheidende Unterschied, den alle verstehen müssen:** Das Modell sagt nicht voraus, was **richtig** ist – sondern was **statistisch am wahrscheinlichsten** ist. In den allermeisten Fällen fällt beides zusammen. Aber es gibt keine Garantie dafür. Die Statistik kann aus verschiedenen Gründen "verzerrt" sein – etwa durch lückenhafte oder widersprüchliche Wissensquellen, unklare Instructions, mehrdeutige Fragen oder Themen, zu denen es einfach keine verlässliche Grundlage gibt.

**Die eigentliche Kernbotschaft dieses Exkurses:** Wie überzeugend und flüssig eine Antwort klingt, sagt nichts darüber aus, ob sie inhaltlich korrekt ist. Genau das macht das Risiko tückisch – wir Menschen neigen dazu, gut formulierten, selbstsicher klingenden Antworten automatisch zu vertrauen. Es besteht deshalb immer ein **Restrisiko**, und man darf nicht blind auf die KI vertrauen.

**Optional live zeigen:** Im Referenz-Agent im **Preview**-Tab bewusst eine Frage stellen, die außerhalb der hinterlegten Knowledge-Quelle liegt, und gemeinsam beobachten, wie der Agent reagiert – als Lehrmoment, unabhängig davon, ob die Antwort verweigert oder (weniger gut abgesichert) eine unsichere Antwort generiert wird.

**Interaktion:** Kurze Verständnisfrage in die Runde: "Was überrascht euch an dieser Erklärung am meisten?"

#### Teil C – Risiken ganz klar benennen (10 Min)

Bevor es ans eigene Bauen geht, muss allen klar sein: Ein Agent ist kein harmloses Spielzeug – er kann auf echte Daten zugreifen und echte Aktionen auslösen. Dieser Teil bleibt bewusst konzeptionell und **ohne Admin-Center-Ausflug** – die Risiken werden direkt am gerade gezeigten Referenz-Agent verankert (Trainer bleibt im Build-Tab bzw. wechselt kurz zurück in die schon geöffneten Bereiche).

1. **Halluzinationsrisiko – die direkte Konsequenz aus Teil B**
   - Kurze Brücke: Weil das Modell statistisch vorhersagt statt nachzuschlagen, kann es Informationen erfinden oder falsch kombinieren ("Fabrication"/"Halluzination") – besonders bei unklaren Instructions oder Wissenslücken.
   - Praktische Konsequenz: Je sensibler das Thema (z. B. rechtliche, finanzielle oder personalbezogene Auskünfte), desto wichtiger sind klare Grenzen in den Instructions ("nur aus Knowledge antworten", "bei Unsicherheit an Menschen verweisen") und ein Testlauf mit kritischen Fragen vor dem Rollout.

**Wichtige Einordnung zu den folgenden drei Punkten (laut Copilot-Studio-Dokumentation):** *"Copilot Studio is secure by default. The system tailors its responses based on who is speaking to it, and the permissions they have."* Ein Agent ist also nicht per se unsicher – Copilot Studio ist standardmäßig auf Sicherheit ausgelegt. Das eigentliche Risiko entsteht dort, wo Maker diese sicheren Standardeinstellungen bewusst oder unbewusst lockern. Genau diese drei Stellen prüft Copilot Studio automatisch mit einem **Security-Scan vor jeder Veröffentlichung** (das sehen wir live in Block 8):

2. **Authentifizierung lockern**
   - Standard: **"Authenticate with Microsoft"** – nur angemeldete Personen können chatten.
   - Risiko-Einstellung: **"No authentication"** – jede Person mit dem Link kann den Agent nutzen, unabhängig davon, ob sie zur Organisation gehört.
   - Praktische Konsequenz: "No authentication" nur bewusst und für wirklich öffentliche Anwendungsfälle wählen (z. B. ein öffentlicher FAQ-Bot ohne sensible Inhalte).

3. **Tool-/Connector-Credentials umstellen**
   - Standard: **"End user credentials"** – jede Person kann über das Tool nur das tun, wozu sie selbst berechtigt ist.
   - Risiko-Einstellung: **"Maker-provided credentials"** – der Agent handelt dann mit den Rechten des Makers. Das kann dazu führen, dass Endnutzer:innen über den Agent Dinge abrufen oder auslösen, die eigentlich nur das Konto des Makers darf.
   - Praktische Konsequenz: Maker-Credentials nur verwenden, wenn es einen bewussten, geprüften Grund dafür gibt – nicht aus Bequemlichkeit.

4. **Teilen auf "Everyone in the organization" ausweiten**
   - Standard: Ein neuer Agent ist mit **niemandem** geteilt.
   - Risiko-Einstellung: Teilen mit **allen in der Organisation** – deutlich größere Reichweite als ursprünglich beabsichtigt.
   - Praktische Konsequenz: Erst im kleinen Kreis testen (Block 7/8), bevor breiter geteilt wird.

5. **Sonderfall: öffentliche Websites als Knowledge-Quelle**
   - Am gerade gezeigten Knowledge-Bereich anknüpfen: Bei SharePoint & Co. berücksichtigt der Agent laut Doku die Berechtigungen der jeweiligen Person; bei einer **öffentlichen Website als Quelle** gibt es dagegen naturgemäß keine Berechtigungsprüfung – hier lohnt sich die bewusste Frage "Soll dieser Inhalt wirklich für jeden über den Agent abrufbar sein?"

**Verantwortungs-Botschaft zum Abschluss:** *Ein Agent kann nie garantiert zu 100 % korrekt sein – das liegt in der Natur eines statistischen Sprachmodells. Und Copilot Studio ist von Haus aus sicher konfiguriert, aber ihr entscheidet als Citizen Developer aktiv, wenn ihr eine der Standardeinstellungen lockert – Authentifizierung, Credentials, Teilen. Genau dafür warnt euch das Tool auch selbst vor dem Publish. Im Zweifel lieber vorher mit dem Citizen-Developer-Team oder eurer IT/Datenschutz-Anlaufstelle absprechen.*

**Interaktion:** Offene Frage in die Runde: "Für eure eigene Agent-Idee – welches dieser fünf Risikofelder betrifft euch am ehesten, und warum?" Kurze Zurufrunde. Diese Sensibilisierung wird im Hands-on-Block (7) und beim Publish in Block 8 nochmals konkret aufgegriffen.

---

### 3. Anatomie eines Agents: Der Build-Tab im Überblick (10 Min)

*Quelle: [Build overview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/build-overview)*

**Live im Tool:** Weiterhin im Referenz-Agent, jetzt gezielt im **Build**-Tab. Jede Komponente wird angeklickt und kurz kommentiert, in dieser Reihenfolge:

1. **Name & Icon** oben anklicken – Identität des Agents
2. **Instructions-Feld** in der Mitte zeigen (Inhalt noch nicht verändern, das folgt in Block 4)
3. Im Komponenten-Panel rechts der Reihe nach anklicken und je 1–2 Sätze kommentieren:
   - **Model** – welches KI-Modell antwortet; beeinflusst Reasoning-Fähigkeit, Antwortqualität und Geschwindigkeit; in der neuen Experience u. a. Modelle von Anthropic, Mistral oder xAI wählbar
   - **Microsoft IQ** – dynamischer Zugriff auf organisationsweite Daten, aufgeteilt in drei Quellen: **Work IQ** (E-Mails, Chats, Dateien, Aktivität aus M365), **Fabric IQ** (Geschäftsdaten/Analytics aus Microsoft Fabric), **Foundry IQ** (Enterprise-Wissensdatenbanken über Azure AI Search) – Unterschied zu Knowledge: fließt dynamisch je nach Kontext/Berechtigung der fragenden Person, statt fest verbundener Quelle
   - **Skills** – wiederverwendbare, strukturierte Verhaltensweisen (Markdown-basiert)
   - **Tools** – Anbindung an externe Systeme über drei Typen: **Connectors** (vorgefertigte Power-Platform-Konnektoren zu Diensten wie SharePoint, Outlook, Salesforce, ServiceNow, SAP …), **MCP-Server** (Model-Context-Protocol – für individuelle/interne Services, Datenbanken, APIs) und **Workflows** (in Copilot Studio selbst gebaute, mehrstufige automatisierte Abläufe für wiederkehrende, deterministische Prozesse)
   - **Knowledge** – vertrauenswürdige Datenquellen (Dateiupload, öffentliche Websites, SharePoint, Dataverse, Dynamics 365, Salesforce, ServiceNow, Azure SQL, Azure AI Search …)
   - **Connected Agents** – andere, spezialisierte Agents als Kollaborationspartner; sinnvoll, wenn ein "Front-Door-Agent" Anfragen an spezialisierte Fach-Agents weiterleiten soll (Trennung von Zuständigkeiten, Wiederverwendbarkeit)
   - **Memory** – Kontext über mehrere Gespräche hinweg, pro Nutzer:in und pro Agent gespeichert (eigener "Memory-Ordner"); Ablauf: Agent erfasst Signale → speichert sie → nutzt sie bei künftigen Interaktionen

**Kernbotschaft (während des Klickens sagen):** Statt Flows zu zeichnen, beschreibt man in der neuen Experience das Verhalten – die Orchestrierung entscheidet zur Laufzeit, was benötigt wird (Wissen, Tool, Skill).

**Was hier bewusst fehlt (wichtig für alle, die die klassische Experience kennen):** Diese sieben Komponenten sind wirklich **alles**, was es in der neuen Experience gibt – es gibt kein separates Einstellungs-Panel für Topics, System-Topics (z. B. den früheren "Escalate"-Topic mit Transfer-Node), Trigger oder Node-Flows. Alles, was früher über solche festen Regeln lief, muss jetzt komplett über die **Instructions** in natürlicher Sprache formuliert werden. Das ist bewusst so reduziert und einfacher – bedeutet aber auch: weniger deterministische, garantierte Kontrolle über exakte Abläufe als in der klassischen Experience.

**Interaktion:** Teilnehmende dürfen zurufen, sobald sie eine Komponente sehen, die sie schon aus einem anderen Microsoft-365-Tool kennen (z. B. SharePoint, Power Automate) – Trainer knüpft live daran an.

---

### 4. Instructions vertieft: Wie schreibe ich gute Anweisungen? (10 Min)

*Quelle: [Configure agent details and instructions](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/authoring-instructions)*

Instructions sind der wichtigste Hebel zur Steuerung des Agent-Verhaltens. Gute Instructions enthalten:

- **Rolle & Zweck** des Agents ("Du bist ein interner HR-Assistent für Urlaubsfragen…")
- **Ton & Stil** (formell, freundlich, knapp …) – in der neuen Experience gibt es dafür **keinen** separaten Tonalitäts-Regler; Ton wird ausschließlich über die Formulierung in den Instructions gesteuert
- **Grenzen:** Themen/Aufgaben, die der Agent ablehnen oder weiterleiten soll
- **Umgang mit Unklarheit:** Wie reagiert der Agent auf mehrdeutige Anfragen?
- **Eskalations-/Übergabe-Trigger:** Wann soll an einen Menschen übergeben werden?

**Wichtiger Caveat zu Eskalations-Triggern (unbedingt explizit ansprechen):** In der klassischen Experience gab es dafür ein hartes, vom System garantiertes Feature – den **"Escalate"-System-Topic** mit einem konfigurierbaren **Transfer-conversation-Node**, inklusive fester Standardregel ("nach zwei erfolglosen Verständigungsversuchen eskalieren"). Dieses Feature **gibt es in der neuen Experience nicht mehr**. Eine Formulierung wie "Wenn du nach zwei Versuchen nicht weiterhelfen kannst, verweise an support@firma.de" in den Instructions ist nur eine **weiche Bitte an das LLM** – das Modell hält sich in der Regel daran, aber es ist keine vom System hart erzwungene Regel wie früher. Für den Workshop heißt das: Eskalationshinweise unbedingt in die Instructions schreiben, aber im Preview-Tab explizit testen, ob sich der Agent auch wirklich daran hält – und den Teilnehmenden ehrlich sagen, dass es hierfür (noch) keine 100%ige Garantie gibt.

**Praxis-Tipp aus der Doku:** Klein anfangen (einfache Zweckbeschreibung), dann iterativ im Preview-Tab testen und verfeinern.

**Wichtige Stolperfalle (explizit erwähnen):** Instructions sollten **nicht** versuchen, das system-eigene Zitierverhalten des Agents zu verändern oder zu unterdrücken (z. B. Anweisungen wie "zeige keine Quellen an" oder "ändere das Zitierformat"). Laut Doku kann das dazu führen, dass der Orchestrator Zitationen nicht mehr korrekt erkennt und Antworten fälschlich verwirft – der Agent wirkt dann "kaputt", obwohl nur die Instructions zu weit gegriffen haben.

**Live-Demo im Tool (statt Erklärung auf Folie):**

1. Im Referenz-Agent eine Testfrage im **Preview**-Tab stellen, Antwort im Standardton beobachten
2. Zurück in den **Build**-Tab, Instructions-Text live ändern (z. B. Ton von "freundlich-locker" auf "sehr formell" umschreiben) und **Save** klicken
3. Sofort wieder in **Preview** wechseln, dieselbe Testfrage erneut stellen → Unterschied in der Antwort live erleben
4. Optional ein zweites Mal wiederholen, um das iterative Prinzip (ändern → testen → beobachten) sichtbar zu machen

**Interaktion:** "Ruft mir spontan 2–3 Sätze zu, die in den Instructions eures Wunsch-Agents stehen könnten" (mündlich oder Chat) – wird später im Hands-on wiederverwendet.

---

### 5. Knowledge, Tools & Skills – Konzepte und Unterschiede (15 Min)

*Quellen: [Knowledge overview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/knowledge-copilot-studio), [Tools overview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/tools-overview), [Skills overview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/skills-overview)*

**Live im Tool:** Weiterhin im Referenz-Agent, jeweils den passenden Bereich im **Build**-Tab öffnen, bevor das Konzept erklärt wird – nicht umgekehrt.

**Knowledge (5 Min):**
- Im **Build**-Tab den Bereich **Knowledge** öffnen, die dort hinterlegte Beispielquelle (Dokument/Website/SharePoint) anklicken und zeigen, wie sie eingebunden wurde
- Direkt im **Preview**-Chat eine Frage stellen, die nur aus dieser Quelle beantwortbar ist, und in der Antwort auf die Quellenangabe/Zitation zeigen
- Konzept nebenbei erklären: Beim Klick auf **Knowledge hinzufügen** zeigt Copilot Studio Quelltypen wie **Dateiupload, öffentliche Websites, SharePoint, Azure AI Search, Dataverse, Dynamics 365, Salesforce, ServiceNow, Azure SQL** (das genaue Angebot kann je nach Environment/Lizenz variieren); Unterschied zu **Microsoft IQ** (dynamischer, berechtigungsabhängiger M365-Kontext) kurz wiederholen aus Block 3

**Tools (5 Min):**
- Im **Build**-Tab den Bereich **Tools** öffnen, das dort hinterlegte Beispiel-Tool anklicken und **Name** sowie **Beschreibung** zeigen
- Im **Preview**-Chat eine Frage stellen, die das Tool triggert, und beobachten, wie der Agent das Tool aufruft
- Konzept nebenbei erklären: Tools erlauben Aktionen statt nur Antworten (Daten abrufen, Datensätze anlegen, Benachrichtigungen senden, Workflows anstoßen); genau **drei Tool-Typen**: **Connectors** (fertige Anbindungen an bekannte Dienste), **MCP-Server** (für individuelle/interne Services und APIs) und **Workflows** (mehrstufige, in Copilot Studio selbst gebaute automatisierte Abläufe für wiederkehrende, deterministische Prozesse); entscheidend sind **Name und Beschreibung**, da der Orchestrator danach auswählt

**Skills (5 Min):**
- Im **Build**-Tab den Bereich **Skills** öffnen, die hinterlegte Beispiel-Skill anklicken und den Markdown-Inhalt (Name, Beschreibung, Anweisungen) zeigen
- Kurz den Unterschied zu Tools live sichtbar machen: keine externe Systemanbindung, sondern in sich geschlossene Anweisungen/Logik
- Erwähnen: portabel als `SKILL.md`-Datei oder ZIP-Paket, wiederverwendbar über mehrere Agents hinweg
- Praktischer Hinweis für später (Hands-on): Skill-Namen dürfen laut Doku nur Kleinbuchstaben, Zahlen und Bindestriche enthalten und weder mit einem Bindestrich beginnen noch enden

**Abgrenzungs-Tabelle (mündlich zusammenfassen, nicht als Folie zeigen):**

| Komponente | Zweck | Verwaltet über |
|---|---|---|
| Instructions | Grundverhalten & Persönlichkeit | Identitäts-Konfiguration |
| Knowledge | Daten, auf die referenziert wird | Wissensquellen |
| Tools | Aktionen über externe Systeme | Connectors, MCP-Server, Workflows |
| Skills | Wiederverwendbare, aufgabenspezifische Fähigkeiten | Markdown-Dateien/Pakete |

**Interaktion (Diskussion, 3–4 Min):** "Für euren Wunsch-Agent: Braucht ihr eher Knowledge, ein Tool, oder reichen gute Instructions?" – kurze Zurufrunde, Trainer ordnet Beispiele live am Referenz-Agent zu (z. B. den passenden Bereich im Build-Tab nochmal kurz aufklappen).

---

### PAUSE (5 Min)

---

### 7. Hands-on: Gemeinsam einen Agent bauen (30 Min)

*Quellen: [Create an agent](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/authoring-first-bot), [Quickstart: natural language](https://learn.microsoft.com/en-us/microsoft-copilot-studio/create-automation-natural-language)*

**Format:** Der Trainer baut live einen Beispiel-Agent Schritt für Schritt vor; Teilnehmende bauen parallel auf eigenen Laptops mit (idealerweise ihre eigene mitgebrachte Idee, sonst ein vorgegebenes Beispiel-Szenario, z. B. "Onboarding-Assistent" oder "IT-Support-FAQ-Bot"). Trainer + ggf. Co-Trainer gehen währenddessen herum / schauen in Break-out-Räume, um zu helfen.

**Schritt-für-Schritt-Ablauf:**

1. **Anlegen (5 Min)**
   - In [copilotstudio.microsoft.com](https://copilotstudio.microsoft.com) einloggen → **Home** → Kachel **Agent** wählen (oder **Agents** → **New Agent**)
   - Agent-Namen vergeben (Hinweis: Der zuletzt eingegebene Name vor dem ersten Speichern bestimmt den technischen Schemanamen – danach nicht mehr änderbar)
   - Optional: Sprache/Solution anpassen

2. **Instructions schreiben (6 Min)**
   - Rolle, Ton, Grenzen als natürlichsprachigen Text im Instructions-Feld eintragen (Teilnehmende nutzen ihre Stichpunkte aus Block 4)
   - Speichern → **Preview**- und **Evaluate**-Tab werden freigeschaltet

3. **Knowledge hinzufügen (7 Min)**
   - Im **Build**-Tab auf **Knowledge** klicken → im Dialog **Add knowledge** eine Quelle wählen: Datei per Drag&Drop hochladen, oder Quelltyp wie **Public websites**/**SharePoint** auswählen und konfigurieren → **Save**/**Add**
   - Kurz erklären: Der Agent entscheidet selbst, wann er darauf zugreift

4. **Ein Tool oder eine Skill hinzufügen (7 Min)**
   - Je nach Zeit/Umgebung: im **Build**-Tab auf **Tools** klicken → im Dialog nach einem Connector/MCP-Server/Workflow suchen oder filtern → Tool auswählen, Details/Beschreibung prüfen → **Add**; alternativ im Bereich **Skills** auf **Create from blank** → Name (nur Kleinbuchstaben/Zahlen/Bindestriche, kein Bindestrich am Anfang/Ende), Beschreibung und Markdown-Instructions eintragen → **Create**
   - Wichtig: gute, präzise **Namen und Beschreibungen** vergeben – das entscheidet, ob der Agent das Tool/die Skill findet und korrekt aktiviert

5. **Erste Live-Tests (5 Min)**
   - Direkt im **Preview**-Tab 2–3 Testfragen stellen
   - Gemeinsam beobachten: Nutzt der Agent die Wissensquelle? Wird das Tool korrekt ausgelöst?
   - Kleine Korrekturen an Instructions vornehmen und Effekt sofort erneut testen (iteratives Prinzip aus Block 4 wird hier praktisch erlebt)

**Facilitator-Tipps:**
- Vorher ein Fallback-Szenario vorbereiten, falls Teilnehmende keine eigene Idee mitgebracht haben ("IT-Helpdesk-FAQ-Agent" mit einem Beispiel-PDF)
- Zeitboxen sichtbar machen (Timer einblenden), damit die Gruppe im Takt bleibt
- Nach jedem Teilschritt kurz im Plenum nachfragen: "Wer ist mitgekommen? Wer hängt?" – niedrige Hemmschwelle für Fragen schaffen

---

### 8. Testen im Preview-Tab & Veröffentlichen (10 Min)

*Quelle: [Quickstart: natural language – Publish-Abschnitt](https://learn.microsoft.com/en-us/microsoft-copilot-studio/create-automation-natural-language)*

- Vertiefender Blick auf den **Preview**-Tab als Testumgebung. Kurze Faustregel zum Unterschied zu **Evaluate** (laut Doku):

  | Szenario | Preview | Evaluate |
  |---|---|---|
  | Schnelles, interaktives Testen während der Entwicklung | ✓ | |
  | Eine einzelne Antwort/einen Tool-Aufruf debuggen | ✓ | |
  | Instructions oder Knowledge iterativ verfeinern | ✓ | |
  | Qualität über viele Testfälle hinweg messen | | ✓ |
  | Wiederholbares, automatisiertes Testen vor dem Publish | | ✓ |

  → Für den Workshop reicht **Preview**; **Evaluate** als "nächster Reifegrad" für den produktiven Einsatz erwähnen.

- Live-Demo Veröffentlichung:
  1. Agent öffnen → Chevron neben **Publish** → Dialog **Publish agent** öffnet sich, zeigt Agent-Details und zu konfigurierende Kanäle
  2. Falls der Dialog anzeigt, dass Name, Beschreibung oder Instructions fehlen: das live beheben (guter Realitäts-Check, dass Copilot Studio unvollständige Agents nicht klaglos veröffentlicht)
  3. Falls beim Publizieren eine Sicherheitswarnung erscheint (Copilot Studio führt vor jedem Publish automatisch einen **Security-Scan** durch und warnt, wenn eine der drei Standardeinstellungen aus Block 2 geändert wurde – Authentifizierung, Maker-Credentials, Teilen mit allen): kurz stehen bleiben und live zeigen – das ist der greifbarste Moment im gesamten Workshop, um die Risiko-Botschaft aus Block 2 zu bestätigen ("Seht ihr, das Tool warnt euch selbst, wenn eine dieser drei Einstellungen verändert wurde")
  4. Kanal **Demo website** wählen und konfigurieren
  5. **Publish** auswählen, Fortschritt abwarten → nach Erfolg erscheint eine Bestätigung mit Optionen zum Teilen bzw. Hinzufügen zum Organisationskatalog
  6. URL kopieren und in den Chat/auf den Bildschirm teilen, damit alle den live veröffentlichten Agent sofort ausprobieren können
- **Wichtiger Hinweis:** Mit einer Trial-Lizenz ist dieser Schritt nicht möglich – ggf. vorher klären, wessen Lizenz für die Live-Demo verwendet wird
- Kurzer Ausblick: Weitere Kanäle (Teams, Website-Widget, Power Pages …) existieren, werden hier nur erwähnt, nicht vertieft (Zeitgrund)
- Hinweis: Jede spätere Änderung am Agent erfordert ein erneutes Publizieren, bevor Nutzer:innen sie sehen ("Publish updates")
- Kurze Erinnerung an Risikofeld 4 aus Block 2 ("Teilen auf 'Everyone in the organization' ausweiten"): Mit dem Klick auf **Publish** und der Kanal-/Freigabewahl entscheidet man bewusst, wer über den Link Zugriff bekommt

**Interaktion:** Alle Teilnehmenden testen kurz den live veröffentlichten Demo-Agent auf dem eigenen Handy/Laptop und posten eine Beobachtung in den Chat ("Was hat gut funktioniert, was nicht?").

---

### 9. Offene Fragen, Wrap-up, nächste Schritte (10 Min)

- Freie Fragerunde (aktiv einladen, ggf. gesammelte Chat-Fragen aus den vorherigen Blöcken aufgreifen)
- Zusammenfassung der 6 Lernziele – kurzer Abgleich, ob erreicht
- Nächste Schritte für die Teilnehmenden benennen:
  - Eigenen Agent in der Sandbox weiterbauen (mitgebrachte Idee)
  - Wo finden sie Hilfe? (interner Kanal/Ansprechpartner des Citizen Developer Programms, Microsoft-Learn-Dokumentation)
  - Ausblick auf mögliche Folge-Workshops (z. B. Tools/Connectors vertiefen, Evaluate-Tab & Qualitätsmessung, Governance-Deep-Dive)
- Feedback einholen (kurze Live-Umfrage oder Zuruf: "Ein Wort, das euren Eindruck vom Workshop beschreibt")

---

## Glossar (als Handout/Cheat-Sheet nutzbar)

| Begriff | Kurzerklärung |
|---|---|
| **Agent** | Die in Copilot Studio gebaute KI-Anwendung, die Fragen beantwortet und/oder Aktionen ausführt |
| **LLM (Large Language Model)** | Das statistische Sprachmodell hinter dem Agent; sagt Wort für Wort die statistisch wahrscheinlichste Fortsetzung eines Textes vorher – keine Garantie für inhaltliche Korrektheit |
| **Build-Tab** | Zentrale Konfigurationsoberfläche eines Agents (Instructions, Model, Knowledge, Tools, Skills …) |
| **Instructions** | Natürlichsprachige Beschreibung von Rolle, Ton, Grenzen des Agents |
| **Knowledge** | Explizit verbundene Datenquellen, auf die der Agent zugreifen kann |
| **Microsoft IQ** | Dynamischer Zugriff auf M365-Organisationskontext (Mail, Kalender, Teams) |
| **Tools** | Anbindungen an externe Systeme, mit denen der Agent Aktionen ausführt – drei Typen: Connectors, MCP-Server, Workflows |
| **Skills** | Wiederverwendbare, Markdown-basierte Verhaltensbausteine für spezifische Aufgaben |
| **Connected Agents** | Andere, spezialisierte Agents, die als Kollaborationspartner eingebunden werden |
| **Memory** | Kontext, den der Agent pro Nutzer:in und pro Agent über mehrere Gespräche hinweg behält |
| **Orchestrierung** | Die Laufzeit-Logik, die entscheidet, wann Wissen/Tools/Skills eingesetzt werden |
| **Escalate-System-Topic (nur klassische Experience)** | Fest konfigurierbarer Topic mit Transfer-conversation-Node, der deterministisch (z. B. nach zwei erfolglosen Versuchen) an einen Menschen übergibt – existiert in der neuen Experience nicht; dort nur über weiche Instructions-Formulierungen nachbildbar |
| **Preview-Tab** | Testchat zum interaktiven Ausprobieren des Agents vor Veröffentlichung |
| **Evaluate-Tab** | Strukturierte Testsets zur systematischen, wiederholbaren Qualitätsmessung |
| **Monitor-Tab** | Übersicht über Aktivität/Nutzung des Agents nach Go-Live |
| **Security-Scan** | Automatische Prüfung von Copilot Studio vor jedem Publish; warnt, wenn Authentifizierung, Tool-Credentials oder Freigabe von den sicheren Standardeinstellungen abweichen |
| **Fabrication/Halluzination** | Der Agent erfindet oder kombiniert Informationen, die nicht in den zugrunde liegenden Daten stehen |
| **Environment** | Abgegrenzter Arbeitsbereich (z. B. Sandbox vs. Produktiv) in Power Platform |
| **Publish** | Veröffentlichung des Agents auf einem Kanal (Demo-Website, Teams, SharePoint, Power Pages …) |

---

## Referenzen (verwendete Microsoft-Learn-Quellen)

- [Quickstart: Create an automated solution with natural language](https://learn.microsoft.com/en-us/microsoft-copilot-studio/create-automation-natural-language)
- [Agents overview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/overview)
- [Create an agent (authoring-first-bot)](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/authoring-first-bot)
- [Build an agent overview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/build-overview)
- [Configure agent details and instructions](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/authoring-instructions)
- [Knowledge overview for agents](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/knowledge-copilot-studio)
- [Tools overview for agents](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/tools-overview)
- [Skills overview for agents](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/skills-overview)
- [Security and governance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance)
- Ergänzend ausgewertet: die vollständige, lokal abgelegte Copilot-Studio-Dokumentation (`microsoft-copilot-studio.md`, ~55.000 Zeilen), durchsucht über das mitgelieferte [search_docs.py](search_docs.py) – u. a. für die Details zu Security-Scan/Standardeinstellungen, Tool-Typen, Microsoft-IQ-Quellen, Memory-Mechanik und Skill-Namenskonventionen

*Hinweis: Alle referenzierten Seiten sind aktuell als "prerelease documentation"/Preview gekennzeichnet (neue Agent-Experience). Vor dem Workshop empfiehlt es sich, kurz zu prüfen, ob sich UI-Bezeichnungen zwischenzeitlich geändert haben.*
