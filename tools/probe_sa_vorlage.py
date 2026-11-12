import os, re
here = os.path.dirname(os.path.abspath(__file__))

# ---------- Zahlengerade ----------
def zg():
    x0, step, y = 30, 34, 40
    s = ['<svg width="600" height="78" viewBox="0 0 600 78" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica" font-size="14">']
    s.append(f'<line x1="{x0-15}" y1="{y}" x2="{x0+16*step+25}" y2="{y}" stroke="#222" stroke-width="1.6"/>')
    s.append(f'<polygon points="{x0+16*step+32},{y} {x0+16*step+22},{y-5} {x0+16*step+22},{y+5}" fill="#222"/>')
    for i in range(17):
        x = x0 + i*step
        big = i % 4 == 0
        h = 10 if big else 5
        s.append(f'<line x1="{x}" y1="{y-h}" x2="{x}" y2="{y+h}" stroke="#222" stroke-width="{1.6 if big else 1}"/>')
        if big:
            v = i//4 - 2
            lab = f'−{-v}' if v < 0 else str(v)
            s.append(f'<text x="{x}" y="{y+28}" text-anchor="middle">{lab}</text>')
    for name, val in (('D', -0.75), ('E', 1.5)):
        x = x0 + (val+2)*4*step
        s.append(f'<circle cx="{x}" cy="{y}" r="4.5" fill="#c8102e"/><text x="{x}" y="{y-16}" text-anchor="middle" font-weight="bold" fill="#c8102e">{name}</text>')
    s.append('</svg>')
    return ''.join(s)

# ---------- Bilder (selbst gezeichnet) ----------
ROBSON = '''<svg width="150" height="130" viewBox="0 0 150 130" xmlns="http://www.w3.org/2000/svg">
<ellipse cx="75" cy="122" rx="55" ry="6" fill="#cfe3f5"/>
<path d="M30 118 Q20 80 50 62 Q75 50 100 64 Q125 82 118 118 Z" fill="#8f9aa6"/>
<path d="M48 118 Q45 92 75 86 Q104 92 100 118 Z" fill="#c9d1d9"/>
<path d="M30 112 Q12 116 8 126 Q26 126 40 118 Z" fill="#7a8591"/>
<path d="M118 112 Q136 116 142 126 Q124 126 110 118 Z" fill="#7a8591"/>
<circle cx="75" cy="48" r="32" fill="#9aa5b1"/>
<ellipse cx="75" cy="60" rx="17" ry="12" fill="#d5dbe1"/>
<circle cx="62" cy="44" r="6" fill="#111"/><circle cx="88" cy="44" r="6" fill="#111"/>
<circle cx="64" cy="42" r="2" fill="#fff"/><circle cx="90" cy="42" r="2" fill="#fff"/>
<ellipse cx="75" cy="55" rx="5" ry="3.5" fill="#222"/>
<path d="M70 62 Q75 66 80 62" stroke="#222" stroke-width="1.6" fill="none"/>
<circle cx="54" cy="56" r="4" fill="#f4a7b9" opacity=".8"/><circle cx="96" cy="56" r="4" fill="#f4a7b9" opacity=".8"/>
<g stroke="#555" stroke-width="1"><line x1="66" y1="59" x2="46" y2="56"/><line x1="66" y1="62" x2="47" y2="64"/><line x1="84" y1="59" x2="104" y2="56"/><line x1="84" y1="62" x2="103" y2="64"/></g>
<path d="M45 30 Q47 6 75 5 Q103 6 105 30 Z" fill="#ffcc00" stroke="#c99a00" stroke-width="1.5"/>
<path d="M38 30 L112 30 Q114 36 108 36 L42 36 Q36 36 38 30 Z" fill="#ffcc00" stroke="#c99a00" stroke-width="1.5"/>
<rect x="68" y="11" width="14" height="14" rx="3" fill="#c8102e"/><text x="75" y="23" font-family="Helvetica" font-size="11" font-weight="bold" fill="#fff" text-anchor="middle">R</text>
</svg>'''

