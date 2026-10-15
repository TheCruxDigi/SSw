# -*- coding: utf-8 -*-
"""Generador de referencia (ronda 3): implementa spec_fichas.json sobre src/all.json.
Uso: python3 gen.py SPEC ALLJSON [salida.json]
Si alguna validación de validacion.reglas o validacion.rangos_por_nivel falla, termina con código 1."""
import json, re, ast, sys, math, collections, unicodedata, itertools

SPEC = json.load(open(sys.argv[1], encoding="utf-8"))
DATA = json.load(open(sys.argv[2], encoding="utf-8"))
OUT = sys.argv[3] if len(sys.argv) > 3 else None

def L(x):
    if isinstance(x, list): return x
    if x in (None, "", "None", "[]"): return []
    try: return list(ast.literal_eval(x))
    except Exception: return []
def B(x): return x is True or str(x).strip().lower() == "true"

# ---------------------------------------------------------------- normalización y raíces
def norm(s):
    s = (s or "").replace("ｰ", "-").replace("’", "'").replace("‘", "'")
    s = re.sub(r"\([^)]*\)", " ", s)
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()
def nroot(r):
    s = unicodedata.normalize("NFKD", r.replace("ｰ", "-")).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"[^a-z0-9*]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()

SUF = r"(?:s|es|ed|ing)?\b"
_c = {}
def rx(root):
    if root in _c: return _c[root]
    r = root.lower().strip()
    if " " in r:
        words = r.split(); parts = []
        for w in words:
            if w == "*": parts.append(r"\w+")
            elif w.endswith("*"): parts.append(re.escape(w[:-1]) + r"\w*")
            else: parts.append(re.escape(w))
        pat = r"\b" + r"\s+".join(parts) + ("" if words[-1].endswith("*") else SUF)
    elif r.endswith("*"):
        pat = r"\b" + re.escape(r[:-1])
    elif len(r) >= 6:
        pat = r"\b" + re.escape(r)
    else:
        pat = r"\b" + re.escape(r) + SUF
    _c[root] = re.compile(pat)
    return _c[root]
def has(t, roots): return bool(t) and any(rx(r).search(t) for r in roots)
def count(t, roots): return sum(1 for r in roots if t and rx(r).search(t))
def pos(t, roots):
    b = None
    for r in roots:
        m = rx(r).search(t)
        if m and (b is None or m.start() < b): b = m.start()
    return b

def contexto(bg, move, moves):
    """Tramo que empieza tras el nombre del ataque y termina en el siguiente ataque nombrado o en el final de la frase."""
    if not bg: return ""
    sents = re.split(r"(?<=[.!?])\s+", bg)
    out = []; ml = move.lower(); others = [om.lower() for om in moves if om != move]
    for i, s in enumerate(sents):
        sl = s.lower(); p = sl.find(ml)
        if p < 0: continue
        start, end = p + len(ml), len(s)
        for om in others:
            for m in re.finditer(re.escape(om), sl):
                if start <= m.start() < end: end = m.start()
        out.append(s[start:end])
        if i + 1 < len(sents) and re.match(r"(This |The attack|The technique|The move|Those (who|hit|struck))", sents[i + 1]) \
                and not any(om in sents[i + 1].lower() for om in others):
            out.append(sents[i + 1])
    return norm(" ".join(out))

# ---------------------------------------------------------------- tablas
NIV = SPEC["niveles"]; ROL = {r["id"]: r for r in SPEC["roles"]}; ATR = SPEC["atributos"]
FAM = {}; FAMT = {}
for f in SPEC["familias"]:
    FAM[f["id"]] = f
    for t in f["tipos"]: FAMT[t] = f["id"]
