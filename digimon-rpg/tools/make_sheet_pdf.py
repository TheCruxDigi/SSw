# -*- coding: utf-8 -*-
"""Genera la ficha de personaje rellenable (PDF con campos AcroForm) de Digimon: Lazos de Código.
Uso: python3 make_sheet_pdf.py salida.pdf"""
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, white
from reportlab.pdfgen import canvas

OUT = sys.argv[1] if len(sys.argv) > 1 else "ficha_lazos_de_codigo.pdf"
W, H = A4
M = 28  # margen
INK = HexColor("#14213d"); MUTED = HexColor("#59647a"); LINE = HexColor("#c9d2de"); ACC = HexColor("#e8621a"); SUNK = HexColor("#eef2f6"); CYAN = HexColor("#13879a")

c = canvas.Canvas(OUT, pagesize=A4)
c.setTitle("Ficha de personaje — Digimon: Lazos de Código")
c.setAuthor("Digimon: Lazos de Código (obra de fans, no oficial)")
form = c.acroForm
_n = [0]

def fid(name):
    _n[0] += 1
    return f"{name}_{_n[0]}"

def label(x, y, t, size=6.6, col=MUTED, bold=True):
    c.setFillColor(col); c.setFont("Helvetica-Bold" if bold else "Helvetica", size); c.drawString(x, y, t.upper() if bold else t)

def field(name, x, y, w, h, lab=None, size=9, multi=False, align=0, big=False):
    if lab:
        label(x, y + h + 2.5, lab)
    form.textfield(name=fid(name), x=x, y=y, width=w, height=h, borderColor=LINE, fillColor=white, textColor=INK, borderWidth=0.8,
                   fontName="Helvetica-Bold" if big else "Helvetica", fontSize=size, fieldFlags="multiline" if multi else "", forceBorder=True,
                   **({"maxlen": 0} if False else {}))
    if align:
        pass

def check(name, x, y, lab, size=8):
    form.checkbox(name=fid(name), x=x, y=y, size=size, borderColor=LINE, fillColor=white, textColor=INK, buttonStyle="check", forceBorder=True)
    c.setFillColor(INK); c.setFont("Helvetica", 7.5); c.drawString(x + size + 3, y + 1.5, lab)

def section(x, y, w, t):
    c.setFillColor(INK); c.setFont("Helvetica-Bold", 10.5); c.drawString(x, y, t)
    c.setStrokeColor(ACC); c.setLineWidth(1.4); c.line(x, y - 3, x + w, y - 3)

def header(sub):
    c.setFillColor(INK); c.rect(0, H - 54, W, 54, stroke=0, fill=1)
    c.setFillColor(ACC)
    p = c.beginPath(); cx, cy, r = M + 12, H - 27, 12
    p.moveTo(cx - r * .5, cy + r * .87); p.lineTo(cx + r * .5, cy + r * .87); p.lineTo(cx + r, cy); p.lineTo(cx + r * .5, cy - r * .87); p.lineTo(cx - r * .5, cy - r * .87); p.lineTo(cx - r, cy); p.close()
    c.drawPath(p, stroke=0, fill=1)
    c.setFillColor(white); c.setFont("Helvetica-Bold", 17); c.drawString(M + 32, H - 26, "DIGIMON: LAZOS DE CÓDIGO")
    c.setFont("Helvetica", 9); c.drawString(M + 32, H - 40, sub)
    c.setFont("Helvetica", 6.5); c.drawRightString(W - M, H - 40, "Juego de rol de fans, no oficial y sin ánimo de lucro")

def footer(n):
    c.setFillColor(MUTED); c.setFont("Helvetica", 6.5)
    c.drawString(M, 16, "Digimon y todos sus nombres pertenecen a sus propietarios. Este proyecto no está afiliado ni respaldado por ellos.")
    c.drawRightString(W - M, 16, f"Página {n}/2")

# ---------------- página 1: Tamer ----------------
header("Ficha del Tamer")
y = H - 86
field("jugador", M, y, 160, 16, "Jugador/a")
field("tamer_nombre", M + 170, y, 210, 16, "Nombre del Tamer", size=11, big=True)
field("edad", M + 390, y, 50, 16, "Edad")
field("nivel_tamer", W - M - 70, y, 70, 16, "Nivel (1-10)", size=11, big=True)
y -= 32
field("aspecto", M, y, 300, 16, "Aspecto")
field("falta", M + 310, y, W - 2 * M - 310, 16, "¿Qué te falta en tu vida?")