TRUCK = '''<svg width="170" height="92" viewBox="0 0 170 92" xmlns="http://www.w3.org/2000/svg">
<rect x="6" y="34" width="112" height="38" rx="4" fill="#c8102e"/>
<path d="M118 34 L146 34 Q160 36 162 52 L162 72 L118 72 Z" fill="#c8102e"/>
<path d="M124 39 L144 39 Q153 41 155 52 L124 52 Z" fill="#bfe3ff" stroke="#7a1010" stroke-width="1.2"/>
<rect x="138" y="25" width="12" height="8" rx="2" fill="#2f7cf6"/>
<g stroke="#e8e8e8" stroke-width="3"><line x1="10" y1="26" x2="118" y2="26"/><line x1="10" y1="34" x2="118" y2="34"/></g>
<g stroke="#e8e8e8" stroke-width="2.4"><line x1="18" y1="26" x2="18" y2="34"/><line x1="34" y1="26" x2="34" y2="34"/><line x1="50" y1="26" x2="50" y2="34"/><line x1="66" y1="26" x2="66" y2="34"/><line x1="82" y1="26" x2="82" y2="34"/><line x1="98" y1="26" x2="98" y2="34"/><line x1="114" y1="26" x2="114" y2="34"/></g>
<rect x="6" y="54" width="156" height="6" fill="#ffcc00"/>
<rect x="18" y="40" width="26" height="12" rx="2" fill="#a30d25"/><rect x="52" y="40" width="26" height="12" rx="2" fill="#a30d25"/><rect x="86" y="40" width="26" height="12" rx="2" fill="#a30d25"/>
<circle cx="34" cy="74" r="12" fill="#222"/><circle cx="34" cy="74" r="5" fill="#bbb"/>
<circle cx="136" cy="74" r="12" fill="#222"/><circle cx="136" cy="74" r="5" fill="#bbb"/>
<circle cx="160" cy="64" r="3" fill="#ffe680"/>
</svg>'''

HELMET = '''<svg width="80" height="62" viewBox="0 0 80 62" xmlns="http://www.w3.org/2000/svg">
<path d="M12 44 Q12 8 40 6 Q68 8 68 44 Z" fill="#ffcc00" stroke="#c99a00" stroke-width="2"/>
<path d="M40 6 L40 44" stroke="#e0b000" stroke-width="5"/>
<path d="M2 44 L78 44 Q80 54 70 54 L10 54 Q0 54 2 44 Z" fill="#ffcc00" stroke="#c99a00" stroke-width="2"/>
<rect x="31" y="18" width="18" height="16" rx="3" fill="#c8102e"/>
</svg>'''

HYDRANT = '''<svg width="54" height="74" viewBox="0 0 54 74" xmlns="http://www.w3.org/2000/svg">
<rect x="8" y="66" width="38" height="7" rx="2" fill="#7a1010"/>
<rect x="14" y="22" width="26" height="44" rx="4" fill="#c8102e"/>
<path d="M12 22 Q27 4 42 22 Z" fill="#c8102e"/><rect x="23" y="4" width="8" height="7" rx="2" fill="#a30d25"/>
<rect x="4" y="32" width="10" height="12" rx="3" fill="#a30d25"/><rect x="40" y="32" width="10" height="12" rx="3" fill="#a30d25"/>
<circle cx="27" cy="42" r="6" fill="#ffcc00"/>
</svg>'''

def bubble(text):
    return f'<div class="bubble">{text}</div>'

def task(nr, pts, body, heft=False, extra_left=''):
    left = f'<div class="nr">{nr}.</div>' + ''.join(f'<div class="pt">({p})</div>' for p in pts)
    if heft: left += '<div class="heft">Heft</div>'
    left += extra_left
    return f'<tr><td class="lc">{left}</td><td class="rc">{body}</td></tr>'

def teil(text):
    return f'<tr class="teil"><td colspan="2">{text}</td></tr>'

def zm(nums):
    head = '<tr><th>Zahl</th>' + ''.join(f'<th>{h}</th>' for h in ['ℕ','ℤ⁺','ℤ⁻','ℤ','ℚ⁺','ℚ⁻','ℚ']) + '</tr>'
    return '<table class="zm">' + head + ''.join(f'<tr><td>{n}</td>' + '<td></td>'*7 + '</tr>' for n in nums) + '</table>'

BX = '<span class="bx"></span>'
L = lambda w=160: f'<span class="ln" style="width:{w}px"></span>'
RF = '<span class="rf">richtig <span class="bx s"></span> falsch <span class="bx s"></span></span>'