ELE = {e["id"]: e for e in SPEC["elementos"]}
ORD_E = SPEC["clasificador"]["orden_prioridad_elementos"]
ORD_D = SPEC["orden_debilidad"]
EFE = {e["id"]: e for e in SPEC["efectos"]}
ORD_F = SPEC["orden_efectos"]
CL = SPEC["clasificador"]; RA = SPEC["rol_algoritmo"]
AL = CL["alcance"]; AR = CL["area"]
APOYO_N = [r for k in ORD_F["apoyo"] for r in EFE[k]["raices"]]
APOYO_C = [r for k in ORD_F["apoyo"] for r in EFE[k]["raices_contexto"]]
NOAPOYO_C = [r for g in ("dano", "estado", "tactica") for k in ORD_F[g] for r in EFE[k]["raices_contexto"]]
ALL_EF_N = [r for e in SPEC["efectos"] for r in e["raices"]]
ALL_EL_N = [r for e in SPEC["elementos"] for r in e["raices"]]
PDANO = CL["apoyo"]["palabras_dano"]
CA = CL["apoyo"]["contexto_aliado"]
def _alt(xs): return "|".join(re.escape(v[:-1]) + r"\w*" if v.endswith("*") else re.escape(v) + SUF[:-2] for v in xs)
ALLY_RX = re.compile(r"\b(?:%s)\w*(?:\s+\w+){0,%d}\s+(?:%s)\b" % (_alt(CA["verbos"]), CA["distancia_max_palabras"] - 1, _alt(CA["destinatarios"])))
OV = SPEC["overrides_iniciales"]
PLT = {p["id"]: p for p in SPEC["plantillas"]}
AM = SPEC["amenaza"]
LEG = {i: g for g, ids in AM["legendarios"].items() for i in ids}
JEF = set(i for ids in AM["jefes_sugeridos"].values() for i in ids)
ESB = set(AM["esbirros_sugeridos"])
VUELA_IDS = set(SPEC["vuelo"]["ids"])
CONTROL_DURO = [k for k, e in EFE.items() if e["control_duro"]]
BEBE_PROHIBIDAS = ["ejecutar"] + CONTROL_DURO

def fila(x):
    row = NIV[x["level"]]
    tgt = row.get("por_id", {}).get(x["id"])
    if tgt: base = dict(NIV[tgt]); base["etiqueta"] = row.get("etiqueta"); return base, row
    return row, row

def afinidad(fam, tipo):
    f = FAM[fam]
    if f["afinidad"] == "segun_tipo": return f["elemento_por_tipo"][tipo]["afinidad"]
    return f["afinidad"]

def potencias(n, nivel, rango):
    if nivel == "In-Training 1": return ["P1"] * n
    if nivel == "In-Training 2": return ["P2"] + ["P1"] * (n - 1)
    if n == 1: return ["P2/P3"]
    out = ["P3", "P2", "P2" if rango >= 3 else "P1"] + ["P1"] * max(0, n - 3)
    return out[:n]
PN = {"P1": 1, "P2": 2, "P3": 3, "P2/P3": 3}

def find_effects(t, group, ctx=False):
    key = "raices_contexto" if ctx else "raices"
    return [k for k in ORD_F[group] if has(t, EFE[k][key])]

def elemento_en(t, key):
    if not t: return None
    for e in ORD_E:
        if any(" " in r and rx(r).search(t) for r in ELE[e][key]): return e
    for e in ORD_E:
        if any(" " not in r and rx(r).search(t) for r in ELE[e][key]): return e
    return None

def es_apoyo(name, ctx):
    o = OV["tecnicas"].get(name, {})
    if "apoyo" in o: return o["apoyo"]
    n = norm(name)
    if has(n, APOYO_N) and not has(n, PDANO): return True
    if not has(n, ALL_EF_N) and not has(n, ALL_EL_N) and not has(n, PDANO) and has(ctx, APOYO_C) and not has(ctx, NOAPOYO_C) and not has(ctx, PDANO): return True
    if not has(n, PDANO) and ctx and ALLY_RX.search(ctx) and not has(ctx, PDANO): return True
    return False

