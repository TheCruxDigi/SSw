# -*- coding: utf-8 -*-
"""Generador de fichas d20 de «Digimon: Lazos de Código».

Uso: python3 gen_d20.py BESTIARIO_2D6.json HABILIDADES.json DIR_DATOS_D20 SALIDA.json

- Parte de las fichas ya generadas de la edición 2d6 (nivel, rango, rol, familia, técnicas clasificadas…).
- Aplica las tablas de la biblia d20 (VD, BC, CA, PG, dados por nivel, roles y familias).
- Asigna habilidades especiales automáticas por familia, tipo y forma, y fusiona las elegidas a mano
  (DIR_DATOS_D20/*.json: {id: {"habilidades": [{"id", "detalle"}], "sello", "desatado"}}).
"""
import glob, json, math, os, sys

SRC, HAB, DDIR, OUT = sys.argv[1:5]
best = json.load(open(SRC, encoding="utf-8"))
HABS = {h["id"]: h for h in json.load(open(HAB, encoding="utf-8"))}
extra = {}
if os.path.isdir(DDIR):
    for f in sorted(glob.glob(os.path.join(DDIR, "*.json"))):
        extra.update(json.load(open(f, encoding="utf-8")))

# ---------- tablas (biblia d20, 5.3, 7.1, 7.2) ----------
VD_TAB = {  # vd: (BC, CA, PG, PX)
    "1/8": (2, 11, 9, 25), "1/4": (2, 12, 14, 50), "1/2": (2, 12, 22, 100), "1": (2, 13, 32, 200), "2": (2, 13, 48, 450),
    "3": (2, 14, 64, 700), "4": (2, 14, 80, 1100), "5": (3, 15, 96, 1800), "6": (3, 15, 112, 2300), "7": (3, 15, 128, 2900),
    "8": (3, 16, 144, 3900), "9": (4, 16, 160, 5000), "10": (4, 17, 176, 5900), "11": (4, 17, 192, 7200), "12": (4, 17, 208, 8400),
    "13": (5, 18, 224, 10000), "14": (5, 18, 240, 11500), "15": (5, 18, 256, 13000), "16": (5, 19, 272, 15000), "17": (6, 19, 290, 18000),
    "18": (6, 19, 310, 20000), "19": (6, 20, 330, 22000), "20": (6, 20, 350, 25000), "21": (7, 21, 380, 33000), "22": (7, 21, 410, 41000),
}
TIER_BY_RANGO = {0: "bebe", 1: "novato", 2: "campeon", 3: "perfecto", 4: "definitivo"}
TIER = {  # dado, dados P1, P2, Firma, ataques, mod principal, radio de Zona, umbral Ejecutar, nombre
    "bebe": dict(d=4, p1=1, p2=2, f=3, ata=1, mod=1, radio="1,5 m", ejec=5, nombre="Bebé"),
    "novato": dict(d=6, p1=1, p2=2, f=4, ata=1, mod=3, radio="3 m", ejec=10, nombre="Novato"),
    "campeon": dict(d=8, p1=1, p2=2, f=7, ata=2, mod=4, radio="4,5 m", ejec=20, nombre="Campeón"),
    "perfecto": dict(d=10, p1=1, p2=3, f=9, ata=2, mod=5, radio="6 m", ejec=35, nombre="Perfecto"),
    "definitivo": dict(d=12, p1=1, p2=3, f=13, ata=3, mod=6, radio="9 m", ejec=50, nombre="Definitivo"),
}
VD_BY_TIER = {"novato": ["1/2", "1", "2"], "campeon": ["3", "4", "5"], "perfecto": ["7", "8", "9"], "definitivo": ["12", "13", "14"]}
AMZ = {"baja": 0, "media": 1, "alta": 2}
LEGEND_GROUPS = {"caballeros_reales", "senores_demonio", "olimpo_xii", "bestias_sagradas", "grandes_angeles", "guerreros_antiguos"}