rows = []
rows.append(teil('<b>Teil 1:</b> Grundkompetenzen'))
rows.append(task(1, ['3P'], f'''Penny sortiert die Feuerwehrschläuche nach Zahlen. Kreuze an, zu welchen <span class="kw">Zahlenmengen</span> die Zahl gehört.
<div style="margin-top:6px">{zm(['−{14/7}', '0,6', '{24/8}'])}</div>'''))
rows.append(task(2, ['2P', '2P'], f'''<b>a)</b> Zeichne auf der Zahlengeraden ein: &nbsp; A = −1,75 &nbsp;·&nbsp; B = −{{1/2}} &nbsp;·&nbsp; C = {{1 1/4}}
<div class="zg">{zg()}</div>
<b>b)</b> Lies die Punkte D und E ab. Schreibe sie als <span class="kw">Bruch</span> und als <span class="kw">Dezimalzahl</span>.<br>
<div class="frow">D = {L(170)} &nbsp;&nbsp;&nbsp; E = {L(170)}</div>'''))
rows.append(task(3, ['3P'], f'''Setze <b>&lt;</b> , <b>&gt;</b> oder <b>=</b> ein.
<div class="cmp"><span>−0,6 {BX} −0,65</span><span>−{{2/3}} {BX} −{{3/5}}</span><span>−{{1 1/4}} {BX} −1,25</span></div>'''))
rows.append(task(4, ['3P'], f'''Entscheide, ob die Aussagen <span class="kw">richtig</span> oder <span class="kw">falsch</span> sind.
<table class="rft">
<tr><td>a) −1,8 liegt näher an −2 als an −1.</td><td>{RF}</td></tr>
<tr><td>b) −{{3 2/5}} liegt näher an −4 als an −3.</td><td>{RF}</td></tr>
<tr><td>c) −0,5 liegt genau in der Mitte zwischen −1 und 0.</td><td>{RF}</td></tr>
</table>'''))
rows.append(task(5, ['1P', '1P', '1P'], f'''<div class="frow"><b>a)</b> |−4,2| = {L(80)} &nbsp;&nbsp; Gegenzahl von −{{3/5}}: {L(80)}</div>
<div class="frow"><b>b)</b> −(−(−6)) = {L(80)}</div>
<div class="frow" style="padding-top:18px"><b>c)</b> Schreibe über jedes Minuszeichen <b>V</b> (Vorzeichen), <b>R</b> (Rechenzeichen) oder <b>G</b> (Gegenzahl). Rechne dann aus.</div>
<div class="frow" style="padding-top:22px; font-size:15pt">−(−2) − 5 = {L(220)}</div>'''))
rows.append(task(6, ['3P'], f'''Wandle um.
<div class="frow">−0,45 als <span class="kw">gekürzter Bruch</span>: {L(120)} &nbsp;&nbsp; 1,8 als <span class="kw">gemischte Zahl</span>: {L(110)}</div>
<div class="frow">{{3/8}} als Dezimalzahl: {L(120)}</div>'''))