def tecnica(name, ctx, pot, firma, rango, nivel, fam, tipo, mon_name):
    n = norm(name)
    T = {"nombre": name.replace("ｰ", "-"), "nombre_dato": name, "tipo": "oficial", "firma": firma, "potencia": pot}
    bebe = nivel in ("In-Training 1", "In-Training 2")
    if not firma and has(n, CL["palabras_menores"]) and pot in ("P2", "P3"):
        T["potencia"] = pot = "P%d" % (PN[pot] - 1)
    apoyo = es_apoyo(name, ctx)
    T["apoyo"] = apoyo
    # alcance
    by_word = True
    if apoyo:
        alc = "personal" if has(n, ["self", "body"]) else "distancia"
    elif has(n, AL["larga"]): alc = "larga"
    elif has(n, AL["distancia_fuerte"]) and not has(n, AL["toque"]): alc = "distancia"
    elif has(n, AL["toque"]) and not has(n, AL["distancia_fuerte"]): alc = "toque"
    elif has(n, AL["toque"]) and has(n, AL["distancia_fuerte"]):
        alc = "distancia" if pos(n, AL["distancia_fuerte"]) > pos(n, AL["toque"]) else "toque"
    else:
        ct, cd = count(ctx, AL["verbos_contexto_toque"]), count(ctx, AL["verbos_contexto_distancia"])
        if ct != cd: alc = "toque" if ct > cd else "distancia"
        elif has(n, AL["distancia_debil"]): alc = "distancia"
        else:
            by_word = False
            if firma: alc = "distancia"
            else: alc = "toque" if FAM[fam]["rol_primario"] in ("bruto", "tanque", "agil", "acechador", "versatil") else "distancia"
    T["alcance"] = alc; T["_alc_palabra"] = by_word
    # elemento
    el = elemento_en(n, "raices") or elemento_en(ctx, "raices_contexto")
    if el is None:
        af = afinidad(fam, tipo)
        el = af if (alc != "toque" and af != "neutro") else "neutro"
    T["elemento"] = el
    # área
    p = PN[pot]
    if apoyo: area = "zona" if has(n, AR["zona"]) else "individual"
    elif firma and rango == 4 and p >= 2 and has(n, AR["total"]): area = "total"
    elif has(n, AR["zona"]): area = "zona"
    elif not has(n, AR["rafaga"]) and p >= 2 and has(ctx, AR["zona_contexto"]): area = "zona"
    elif has(n, AR["rafaga"]): area = "rafaga"
    else: area = "individual"
    if not apoyo and p == 1: area = "individual"
    T["area"] = area
    # palabras clave
    if apoyo:
        sup = find_effects(n, "apoyo") + [k for k in find_effects(ctx, "apoyo", True) if k not in find_effects(n, "apoyo")]
        cl = [sup[0] if sup else "escudo"]
        rest = [k for k in sup if k not in cl]
        if rest: cl.append(rest[0])
        found = list(cl)
    else:
        cand = []
        for src, isctx in ((n, False), (ctx, True)):
            for g in ("apoyo", "dano", "estado", "tactica"):
                fe = find_effects(src, g, isctx)
                if fe and fe[0] not in cand: cand.append(fe[0])
        cl = []
        for c in cand:
            if bebe and c in BEBE_PROHIBIDAS: continue
            if area == "total" and EFE[c]["control_duro"]: continue
            if c == "ejecutar" and area != "individual":
                c = "brutal"
                if c in cl: continue
            if len(cl) < 2 and c not in cl: cl.append(c)
        found = list(cl)
    T["claves"] = cl; T["_found"] = found
    return T

def apply_ov_tec(T):
    o = OV["tecnicas"].get(T["nombre_dato"])
    if not o: return T
    for k, v in o.items():
        if k == "nota": T.setdefault("notas", []).append(v)
        else: T[k] = v
    if "claves" in o: T["_claves_fijas"] = True; T["_found"] = list(o["claves"])
    if "alcance" in o: T["_alc_palabra"] = True
    if "apoyo" in o and o["apoyo"] is False and T.get("claves") and EFE[T["claves"][0]]["grupo"] == "apoyo" and "claves" not in o:
        T["claves"] = T["claves"][1:]
    if not T.get("apoyo") and T.get("potencia") == "P1" and T.get("area") != "individual": T["area"] = "individual"
    if "apoyo" in o and o["apoyo"] is True and "claves" not in o:
        T["claves"] = [c for c in T["claves"] if EFE[c]["grupo"] == "apoyo"] or ["escudo"]
    return T

EVID = {"mistico": ["dormir", "encantar", "confundir", "sellar", "regresion", "atrapar", "ralentizar", "debilitar", "asustar", "cegar"],
        "acechador": ["perforante", "certero", "ejecutar", "ocultar"], "agil": ["rapido"],
        "bruto": ["brutal", "romper", "derribar", "aturdir"]}
ORDEN_FIJO = ["bruto", "versatil", "tirador", "mistico", "agil", "acechador", "tanque", "apoyo"]