ROL = {  # CA, PG mult, ataque, CD, salvaciones, velocidad extra, iniciativa
    "bruto": dict(ca=-1, pg=1.1, atq=1, cd=0, sv=["FUE", "CON"], vel=0, ini=0),
    "tanque": dict(ca=2, pg=1.2, atq=-1, cd=0, sv=["FUE", "CON"], vel=0, ini=0),
    "agil": dict(ca=1, pg=0.9, atq=0, cd=0, sv=["DES", "SAB"], vel=3, ini=2),
    "tirador": dict(ca=-1, pg=0.9, atq=1, cd=0, sv=["DES", "INT"], vel=0, ini=0),
    "mistico": dict(ca=-1, pg=0.9, atq=0, cd=1, sv=["SAB", "CAR"], vel=0, ini=0),
    "apoyo": dict(ca=0, pg=1.0, atq=-1, cd=0, sv=["SAB", "CAR"], vel=0, ini=0),
    "acechador": dict(ca=0, pg=0.9, atq=1, cd=0, sv=["DES", "INT"], vel=0, ini=2),
    "versatil": dict(ca=0, pg=1.0, atq=0, cd=0, sv=["CON", "SAB"], vel=0, ini=0),
    None: dict(ca=0, pg=1.0, atq=0, cd=0, sv=["DES"], vel=0, ini=0),
}
ROL_RASGO = {
    "arrollador": "Una vez por turno, cuando reduce a una criatura a 0 PG con un ataque cuerpo a cuerpo, puede moverse hasta la mitad de su velocidad y hacer un ataque con su técnica básica como acción adicional.",
    "guardian": "Una vez por asalto, como reacción, impone desventaja a un ataque contra un aliado a 1,5 m o se convierte en su objetivo.",
    "escurridizo": "No provoca ataques de oportunidad. Tras usar su acción, puede moverse 3 m extra.",
    "francotirador": "+1 a sus ataques a distancia contra objetivos a más de 3 m. Su técnica básica es a distancia y el alcance de su Firma a distancia se duplica.",
    "maestro_de_estados": "Los objetivos tienen desventaja en las salvaciones contra los estados de su Firma (salvo control duro).",
    "sanador": "Sus técnicas de apoyo afectan a un aliado más dentro del alcance; el objetivo principal suma su BC a la curación o a los PG temporales.",
    "emboscada": "Una vez por turno, +1 dado de daño contra un objetivo que aún no ha actuado en el combate, derribado, apresado, cegado o marcado, o si ataca desde invisible o escondido.",
    "adaptable": "Una vez por combate, repite una tirada de ataque o de salvación propia (o, como PNJ, obliga a repetir un ataque que le haya impactado).",
}
ATR_RASGO = {
    "antivirus": "+1 CA (incluido).", "agresion": "+1 a sus tiradas de ataque (incluido).", "procesamiento": "+2 a la iniciativa y +BC PG (incluidos).",
    "libre": "Fuera del triángulo de atributos; +BC PG (incluido).", "ilegible": "Fuera del triángulo; +1 CA (incluido). Analizar contra él tiene desventaja.",
    "mutable": "Al empezar cada escena elige ser Vacuna, Datos o Virus para el triángulo.",
}
FAM_RASGO = {
    "dragon": ("Corazón de dragón", "Con la mitad de sus PG o menos, tiene ventaja en sus tiradas de ataque."),
    "saurio": ("Piel gruesa", "PG ×1,1 (incluido)."),
    "bestia": ("Manada", "Ventaja en el ataque contra una criatura que un aliado ya haya atacado en este asalto."),
    "ave": ("Vuelo", "Vuela. Las criaturas sin vuelo ni alcance tienen desventaja en ataques cuerpo a cuerpo contra él mientras está en el aire, salvo que esté apresado o derribado."),
    "acuatico": ("Anfibio", "Respira bajo el agua y nada. En agua o bajo la lluvia, +1 CA."),
    "naturaleza": ("Toxinas y raíces", "Inmune al daño de veneno y al estado envenenado. Sus salvaciones contra apresado tienen ventaja."),
    "maquina": ("Blindaje", "+1 CA (incluido). Inmune a dormido y hechizado."),
    "juguete": ("Relleno", "Una vez por combate, reduce a la mitad el daño de un impacto. Inmune a asustado."),
    "sagrado": ("Aura sagrada", "+1 dado de daño con técnicas de Luz contra la familia Oscuro."),
    "caballero": ("Honor", "Inmune a asustado y hechizado. +1 CA mientras usa Proteger."),
    "oscuro": ("Hambre oscura", "Cuando hace un crítico o un objetivo falla una salvación contra su Firma por 5 o más, recupera BC × 2 PG."),
    "arcano": ("Hechicería", "Sus técnicas a distancia tienen alcance Larga. Inmune a confundido."),
    "elemental": ("Cuerpo elemental", "Resistencia al daño de su elemento (incluida) e inmune a su estado asociado."),
    "anomalia": ("Adaptación", "Tras recibir daño de un elemento, gana resistencia a ese elemento hasta el final del combate (solo uno a la vez)."),
}
PLANT_RASGO = {
    "anticuerpo_x": "Inmune a sellado y a Ejecutar. Una vez por combate, repite una salvación (o, como PNJ, obliga a repetir un ataque que le haya impactado).",
    "poder_desatado": "Al entrar en este modo, su Firma se recarga.",
    "cambio_de_modo": "Cambiar a otro modo de la misma especie gasta su movimiento y conserva el daño recibido.",
    "poder_del_huevo": "Resistencia al elemento de su Firma (incluida). Funciona aunque la digievolución normal esté bloqueada; no puede digievolucionar a otro nivel desde esta forma.",
    "espiritu": "Es la transformación de un Tamer (módulo de Espíritus).",
    "fusion_espiritus": "Combina los Espíritus Humano y Bestia.",
    "descontrol": "+1 dado de daño en todas sus técnicas y desventaja en salvaciones contra técnicas de Luz. Un compañero en esta forma lo controla el DJ.",
    "bebe": "No tiene Firma con recarga ni aplica control duro. Ventaja en pruebas para esconderse o huir.",
}
MANIOBRA = {
    "arremetida": "Antes de atacar se mueve hasta 6 m hacia el objetivo sin provocar ataques de oportunidad; ataque cuerpo a cuerpo de 1 dado + mod.; salvación de FUE o derribado.",
    "golpe_y_fuga": "Ataque cuerpo a cuerpo de 1 dado + mod.; después se mueve hasta 3 m sin provocar ataques de oportunidad.",
    "interferencia": "Acción, 18 m, sin daño: el objetivo hace una salvación (CON) o queda debilitado o ralentizado (a elegir) hasta el final de su próximo turno.",
    "cambio_de_guardia": "Ataque cuerpo a cuerpo con +2 de 1 dado + mod.; +1 CA hasta su próximo turno.",
    "desafio": "Acción: cada enemigo a 3 m hace una salvación de SAB o queda provocado hasta el final de su próximo turno.",
    "disparo_certero": "Ataque a distancia (36 m) de 1 dado + mod., con +2 al ataque; ignora la cobertura media y de tres cuartos.",
    "pulso_restaurador": "Acción adicional, 18 m: un aliado recupera 1 dado + mod. PG o termina un estado (recarga 5–6).",
    "marca_de_caza": "Acción adicional, 36 m: un enemigo queda marcado hasta el final del siguiente asalto o hasta que reciba un ataque.",
}
ELE = {"neutro": "neutro", "fuego": "fuego", "hielo": "hielo", "electrico": "eléctrico", "agua": "agua", "planta": "planta", "viento": "viento",
       "tierra": "tierra", "acero": "acero", "veneno": "veneno", "luz": "luz", "oscuridad": "oscuridad", "mental": "mental", "cosmico": "cósmico"}
