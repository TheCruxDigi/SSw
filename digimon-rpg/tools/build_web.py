# -*- coding: utf-8 -*-
"""Genera los datos de la web del manual.

Uso:
  python3 build_web.py --spec spec_fichas.json --all all.json --gen gen.py --out ../web \
      [--desc DIR_DESCRIPCIONES] [--chapters DIR_CAPITULOS] [--biblia biblia_reglas.md]

- Ejecuta el generador de referencia (gen.py) sobre la especificación y el dataset.
- Fusiona las descripciones (ficheros *.json {id: {descripcion, tacticas, gancho}}).
- Escribe web/data/bestiario.json y web/data/reglas.json.
- Copia los capítulos (con manifest.json) o, si no hay, trocea la biblia en capítulos provisionales.
"""
import argparse, glob, json, os, re, shutil, subprocess, sys, tempfile

ap = argparse.ArgumentParser()
ap.add_argument("--spec", required=True)
ap.add_argument("--all", required=True)
ap.add_argument("--gen", required=True)
ap.add_argument("--out", required=True)
ap.add_argument("--desc")
ap.add_argument("--chapters")
ap.add_argument("--biblia")
a = ap.parse_args()

spec = json.load(open(a.spec, encoding="utf-8"))
os.makedirs(os.path.join(a.out, "data"), exist_ok=True)
os.makedirs(os.path.join(a.out, "capitulos"), exist_ok=True)

# 1. fichas
with tempfile.TemporaryDirectory() as td:
    tmp = os.path.join(td, "fichas.json")
    r = subprocess.run([sys.executable, "-I", a.gen, a.spec, a.all, tmp], capture_output=True, text=True)
    print(r.stdout[-1500:])
    if r.returncode != 0:
        print(r.stderr[-3000:]); sys.exit("gen.py falló")
    fichas = json.load(open(tmp, encoding="utf-8"))

desc = {}
if a.desc:
    for f in sorted(glob.glob(os.path.join(a.desc, "*.json"))):
        try:
            desc.update(json.load(open(f, encoding="utf-8")))
        except Exception as e:
            print("AVISO: descripción ilegible", f, e)
faltan = 0
for x in fichas:
    x.pop("_scores", None)
    dd = desc.get(x["id"])
    if dd:
        for k in ("descripcion", "tacticas", "gancho"):
            if dd.get(k):
                x[k] = dd[k].strip()
    else:
        faltan += 1
json.dump(fichas, open(os.path.join(a.out, "data", "bestiario.json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print(f"bestiario: {len(fichas)} fichas; sin descripción: {faltan}")

# 2. reglas (subconjunto que usa la web)
strip = lambda lst, keys: [{k: v for k, v in o.items() if k not in keys} for o in lst]
juego = spec["meta"]["juego"]
titulo, _, subtitulo = juego.partition(" — ")
reglas = {
    "meta": {"titulo": "Digimon: Lazos de Código" if "LAZOS DE C" in titulo.upper() else titulo.strip().title(), "subtitulo": subtitulo.strip() or "Juego de rol no oficial", "aviso_legal": "Obra de fans, no oficial y sin ánimo de lucro. Digimon y todos sus nombres, personajes y técnicas pertenecen a sus propietarios; este proyecto no está afiliado ni respaldado por ellos. Las reglas, las descripciones y las aventuras son texto original.", "version": spec["meta"].get("version", "")},
    "roles": spec["roles"],
    "familias": strip(spec["familias"], {"tipos"}),
    "atributos": spec["atributos"],
    "elementos": strip(spec["elementos"], {"raices"}),
    "efectos": strip(spec["efectos"], {"raices", "raices_contexto"}),
    "alcances": spec["alcances"],
    "areas": spec["areas"],
    "plantillas": strip(spec["plantillas"], {"marcas", "si"}),
    "amenaza": {k: v for k, v in spec["amenaza"].items() if k in ("esbirro", "estandar", "elite", "jefe", "legendario", "pa_por_diferencia_de_nivel", "presupuesto")},
    "grupos": {
        "caballeros_reales": "Caballeros Reales", "senores_demonio": "Señores Demonio", "olimpo_xii": "Olimpo XII",
        "bestias_sagradas": "Bestias Sagradas", "grandes_angeles": "Grandes Ángeles", "guerreros_antiguos": "Diez Guerreros Antiguos",
        "amenazas_finales": "Amenazas finales",
    },
}
json.dump(reglas, open(os.path.join(a.out, "data", "reglas.json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))

# 3. capítulos
dst = os.path.join(a.out, "capitulos")
for f in glob.glob(os.path.join(dst, "*")):
    os.remove(f)
if a.chapters and os.path.exists(os.path.join(a.chapters, "manifest.json")):
    man = json.load(open(os.path.join(a.chapters, "manifest.json"), encoding="utf-8"))
    for c in man:
        shutil.copy(os.path.join(a.chapters, c["archivo"]), os.path.join(dst, c["archivo"]))
    json.dump(man, open(os.path.join(dst, "manifest.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"capítulos: {len(man)}")
elif a.biblia:
    txt = open(a.biblia, encoding="utf-8").read()
    parts = re.split(r"(?m)^## (?=\d+\.)", txt)
    grupos = {0: "Fundamentos", 1: "Fundamentos", 2: "Fundamentos", 3: "Personajes", 4: "Personajes", 5: "Personajes", 6: "Reglas", 7: "Reglas", 8: "Reglas",
              9: "Reglas", 10: "Reglas", 11: "Reglas", 12: "Reglas", 13: "Equipo", 14: "Equipo", 15: "Equipo", 16: "Equipo", 17: "Personajes",
              18: "Director de juego", 19: "Director de juego", 20: "Reglas opcionales", 21: "Bestiario", 22: "Referencia"}
    man = []
    for p in parts[1:]:
        head, _, body = p.partition("\n")
        m = re.match(r"(\d+)\.\s*(.+)", head)
        n = int(m.group(1)); tit = re.sub(r"\s*\[[NAO]\]\s*$", "", m.group(2)).strip()
        fn = f"{n:02d}.md"
        open(os.path.join(dst, fn), "w", encoding="utf-8").write(f"# {tit}\n\n> Versión de trabajo: texto de la biblia de reglas. El capítulo definitivo, con ejemplos y consejos, sustituirá a este.\n\n" + body.replace("\n### ", "\n## "))
        man.append({"id": f"c{n:02d}", "n": f"{n:02d}", "titulo": tit, "grupo": grupos.get(n, "Reglas"), "archivo": fn, "resumen": ""})
    json.dump(man, open(os.path.join(dst, "manifest.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"capítulos provisionales: {len(man)}")
