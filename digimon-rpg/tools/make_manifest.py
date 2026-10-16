# -*- coding: utf-8 -*-
"""Reúne los capítulos terminados en digimon-rpg/capitulos/ y escribe su manifest.json.
Uso: python3 make_manifest.py DIR_CAPITULOS_FUENTE DIR_DESTINO BIBLIA.md [resumenes.json]
- Copia al destino los capítulos que existan (en el orden del manual).
- Añade la biblia de reglas como apéndice técnico.
"""
import json, os, re, shutil, sys

SRC, DST, BIB = sys.argv[1], sys.argv[2], sys.argv[3]
RES = json.load(open(sys.argv[4], encoding="utf-8")) if len(sys.argv) > 4 and os.path.exists(sys.argv[4]) else {}

CH = [
    ("01", "01-que-es-el-rol.md", "¿Qué es un juego de rol?", "Fundamentos"),
    ("02", "02-como-se-juega.md", "Cómo se juega", "Fundamentos"),
    ("03", "03-mundo-digital.md", "El Mundo Digital", "Fundamentos"),
    ("04", "04-el-tamer.md", "Crear tu Tamer", "Personajes"),
    ("05", "05-el-companero.md", "Tu compañero Digimon", "Personajes"),
    ("06", "06-digievolucion.md", "Chispa, Vínculo y digievolución", "Personajes"),
    ("07", "07-combate.md", "Combate", "Reglas"),
    ("08", "08-tecnicas-y-estados.md", "Técnicas, elementos y estados", "Reglas"),
    ("09", "09-programas.md", "Programas: las tarjetas del Tamer", "Reglas"),
    ("10", "10-equipo-digivices-emblemas.md", "Equipo, Digivices y Emblemas", "Reglas"),
    ("11", "11-progresion.md", "Progresión y experiencia", "Personajes"),
    ("12", "12-guia-del-dj.md", "Guía del Director de Juego", "Director de juego"),
    ("13", "13-reglas-opcionales.md", "Reglas opcionales y avanzadas", "Reglas"),
    ("14", "14-como-usar-el-bestiario.md", "Cómo usar el bestiario", "Director de juego"),
    ("15", "15-personajes-pregenerados.md", "Personajes pregenerados", "Aventuras"),
    ("16", "16-aventura-la-primera-puerta.md", "Aventura: La primera Puerta", "Aventuras"),
    ("17", "17-aventura-la-sombra-del-engranaje.md", "Aventura: La sombra del Engranaje", "Aventuras"),
    ("18", "18-aventura-el-trono-vacio.md", "Aventura: El trono vacío", "Aventuras"),
    ("19", "19-referencia-rapida.md", "Referencia rápida y glosario", "Referencia"),
]
GROUP_ORDER = ["Fundamentos", "Personajes", "Reglas", "Director de juego", "Aventuras", "Referencia"]

os.makedirs(DST, exist_ok=True)
for f in os.listdir(DST):
    os.remove(os.path.join(DST, f))
man = []
for n, fn, tit, grp in CH:
    p = os.path.join(SRC, fn)
    if not os.path.exists(p):
        continue
    shutil.copy(p, os.path.join(DST, fn))
    first = open(p, encoding="utf-8").readline()
    m = re.match(r"#\s+(.+)", first)
    man.append({"id": f"c{n}", "n": n, "titulo": m.group(1).strip() if m else tit, "grupo": grp, "archivo": fn, "resumen": RES.get(n, "")})
man.sort(key=lambda c: (GROUP_ORDER.index(c["grupo"]), c["n"]))
# apéndice: biblia completa
bib = open(BIB, encoding="utf-8").read()
bib = re.sub(r"^# .*\n", "", bib, count=1)
bib = re.sub(r"^## Juego de rol no oficial.*\n", "", bib, count=1, flags=re.M)
bib = re.sub(r"^(#{2,3} .*?)\s*\[[NAO]\]\s*$", r"\1", bib, flags=re.M)
open(os.path.join(DST, "apendice-biblia.md"), "w", encoding="utf-8").write(
    "# Apéndice: biblia de reglas\n\n> Esta es la referencia técnica completa del sistema: todas las reglas, cifras y la especificación con la que se generan las fichas del bestiario. Los capítulos del manual explican lo mismo con ejemplos y consejos; si alguna vez encuentras una diferencia, manda esta biblia.\n\n" + bib)
man.append({"id": "apendice", "n": "A", "titulo": "Apéndice: biblia de reglas", "grupo": "Referencia", "archivo": "apendice-biblia.md", "resumen": "La referencia técnica completa del sistema, con todas las reglas y la especificación de las fichas."})
json.dump(man, open(os.path.join(DST, "manifest.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{len(man)} capítulos en el manifiesto: " + ", ".join(c["n"] for c in man))