SAVE = {"quemar": ("DES", "ardiendo"), "congelar": ("CON", "congelado"), "paralizar": ("CON", "entumecido"), "veneno": ("CON", "envenenado"),
        "aturdir": ("CON", "aturdido"), "dormir": ("SAB", "dormido"), "cegar": ("CON", "cegado"), "confundir": ("SAB", "confundido"),
        "asustar": ("SAB", "asustado"), "encantar": ("SAB", "hechizado"), "sellar": ("CAR", "sellado"), "regresion": ("CAR", "en regresión"),
        "ralentizar": ("DES", "ralentizado"), "atrapar": ("FUE", "apresado"), "debilitar": ("CON", "debilitado"), "romper": ("FUE", "roto"),
        "derribar": ("FUE", "derribado"), "empujar": ("FUE", "empujado 3 m"), "provocar": ("SAB", "provocado")}
NOTE = {"perforante": "Perforante: ignora resistencias y reducción de daño", "brutal": "Brutal: crítico con 19–20", "certero": "Certero: +2 al ataque, ignora cobertura",
        "drenar": "Drenar: recupera la mitad del daño", "retroceso": "Retroceso: +2 dados; el usuario recibe BC + mod. de daño",
        "ejecutar": "Ejecutar", "cargado": "Cargado: requiere cargar 1 acción; luego ventaja y +2 dados", "marcar": "el objetivo queda marcado",
        "rapido": "Rápido: se mueve 3 m antes sin provocar", "contraataque": "Contraataque (reacción preparada)", "invocar": "Invocar: crea un enjambre de 3 m durante 1 minuto",
        "ocultar": "Ocultar: queda invisible hasta su próximo turno", "curar": "Curar", "escudo": "Escudo", "mejora": "Mejora", "purificar": "Purificar"}