def rol_de(x, fam, tecs, rango, hibrido):
    S = collections.Counter()
    W = RA["pesos"]
    if hibrido: S["versatil"] += 3
    else:
        S[FAM[fam]["rol_primario"]] += W["familia_primario"]; S[FAM[fam]["rol_secundario"]] += W["familia_secundario"]
    exc = None
    for r, ts in RA["excepciones_tipo"].items():
        if x["type"] in ts and not hibrido: S[r] += W["excepcion_tipo"]; exc = r
    for T in tecs:
        w = W["peso_firma"] if T["firma"] else W["peso_otra"]
        if T["apoyo"]: S["apoyo"] += 3 * w
        else:
            if T["alcance"] == "toque" and T["_alc_palabra"]: S["bruto"] += w
            if T["alcance"] in ("distancia", "larga") and T["_alc_palabra"]: S["tirador"] += w
        for c in T["_found"]:
            for r, ks in EVID.items():
                if c in ks: S[r] += w
            if c in ("contraataque", "provocar") or (c == "escudo" and not T["apoyo"]): S["tanque"] += w
            if c in ("invocar", "drenar") or (c in ("mejora", "curar") and not T["apoyo"]): S["mistico"] += w
    if rango == 4 and any(T["alcance"] == "toque" for T in tecs) and any(T["alcance"] in ("distancia", "larga") for T in tecs):
        S["versatil"] += 2
    if tecs and sum(1 for T in tecs if T["apoyo"]) * 2 > len(tecs): S["apoyo"] += 4
    if fam == "elemental" and x["type"] == "Fire": S["bruto"] += 1
    best = max(S.values()) if S else 0
    tops = [r for r in ORDEN_FIJO if S[r] == best]
    prim = "versatil" if hibrido else FAM[fam]["rol_primario"]
    if prim in tops: return prim, S
    if exc in tops: return exc, S
    return tops[0], S

def plantillas(x, row):
    out = []; name = x["name"]; lvl = x["level"]
    if B(x["x_antibody"]): out.append("x_antibody")
    if B(x["is_mode"]) and lvl != "Hybrid":
        if any(m in name for m in PLT["supremo"]["marcas"]): out.append("supremo")
        elif any(m in name for m in PLT["modo_oscuro"]["marcas"]): out.append("modo_oscuro")
        else: out.append("modo_alterno")
    if lvl == "Hybrid":
        if NIV["Hybrid"].get("clase_por_id", {}).get(x["id"]) == "fusion": out.append("fusion")
        out.append("hibrido")
    if lvl == "Armor": out.append("armadura")
    if lvl in ("In-Training 1", "In-Training 2"): out.append("bebe")
    return out

def deb_res(fam, tipo, main):
    f = FAM[fam]
    if f["afinidad"] == "segun_tipo":
        d0, r0 = list(f["elemento_por_tipo"][tipo]["debilidad"]), list(f["elemento_por_tipo"][tipo]["resistencia"])
    else:
        d0, r0 = list(f["debilidad"]), list(f["resistencia"])
    exc = f.get("excepciones_tipo", {}).get(tipo)
    if exc: d0, r0 = list(exc["debilidad"]), list(exc["resistencia"])
    d, r = list(d0), list(r0)
    if main:
        beat = next((e for e in ORD_D if main in ELE[e]["vence_a"] and e not in d0 and e not in r0), None)
        if beat: d.append(beat)
        if main not in ("neutro", "cosmico") and main not in r: r.append(main)
    both = set(d) & set(r)
    d = [e for e in d if e not in both][:2]; r = [e for e in r if e not in both][:2]
    return d, r

# ---------------------------------------------------------------- índice de amenaza
def _p_bandas(mod):
    o = {10: 0.0, 7: 0.0, 6: 0.0}
    for a, b in itertools.product(range(1, 7), repeat=2):
        if (a, b) == (6, 6): k = 10
        elif (a, b) == (1, 1): k = 6
        else:
            s = a + b + mod; k = 10 if s >= 10 else 7 if s >= 7 else 6
        o[k] += 1 / 36
    return o
