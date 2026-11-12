# Mathematik-Lernbegleitung (Tochter, Unterstufe)

Der Vater bereitet mit der Tochter die Mathematik-Schularbeiten vor. Lehrerin: Bettina Windhaber. Pro Schularbeit gibt es einen Ordner, zum Beispiel `Lehrer_Bettina_Windhaber/3_Klasse/1_SA/`, mit eigener `CLAUDE.md`, Lernplan, Tagesübungen und Lösungen.

## Bisherige Schularbeiten
| SA | Datum | Stoff | Probe-SA | Ergebnis | Analyse |
|---|---|---|---|---|---|
| 3. Kl. 1. SA | 10.11.2026 | rationale Zahlen, Brüche | 39,5/48 (Vortag) | **35/48 Befriedigend** | `Lehrer_Bettina_Windhaber/3_Klasse/1_SA/Analyse_1_M-SA.md` |

## Ablauf, der sich bewährt hat
1. **Material sichten:** Lernzielblatt der Lehrerin, Hefte (Schulübung, Hausübung, Theorieheft) als Scan, Buchseiten, Zettel der Lehrerin.
2. **Lernplan** `Lernplan_N_M-SA.md` mit Tagesplan, Liste der Heft-Aufgaben, Fehlerliste (F1, F2, …) und Bauplan der Probe-SA.
3. **Täglich:**
   - Der Vater schickt den Scan der erledigten Übung (`Tagesübungen/Übungen_gemacht_TagN.pdf`).
   - Ich analysiere ihn, trage neue Fehler in die Fehlerliste ein und schreibe den Entwurf `TagN_TT-MM_Entwurf.md` mit Lösungen.
   - Erst nach der Freigabe baue ich die PDFs: `Tagesübungen/TagN_TT-MM_Uebung.pdf` (Blatt + Mini-Test am Schluss) und `Lösungen/TagN_TT-MM_Loesungen.pdf` (für Papa, mit Fehlernummern).
4. **Probe-SA** im Stil der Lehrerin (48 P, Teil 1 / Teil 2, Notenschlüssel), 50 min unter echten Bedingungen.
5. **Nach der SA:** Scan analysieren, `Analyse_N_M-SA.md` schreiben und die Tabelle oben ergänzen.

## Erkenntnisse aus der 1. SA (für die Planung jeder weiteren SA)
- **Die Lehrerin nimmt Heft- und Buchaufgaben fast wörtlich** (2026: Nr. 172 b und eine Variante von 168 d). → Heft- und Buchaufgaben samt Varianten haben Vorrang.
- **Teil 1 (Grundwissen) bringt etwa die Hälfte der Punkte** (2026: 25 von 48). Er fragt Begriffe auch **umgekehrt** ab: Vorzeichen ergänzen, wahr/falsch mit Sonderfall 0, Buchstaben auf der Zahlengeraden mit Betrag, „begründe“. → Zu jedem Begriff diese Formate üben. Die Probe-SA ebenso gewichten.
- **Probe-SA 4–5 Tage vorher**, nicht am Vortag. Fehler aus der Probe-SA, die nur am Vorabend verbessert wurden, kamen in der SA wieder (Punkt vor Strich, verschiedene Vorzeichen).
- **Fehler-Drill:** Jeder Fehler aus der Fehlerliste kommt mit 2–3 Mini-Aufgaben in jede Tagesübung, bis er 3 Tage hintereinander richtig ist.
- **Textaufgaben** mit Skizze (senkrechte Zahlengerade), Rechnung und Antwortsatz mit Einheit. Höhenunterschied = oben − unten mit Vorzeichen.
- **Schluss-Check:** NR-Ergebnis richtig übertragen, kürzen, gemischte Zahl, Plausibilität. Die Lehrerin zieht dafür Punkte ab.
- **Tempo:** In den Übungen wurden die letzten Aufgaben oft nicht geschafft. Mini-Tests auf Zeit helfen.
- **Motivation:** Kleine Bilder und Wünsche der Tochter einbauen (Bär, Robson die Robbe, Feuerwehrmann-Sam-Thema). Das kommt sehr gut an.
- **8 Tage reichen knapp.** Besser sind 10–12 Tage mit Puffer nach der Probe-SA.

## Vereinbarungen (gelten für alle SAs)
- **Entwurf zuerst** als .md, PDF erst nach Freigabe des Vaters. Umfang knapp halten.
- **Kein Taschenrechner.** Alles muss von Hand lösbar sein.
- **Schreibweise der Schule:** `Rechnung:` / `Antwort:`, NR am Rand, Schritte untereinander mit `=`, kürzen, gemischte Zahlen.
- Nur Zettel der Lehrerin anhängen (`Übungen/`, `Arbeitsblätter/`). Online-Arbeitsblätter (lw3_ab_Sxx) wurden in der Schule nie verwendet.
- Nicht committen, außer der Vater sagt es.
- Bilder von Figuren nicht selbst aus dem Netz laden (fandom.com blockt Bots). Der Vater legt sie bei Bedarf selbst ab.

## Werkzeuge (`tools/`)
- `render.swift`: PDF-Seiten als JPG rendern, für große Scans. Bauen mit `swiftc -O tools/render.swift -o <scratchpad>/render`, aufrufen mit `render <pdf> <präfix> <skala> [seite]`.
- `pre.py`: Bruch-Kurzschreibweise im HTML: `{3/4}` wird zum gestapelten Bruch, `{2 1/3}` zur gemischten Zahl. Aufruf `python3 pre.py quelle.src.html ziel.html`.
- `style.css`: Stil der Tagesblätter (`.box`, `.tip`, `.task`, `.steps .dots`, `.frow`, `.ln`, `h1.page` für einen Seitenumbruch, `.err` rot in den Lösungen).
- `probe_sa_vorlage.py`: Generator der Probe-SA im Layout der Lehrerin (Kopfband, Punktespalte, Teil 1/2, Notenschlüssel, Zahlengerade als SVG). Die Bilder werden aus `img/` neben der Datei geladen.
- **HTML → PDF:** `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --no-pdf-header-footer --print-to-pdf=$PWD/f.pdf file://$PWD/f.html`
- **PDFs zusammenfügen:** mit Swift/PDFKit (`PDFDocument.insert`). Word-Zettel per AppleScript als PDF exportieren (siehe `1_SA/CLAUDE.md`).