STAT_BY_FAM = {  # característica principal de técnicas «místicas» por familia
    "arcano": "INT", "sagrado": "SAB", "juguete": "CAR", "oscuro": "CAR", "naturaleza": "SAB", "maquina": "INT", "anomalia": "INT", "elemental": "SAB",
}
FAM_SKILLS = {"dragon": ["Atletismo", "Intimidación"], "saurio": ["Atletismo", "Supervivencia"], "bestia": ["Percepción", "Supervivencia"], "ave": ["Percepción", "Acrobacias"],
              "acuatico": ["Atletismo", "Supervivencia"], "naturaleza": ["Sigilo", "Naturaleza"], "maquina": ["Tecnología", "Atletismo"], "juguete": ["Engaño", "Interpretación"],
              "sagrado": ["Perspicacia", "Mitos"], "caballero": ["Atletismo", "Historia"], "oscuro": ["Intimidación", "Sigilo"], "arcano": ["Saber digital", "Engaño"],
              "elemental": ["Atletismo", "Saber digital"], "anomalia": ["Saber digital", "Engaño"]}
SKILL_STAT = {"Atletismo": "FUE", "Acrobacias": "DES", "Sigilo": "DES", "Juego de manos": "DES", "Saber digital": "INT", "Historia": "INT", "Investigación": "INT",
              "Naturaleza": "INT", "Mitos": "INT", "Tecnología": "INT", "Trato con animales": "SAB", "Perspicacia": "SAB", "Medicina": "SAB", "Percepción": "SAB",
              "Supervivencia": "SAB", "Engaño": "CAR", "Intimidación": "CAR", "Interpretación": "CAR", "Persuasión": "CAR"}
STATS = ["FUE", "DES", "CON", "INT", "SAB", "CAR"]
SIZE_DIE = {"Diminuto": 4, "Pequeño": 6, "Mediano": 8, "Grande": 10, "Enorme": 12, "Gargantuesco": 20}
BIG_FAM = {"dragon", "saurio", "maquina"}


def frac(vd):
    return {"1/8": 0.125, "1/4": 0.25, "1/2": 0.5}.get(vd) or float(vd)


def tier_of(d):
    if d["nivel"].startswith("Bebé"):
        return "bebe"
    return TIER_BY_RANGO.get(d.get("rango") if d.get("rango") is not None else 1, "novato")


def vd_of(d, tier):
    if d["nivel"] == "Bebé I":
        return "1/8"
    if tier == "bebe":
        return "1/4"
    a = AMZ.get(d.get("amenaza_nivel"), 1)
    if tier == "definitivo" and d.get("grupo_legendario") == "amenazas_finales":
        return str(20 + a)
    if tier == "definitivo" and d.get("grupo_legendario") in LEGEND_GROUPS:
        return str(15 + a)
    return VD_BY_TIER[tier][a]