def indice_amenaza(F, caras):
    """amenaza.indice_amenaza: ofensiva × PV efectivos frente a una pareja media de su mismo rango."""
    m = (caras + 1) / 2; R = F["rango"]
    otras = [(PN[t["potencia"]] if t["potencia"] != "P2/P3" else 2) for t in F["tecnicas"] if t["tipo"] == "oficial" and not t["apoyo"] and not t["firma"] and t.get("potencia")]
    firma = next((t for t in F["tecnicas"] if t.get("firma") and not t["apoyo"]), None)
    df = 3 if firma else 2
    dados = (df + max(otras + [1])) / 2
    pb = _p_bandas((R + 1) - F["atq"])          # Defensa del PJ medio: Def = rango + 1
    f_area = AM["indice_amenaza"]["factor_area"].get(firma["area"], 1) if firma else 1
    ofensiva = m * dados * (pb[6] + 0.5 * pb[7]) * f_area
    pa = _p_bandas((R + 1) - F["def"])           # ataque del PJ medio: Atq = rango + 1
    p_imp = pa[10] + pa[7]
    g_arm = (2 * m) / max(1.0, 2 * m - F["arm"])
    g_res = 1 + 0.15 * len(F["resistencias"])
    cura = any("drenar" in t["claves"] for t in F["tecnicas"] if t["tipo"] == "oficial" and t.get("firma")) or F["familia"] == "oscuro"
    pv_ef = F["pv"] * g_arm * g_res * (1.2 if cura else 1) / max(0.05, p_imp)
    return round(ofensiva * ofensiva * pv_ef, 1)