# atributos
y -= 30
section(M, y, 250, "Atributos")
label(M + 98, y + 1, "reparte +2, +1, +1 y 0", bold=False, size=7)
ay = y - 52
attrs = [("Valor", "Coraje y cuerpo · Aguante"), ("Astucia", "Mente y técnica · Carga"), ("Corazón", "Empatía y voluntad"), ("Destreza", "Agilidad · Defensa")]
for i, (a, d) in enumerate(attrs):
    x = M + i * 64
    c.setFillColor(SUNK); c.roundRect(x, ay - 6, 58, 54, 5, stroke=0, fill=1)
    c.setFillColor(INK); c.setFont("Helvetica-Bold", 8); c.drawCentredString(x + 29, ay + 38, a.upper())
    form.textfield(name=fid("attr_" + a), x=x + 14, y=ay + 6, width=30, height=26, borderColor=LINE, fillColor=white, textColor=INK, fontName="Helvetica-Bold", fontSize=16, forceBorder=True)
    c.setFillColor(MUTED); c.setFont("Helvetica", 5.2); c.drawCentredString(x + 29, ay - 2, d)

# recursos
rx = M + 270
section(rx, y, W - M - rx, "Recursos")
res = [("XP", 0), ("Bits", 0)]
field("xp", rx, ay + 22, 70, 18, "XP", size=11, big=True)
field("vinculo", rx + 78, ay + 22, 70, 18, "Vínculo (1-5 o Estrella)", size=11, big=True)
field("bits", rx + 156, ay + 22, W - M - rx - 156, 18, "Bits", size=11, big=True)
pools = [("Chispa", "máx. 3 + Vínculo"), ("Aguante", "6 + Valor"), ("Carga", "3 + Astucia + Digivice")]
pw = (W - M - rx - 16) / 3
for i, (p, f) in enumerate(pools):
    x = rx + i * (pw + 8)
    label(x, ay + 6, p)
    form.textfield(name=fid(p + "_act"), x=x, y=ay - 14, width=pw / 2 - 4, height=18, borderColor=LINE, fillColor=white, textColor=INK, fontName="Helvetica-Bold", fontSize=11, forceBorder=True)
    c.setFillColor(MUTED); c.setFont("Helvetica", 9); c.drawCentredString(x + pw / 2, ay - 9, "/")
    form.textfield(name=fid(p + "_max"), x=x + pw / 2 + 4, y=ay - 14, width=pw / 2 - 4, height=18, borderColor=LINE, fillColor=white, textColor=INK, fontName="Helvetica", fontSize=11, forceBorder=True)
    c.setFont("Helvetica", 5.6); c.drawString(x, ay - 21, f)

# identidad
y = ay - 46
field("trasfondo", M, y, 120, 16, "Trasfondo")
field("senda", M + 128, y, 110, 16, "Senda")
field("virtud", M + 246, y, 90, 16, "Cualidad")
field("defecto", M + 344, y, 90, 16, "Defecto")
field("emblema", M + 442, y, W - M - (M + 442), 16, "Emblema")
y -= 30
field("digivice", M, y, 180, 16, "Digivice (modelo y función)")
field("rasgo_trasfondo", M + 188, y, W - 2 * M - 188, 16, "Rasgo del trasfondo")

# habilidades
y -= 28
section(M, y, 250, "Habilidades")
label(M + 82, y + 1, "0 sin entrenar · +1 entrenada · +2 experta", bold=False, size=7)
habs = [("Atletismo", "VAL/DES"), ("Sigilo", "DES"), ("Tecnología", "AST"), ("Saber Digital", "AST"), ("Observación", "AST/COR"), ("Supervivencia", "AST/VAL"),
        ("Medicina", "AST/COR"), ("Persuasión", "COR"), ("Engaño", "COR/AST"), ("Empatía", "COR"), ("Táctica", "AST/VAL"), ("Arte", "COR/DES")]
hy = y - 20
for i, (h, a) in enumerate(habs):
    col, row = i % 2, i // 2
    x = M + col * 128; yy = hy - row * 19
    form.textfield(name=fid("hab_" + h), x=x, y=yy, width=22, height=15, borderColor=LINE, fillColor=white, textColor=INK, fontName="Helvetica-Bold", fontSize=9, forceBorder=True)
    c.setFillColor(INK); c.setFont("Helvetica-Bold", 8); c.drawString(x + 27, yy + 6, h)
    c.setFillColor(MUTED); c.setFont("Helvetica", 6); c.drawString(x + 27, yy - 0.5, a)