def size_of(d, tier, habs):
    if tier == "bebe":
        return "Diminuto"
    if "gigante" in habs:
        return "Enorme" if tier != "definitivo" else "Gargantuesco"
    if tier == "novato":
        return "Pequeño"
    if tier == "campeon":
        return "Grande" if d["familia"] in BIG_FAM else "Mediano"
    if tier == "perfecto":
        return "Grande"
    return "Enorme" if d["familia"] in BIG_FAM else "Grande"


def auto_habs(d, tier):
    t = (d.get("tipo") or "").lower()
    fam, h = d["familia"], []
    def add(x):
        if x not in h:
            h.append(x)
    if d.get("vuela"):
        add("vuelo")
    if d.get("nada"):
        add("anfibio" if fam == "acuatico" else "nado")
    if fam == "oscuro" or any(k in t for k in ("undead", "ghost", "demon", "dark", "evil", "fallen")) or d.get("elemento_principal") == "oscuridad":
        add("vision_oscuridad")
    if "ghost" in t:
        add("fase")
    if "undead" in t or "ghost" in t:
        add("no_muerto")
    if fam == "maquina" or any(k in t for k in ("cyborg", "machine", "android")):
        add("constructo")
    if fam == "bestia":
        add("olfato_agudo")
    if fam == "ave":
        add("vista_aguda")
    if fam == "sagrado":
        add("detectar_mal")
    if tier == "bebe":
        add("diminuto")
    if "insect" in t:
        add("trepar")
    return h


def score(mod):
    return 10 + 2 * mod


def dice(n, die, mod):
    avg = int(n * (die + 1) / 2 + mod)
    return f"{avg} ({n}d{die}{' + ' + str(mod) if mod > 0 else (' − ' + str(-mod) if mod < 0 else '')})", avg


def area_txt(area, T, alc):
    if area == "rafaga":
        return "hasta 2 objetivos a 3 m o menos uno del otro"
    if area == "zona":
        return f"todas las criaturas en un radio de {T['radio']}" + (" centrado en el usuario" if alc in ("toque", "personal") else "")
    if area == "total":
        return "todos los enemigos que vea a 18 m o menos"
    return "un objetivo"


def alc_txt(alc, rol, fam, big):
    if alc == "toque":
        return f"cuerpo a cuerpo, alcance {'3' if big else '1,5'} m"
    if alc in ("distancia",):
        return "a distancia, 36 m" if fam == "arcano" or rol == "tirador" else "a distancia, 18 m"
    if alc == "larga":
        return "a distancia, 36 m" if rol != "tirador" else "a distancia, 72 m"
    return "personal"