rows.append(teil('<b>Teil 2:</b> Anwendung und Vernetzung &nbsp;<span class="small">(Rechne im Heft. Schreibe jeden Schritt mit = untereinander, NR am Rand.)</span>'))
rows.append(task(7, ['3P'], f'''Berechne. <div class="frow">−4,8 + 2,3 − (−1,5) − 3,6 =</div>''', heft=True))
rows.append(task(8, ['3P'], f'''Berechne. <span class="kw">Kürze</span> und schreibe das Ergebnis als <span class="kw">gemischte Zahl</span>.
<div class="frow">{{1 2/3}} − {{2 3/4}} + (−{{1/6}}) =</div>''', heft=True))
rows.append(task(9, ['2P', '2P'], f'''Berechne und kürze so weit wie möglich.
<div class="frow"><b>a)</b> (−{{3 3/4}}) · (−{{8/15}}) = &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>b)</b> (−{{4/9}}) : (+{{1 1/3}}) =</div>''', heft=True))
rows.append(task(10, ['3P', '2P'], f'''Berechne. Achte auf die <span class="kw">Klammern</span> und auf <span class="kw">Punkt vor Strich</span>.
<div class="frow"><b>a)</b> [−6 − (1,5 − 4)] · (−3) =</div>
<div class="frow"><b>b)</b> (−24) : [−5 − (−2) · 4 + 1] =</div><div style="height:62px"></div>''', heft=True))
rows.append(task(11, ['3P', '3P', '2P'], f'''Schreibe jeweils eine <span class="kw">Rechnung</span> und eine <span class="kw">Antwort</span> mit Einheit.
<div class="tx"><b>a)</b> Sam steht auf der Drehleiter von Jupiter <b>12 m über</b> dem Meer. Robson die Robbe taucht im Hafen von Pontypandy <b>4,5 m unter</b> der Wasseroberfläche. Wie groß ist der Höhenunterschied zwischen den beiden?
<div class="ra">Rechnung: {L(430)}</div><div class="ra">Antwort: {L(440)}</div></div>
<div class="tx"><b>b)</b> Am Pontypandy-Berg hat es in der Früh <b>−6 °C</b>. Bis Mittag steigt die Temperatur um <b>9 °C</b>, bis zum Abend fällt sie wieder um <b>5,5 °C</b>. Wie viel Grad hat es am Abend?
<div class="ra">Rechnung: {L(430)}</div><div class="ra">Antwort: {L(440)}</div></div>
<div class="tx"><b>c)</b> Dilys hat {{4 1/2}} kg Kekse im Laden. Norman kauft {{1/6}} davon. Wie viel kg Kekse kauft Norman?
<div class="ra">Rechnung: {L(430)}</div><div class="ra">Antwort: {L(440)}</div></div>''', extra_left='<div class="pic-l">'+HYDRANT+'</div>'))
rows.append(task(12, ['6P'], f'''Berechne. <span class="kw">Kürze</span> das Ergebnis, schreibe es wenn möglich als <span class="kw">gemischte Zahl</span> und auch als <span class="kw">Dezimalzahl</span>.
<div class="frow" style="font-size:15pt; padding:14px 0 8px">[{{2 1/3}} + (−{{1 1/6}})] : [{{1/3}} − {{1 1/9}}] + {{3/4}} =</div>''', heft=True))

footer = f'''<tr class="foot"><td colspan="2"><div class="footin">
<div class="robson">{bubble('Du schaffst das!')}{ROBSON}<div class="rname">Robson</div></div>
<div class="beurt"><b>Beurteilung:</b><br>
Teil 1: ________ Punkte von 19 Punkten erreicht<br>
Teil 2: ________ Punkte von 29 Punkten erreicht<br>
Gesamt: ________ Punkte von 48 Punkten erreicht</div></div></td></tr>
<tr class="scale"><td colspan="2"><div class="sc"><span>Sehr gut 44–48 P</span><span>Gut 38–43 P</span><span>Befriedigend 30–37 P</span><span>Genügend 24–29 P</span><span>Nicht genügend 0–23 P</span></div></td></tr>'''