# talentos al lado
tx = M + 270
section(tx, y, W - M - tx, "Talentos de Senda")
form.textfield(name=fid("talentos"), x=tx, y=hy - 96, width=W - M - tx, height=110, borderColor=LINE, fillColor=white, textColor=INK, fontName="Helvetica", fontSize=8.5, fieldFlags="multiline", forceBorder=True)

# programas y equipo
y = hy - 5 * 19 - 34
section(M, y, (W - 2 * M) / 2 - 8, "Programas (Tarjetas)")
section(M + (W - 2 * M) / 2 + 8, y, (W - 2 * M) / 2 - 8, "Equipo y objetos")
bw = (W - 2 * M) / 2 - 8
form.textfield(name=fid("programas"), x=M, y=y - 132, width=bw, height=124, borderColor=LINE, fillColor=white, textColor=INK, fontName="Helvetica", fontSize=8.5, fieldFlags="multiline", forceBorder=True)
form.textfield(name=fid("equipo"), x=M + bw + 16, y=y - 132, width=bw, height=124, borderColor=LINE, fillColor=white, textColor=INK, fontName="Helvetica", fontSize=8.5, fieldFlags="multiline", forceBorder=True)
y -= 150
section(M, y, W - 2 * M, "Notas, relaciones y arco del Emblema")
form.textfield(name=fid("notas_tamer"), x=M, y=36, width=W - 2 * M, height=y - 44, borderColor=LINE, fillColor=white, textColor=INK, fontName="Helvetica", fontSize=8.5, fieldFlags="multiline", forceBorder=True)
footer(1)
c.showPage()

# ---------------- página 2: compañero ----------------
header("Ficha del compañero Digimon")
y = H - 86
field("apodo", M, y, 150, 16, "Nombre o apodo", size=11, big=True)
field("especie", M + 158, y, 150, 16, "Especie (Novato)")
field("bebe2", M + 316, y, 110, 16, "Forma Bebé II")
field("rol_fijado", M + 434, y, W - M - (M + 434), 16, "Rol fijado")
y -= 30
field("personalidad", M, y, 150, 16, "Personalidad")
field("mejoras", M + 158, y, W - 2 * M - 158, 16, "Mejoras del compañero (se aplican a todas sus formas)")

# formas
y -= 28
section(M, y, W - 2 * M, "Formas desbloqueadas")
cols = [("Nivel", 62), ("Forma", 120), ("PV máx.", 44), ("PV act.", 44), ("Atq", 34), ("Def", 34), ("Arm", 34), ("Ini", 34), ("Dado", 36), ("Familia / Rol / Atributo", 0)]
tw = W - 2 * M
fixed = sum(w for _, w in cols)
cols[-1] = (cols[-1][0], tw - fixed)
yy = y - 16
x = M
for n, w in cols:
    label(x + 2, yy, n, size=6); x += w
niveles = ["Bebé II", "Novato", "Campeón", "Perfecto", "Definitivo", "Otra forma"]
for r, nv in enumerate(niveles):
    ry = yy - 20 - r * 20
    x = M
    for j, (n, w) in enumerate(cols):
        if j == 0:
            c.setFillColor(SUNK); c.rect(x, ry, w - 3, 16, stroke=0, fill=1)
            c.setFillColor(INK); c.setFont("Helvetica-Bold", 8); c.drawString(x + 4, ry + 5, nv)
        else:
            form.textfield(name=fid(f"forma_{r}_{n}"), x=x, y=ry, width=w - 3, height=16, borderColor=LINE, fillColor=white, textColor=INK, fontName="Helvetica", fontSize=8.5, forceBorder=True)
        x += w