def conv_tech(t, d, ctx):
    T, rol, fam = ctx["T"], d.get("rol"), d["familia"]
    tipo = t.get("tipo")
    alc = t.get("alcance") or "toque"
    if tipo == "basica" and (rol == "tirador" or fam == "arcano"):
        alc = "distancia"
    area = t.get("area") or "individual"
    claves = [c for k in (t.get("claves") or []) for c in k.split("|")]
    pot = t.get("potencia") or ""
    firma = bool(t.get("firma"))
    out = {"nombre": t["nombre"], "tipo": tipo, "firma": firma, "elemento": ELE.get(t.get("elemento"), t.get("elemento") or "neutro"),
           "alcance": alc_txt(alc, rol, fam, ctx["big"]), "objetivo": area_txt(area, T, alc), "claves": claves}
    if t.get("efecto"):
        out["efecto"] = dict(t["efecto"])
    if tipo == "maniobra":
        out["texto"] = MANIOBRA.get(t.get("id"), t.get("regla", ""))
        out["accion"] = "acción adicional" if t.get("id") in ("pulso_restaurador", "marca_de_caza") else "acción"
        return out
    # número de dados
    if ctx["tier"] == "bebe":
        n = {"P1": 1, "P2": 2}.get(pot, 1) if not firma else T["f"] if pot.startswith("P2") or pot == "P3" else T["p1"]
        if firma and pot == "P1":
            n = 2
    elif firma:
        n = T["f"] + (1 if rol == "bruto" else 0)
    else:
        n = T["p2"] if pot.startswith("P2") or pot == "P3" else T["p1"]
    if t.get("apoyo"):
        stat_mod = ctx["mods"]["SAB"]
        res = []
        nn = n + (1 if rol == "apoyo" and not firma else 0)
        for c in claves:
            if c == "curar":
                res.append(f"un aliado recupera {dice(nn, T['d'], stat_mod)[0]} PG" if area == "individual" else f"cada aliado en el área recupera {dice(max(1, nn - nn // 4), T['d'], stat_mod)[0]} PG")
            elif c == "escudo":
                res.append(f"un aliado gana {nn * T['d'] // 2 + ctx['mod']} PG temporales" if area == "individual" else f"cada aliado en el área gana {max(1, nn - nn // 4) * T['d'] // 2 + ctx['mod']} PG temporales")
            elif c == "mejora":
                res.append("el aliado tiene ventaja en su próximo ataque" + (" y +1 dado de daño" if n >= 2 else "") + (" (todos los aliados del área)" if firma or area != "individual" else ""))
            elif c == "purificar":
                res.append("termina " + ("un estado" if n <= 1 else "todos los estados de un aliado" if area == "individual" else "todos los estados de los aliados del área"))
            elif c in NOTE:
                res.append(NOTE[c])
        out["apoyo"] = True
        out["accion"] = "acción adicional" if pot == "P1" else "acción"
        txt = "; ".join(res)
        out["texto"] = (txt[:1].upper() + txt[1:] + ".") if res else "Efecto de apoyo."
        if firma:
            out["recarga"] = "5–6"
        return out
    mod = ctx["mod"]
    extra = 2 if "retroceso" in claves else 0
    dmg, avg = dice(n + extra, T["d"], mod)
    out["dados"] = f"{n + extra}d{T['d']}"
    out["dano"] = dmg
    out["media"] = avg
    if area != "individual":
        m = max(1, (n + extra) - (n + extra) // 4)
        out["dano_area"] = dice(m, T["d"], mod)[0]
        out["salvacion"] = "DES"
    else:
        out["ataque"] = ctx["atq"] + (2 if "certero" in claves else 0)
    efs = []
    for c in claves:
        if c in SAVE:
            sv, st = SAVE[c]
            if c == "romper":
                efs.append(f"salvación de {sv} o queda {st} (−2 CA hasta el final de la escena)")
            elif c == "empujar":
                efs.append(f"salvación de {sv} o es empujado {'6' if ctx['tier'] in ('perfecto', 'definitivo') else '3'} m")
            elif c == "marcar":
                pass
            else:
                efs.append(f"salvación de {sv} o queda {st}")
        elif c == "marcar":
            efs.append("el objetivo queda marcado")
        elif c == "ejecutar":
            efs.append(f"Ejecutar: si queda con {T['ejec']} PG o menos (no Jefes), cae a 0")
        elif c in ("curar", "escudo", "mejora", "purificar"):
            efs.append({"curar": f"el usuario recupera 1d{T['d']} PG", "escudo": f"el usuario gana {T['d'] // 2 + 1} PG temporales",
                        "mejora": "el usuario tiene ventaja en su próximo ataque", "purificar": "el usuario termina un estado; +1 dado contra la familia Oscuro"}[c])
        elif c in NOTE:
            efs.append(NOTE[c])
    out["efectos"] = efs
    if firma:
        out["recarga"] = "5–6" if ctx["tier"] != "bebe" else None
        if pot == "P2/P3":
            out["version_p2"] = dice(T["p2"], T["d"], mod)[0]
    return out


fichas = []
for d in best:
    tier = tier_of(d)
    T = TIER[tier]
    vd = vd_of(d, tier)
    BC, CA, PG, PX = VD_TAB[vd]
    rol = d.get("rol")
    R = ROL.get(rol, ROL[None])
    fam = d["familia"]
    E = extra.get(d["id"], {})
    habs = auto_habs(d, tier)
    for h in E.get("habilidades", []):
        if h.get("id") in HABS and h["id"] not in habs:
            habs.append(h["id"])
    size = size_of(d, tier, habs)
    big = size in ("Enorme", "Gargantuesco")
    mod = T["mod"] + (1 if frac(vd) >= 17 else 0)
    # característica principal
    firma = next((t for t in d["tecnicas"] if t.get("firma")), None)
    falc = (firma or {}).get("alcance", "toque")
    if rol in ("mistico", "apoyo") or (firma and firma.get("apoyo")):
        main = STAT_BY_FAM.get(fam, "SAB")
    elif falc == "toque":
        main = "FUE"
    else:
        main = "DES" if fam not in ("arcano",) else "INT"
    mods = {s: 0 for s in STATS}
    second = {"FUE": "CON", "DES": "SAB", "INT": "SAB", "SAB": "CAR", "CAR": "INT"}[main]
    mods[main] = mod
    mods[second] = max(mods[second], mod - 2)
    mods["CON"] = max(mods["CON"], mod - 1 if rol != "tanque" else mod)
    mods["DES"] = max(mods["DES"], mod - 2 if rol in ("agil", "acechador", "tirador") else min(mods["DES"], 1))
    if rol in ("agil", "acechador"):
        mods["DES"] = max(mods["DES"], mod - 1)
    if rol in ("bruto", "tanque", "versatil") and main != "FUE":
        mods["FUE"] = max(mods["FUE"], mod - 1)
    for s, v in {"arcano": {"INT": 1}, "sagrado": {"SAB": 1}, "bestia": {"SAB": 1}, "maquina": {"INT": 1}, "juguete": {"CAR": 1}, "oscuro": {"CAR": 1}, "caballero": {"CAR": 1},
                 "dragon": {"CAR": 1}, "saurio": {"INT": -1}, "naturaleza": {"SAB": 1}}.get(fam, {}).items():
        if s != main:
            mods[s] += v
    if tier == "bebe":
        mods = {s: (1 if s == main else 0) for s in STATS}
        mods["FUE"] = min(mods["FUE"], -1) if main != "FUE" else mods["FUE"]
    # CA y PG
    ca = CA + R["ca"] + (1 if fam == "maquina" else 0) + (1 if d["atributo"] in ("vacuna", "ilegible") else 0)
    pg_t = PG * R["pg"] * (1.1 if fam == "saurio" else 1)
    if d["atributo"] in ("datos", "libre"):
        pg_t += BC * 2
    hd = SIZE_DIE[size]
    con = mods["CON"]
    n_hd = max(1, round(pg_t / (hd / 2 + 0.5 + con)))
    pg = max(1, int(n_hd * (hd / 2 + 0.5)) + n_hd * con)
    atq = BC + mod + R["atq"] + (1 if d["atributo"] == "virus" else 0)
    cd = 8 + BC + mod + R["cd"]
    ini = mods["DES"] + R["ini"] + (2 if d["atributo"] == "datos" else 0)
    ctx = dict(T=T, tier=tier, mod=mod, mods=mods, atq=atq, big=big)
    tecs = [conv_tech(t, d, ctx) for t in d["tecnicas"]]
    # efecto de Firma d20 (Sello y Desatado reescritos) — si falta, se deja el de 2d6 marcado como provisional
    for t in tecs:
        if t.get("firma") and t.get("efecto"):
            e = t["efecto"]
            if E.get("sello"):
                e["sello"] = E["sello"]; e["desatado"] = E.get("desatado"); e["d20"] = True
            else:
                e["d20"] = False
    vel = 9 + R["vel"]
    movs = [f"{vel} m"]
    if "vuelo" in habs:
        movs.append(f"volar {18 + (6 if rol == 'agil' else 0)} m")
    if "levitar" in habs and "vuelo" not in habs:
        movs.append("volar 9 m (flotar)")
    if "anfibio" in habs or "nado" in habs:
        movs.append(f"nadar {vel} m")
    if "excavar" in habs:
        movs.append("excavar 9 m")
    if "trepar" in habs:
        movs.append(f"trepar {vel} m")
    sentidos = []
    if "vision_oscuridad" in habs:
        sentidos.append("visión en la oscuridad 18 m")
    if "vision_ciega" in habs:
        sentidos.append("visión ciega 9 m")
    if "vision_verdadera" in habs:
        sentidos.append("visión verdadera 36 m")
    if "sentido_sismico" in habs:
        sentidos.append("sentido sísmico 18 m")
    skills = list(FAM_SKILLS.get(fam, []))
    if rol == "acechador" and "Sigilo" not in skills:
        skills.append("Sigilo")
    if rol in ("mistico", "apoyo") and "Perspicacia" not in skills:
        skills.append("Perspicacia")
    pas = 10 + mods["SAB"] + (BC if "Percepción" in skills else 0) + (5 if "vista_aguda" in habs or "olfato_agudo" in habs else 0)
    sentidos.append(f"Percepción pasiva {pas}")
    salv = {s: mods[s] + (BC if s in R["sv"] else 0) for s in STATS}
    inm_est = []
    if fam in ("maquina",) or "constructo" in habs:
        inm_est += ["dormido", "hechizado"]
    if fam in ("caballero",):
        inm_est += ["asustado", "hechizado"]
    if fam == "juguete":
        inm_est.append("asustado")
    if fam == "naturaleza" or "constructo" in habs or "no_muerto" in habs:
        inm_est.append("envenenado")
    if fam == "arcano":
        inm_est.append("confundido")
    if "anticuerpo_x" in [z["id"] for z in d["rasgos"]]:
        inm_est.append("sellado")
    rasgos = []
    for z in d["rasgos"]:
        if z["origen"] == "rol" and z["id"] in ROL_RASGO:
            rasgos.append({"nombre": z["nombre"], "regla": ROL_RASGO[z["id"]], "origen": "rol"})
        elif z["origen"] == "familia" and fam in FAM_RASGO:
            n_, r_ = FAM_RASGO[fam]
            rasgos.append({"nombre": n_, "regla": r_, "origen": "familia"})
        elif z["origen"] == "atributo" and z["id"] in ATR_RASGO:
            rasgos.append({"nombre": z["nombre"], "regla": ATR_RASGO[z["id"]], "origen": "atributo"})
        elif z["origen"] == "plantilla" and z["id"] in PLANT_RASGO:
            rasgos.append({"nombre": z["nombre"], "regla": PLANT_RASGO[z["id"]], "origen": "plantilla"})
    hab_out = []
    det = {h["id"]: h.get("detalle") for h in E.get("habilidades", []) if h.get("id")}
    for h in habs:
        H = HABS[h]
        hab_out.append({"id": h, "nombre": H["nombre"], "regla": H["d20"], "detalle": det.get(h)})
    fichas.append({
        "id": d["id"], "vd": vd, "px": PX, "bc": BC, "tam": size, "ca": ca, "pg": pg, "dg": f"{n_hd}d{hd}{' + ' + str(n_hd * con) if con > 0 else ''}",
        "vel": ", ".join(movs), "car": {s: score(mods[s]) for s in STATS}, "salv": {s: v for s, v in salv.items() if s in R["sv"]},
        "hab_pericia": {s: mods[SKILL_STAT[s]] + BC for s in skills}, "sentidos": ", ".join(sentidos),
        "inm_estados": sorted(set(inm_est)), "atq": atq, "cd": cd, "ini": ini, "ataques": T["ata"] if tier != "bebe" else 1,
        "dado": f"d{T['d']}", "mod": mod, "main": main, "tecnicas": tecs, "rasgos": rasgos, "habilidades": hab_out,
    })

json.dump(fichas, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print(f"fichas d20: {len(fichas)}; con Sello/Desatado d20: {sum(1 for f in fichas for t in f['tecnicas'] if t.get('efecto', {}).get('d20'))}; "
      f"con habilidades elegidas: {sum(1 for f in fichas if f['id'] in extra)}")