def asignar_mod_pa(fichas):
    IA = AM["indice_amenaza"]
    grupos = collections.defaultdict(list)
    for F in fichas:
        if F["rol"] is None: F["mod_pa"] = 1; F["amenaza_nivel"] = "media"; continue
        grupos[F["fila_validacion"]].append(F)
    cortes = {}
    for g, fs in grupos.items():
        xs = sorted(F["indice_amenaza"] for F in fs)
        t1, t2 = xs[len(xs) // 3], xs[(2 * len(xs)) // 3]
        cortes[g] = [t1, t2]
        for F in fs:
            v = F["indice_amenaza"]
            if v < t1: F["mod_pa"], F["amenaza_nivel"] = IA["mod_pa"]["baja"], "baja"
            elif v >= t2: F["mod_pa"], F["amenaza_nivel"] = IA["mod_pa"]["alta"], "alta"
            else: F["mod_pa"], F["amenaza_nivel"] = IA["mod_pa"]["media"], "media"
    return cortes

# ---------------------------------------------------------------- ficha
def ficha(x):
    row, raw = fila(x)
    lvl = x["level"]; R = row["rango"]; caras = row["dado_caras"]; vf = row["vf"]
    bebe = lvl in ("In-Training 1", "In-Training 2"); hibrido = lvl == "Hybrid"
    fam = FAMT[x["type"]]
    moves = L(x["moves"]); bg = x.get("background_EN_reference_only", "")
    ap = [es_apoyo(m, contexto(bg, m, moves)) for m in moves]
    dmg = [i for i in range(len(moves)) if not ap[i]] or list(range(len(moves)))
    fi = next((i for i in dmg if has(norm(moves[i]), CL["firma"]["palabras_potencia_maxima"])), dmg[0] if dmg else 0)
    if moves: moves = [moves[fi]] + [m for i, m in enumerate(moves) if i != fi]
    pots = potencias(len(moves), lvl, R)
    tecs = []
    for i, m in enumerate(moves):
        T = tecnica(m, contexto(bg, m, moves), pots[i], i == 0, R, lvl, fam, x["type"], x["name"])
        tecs.append(apply_ov_tec(T))
    if not moves and not bebe:
        sd = CL["sin_tecnicas"]
        tecs.append({"nombre": sd["nombre"], "nombre_dato": None, "tipo": "generica", "firma": True, "potencia": "P2/P3", "apoyo": False,
                     "alcance": "distancia", "_alc_palabra": False, "elemento": afinidad(fam, x["type"]), "area": "individual",
                     "claves": [], "_found": []})
    rol = None; S = {}
    if not bebe:
        rol, S = rol_de(x, fam, [t for t in tecs if t["tipo"] == "oficial"], R, hibrido)
        o = OV["digimon"].get(x["id"], {})
        if "rol" in o: rol = o["rol"]
    for T in tecs:
        if T.get("_claves_fijas"): continue
        if not T["apoyo"]:
            if not any(EFE[c]["grupo"] == "estado" for c in T["claves"]) and len(T["claves"]) < 2:
                ds = ELE[T["elemento"]]["estado_por_defecto"]
                if ds and ds not in T["claves"] and not (bebe and EFE[ds]["control_duro"]): T["claves"].append(ds)
            if T["firma"] and rol and len(T["claves"]) < 2:
                pf = ROL[rol]["palabra_firma"]
                if pf and pf not in T["claves"]: T["claves"].append(pf)
        if rol == "tirador" and T["firma"] and T["alcance"] == "distancia": T["alcance"] = "larga"
    pl = plantillas(x, row)
    rm = ROL[rol]["mods"] if rol else {"atq": 0, "def": 0, "pv_mult": 0, "arm": 0, "ini": 0}
    fm = FAM[fam]["mods"] if not bebe else {"pv_mult": 0, "arm": 0, "ini": 0}
    am = ATR[x["attribute"]]["mods"]
    sp = lambda k: sum(PLT[p]["mods"].get(k, 0) for p in pl)
    if bebe: pv = row["pv_base"]
    else: pv = vf * (7 + rm["pv_mult"] + fm["pv_mult"] + am["pv_mult"] + sp("pv_mult"))
    atq = R + rm["atq"] + am["atq"] + sp("atq")
    de = R + rm["def"] + am["def"] + sp("def")
    arm = 0 if bebe else min(2, rm["arm"] + fm["arm"] + sp("arm"))
    ini = R + rm["ini"] + am["ini"] + fm["ini"] + sp("ini")
    of = [t for t in tecs if t["tipo"] == "oficial" and t["elemento"] != "neutro"]
    if FAM[fam]["afinidad"] == "segun_tipo": main = afinidad(fam, x["type"])
    elif of:
        c = collections.Counter(t["elemento"] for t in of); mx = max(c.values())
        main = next(t["elemento"] for t in of if c[t["elemento"]] == mx)
    else: main = None
    deb, res = ([], []) if bebe else deb_res(fam, x["type"], main)
    if "armadura" in pl and tecs and tecs[0]["elemento"] not in ("neutro",) and tecs[0]["elemento"] not in res:
        res = (res + [tecs[0]["elemento"]])[:2]; deb = [d for d in deb if d not in res]
    vuela = fam == "ave" or x["type"] in SPEC["vuelo"]["tipos"] or x["id"] in VUELA_IDS
    nada = fam == "acuatico" or x["type"] in SPEC["nado"]["tipos"]
    o = OV["digimon"].get(x["id"], {})
    if "vuela" in o: vuela = o["vuela"]
    fb = FAM[fam]["tecnica_basica"]
    bel = afinidad(fam, x["type"]) if fb["elemento"] == "afinidad" else fb["elemento"]
    balc = "distancia" if (rol == "tirador" or FAM[fam].get("basica_alcance") == "distancia") else "toque"
    basica = {"nombre": "Disparo" if rol == "tirador" else fb["nombre"], "tipo": "basica", "firma": False, "potencia": "P1",
              "dados": "1d%d" % caras, "alcance": balc, "area": "individual", "elemento": bel, "claves": [], "apoyo": False, "agotadora": False}
    out_t = [basica]
    if rol:
        mn = dict(ROL[rol]["maniobra"]); mn["tipo"] = "maniobra"
        if mn.get("elemento") == "afinidad": mn["elemento"] = afinidad(fam, x["type"])
        mn["agotadora"] = mn.get("uso") == "agotadora"
        out_t.append(mn)
    for T in tecs:
        p = T["potencia"]; nd = PN[p] if p != "P2/P3" else 2
        area_on = T["area"] != "individual"
        dados = dados_a = med = med_a = None
        if not T["apoyo"]:
            if p == "P2/P3":
                dados = "2d%d / 3d%d" % (caras, caras); med = [2 * (caras + 1) / 2, 3 * (caras + 1) / 2]
                if area_on: dados_a = "1d%d / 2d%d" % (caras, caras); med_a = [(caras + 1) / 2, caras + 1]
            else:
                dados = "%dd%d" % (nd, caras); med = nd * (caras + 1) / 2
                if area_on: dados_a = "%dd%d" % (max(1, nd - 1), caras); med_a = max(1, nd - 1) * (caras + 1) / 2
        apoyo_cd = T["apoyo"] and any(c in ("curar", "escudo") for c in T["claves"])
        if T["apoyo"] and not any(c in ("curar", "escudo", "mejora", "purificar") for c in T["claves"]): p = None
        out_t.append({"nombre": T["nombre"], "nombre_dato": T.get("nombre_dato"), "tipo": T["tipo"], "firma": T["firma"], "potencia": p,
                      "dados": dados, "dano_medio": med, "dados_area": dados_a, "dano_medio_area": med_a,
                      "alcance": T["alcance"], "area": T["area"], "elemento": T["elemento"], "claves": T["claves"], "apoyo": T["apoyo"],
                      "agotadora": (p in ("P3", "P2/P3")) or apoyo_cd, "_fijas": bool(T.get("_claves_fijas"))})
    rasgos = []
    if rol: rasgos.append(dict(ROL[rol]["rasgo"], origen="rol"))
    if not bebe: rasgos.append({"id": FAM[fam]["id"], "nombre": FAM[fam]["rasgo"]["nombre"], "origen": "familia", "regla": FAM[fam]["rasgo"]["regla"]})
    if ATR[x["attribute"]]["rasgo"]: rasgos.append(dict(ATR[x["attribute"]]["rasgo"], origen="atributo"))
    for pp in pl: rasgos.append(dict(PLT[pp]["rasgo"], origen="plantilla"))
    amen = "legendario" if x["id"] in LEG else ("jefe" if x["id"] in JEF else ("esbirro" if x["id"] in ESB else "estandar"))
    notas = []
    if lvl == "Rookie" and not any(any(d["name"] == pn and d["level"] == "In-Training 2" for d in DATA) for pn in L(x["prev"])):
        notas.append("Sin Bebé II en los datos: el jugador elige con el DJ uno de la misma familia o de aspecto parecido, o usa la ficha genérica de Bebé II (10 PV, d4).")
    esp = [FAM[fam]["especialidad"]] if not bebe else []
    if rol: esp.append(ROL[rol]["especialidad"])
    fv = row["id"] if row["id"] in SPEC["validacion"]["rangos_por_nivel"] else NIV[lvl].get("fila_de", row["id"])
    F = {"id": x["id"], "nombre": x["name"], "nivel": row["nombre"] if not row.get("etiqueta") else raw["nombre"],
         "fila": row["id"], "fila_validacion": fv, "rango": R, "familia": fam, "tipo": x["type"], "tipo_es": SPEC["traduccion_tipos"][x["type"]],
         "rol": rol, "atributo": ATR[x["attribute"]]["id"], "plantillas": pl, "amenaza_sugerida": amen,
         "grupo_legendario": LEG.get(x["id"]), "dado": "d%d" % caras, "vf": vf, "pv": pv, "atq": atq, "def": de,
         "arm": arm, "ini": ini, "vuela": vuela, "nada": nada, "elemento_principal": main, "debilidades": deb,
         "resistencias": res, "especialidades": esp, "rasgos": rasgos, "tecnicas": out_t, "prev": L(x["prev"]), "next": L(x["next"]),
         "modos": L(x["modes"]), "notas": notas, "_scores": dict(S)}
    F["indice_amenaza"] = 0 if bebe else indice_amenaza(F, caras)
    return F

# ---------------------------------------------------------------- validación
def _raices_spec():
    out = []
    for e in SPEC["elementos"]: out += e["raices"] + e["raices_contexto"]
    for e in SPEC["efectos"]: out += e["raices"] + e["raices_contexto"]
    for k, v in CL["alcance"].items():
        if k != "orden": out += v
    for k, v in CL["area"].items():
        if k != "orden": out += v
    out += CL["firma"]["palabras_potencia_maxima"] + CL["palabras_menores"] + PDANO + CA["verbos"] + CA["destinatarios"]
    return out

def validar(fichas):
    err = []
    V = SPEC["validacion"]["rangos_por_nivel"]
    for F in fichas:
        r = V.get(F["fila_validacion"])
        if r is None: err.append((F["id"], "sin rango de validación", F["fila"]))
        else:
            for k in ("pv", "atq", "def", "arm"):
                if not (r[k][0] <= F[k] <= r[k][1]): err.append((F["id"], F["fila_validacion"], k, F[k]))
        of = [t for t in F["tecnicas"] if t["tipo"] in ("oficial", "generica")]
        if sum(1 for t in of if t["potencia"] in ("P3", "P2/P3")) > 1: err.append((F["id"], "más de una P3"))
        bebe = "bebe" in F["plantillas"]
        for t in F["tecnicas"]:
            cl = [c.split("|")[0] for c in t.get("claves", [])]
            if len(cl) > 2: err.append((F["id"], t["nombre"], "más de 2 claves"))
            if bebe and (t.get("potencia") in ("P3", "P2/P3") or any(c in BEBE_PROHIBIDAS for c in cl)): err.append((F["id"], t["nombre"], "Bebé con P3/Ejecutar/control duro"))
            if t["area"] == "total" and not (t.get("firma") and F["rango"] == 4): err.append((F["id"], t["nombre"], "Total fuera de Firma de rango 4"))
            if t["tipo"] != "oficial": continue
            if "ejecutar" in cl and t["area"] != "individual": err.append((F["id"], t["nombre"], "Ejecutar en área"))
            if not t["apoyo"] and t["potencia"] == "P1" and t["area"] != "individual": err.append((F["id"], t["nombre"], "P1 de daño con área"))
            if t["apoyo"]:
                if t.get("dados"): err.append((F["id"], t["nombre"], "apoyo con daño"))
                if any(EFE[c]["grupo"] in ("dano", "estado") for c in cl): err.append((F["id"], t["nombre"], "apoyo con palabra de daño o estado"))
                if any(EFE[c]["grupo"] == "tactica" for c in cl) and not t.get("_fijas"): err.append((F["id"], t["nombre"], "apoyo con táctica sin override"))
        tipos = [t["tipo"] for t in F["tecnicas"]]
        if "basica" not in tipos or (not bebe and "maniobra" not in tipos): err.append((F["id"], "sin básica o maniobra"))
    asign = [t for f in SPEC["familias"] for t in f["tipos"]]
    if len(asign) != len(set(asign)) or len(set(asign)) != 140: err.append(("familias", "los 140 tipos no están asignados una sola vez", len(asign), len(set(asign))))
    moves = set(m for x in DATA for m in L(x["moves"])); ids = set(x["id"] for x in DATA)
    for k in OV["tecnicas"]:
        if k not in moves: err.append(("override de técnica inexistente", k))
    for k in OV["digimon"]:
        if k not in ids: err.append(("override de Digimon con id inexistente", k))
    listas = list(LEG) + list(JEF) + list(ESB) + list(VUELA_IDS)
    for lv in NIV.values():
        listas += list(lv.get("por_id", {})) + list(lv.get("clase_por_id", {}))
    for i in listas:
        if i not in ids: err.append(("id inexistente en una lista", i))
    for r in _raices_spec():
        if nroot(r) != r: err.append(("raíz sin normalizar", r))
    return err

if __name__ == "__main__":
    fichas = [ficha(x) for x in DATA]
    cortes = asignar_mod_pa(fichas)
    err = validar(fichas)
    c = collections.Counter(F["rol"] for F in fichas)
    print("roles", c.most_common())
    ofi = [t for F in fichas for t in F["tecnicas"] if t["tipo"] == "oficial"]
    print("tecnicas", len(ofi), "elementos", collections.Counter(t["elemento"] for t in ofi).most_common())
    print("alcances", collections.Counter(t["alcance"] for t in ofi).most_common())
    print("areas", collections.Counter(t["area"] for t in ofi).most_common())
    print("apoyo", sum(t["apoyo"] for t in ofi), "sin claves", sum(1 for t in ofi if not t["claves"]))
    print("claves", collections.Counter(k for t in ofi for k in t["claves"]).most_common())
    print("amenaza", collections.Counter(F["amenaza_sugerida"] for F in fichas).most_common())
    print("debilidades", collections.Counter(d for F in fichas for d in F["debilidades"]).most_common())
    print("cortes de indice de amenaza", cortes)
    for fila_id in ("novato", "campeon", "perfecto", "definitivo"):
        pvs = [F["pv"] for F in fichas if F["fila"] == fila_id]
        if pvs: print(fila_id, "pv min/med/max", min(pvs), round(sum(pvs) / len(pvs), 1), max(pvs), "n", len(pvs))
    if OUT:
        json.dump(fichas, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("errores de validación:", len(err))
    for e in err[:40]: print("  ", e)
    if err: sys.exit(1)