# estado
y = yy - 20 - 6 * 20 - 10
section(M, y, W - 2 * M, "Estado en la escena")
sy = y - 20
for i, st in enumerate(["Hambriento", "Agotado", "Expuesto", "Quemado", "Envenenado", "Paralizado", "Congelado", "Asustado", "Confundido", "Atrapado", "Cegado", "Dormido"]):
    check("estado_" + st, M + (i % 6) * 89, sy - (i // 6) * 15, st)
field("otros_estados", M, sy - 46, W - 2 * M, 14, "Otros estados y duración", size=8)

# técnicas
y = sy - 66
section(M, y, W - 2 * M, "Técnicas de la forma actual")
tcols = [("Técnica", 150), ("Pot.", 32), ("Daño", 48), ("Alcance / Área", 84), ("Elemento", 62), ("Efectos y notas", 0)]
tcols[-1] = (tcols[-1][0], tw - sum(w for _, w in tcols))
ty = y - 16
x = M
for n, w in tcols:
    label(x + 2, ty, n, size=6); x += w
for r in range(7):
    ry = ty - 19 - r * 18
    x = M
    for n, w in tcols:
        form.textfield(name=fid(f"tec_{r}_{n}"), x=x, y=ry, width=w - 3, height=15, borderColor=LINE, fillColor=white, textColor=INK, fontName="Helvetica", fontSize=8, forceBorder=True)
        x += w
y = ty - 19 - 7 * 18 - 8
field("heredadas", M, y - 30, (W - 2 * M) / 2 - 6, 30, "Técnicas heredadas o aprendidas", size=8, multi=True)

# referencia rápida
qx = M + (W - 2 * M) / 2 + 6; qw = W - M - qx
c.setFillColor(SUNK); c.roundRect(qx, 30, qw, y - 30 + 8, 6, stroke=0, fill=1)
c.setFillColor(INK); c.setFont("Helvetica-Bold", 9); c.drawString(qx + 8, y - 6, "REFERENCIA RÁPIDA")
lines = [
    ("2d6 + modificador", "10+ éxito · 7–9 éxito con coste · 6– fallo (+1 Chispa)"),
    ("Atacar", "2d6 + Atq propio − Def del objetivo"),
    ("Defender", "2d6 + Def propia − Atq del atacante"),
    ("Dado de Vínculo", "1/asalto: 3d6, quédate los 2 mejores; un 6 = +1 Chispa"),
    ("Digievolucionar", "2 Chispa por nivel sobre el estable (+1 si Hambriento)"),
    ("Técnicas", "P1 y P2 a voluntad · P3 Firma: no dos turnos seguidos"),
    ("Desatar la Firma", "1 Chispa al declararla como P3, 1 vez por combate"),
    ("Triángulo", "Vacuna > Virus > Datos > Vacuna: ±1 a la tirada"),
    ("Daño", "dados de poder: Bebé d4 · Novato d6 · Campeón d8 · Perfecto d10 · Definitivo d12"),
]
ly = y - 22
for a, b in lines:
    c.setFillColor(CYAN); c.setFont("Helvetica-Bold", 7.2); c.drawString(qx + 8, ly, a)
    c.setFillColor(INK); c.setFont("Helvetica", 7)
    words = b.split(); line = ""; yy2 = ly
    for wd in words:
        t = (line + " " + wd).strip()
        if c.stringWidth(t, "Helvetica", 7) > qw - 92:
            c.drawString(qx + 84, yy2, line); yy2 -= 9; line = wd
        else:
            line = t
    c.drawString(qx + 84, yy2, line)
    ly = yy2 - 12
c.setFillColor(MUTED); c.setFont("Helvetica-Bold", 6.5); c.drawString(qx + 8, ly - 2, "VÍNCULO  ·  ESTABLE  ·  MÁXIMO")
c.setFont("Helvetica", 6.8)
for i, (v, e, mx) in enumerate([("1", "Novato", "Campeón"), ("2", "Novato", "Perfecto"), ("3", "Campeón", "Perfecto"), ("4", "Campeón", "Definitivo"), ("5", "Perfecto", "Definitivo"), ("Estrella", "Definitivo", "Modo Supremo")]):
    c.setFillColor(INK); c.drawString(qx + 8 + (i % 2) * (qw / 2), ly - 14 - (i // 2) * 10, f"{v}: {e} → {mx}")
field("efecto_firma", M, y - 124, (W - 2 * M) / 2 - 6, 80, "Efecto de Firma: Sello · Desatado (1 Chispa) · Eco", size=8, multi=True)
field("notas_digimon", M, 36, (W - 2 * M) / 2 - 6, y - 174, "Notas del compañero", size=8, multi=True)
footer(2)
c.showPage()
c.save()
print("OK", OUT)