html = f'''<!doctype html><html lang="de"><head><meta charset="utf-8"><title>Probe-SA</title>
<style>
@page {{ size:A4; margin:12mm 12mm 12mm 12mm; }}
* {{ box-sizing:border-box; }}
body {{ font-family:"Century Gothic","Avenir Next","Helvetica Neue",Arial,sans-serif; font-size:11.5pt; color:#111; margin:0; line-height:1.4; }}
.head {{ background:#c8102e; color:#fff; display:flex; align-items:center; gap:18px; padding:10px 12px 10px 12px; font-weight:bold; font-size:14.5pt; border:1px solid #7a1010; border-bottom:none; position:relative; }}
.head .name {{ flex:1; display:flex; align-items:center; gap:8px; }}
.head .name span {{ flex:1; background:#fff; height:30px; border-radius:6px; }}
.stripe {{ height:12px; background:repeating-linear-gradient(-45deg,#ffcc00 0 12px,#111 12px 24px); border-left:1px solid #7a1010; border-right:1px solid #7a1010; }}
.helm {{ position:absolute; right:-6px; top:-30px; }}
table.sa {{ width:100%; border-collapse:collapse; border:1px solid #7a1010; }}
table.sa > tbody > tr > td {{ border-top:1px solid #7a1010; vertical-align:top; }}
tr {{ break-inside:avoid; }}
td.lc {{ width:62px; background:#f6c9c9; padding:8px 8px; border-right:1px solid #7a1010; position:relative; }}
td.rc {{ padding:8px 12px 10px; position:relative; }}
.nr {{ font-weight:bold; margin-bottom:14px; }} .pt {{ margin:6px 0 22px; }}
.heft {{ color:#a30d25; font-weight:bold; margin-top:10px; }}
.pic-l {{ position:absolute; bottom:8px; left:4px; }}
tr.teil td {{ background:#f6c9c9; padding:6px 10px; font-size:12.5pt; }}
.kw {{ color:#c8102e; font-weight:bold; }}
.small {{ font-size:9.5pt; color:#333; }}
table.zm {{ border-collapse:collapse; width:100%; }} .zm th,.zm td {{ border:1px solid #7a1010; text-align:center; height:34px; }}
.zm th {{ background:#f6c9c9; font-weight:normal; }} .zm td:first-child {{ width:95px; font-size:13pt; }}
.zg {{ margin:4px 0 2px 10px; }}
.frow {{ font-size:13pt; padding:9px 0 4px; white-space:nowrap; }}
.ln {{ display:inline-block; border-bottom:1px solid #333; height:1em; vertical-align:baseline; }}
.bx {{ display:inline-block; width:30px; height:26px; border:1.5px solid #c8102e; border-radius:5px; vertical-align:middle; margin:0 8px; }}
.bx.s {{ width:20px; height:18px; margin:0 12px 0 4px; }}
.cmp {{ display:flex; justify-content:space-around; font-size:13pt; padding:12px 0 6px; }}
table.rft {{ width:100%; border-collapse:collapse; margin-top:4px; }} .rft td {{ padding:7px 2px; border-bottom:1px dotted #999; font-size:12pt; }} .rft td:last-child {{ text-align:right; white-space:nowrap; }}
.tx {{ margin:8px 0 6px; padding-right:4px; }} .ra {{ margin:12px 0 0 18px; }}
.fr {{ display:inline-flex; flex-direction:column; vertical-align:middle; text-align:center; font-size:.95em; line-height:1.1; margin:0 1px; }}
.fr .n {{ border-bottom:1px solid currentColor; padding:0 2px; }} .fr .d {{ padding:0 2px; }} .mx {{ white-space:nowrap; }}
.ph {{ position:absolute; mix-blend-mode:multiply; }}
.truck {{ position:absolute; right:10px; bottom:8px; }}
tr.foot td {{ padding:8px 12px; }}
.footin {{ display:flex; align-items:flex-end; gap:30px; }}
.robson {{ position:relative; width:210px; padding-top:44px; }}
.robson svg {{ margin-left:0; }}
.rname {{ font-weight:bold; color:#555; margin-left:52px; font-size:10pt; }}
.bubble {{ position:absolute; left:120px; top:0; border:2px solid #c8102e; border-radius:50%; padding:10px 16px; color:#c8102e; font-weight:bold; font-size:11pt; text-align:center; background:#fff; white-space:nowrap; }}
.bubble:after {{ content:""; position:absolute; left:14px; bottom:-12px; border:7px solid transparent; border-top:10px solid #c8102e; transform:rotate(20deg); }}
.beurt {{ line-height:2.3; font-size:12pt; padding-bottom:14px; }}
tr.scale td {{ padding:0; }}
.sc {{ display:flex; background:#c8102e; color:#fff; font-size:10pt; }} .sc span {{ flex:1; text-align:center; padding:6px 2px; border-right:1px solid #fff; }} .sc span:last-child {{ border-right:none; }}
</style></head><body>
<div class="head">Probe-Schularbeit · Mo 9.11.2026 &nbsp; Mathematik 3. Klasse <div class="name">Name: <span></span></div></div>
<div class="stripe"></div>
<table class="sa"><tbody>
{''.join(rows)}
{footer}
</tbody></table>
</body></html>'''

# Bilder in Aufgaben platzieren
html = html.replace('Wandle um.', '<img class="ph" src="img/penny.jpeg" style="right:28px;top:6px;height:122px">Wandle um.', 1)
html = html.replace('Berechne. Achte auf die', '<img class="ph" src="img/sam.jpg" style="right:30px;top:8px;height:160px;filter:brightness(1.04)">Berechne. Achte auf die', 1)
html = html.replace('Berechne. <div class="frow">−4,8', '<img class="ph" src="img/jupiter.jpeg" style="right:14px;top:2px;height:118px">Berechne. <div class="frow">−4,8', 1)
open(os.path.join(here, 'sa.src.html'), 'w').write(html)
