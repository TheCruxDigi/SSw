# -*- coding: utf-8 -*-
"""Trocea la biblia d20 en capítulos para la web y añade el catálogo de habilidades especiales.
Uso: python3 make_d20_chapters.py biblia_d20.md habilidades.json DIR_SALIDA
"""
import json, os, re, sys

BIB, HAB, DST = sys.argv[1:4]
os.makedirs(DST, exist_ok=True)
for f in os.listdir(DST):
    os.remove(os.path.join(DST, f))
txt = open(BIB, encoding="utf-8").read()
head, *parts = re.split(r"(?m)^## (?=\d+\.)", txt)
intro = re.sub(r"^# .*\n|^## Biblia.*\n", "", head, flags=re.M).strip()
GRUPO = {0: "Fundamentos d20", 1: "Fundamentos d20", 2: "Personajes d20", 3: "Personajes d20", 4: "Personajes d20", 5: "Reglas d20", 6: "Reglas d20",
         7: "Director de juego d20", 8: "Director de juego d20", 9: "Reglas d20", 10: "Director de juego d20"}
RES = {0: "Qué comparte la edición d20 con la 2d6 y qué cambia.", 1: "La tirada d20, la ventaja, el BC, las características y las 19 habilidades.",
       2: "La clase Tamer del 1 al 20, sus rasgos, trasfondos, programas y las cinco Sendas.", 3: "Formas, niveles y avances del compañero Digimon.",
       4: "Cómo se gana y se gasta la Chispa y cómo funciona la digievolución en d20.", 5: "El asalto, las distancias, los ataques, el daño y los modificadores del Mundo Digital.",
       6: "Las 35 palabras clave y los estados con su salvación, y los efectos de Firma en d20.", 7: "VD, tabla de cifras, roles, familias y plantillas de amenaza.",
       8: "Cómo montar un combate equilibrado con PX.", 9: "Qué son las habilidades especiales de los Digimon.", 10: "Equivalencias para pasar material de 2d6 a d20."}
man = []
for p in parts:
    title, _, body = p.partition("\n")
    m = re.match(r"(\d+)\.\s*(.+)", title)
    n = int(m.group(1)); tit = m.group(2).strip()
    fn = f"d{n:02d}.md"
    pre = f"# {tit}\n\n" + (intro + "\n\n" if n == 0 else "")
    open(os.path.join(DST, fn), "w", encoding="utf-8").write(pre + body.replace("\n### ", "\n## "))
    man.append({"id": f"e{n:02d}", "n": f"{n:02d}", "titulo": tit, "grupo": GRUPO.get(n, "Reglas d20"), "archivo": fn, "resumen": RES.get(n, "")})
# capítulo de habilidades especiales
habs = json.load(open(HAB, encoding="utf-8"))
CAT = {"sentido": "Sentidos", "movimiento": "Movimiento", "defensa": "Defensa", "social": "Comunicación y presencia", "poder": "Poderes"}
md = ["# Catálogo de habilidades especiales", "",
      "Cada Digimon del bestiario d20 tiene de 1 a 4 habilidades especiales. Unas las da su familia, su tipo o su forma (vuelo, visión en la oscuridad, cuerpo artificial…); otras se eligieron una a una según su historia y su diseño, y llevan un **detalle** propio en su ficha. Cada habilidad tiene su regla en d20 y su equivalente para la edición 2d6, así que también puedes usarlas en esa edición.",
      "", "> **Para el DJ:** un compañero puede ganar una habilidad nueva como avance (niveles 4, 8, 12, 16 y 19 del Tamer) si encaja con lo vivido en la campaña. Las habilidades potentes (Posesión, Borrado de datos, Distorsión temporal, Abrir puertas, Visión verdadera, Dominio mental, Llamada de la legión, Regeneración, Renacer, Presencia aterradora y Coloso) solo deberían aparecer en Perfectos y Definitivos.", ""]
for c, name in CAT.items():
    md += [f"## {name}", ""]
    for h in habs:
        if h["cat"] == c:
            md += [f"### {h['nombre']}", "", f"**d20.** {h['d20']}", "", f"**2d6.** {h['d2d6']}", ""]
open(os.path.join(DST, "d11-habilidades.md"), "w", encoding="utf-8").write("\n".join(md))
man.append({"id": "e11", "n": "11", "titulo": "Catálogo de habilidades especiales", "grupo": "Reglas d20", "archivo": "d11-habilidades.md",
            "resumen": f"Las {len(habs)} habilidades especiales de los Digimon, con su regla en d20 y en 2d6."})
ORDER = ["Fundamentos d20", "Personajes d20", "Reglas d20", "Director de juego d20"]
man.sort(key=lambda c: (ORDER.index(c["grupo"]), c["n"]))
json.dump(man, open(os.path.join(DST, "manifest.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{len(man)} capítulos d20")
