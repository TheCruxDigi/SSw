"use strict";
/* Digimon: Lazos de Código — lector del manual, bestiario y ficha editable. */
(() => {
const $ = (s, el = document) => el.querySelector(s);
const $$ = (s, el = document) => [...el.querySelectorAll(s)];
const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const slug = id => String(id).replace(/[^A-Za-z0-9._~-]/g, "-");
const norm = s => String(s || "").toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");
const sgn = n => (n > 0 ? "+" : n < 0 ? "−" : "+") + Math.abs(n);
const store = {
  get(k, d) { try { const v = localStorage.getItem(k); return v == null ? d : JSON.parse(v); } catch (e) { return d; } },
  set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} },
};

const S = { manifest: [], best: [], byId: new Map(), bySlug: new Map(), byName: new Map(), R: null, mdCache: new Map(), view: null };
const main = $("#main"), rail = $("#rail");
const LEVEL_ORDER = ["Bebé I", "Bebé II", "Novato", "Campeón", "Armadura", "Híbrido", "Perfecto", "Definitivo", "Desconocido"];
const ATTR_CLASS = { vacuna: "vac", datos: "dat", virus: "vir" };

/* ---------- carga de datos ---------- */
async function loadJSON(p) { const r = await fetch(p); if (!r.ok) throw new Error(p + " " + r.status); return r.json(); }
async function boot() {
  try {
    const [man, best, R] = await Promise.all([loadJSON("capitulos/manifest.json"), loadJSON("data/bestiario.json"), loadJSON("data/reglas.json")]);
    S.manifest = man; S.best = best; S.R = R;
    for (const d of best) {
      S.byId.set(d.id, d); S.bySlug.set(slug(d.id), d);
      const k = norm(d.nombre); if (!S.byName.has(k)) S.byName.set(k, d);
    }
    S.lookup = {
      rol: Object.fromEntries(R.roles.map(x => [x.id, x])),
      fam: Object.fromEntries(R.familias.map(x => [x.id, x])),
      ele: Object.fromEntries(R.elementos.map(x => [x.id, x])),
      efe: Object.fromEntries(R.efectos.map(x => [x.id, x])),
      alc: Object.fromEntries(R.alcances.map(x => [x.id, x])),
      area: Object.fromEntries(R.areas.map(x => [x.id, x])),
      atr: Object.fromEntries(Object.values(R.atributos).map(x => [x.id, x])),
      pla: Object.fromEntries(R.plantillas.map(x => [x.id, x])),
    };
  } catch (e) {
    main.innerHTML = `<div class="doc"><h1>No se pudieron cargar los datos</h1><p>${esc(e.message)}. Recarga la página; si el problema sigue, los archivos del manual no se publicaron completos.</p></div>`;
    return;
  }
  buildRail();
  window.addEventListener("hashchange", route);
  route();
}

/* ---------- índice lateral ---------- */
function buildRail() {
  const groups = [];
  for (const c of S.manifest) { let g = groups.find(x => x.name === c.grupo); if (!g) groups.push(g = { name: c.grupo, items: [] }); g.items.push(c); }
  rail.innerHTML = `<a href="#inicio" data-r="inicio"><span class="n">⌂</span>Portada</a>` +
    groups.map(g => `<h4>${esc(g.name)}</h4>` + g.items.map(c => `<a href="#${c.id}" data-r="${c.id}"><span class="n">${esc(c.n)}</span>${esc(c.titulo)}</a>`).join("")).join("") +
    `<h4>Herramientas</h4><a href="#bestiario" data-r="bestiario"><span class="n">◆</span>Bestiario (${S.best.length})</a><a href="#ficha" data-r="ficha"><span class="n">✎</span>Ficha de personaje</a><a href="#encuentro" data-r="encuentro"><span class="n">⚔</span>Constructor de encuentros</a>`;
  rail.addEventListener("click", e => { if (e.target.closest("a")) rail.classList.remove("open"); });
}
$("#menuBtn").addEventListener("click", () => rail.classList.toggle("open"));
function markNav(r) {
  $$("a[data-r]", rail).forEach(a => a.dataset.r === r ? a.setAttribute("aria-current", "page") : a.removeAttribute("aria-current"));
  $$(".top nav a").forEach(a => a.dataset.nav === r || (r.startsWith("d-") && a.dataset.nav === "bestiario") ? a.setAttribute("aria-current", "page") : a.removeAttribute("aria-current"));
}

/* ---------- router ---------- */
function route() {
  const h = decodeURIComponent(location.hash.slice(1)) || "inicio";
  if (S.view && S.view.startsWith("c:") && h.startsWith(S.view.slice(2) + "_")) { const t = document.getElementById(h); if (t) { t.scrollIntoView(); return; } }
  if (h === "inicio") return home();
  if (h === "bestiario") return bestiary(null);
  if (h.startsWith("d-")) return bestiary(h.slice(2));
  if (h === "ficha") return sheet();
  if (h === "encuentro") return encounter();
  const ch = S.manifest.find(c => c.id === h || h.startsWith(c.id + "_"));
  if (ch) return chapter(ch, h);
  home();
}

/* ---------- portada ---------- */
function home() {
  S.view = "home"; markNav("inicio");
  const counts = {}; for (const d of S.best) counts[d.nivel] = (counts[d.nivel] || 0) + 1;
  const first = S.manifest[0];
  const groups = [];
  for (const c of S.manifest) { let g = groups.find(x => x.name === c.grupo); if (!g) groups.push(g = { name: c.grupo, items: [] }); g.items.push(c); }
  main.innerHTML = `<section class="hero">
    <div class="eyebrow">Juego de rol de mesa · 2d6 · en español</div>
    <h1>${esc(S.R.meta.titulo)}</h1>
    <p class="lead">${esc(S.R.meta.subtitulo)}</p>
    <div class="statline">
      <div><b>${S.best.length.toLocaleString("es")}</b><span>Digimon con ficha</span></div>
      <div><b>${S.manifest.length}</b><span>capítulos</span></div>
      <div><b>${S.R.familias.length}</b><span>familias</span></div>
      <div><b>${S.R.efectos.length}</b><span>efectos de técnica</span></div>
    </div>
    <div class="cards">
      ${first ? `<a class="card" href="#${first.id}"><b>Empieza a leer</b><span>${esc(first.titulo)}: qué es este juego y cómo se usa el manual.</span></a>` : ""}
      <a class="card" href="#bestiario"><b>Bestiario</b><span>Busca cualquier Digimon por nombre, nivel, atributo, familia o rol, y ajusta su ficha como esbirro, élite o jefe.</span></a>
      <a class="card" href="#encuentro"><b>Constructor de encuentros</b><span>Para el DJ: monta un combate con Digimon del bestiario, elige su plantilla y comprueba su dificultad en PA.</span></a>
      <a class="card" href="#ficha"><b>Ficha de personaje</b><span>Crea tu Tamer y tu compañero. Las cifras del Digimon se rellenan solas desde el bestiario.</span></a>
    </div>
    ${groups.map(g => `<div><div class="eyebrow" style="margin-top:14px">${esc(g.name)}</div><div class="cards">${g.items.map(c => `<a class="card" href="#${c.id}"><b>${esc(c.n)} · ${esc(c.titulo)}</b><span>${esc(c.resumen || "")}</span></a>`).join("")}</div></div>`).join("")}
    <p class="notice">${esc(S.R.meta.aviso_legal)}</p>
  </section>`;
  window.scrollTo(0, 0);
}

/* ---------- capítulos ---------- */
function linkDigimon(md) {
  return md.replace(/\[\[([^\]|]+?)(?:\|([^\]]+))?\]\]/g, (m, name, label) => {
    const d = S.byId.get(name.trim()) || S.byName.get(norm(name.trim()));
    const text = (label || name).trim();
    return d ? `<a class="dlink" href="#d-${slug(d.id)}">${esc(text)}</a>` : esc(text);
  });
}
async function chapter(ch, h) {
  S.view = "c:" + ch.id; markNav(ch.id);
  main.innerHTML = `<article class="doc"><p class="eyebrow">Capítulo ${esc(ch.n)}</p><p>Cargando…</p></article>`;
  let md = S.mdCache.get(ch.id);
  if (md == null) {
    try { const r = await fetch("capitulos/" + ch.archivo); md = await r.text(); S.mdCache.set(ch.id, md); }
    catch (e) { main.innerHTML = `<article class="doc"><h1>${esc(ch.titulo)}</h1><p>No se pudo cargar este capítulo. Recarga la página.</p></article>`; return; }
  }
  if (S.view !== "c:" + ch.id) return;
  const html = window.marked ? marked.parse(linkDigimon(md), { mangle: false, headerIds: false }) : `<pre>${esc(md)}</pre>`;
  const art = document.createElement("article"); art.className = "doc";
  art.innerHTML = `<p class="eyebrow">Capítulo ${esc(ch.n)} · ${esc(ch.grupo)}</p>` + html;
  const used = new Set();
  const heads = $$("h2,h3", art).map(hd => {
    let id = ch.id + "_" + norm(hd.textContent).replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "").slice(0, 60);
    while (used.has(id)) id += "-";
    used.add(id); hd.id = id; return hd;
  });
  $$("table", art).forEach(t => { const w = document.createElement("div"); w.className = "tbl"; t.replaceWith(w); w.appendChild(t); });
  const h2 = heads.filter(x => x.tagName === "H2");
  if (h2.length > 2) {
    const toc = document.createElement("nav"); toc.className = "toc"; toc.setAttribute("aria-label", "En este capítulo");
    toc.innerHTML = `<b>En este capítulo</b><ol>${h2.map(x => `<li><a href="#${x.id}">${esc(x.textContent)}</a></li>`).join("")}</ol>`;
    const h1 = $("h1", art); (h1 || art.firstChild).after(toc);
  }
  const i = S.manifest.indexOf(ch), prev = S.manifest[i - 1], next = S.manifest[i + 1];
  const pager = document.createElement("div"); pager.className = "pager";
  pager.innerHTML = (prev ? `<a href="#${prev.id}"><small>Anterior</small>${esc(prev.n)} · ${esc(prev.titulo)}</a>` : "<span></span>") +
    (next ? `<a href="#${next.id}" style="text-align:right"><small>Siguiente</small>${esc(next.n)} · ${esc(next.titulo)}</a>` : `<a href="#bestiario" style="text-align:right"><small>Siguiente</small>Bestiario</a>`);
  art.appendChild(pager);
  main.replaceChildren(art);
  const target = h !== ch.id && document.getElementById(h);
  if (target) target.scrollIntoView(); else window.scrollTo(0, 0);
}

/* ---------- bestiario ---------- */
const F = Object.assign({ q: "", nivel: "", atributo: "", familia: "", rol: "", elemento: "", grupo: "", amenaza: "", vuela: false, orden: "nivel" }, store.get("lazos-filtros", {}));
function chipAttr(id) { const a = S.lookup.atr[id]; return `<span class="chip ${ATTR_CLASS[id] || "neu"}">${esc(a ? a.nombre : id)}</span>`; }
function matches(d) {
  if (F.q) { const q = norm(F.q); if (!norm(d.nombre).includes(q) && !norm(d.tipo_es).includes(q) && !norm(d.tipo).includes(q) && !d.tecnicas.some(t => norm(t.nombre).includes(q))) return false; }
  if (F.nivel && d.nivel !== F.nivel) return false;
  if (F.atributo && d.atributo !== F.atributo) return false;
  if (F.familia && d.familia !== F.familia) return false;
  if (F.rol && d.rol !== F.rol) return false;
  if (F.elemento && d.elemento_principal !== F.elemento) return false;
  if (F.grupo === "legendario" && !d.grupo_legendario) return false;
  if (F.grupo === "x" && !(d.plantillas || []).includes("x_antibody")) return false;
  if (F.grupo === "modo" && !(d.plantillas || []).some(p => /modo|supremo|oscuro/.test(p))) return false;
  if (F.amenaza && d.amenaza_sugerida !== F.amenaza) return false;
  if (F.vuela && !d.vuela) return false;
  return true;
}
function sorted(list) {
  const lv = d => LEVEL_ORDER.indexOf(d.nivel);
  const by = { nivel: (a, b) => lv(a) - lv(b) || a.nombre.localeCompare(b.nombre), nombre: (a, b) => a.nombre.localeCompare(b.nombre), pv: (a, b) => b.pv - a.pv || a.nombre.localeCompare(b.nombre), atq: (a, b) => b.atq - a.atq || a.nombre.localeCompare(b.nombre) }[F.orden];
  return list.slice().sort(by);
}
function opts(list, cur, all) { return `<option value="">${esc(all)}</option>` + list.map(([v, t]) => `<option value="${esc(v)}"${v === cur ? " selected" : ""}>${esc(t)}</option>`).join(""); }
function bestiary(sl) {
  const R = S.R;
  if (S.view !== "bestiario") {
    S.view = "bestiario";
    const levels = LEVEL_ORDER.filter(l => S.best.some(d => d.nivel === l));
    const elems = R.elementos.map(e => [e.id, e.nombre]);
    main.innerHTML = `<div class="bst">
      <div class="bst-head">
        <div><p class="eyebrow">Bestiario</p><h1 class="bst-title">Los ${S.best.length.toLocaleString("es")} Digimon</h1></div>
        <p class="bst-help">Cada ficha sale de la especificación de reglas. Ábrela y elige una plantilla de amenaza para usarla como esbirro, élite o jefe.</p>
      </div>
      <form class="filters" id="filters" role="search" onsubmit="return false">
        <label class="f-q"><span>Buscar</span><input id="f-q" type="search" placeholder="Nombre, tipo o técnica" value="${esc(F.q)}" autocomplete="off"></label>
        <label><span>Nivel</span><select id="f-nivel">${opts(levels.map(l => [l, l]), F.nivel, "Todos")}</select></label>
        <label><span>Atributo</span><select id="f-atributo">${opts(Object.values(R.atributos).map(a => [a.id, a.nombre]), F.atributo, "Todos")}</select></label>
        <label><span>Familia</span><select id="f-familia">${opts(R.familias.map(f => [f.id, f.nombre]), F.familia, "Todas")}</select></label>
        <label><span>Rol</span><select id="f-rol">${opts(R.roles.map(r => [r.id, r.nombre]), F.rol, "Todos")}</select></label>
        <label><span>Elemento</span><select id="f-elemento">${opts(elems, F.elemento, "Todos")}</select></label>
        <label><span>Grupo</span><select id="f-grupo">${opts([["legendario", "Legendarios"], ["x", "X-Antibody"], ["modo", "Modos"]], F.grupo, "Todos")}</select></label>
        <label><span>Orden</span><select id="f-orden">${[["nivel", "Por nivel"], ["nombre", "Alfabético"], ["pv", "Más PV"], ["atq", "Más Ataque"]].map(([v, t]) => `<option value="${v}"${F.orden === v ? " selected" : ""}>${t}</option>`).join("")}</select></label>
        <label class="f-chk"><input id="f-vuela" type="checkbox"${F.vuela ? " checked" : ""}> Vuela</label>
        <button class="pill" id="f-reset" type="button">Quitar filtros</button>
      </form>
      <div class="bst-body">
        <div class="bst-list" id="blist" aria-live="polite"></div>
        <div class="bst-detail" id="bdetail"></div>
      </div>
    </div>`;
    const sync = () => {
      F.q = $("#f-q").value; ["nivel", "atributo", "familia", "rol", "elemento", "grupo", "orden"].forEach(k => F[k] = $("#f-" + k).value);
      F.vuela = $("#f-vuela").checked; store.set("lazos-filtros", F); renderList();
    };
    $("#filters").addEventListener("input", sync);
    $("#f-reset").addEventListener("click", () => {
      Object.assign(F, { q: "", nivel: "", atributo: "", familia: "", rol: "", elemento: "", grupo: "", amenaza: "", vuela: false });
      $("#f-q").value = ""; ["nivel", "atributo", "familia", "rol", "elemento", "grupo"].forEach(k => $("#f-" + k).value = ""); $("#f-vuela").checked = false;
      store.set("lazos-filtros", F); renderList();
    });
    renderList();
  }
  markNav(sl ? "d-" : "bestiario");
  const d = sl && S.bySlug.get(sl);
  const det = $("#bdetail");
  det.innerHTML = d ? statBlock(d) : `<div class="sb-empty"><b>Elige un Digimon</b><span>Toca cualquier nombre de la lista para ver su ficha completa.</span></div>`;
  det.classList.toggle("open", !!d);
  $$("#blist a").forEach(a => a.toggleAttribute("aria-current", !!d && a.dataset.id === d.id));
  if (d) {
    wireStatBlock(det, d);
    if (window.matchMedia("(max-width: 1100px)").matches) det.scrollIntoView({ block: "start" });
  }
}
function renderList() {
  const list = sorted(S.best.filter(matches));
  const el = $("#blist");
  const cur = location.hash.startsWith("#d-") ? location.hash.slice(3) : "";
  let html = `<p class="count">${list.length.toLocaleString("es")} resultado${list.length === 1 ? "" : "s"}</p>`;
  if (!list.length) html += `<p class="sb-empty"><b>Ningún Digimon coincide</b><span>Prueba con menos filtros o con otra palabra.</span></p>`;
  html += list.map(d => `<a class="row" href="#d-${slug(d.id)}" data-id="${esc(d.id)}"${slug(d.id) === cur ? ' aria-current="true"' : ""}>
      <span class="r-name">${esc(d.nombre)}${d.grupo_legendario ? ' <i class="leg" title="Legendario">★</i>' : ""}</span>
      <span class="r-meta">${esc(d.nivel)} · ${esc(d.tipo_es)}</span>
      <span class="r-chips">${chipAttr(d.atributo)}</span>
      <span class="r-stats"><b>${d.pv}</b> PV · ${sgn(d.atq)}/${sgn(d.def)}</span></a>`).join("");
  el.innerHTML = html;
}

/* plantillas de amenaza */
const THREATS = [["estandar", "Estándar"], ["esbirro", "Esbirro"], ["elite", "Élite"], ["jefe", "Jefe"], ["jefe1", "Jefe · Refuerzo I"], ["jefe2", "Jefe · Refuerzo II"], ["legendario", "Legendario"]];
const threatName = t => (THREATS.find(x => x[0] === t) || [0, "Estándar"])[1];
function applyThreat(d, t, N) {
  const base = t === "jefe1" || t === "jefe2" ? "jefe" : t;
  const A = S.R.amenaza[base]; if (!A || base === "estandar") return { pv: d.pv, atq: d.atq, def: d.def, arm: d.arm, ini: d.ini, acciones: 1, extra: 0, reglas: [] };
  const pv = { esbirro: Math.ceil(d.pv / 4), elite: Math.floor(d.pv * 1.5), jefe: Math.floor(d.pv * (N + 2) / 2), jefe1: Math.floor(d.pv * (N + 3) / 2), jefe2: Math.floor(d.pv * (N + 3) / 2), legendario: Math.floor(d.pv * (N + 3) / 2) }[t];
  const acciones = { jefe: Math.ceil(N / 2), jefe1: Math.ceil(N / 2) + 1, jefe2: N, legendario: Math.ceil(N / 2) }[t] || 1;
  const extra = (A.dados_extra || 0) + (t === "jefe2" ? 1 : 0);
  const reglas = (A.reglas || []).slice();
  if (t === "jefe1") reglas.unshift("Refuerzo I (Jefe de la aventura con Vínculo 2-3, o 4 sin Definitivo desbloqueado): PV × (N + 3) / 2 y una acción más por asalto. Para el presupuesto cuenta un nivel por encima.");
  if (t === "jefe2") reglas.unshift("Refuerzo II (Jefe de la aventura con Vínculo 4 con Definitivo desbloqueado, o 5): PV × (N + 3) / 2, N acciones por asalto y +1 dado en todas sus técnicas. Para el presupuesto cuenta un nivel por encima.");
  return { pv, atq: d.atq + (A.atq || 0), def: d.def + (A.def || 0), arm: Math.min(3, d.arm + (A.arm || 0)), ini: d.ini + (A.ini || 0), acciones, extra, reglas };
}
const PA_BASE = { esbirro: 0.25, estandar: 1, elite: 2 };
function paOf(d, t, N, ref) {
  const base = t.startsWith("jefe") ? N : t === "legendario" ? 2 * N : PA_BASE[t] || 1;
  const diff = (d.rango ?? 1) - ref + (t === "jefe1" || t === "jefe2" ? 1 : 0);
  const f = diff <= -3 ? 1 / 8 : diff >= 3 ? 15 : { "-2": 0.25, "-1": 0.5, "0": 1, "1": 2, "2": 5 }[String(diff)];
  return base * f * (d.mod_pa || 1);
}
const fmtPA = x => (Math.round(x * 100) / 100).toLocaleString("es");
const ENC = Object.assign({ N: 4, ref: 1, list: [] }, store.get("lazos-encuentro", {}));
const saveEnc = () => store.set("lazos-encuentro", ENC);
function techRow(t, d, extra) {
  const L = S.lookup;
  const claves = (t.claves || []).map(c => { const e = L.efe[c]; return `<span class="kw" title="${esc(e ? e.regla : c)}">${esc(e ? e.nombre : c)}</span>`; }).join(" ");
  let dados = t.dados || "";
  if (dados && extra) { const m = dados.match(/^(\d+)d(\d+)$/); if (m) dados = `${+m[1] + extra}d${m[2]}`; }
  const media = dados && /^(\d+)d(\d+)$/.test(dados) ? (() => { const [, n, c] = dados.match(/^(\d+)d(\d+)$/); return (n * (+c + 1) / 2).toFixed(1).replace(".0", ""); })() : "";
  const tipo = { basica: "Básica", maniobra: "Maniobra", oficial: "Técnica", generica: "Genérica" }[t.tipo] || "";
  return `<tr>
    <td><b>${esc(t.nombre)}</b>${t.firma ? ' <span class="tag firma">Firma</span>' : ""}${t.agotadora ? ' <span class="tag" title="No puede usarse dos turnos seguidos">Agotadora</span>' : ""}<div class="sub">${tipo}${t.apoyo ? " · Apoyo" : ""}</div></td>
    <td>${esc(t.potencia || "—")}</td>
    <td class="num">${t.apoyo ? "—" : esc(dados || "—")}${media ? `<div class="sub">media ${media}</div>` : ""}</td>
    <td>${esc((L.alc[t.alcance] || {}).nombre || t.alcance || "")}${t.area && t.area !== "individual" ? `<div class="sub">${esc((L.area[t.area] || {}).nombre || t.area)}</div>` : ""}</td>
    <td>${esc((L.ele[t.elemento] || {}).nombre || t.elemento || "")}</td>
    <td>${claves || '<span class="sub">—</span>'}</td></tr>`;
}
function evoLinks(names) {
  if (!names || !names.length) return "—";
  return names.map(n => { const x = S.byName.get(norm(n)); return x ? `<a href="#d-${slug(x.id)}">${esc(n)}</a>` : esc(n); }).join(", ");
}
function statBlock(d, threat) {
  const L = S.lookup, R = S.R;
  threat = threat || d.amenaza_sugerida || "estandar";
  const N = S.groupN || 4;
  const v = applyThreat(d, threat, N);
  const fam = L.fam[d.familia], rol = L.rol[d.rol];
  const usedKw = new Set(); d.tecnicas.forEach(t => (t.claves || []).forEach(c => usedKw.add(c)));
  const sub = [d.nivel, `${d.tipo_es}${d.tipo && d.tipo !== d.tipo_es ? ` (${d.tipo})` : ""}`, fam ? fam.nombre : d.familia, rol ? rol.nombre : null].filter(Boolean).join(" · ");
  const plant = (d.plantillas || []).filter(p => p !== "bebe").map(p => (L.pla[p] || {}).nombre || p);
  return `<article class="sb" data-id="${esc(d.id)}">
    <header class="sb-h">
      <div class="sb-top"><span class="chip lvl">${esc(d.nivel)}</span>${chipAttr(d.atributo)}${d.grupo_legendario ? `<span class="chip">★ ${esc((R.grupos || {})[d.grupo_legendario] || d.grupo_legendario)}</span>` : ""}${plant.map(p => `<span class="chip">${esc(p)}</span>`).join("")}</div>
      <h2>${esc(d.nombre)}</h2>
      <p class="sb-sub">${esc(sub)}</p>
    </header>
    ${d.descripcion ? `<p class="sb-desc">${esc(d.descripcion)}</p>` : ""}
    <div class="sb-threat" role="radiogroup" aria-label="Plantilla de amenaza">
      ${THREATS.map(([k, t]) => `<button type="button" role="radio" aria-checked="${k === threat}" data-t="${k}" class="th${k === threat ? " on" : ""}">${t}</button>`).join("")}
      ${threat.startsWith("jefe") || threat === "legendario" ? `<label class="nsel">Parejas <input type="number" id="sb-n" min="1" max="8" value="${N}"></label>` : ""}
    </div>
    <div class="sb-pa"><span>Vale <b>${fmtPA(paOf(d, threat, ENC.N, ENC.ref))} PA</b> para un grupo de ${ENC.N} parejas con nivel de referencia ${esc(REF_NAMES[ENC.ref])}${d.amenaza_nivel ? ` · índice de amenaza ${esc(d.amenaza_nivel)}` : ""}.</span><button type="button" class="pill" id="sb-add">Añadir al encuentro</button><span class="hint" id="sb-added"></span></div>
    <div class="sb-stats">
      <div><span>PV</span><b>${v.pv}</b></div>
      <div><span>Ataque</span><b>${sgn(v.atq)}</b></div>
      <div><span>Defensa</span><b>${sgn(v.def)}</b></div>
      <div><span>Armadura</span><b>${v.arm}</b></div>
      <div><span>Iniciativa</span><b>${sgn(v.ini)}</b></div>
      <div><span>Dado</span><b>${esc(d.dado)}</b></div>
      ${v.acciones > 1 ? `<div><span>Acciones</span><b>${v.acciones}</b></div>` : ""}
    </div>
    <dl class="sb-kv">
      <div><dt>Movimiento</dt><dd>${[d.vuela ? "Vuela" : "", d.nada ? "Nada" : ""].filter(Boolean).join(", ") || "Terrestre"}</dd></div>
      <div><dt>Elemento</dt><dd>${esc((L.ele[d.elemento_principal] || {}).nombre || d.elemento_principal || "—")}</dd></div>
      <div><dt>Débil a</dt><dd>${(d.debilidades || []).map(x => esc((L.ele[x] || {}).nombre || x)).join(", ") || "—"}</dd></div>
      <div><dt>Resiste</dt><dd>${(d.resistencias || []).map(x => esc((L.ele[x] || {}).nombre || x)).join(", ") || "—"}</dd></div>
      <div><dt>VF</dt><dd>${d.vf} <span class="sub">(valor fijo por dado)</span></dd></div>
      <div><dt>Amenaza sugerida</dt><dd>${esc(threatName(d.amenaza_sugerida))}</dd></div>
      ${d.especialidades && d.especialidades.length ? `<div class="wide"><dt>Fuera de combate</dt><dd>${esc(d.especialidades.join("; "))}</dd></div>` : ""}
    </dl>
    <h3>Técnicas</h3>
    <div class="tbl"><table class="sb-t"><thead><tr><th>Técnica</th><th>Pot.</th><th>Daño</th><th>Alcance</th><th>Elemento</th><th>Efectos</th></tr></thead>
      <tbody>${d.tecnicas.map(t => techRow(t, d, v.extra)).join("")}</tbody></table></div>
    ${usedKw.size ? `<details class="sb-gl"><summary>Qué hace cada efecto</summary><dl>${[...usedKw].map(c => { const e = L.efe[c]; return e ? `<div><dt>${esc(e.nombre)}</dt><dd>${esc(e.regla)}</dd></div>` : ""; }).join("")}</dl></details>` : ""}
    <h3>Rasgos</h3>
    <ul class="sb-traits">${(d.rasgos || []).map(r => `<li><b>${esc(r.nombre)}.</b> ${esc(r.regla)} <span class="sub">${esc(r.origen || "")}</span></li>`).join("") || "<li>—</li>"}</ul>
    ${v.reglas.length ? `<h3>Reglas de ${esc(threatName(threat))}</h3><ul class="sb-traits">${v.reglas.map(r => `<li>${esc(r)}</li>`).join("")}</ul>` : ""}
    ${d.tacticas ? `<h3>En combate</h3><p>${esc(d.tacticas)}</p>` : ""}
    ${d.gancho ? `<h3>Gancho de aventura</h3><p>${esc(d.gancho)}</p>` : ""}
    <h3>Línea evolutiva</h3>
    <dl class="sb-kv evo"><div><dt>Viene de</dt><dd>${evoLinks(d.prev)}</dd></div><div><dt>Evoluciona a</dt><dd>${evoLinks(d.next)}</dd></div>${d.modos && d.modos.length ? `<div><dt>Modos</dt><dd>${evoLinks(d.modos)}</dd></div>` : ""}</dl>
  </article>`;
}
function wireStatBlock(root, d) {
  const onClick = e => {
    const b = e.target.closest("button.th"); if (!b) return;
    root.removeEventListener("click", onClick);
    root.innerHTML = statBlock(d, b.dataset.t); wireStatBlock(root, d);
  };
  root.addEventListener("click", onClick);
  const add = $("#sb-add", root);
  if (add) add.addEventListener("click", () => {
    const t = $("button.th.on", root).dataset.t, v = applyThreat(d, t, ENC.N);
    ENC.list.push({ id: d.id, t, pv: v.pv, k: Date.now() % 1e9 + ENC.list.length }); saveEnc();
    $("#sb-added", root).innerHTML = `Añadido. <a href="#encuentro">Ver encuentro (${ENC.list.length})</a>`;
  });
  const n = $("#sb-n", root);
  if (n) n.addEventListener("change", () => { S.groupN = Math.max(1, Math.min(8, +n.value || 4)); const t = $("button.th.on", root).dataset.t; root.removeEventListener("click", onClick); root.innerHTML = statBlock(d, t); wireStatBlock(root, d); });
}

/* ---------- constructor de encuentros ---------- */
const REF_NAMES = { 0: "Bebé", 1: "Novato", 2: "Campeón", 3: "Perfecto", 4: "Definitivo" };
function encounter() {
  S.view = "encuentro"; markNav("encuentro");
  const N = ENC.N, ref = ENC.ref;
  const rows = ENC.list.map((e, i) => ({ e, i, d: S.byId.get(e.id) })).filter(x => x.d);
  const total = rows.reduce((a, { e, d }) => a + paOf(d, e.t, N, ref), 0);
  const bands = [["Fácil", N / 2], ["Normal", N], ["Difícil", 1.5 * N], ["Épico", 2 * N]];
  let dif = "Mortal"; for (const [n, v] of bands) if (total <= v + 1e-9) { dif = n; break; }
  if (!rows.length) dif = "—";
  main.innerHTML = `<div class="enc">
    <div><p class="eyebrow">Herramienta del DJ</p><h1 class="bst-title">Constructor de encuentros</h1>
    <p class="bst-help">Añade Digimon desde el bestiario con el botón «Añadir al encuentro» o con el buscador de abajo. Los PA siguen la sección de presupuesto de la Guía del DJ: PA de la amenaza × diferencia de nivel × índice de amenaza.</p></div>
    <form class="filters" onsubmit="return false">
      <label><span>Parejas en el grupo</span><input id="enc-n" type="number" min="1" max="8" value="${N}"></label>
      <label><span>Nivel de referencia</span><select id="enc-ref">${[1, 2, 3, 4].map(r => `<option value="${r}"${r === ref ? " selected" : ""}>${REF_NAMES[r]}</option>`).join("")}</select></label>
      <label class="f-q"><span>Añadir Digimon</span><input id="enc-q" list="enc-dl" placeholder="Escribe un nombre y pulsa Intro" autocomplete="off"></label>
      <datalist id="enc-dl">${S.best.map(d => `<option value="${esc(d.nombre)} · ${esc(d.nivel)}"></option>`).join("")}</datalist>
      <button class="pill" id="enc-clear" type="button">Vaciar</button>
    </form>
    <div class="enc-sum">
      <div><span>PA totales</span><b>${fmtPA(total)}</b></div>
      <div><span>Dificultad</span><b class="dif-${norm(dif)}">${esc(dif)}</b></div>
      ${bands.map(([n, v]) => `<div><span>${n}</span><b>≤ ${fmtPA(v)}</b></div>`).join("")}
    </div>
    ${rows.length ? `<div class="tbl"><table class="sb-t enc-t"><thead><tr><th>Digimon</th><th>Plantilla</th><th>PV</th><th>Atq</th><th>Def</th><th>Arm</th><th>Ini</th><th>Acc.</th><th>PA</th><th></th></tr></thead><tbody>
      ${rows.map(({ e, i, d }) => { const v = applyThreat(d, e.t, N); return `<tr data-i="${i}">
        <td><a href="#d-${slug(d.id)}"><b>${esc(d.nombre)}</b></a><div class="sub">${esc(d.nivel)} · ${esc((S.lookup.atr[d.atributo] || {}).nombre || "")}</div></td>
        <td><select class="enc-t-sel">${THREATS.map(([k, t]) => `<option value="${k}"${k === e.t ? " selected" : ""}>${t}</option>`).join("")}</select></td>
        <td class="num"><input class="enc-pv" type="number" min="0" max="${v.pv}" value="${Math.min(e.pv ?? v.pv, v.pv)}"> / ${v.pv}</td>
        <td class="num">${sgn(v.atq)}</td><td class="num">${sgn(v.def)}</td><td class="num">${v.arm}</td><td class="num">${sgn(v.ini)}</td><td class="num">${v.acciones}</td>
        <td class="num">${fmtPA(paOf(d, e.t, N, ref))}</td>
        <td><button type="button" class="pill enc-del" aria-label="Quitar ${esc(d.nombre)}">Quitar</button></td></tr>`; }).join("")}
    </tbody></table></div>` : `<div class="sb-empty"><b>El encuentro está vacío</b><span>Busca un Digimon arriba o ábrelo en el bestiario y pulsa «Añadir al encuentro».</span></div>`}
  </div>`;
  $("#enc-n").addEventListener("change", e => { ENC.N = Math.max(1, Math.min(8, +e.target.value || 4)); saveEnc(); encounter(); });
  $("#enc-ref").addEventListener("change", e => { ENC.ref = +e.target.value; saveEnc(); encounter(); });
  $("#enc-clear").addEventListener("click", () => { ENC.list = []; saveEnc(); encounter(); });
  const q = $("#enc-q");
  const addQ = () => { const name = q.value.split(" · ")[0].trim(), lvl = q.value.split(" · ")[1]; const d = S.best.find(x => norm(x.nombre) === norm(name) && (!lvl || x.nivel === lvl.trim())); if (!d) return; ENC.list.push({ id: d.id, t: d.amenaza_sugerida || "estandar", pv: null }); saveEnc(); encounter(); $("#enc-q").focus(); };
  q.addEventListener("change", addQ);
  $$(".enc-t tr[data-i]").forEach(tr => {
    const i = +tr.dataset.i;
    $(".enc-t-sel", tr).addEventListener("change", ev => { ENC.list[i].t = ev.target.value; ENC.list[i].pv = null; saveEnc(); encounter(); });
    $(".enc-pv", tr).addEventListener("change", ev => { ENC.list[i].pv = Math.max(0, +ev.target.value || 0); saveEnc(); });
    $(".enc-del", tr).addEventListener("click", () => { ENC.list.splice(i, 1); saveEnc(); encounter(); });
  });
  window.scrollTo(0, 0);
}

/* ---------- ficha editable ---------- */
const TRASFONDOS = {
  "Deportista": ["atletismo", "tactica", "Balón o raqueta", "Fondo físico: +2 Aguante."],
  "Cerebrito": ["saber", "observacion", "Portátil", "Lo leí en algún sitio: 1 vez por sesión, pregunta al DJ un dato útil."],
  "Manitas": ["tecnologia", "observacion", "Caja de herramientas", "Ingenio: +1 Carga máxima."],
  "Hermano/a mayor": ["empatia", "medicina", "Botiquín", "Protector: +1 para proteger a alguien más débil o más joven."],
  "Explorador/a": ["supervivencia", "atletismo", "Cuerda y brújula", "Siempre preparado: 1 vez por sesión, saca un objeto común razonable."],
  "Artista": ["arte", "persuasion", "Instrumento o utensilios de cocina", "Inspiración: en un descanso corto, los compañeros recuperan VF PV extra."],
  "Pícaro/a": ["sigilo", "engano", "Tirachinas o ganzúas", "Huidizo: +1 a las tiradas de Defensa de tu Tamer."],
  "Líder nato": ["persuasion", "tactica", "Silbato", "Al mando: tu Orden puede darse a cualquier compañero del grupo."],
  "Chico/a de campo": ["supervivencia", "empatia", "Navaja multiusos", "Mano con los animales: los Digimon salvajes empiezan un paso más amistosos."],
  "Gamer": ["saber", "tecnologia", "Consola portátil", "Me sé este jefe: +1 a Analizar; 1 vez por combate repite una tirada de Analizar."],
};
const HABILIDADES = [["atletismo", "Atletismo"], ["sigilo", "Sigilo"], ["tecnologia", "Tecnología"], ["saber", "Saber Digital"], ["observacion", "Observación"], ["supervivencia", "Supervivencia"], ["medicina", "Medicina"], ["persuasion", "Persuasión"], ["engano", "Engaño"], ["empatia", "Empatía"], ["tactica", "Táctica"], ["arte", "Arte"]];
const SENDAS = { "Estratega": "¡Flanqueo!: tu compañero y un aliado que ataquen al mismo enemigo este asalto tienen +1 contra él.", "Técnico": "Memoria ampliada: +2 Carga máxima y 1 programa de Nivel 1 más.", "Protector": "Vínculo protector: +1 Aguante; en la misma zona, tu compañero tiene +1 Def contra técnicas de área.", "Batidor": "Ojo para el terreno: al empezar cada combate, da Cobertura o Altura a una zona, o quita Terreno difícil.", "Inspirador": "Llama del vínculo: al empezar cada combate, si tienes menos Chispa que tu Vínculo, sube hasta tu Vínculo." };
const DIGIVICES = { "Digivice clásico": 1, "D-3": 1, "D-Arc / D-Power": 1, "D-Tector": 1, "Digivice iC / Burst": 0, "Xros Loader": 0, "Digivice de campaña": 1 };
const EMBLEMAS = ["Valor", "Amistad", "Amor", "Sabiduría", "Pureza", "Sinceridad", "Fiabilidad", "Esperanza", "Luz", "Bondad", "Milagros", "Destino"];
const VINCULO = { 1: ["Novato", "Campeón"], 2: ["Novato", "Perfecto"], 3: ["Campeón", "Perfecto"], 4: ["Campeón", "Definitivo"], 5: ["Perfecto", "Definitivo"], 6: ["Definitivo", "Modo Supremo"] };
const PERSONALIDAD = ["Glotón", "Valiente e impulsivo", "Miedoso", "Orgulloso", "Curioso", "Gruñón", "Leal hasta el extremo", "Bromista", "Serio y responsable", "Cariñoso y pegajoso", "Perezoso", "Tímido"];

function blankChar() {
  return { id: "pj" + Math.random().toString(36).slice(2, 8), ejemplo: false,
    t: { nombre: "", edad: "", aspecto: "", falta: "", val: 0, ast: 0, cor: 0, des: 0, trasfondo: "", hab: {}, senda: "", talentos: "", virtud: "", defecto: "", emblema: "", digivice: "Digivice clásico", nivel: 1, xp: 0, vinculo: 1, chispa: 1, aguante: null, carga: null, bits: 100, programas: "", equipo: "Disco de recuperación S\nCarne digital ×2", notas: "" },
    d: { apodo: "", novato: "", bebe: "", campeon: "", perfecto: "", definitivo: "", forma: "", rolfijo: "", personalidad: "", m_atq: 0, m_def: 0, m_pv: 0, m_ini: 0, tecnicas: "", pv: null, estados: "" } };
}
function exampleChar() {
  const c = blankChar();
  c.ejemplo = true; c.id = "ejemplo";
  Object.assign(c.t, { nombre: "Nora Vidal (ejemplo)", edad: "12", aspecto: "Gafas de bucear en la frente, mochila llena de pegatinas", falta: "Alguien que confíe en ella", val: 2, ast: 1, cor: 1, des: 0, trasfondo: "Deportista", hab: { atletismo: 1, tactica: 1, observacion: 1, persuasion: 1 }, senda: "Protector", virtud: "Valiente", defecto: "Impulsivo/a", emblema: "Valor", digivice: "Digivice clásico", programas: "Carga de poder\nEscudo\nDetección", notas: "Ficha de ejemplo: cámbiala o crea una nueva con «Nueva ficha»." });
  Object.assign(c.d, { apodo: "Agu", novato: "agumon", bebe: "Koromon", campeon: "greymon-first", forma: "agumon", personalidad: "Glotón" });
  return c;
}
let chars = store.get("lazos-fichas", null);
if (!Array.isArray(chars) || !chars.length) chars = [exampleChar()];
let curId = store.get("lazos-ficha-actual", chars[0].id);
const save = () => { store.set("lazos-fichas", chars); store.set("lazos-ficha-actual", curId); };

function formStats(c, id) {
  const d = S.byId.get(id); if (!d) return null;
  const L = S.lookup;
  let atq = d.atq, def = d.def, ini = d.ini, pv = d.pv, arm = d.arm;
  const fix = c.d.rolfijo && L.rol[c.d.rolfijo];
  if (fix && d.rol && L.rol[d.rol] && d.rol !== c.d.rolfijo) {
    const o = L.rol[d.rol].mods, n = fix.mods;
    atq += n.atq - o.atq; def += n.def - o.def; ini += n.ini - o.ini; pv += d.vf * (n.pv_mult - o.pv_mult); arm = Math.max(0, Math.min(2, arm + n.arm - o.arm));
  }
  atq += +c.d.m_atq || 0; def += +c.d.m_def || 0; ini += +c.d.m_ini || 0; pv += +c.d.m_pv || 0;
  return { d, atq, def, ini, pv, arm, rol: fix || L.rol[d.rol] };
}
function derived(c) {
  const t = c.t, tf = TRASFONDOS[t.trasfondo];
  const aguante = Math.max(4, 6 + (+t.val || 0) + (t.trasfondo === "Deportista" ? 2 : 0) + (t.senda === "Protector" ? 1 : 0));
  const carga = 3 + (+t.ast || 0) + (DIGIVICES[t.digivice] || 0) + (t.trasfondo === "Manitas" ? 1 : 0) + (t.senda === "Técnico" ? 2 : 0);
  const v = +t.vinculo || 1;
  return { aguante, carga, chispaMax: 3 + v, estable: VINCULO[v][0], maximo: VINCULO[v][1], tf };
}
function digiOptions(level, cur) {
  const list = S.best.filter(d => d.nivel === level).sort((a, b) => a.nombre.localeCompare(b.nombre));
  return `<option value="">—</option>` + list.map(d => `<option value="${esc(d.id)}"${d.id === cur ? " selected" : ""}>${esc(d.nombre)}${d.atributo ? " · " + esc((S.lookup.atr[d.atributo] || {}).nombre || "") : ""}</option>`).join("");
}
function sheet() {
  S.view = "ficha"; markNav("ficha");
  let c = chars.find(x => x.id === curId) || chars[0]; curId = c.id;
  const t = c.t, dg = c.d, D = derived(c);
  const forms = [["novato", "Novato"], ["campeon", "Campeón"], ["perfecto", "Perfecto"], ["definitivo", "Definitivo"]].filter(([k]) => dg[k]);
  const formaId = dg.forma || dg.novato;
  const fs = formaId ? formStats(c, formaId) : null;
  const hab = HABILIDADES.map(([k, n]) => { const v = +(t.hab[k] || 0); return `<label class="hab"><span>${n}</span><select data-k="t.hab.${k}"><option value="0"${v === 0 ? " selected" : ""}>0</option><option value="1"${v === 1 ? " selected" : ""}>+1</option><option value="2"${v === 2 ? " selected" : ""}>+2</option></select></label>`; }).join("");
  const sel = (k, list, cur, blank = "—") => `<select data-k="${k}"><option value="">${blank}</option>${list.map(x => `<option${x === cur ? " selected" : ""}>${esc(x)}</option>`).join("")}</select>`;
  const num = (k, v, min, max) => `<input type="number" data-k="${k}" value="${esc(v)}" min="${min}" max="${max}">`;
  const txt = (k, v, ph = "") => `<input type="text" data-k="${k}" value="${esc(v)}" placeholder="${esc(ph)}">`;
  const area = (k, v, rows = 3, ph = "") => `<textarea data-k="${k}" rows="${rows}" placeholder="${esc(ph)}">${esc(v)}</textarea>`;
  main.innerHTML = `<div class="sheet">
    <div class="sh-bar">
      <label><span class="sr">Ficha</span><select id="sh-pick">${chars.map(x => `<option value="${esc(x.id)}"${x.id === c.id ? " selected" : ""}>${esc(x.t.nombre || "Sin nombre")}${x.d.apodo ? " & " + esc(x.d.apodo) : ""}</option>`).join("")}</select></label>
      <button class="pill" id="sh-new" type="button">Nueva ficha</button>
      <button class="pill" id="sh-dup" type="button">Duplicar</button>
      <button class="pill" id="sh-del" type="button">Borrar</button>
      <button class="pill" id="sh-exp" type="button">Exportar</button>
      <button class="pill" id="sh-imp" type="button">Importar</button>
      <span class="sh-saved" id="sh-saved">Se guarda sola en este navegador</span>
    </div>
    <div class="sh-io" id="sh-io" hidden></div>
    ${c.ejemplo ? `<p class="notice">Esta es una ficha de ejemplo. Puedes modificarla o pulsar «Nueva ficha» para empezar la tuya.</p>` : ""}
    <div class="sh-grid">
      <section class="sh-card">
        <h2>Tamer</h2>
        <div class="g2">
          <label>Nombre ${txt("t.nombre", t.nombre)}</label>
          <label>Edad ${txt("t.edad", t.edad)}</label>
        </div>
        <label>Aspecto ${txt("t.aspecto", t.aspecto)}</label>
        <label>¿Qué te falta en tu vida? ${txt("t.falta", t.falta, "La semilla de tu Emblema")}</label>
        <h3>Atributos <span class="hint">reparte +2, +1, +1 y 0</span></h3>
        <div class="g4">
          <label class="big">Valor ${num("t.val", t.val, -1, 3)}</label>
          <label class="big">Astucia ${num("t.ast", t.ast, -1, 3)}</label>
          <label class="big">Corazón ${num("t.cor", t.cor, -1, 3)}</label>
          <label class="big">Destreza ${num("t.des", t.des, -1, 3)}</label>
        </div>
        <div class="g2">
          <label>Trasfondo ${sel("t.trasfondo", Object.keys(TRASFONDOS), t.trasfondo)}</label>
          <label>Senda ${sel("t.senda", Object.keys(SENDAS), t.senda)}</label>
        </div>
        ${D.tf ? `<p class="hint">Trasfondo: entrena ${esc(HABILIDADES.find(h => h[0] === D.tf[0])[1])} y ${esc(HABILIDADES.find(h => h[0] === D.tf[1])[1])}. Objeto: ${esc(D.tf[2])}. ${esc(D.tf[3])}</p>` : ""}
        ${t.senda ? `<p class="hint">Talento inicial: ${esc(SENDAS[t.senda])}</p>` : ""}
        <h3>Habilidades <span class="hint">0 sin entrenar · +1 entrenada · +2 experta</span></h3>
        <div class="habs">${hab}</div>
        <div class="g2">
          <label>Cualidad ${txt("t.virtud", t.virtud)}</label>
          <label>Defecto ${txt("t.defecto", t.defecto)}</label>
          <label>Emblema ${sel("t.emblema", EMBLEMAS, t.emblema)}</label>
          <label>Digivice ${sel("t.digivice", Object.keys(DIGIVICES), t.digivice)}</label>
        </div>
        <label>Talentos ${area("t.talentos", t.talentos, 2)}</label>
      </section>

      <section class="sh-card">
        <h2>Recursos</h2>
        <div class="res">
          <div><span>Nivel</span>${num("t.nivel", t.nivel, 1, 10)}</div>
          <div><span>XP</span>${num("t.xp", t.xp, 0, 999)}</div>
          <div><span>Vínculo</span><select data-k="t.vinculo">${[1, 2, 3, 4, 5, 6].map(v => `<option value="${v}"${+t.vinculo === v ? " selected" : ""}>${v === 6 ? "★" : v}</option>`).join("")}</select></div>
          <div><span>Chispa <small>máx. ${D.chispaMax}</small></span>${num("t.chispa", t.chispa, 0, D.chispaMax)}</div>
          <div><span>Aguante <small>máx. ${D.aguante}</small></span>${num("t.aguante", t.aguante ?? D.aguante, 0, D.aguante)}</div>
          <div><span>Carga <small>máx. ${D.carga}</small></span>${num("t.carga", t.carga ?? D.carga, 0, D.carga)}</div>
          <div><span>Bits</span>${num("t.bits", t.bits, 0, 99999)}</div>
        </div>
        <p class="hint">Con Vínculo ${+t.vinculo === 6 ? "★" : t.vinculo}: nivel estable <b>${D.estable}</b>, máximo temporal <b>${D.maximo}</b>. Digievolucionar cuesta 2 Chispa por cada nivel por encima del estable.</p>
        <label>Programas ${area("t.programas", t.programas, 4, "Uno por línea")}</label>
        <label>Equipo y objetos ${area("t.equipo", t.equipo, 4, "Uno por línea")}</label>
        <label>Notas ${area("t.notas", t.notas, 3)}</label>
      </section>

      <section class="sh-card wide">
        <h2>Compañero Digimon</h2>
        <div class="g3">
          <label>Apodo ${txt("d.apodo", dg.apodo)}</label>
          <label>Personalidad ${sel("d.personalidad", PERSONALIDAD, dg.personalidad)}</label>
          <label>Rol fijado ${`<select data-k="d.rolfijo"><option value="">El del bestiario</option>${S.R.roles.map(r => `<option value="${r.id}"${r.id === dg.rolfijo ? " selected" : ""}>${esc(r.nombre)}</option>`).join("")}</select>`}</label>
        </div>
        <div class="g4">
          <label>Novato ${`<select data-k="d.novato">${digiOptions("Novato", dg.novato)}</select>`}</label>
          <label>Campeón ${`<select data-k="d.campeon">${digiOptions("Campeón", dg.campeon)}</select>`}</label>
          <label>Perfecto ${`<select data-k="d.perfecto">${digiOptions("Perfecto", dg.perfecto)}</select>`}</label>
          <label>Definitivo ${`<select data-k="d.definitivo">${digiOptions("Definitivo", dg.definitivo)}</select>`}</label>
        </div>
        <div class="g3">
          <label>Forma Bebé II ${txt("d.bebe", dg.bebe, "De su lista «Viene de»")}</label>
          <label>Mejoras: Atq / Def ${`<span class="g2 tight">${num("d.m_atq", dg.m_atq, 0, 5)}${num("d.m_def", dg.m_def, 0, 5)}</span>`}</label>
          <label>Mejoras: PV / Ini ${`<span class="g2 tight">${num("d.m_pv", dg.m_pv, 0, 99)}${num("d.m_ini", dg.m_ini, 0, 5)}</span>`}</label>
        </div>
        ${forms.length ? `<div class="forms" role="tablist" aria-label="Forma actual">${forms.map(([k, n]) => { const fd = S.byId.get(dg[k]); return `<button type="button" class="pill${dg[k] === formaId ? " on" : ""}" data-forma="${esc(dg[k])}" aria-selected="${dg[k] === formaId}">${esc(n)}: ${esc(fd ? fd.nombre : "?")}</button>`; }).join("")}</div>` : `<p class="hint">Elige el Novato de tu compañero para ver sus cifras.</p>`}
        ${fs ? `<div class="sh-form">
          <div class="sb-stats">
            <div><span>PV máx.</span><b>${fs.pv}</b></div><div><span>Ataque</span><b>${sgn(fs.atq)}</b></div><div><span>Defensa</span><b>${sgn(fs.def)}</b></div>
            <div><span>Armadura</span><b>${fs.arm}</b></div><div><span>Iniciativa</span><b>${sgn(fs.ini)}</b></div><div><span>Dado</span><b>${esc(fs.d.dado)}</b></div>
          </div>
          <div class="g2">
            <label>PV actuales ${num("d.pv", dg.pv ?? fs.pv, 0, fs.pv)}</label>
            <label>Estados ${txt("d.estados", dg.estados, "Hambriento, Agotado…")}</label>
          </div>
          <p class="hint">${esc(fs.d.nombre)} · ${esc(fs.d.nivel)} · ${esc(fs.rol ? fs.rol.nombre : "sin rol")} · ${esc((S.lookup.fam[fs.d.familia] || {}).nombre || "")} · <a href="#d-${slug(fs.d.id)}">abrir en el bestiario</a></p>
          <div class="tbl"><table class="sb-t"><thead><tr><th>Técnica</th><th>Pot.</th><th>Daño</th><th>Alcance</th><th>Elemento</th><th>Efectos</th></tr></thead><tbody>${fs.d.tecnicas.map(x => techRow(x, fs.d, 0)).join("")}</tbody></table></div>
        </div>` : ""}
        <label>Técnicas heredadas o aprendidas ${area("d.tecnicas", dg.tecnicas, 2)}</label>
      </section>
    </div>
  </div>`;
  wireSheet(c);
  window.scrollTo(0, 0);
}
function setPath(obj, path, val) { const ks = path.split("."); let o = obj; while (ks.length > 1) { const k = ks.shift(); o = o[k] = o[k] || {}; } o[ks[0]] = val; }
function wireSheet(c) {
  const root = $(".sheet");
  const NUM = /^(t\.(val|ast|cor|des|nivel|xp|vinculo|chispa|aguante|carga|bits)|t\.hab\..+|d\.(m_atq|m_def|m_pv|m_ini|pv))$/;
  const RERENDER = /^(t\.(val|ast|trasfondo|senda|digivice|vinculo)|d\.(novato|campeon|perfecto|definitivo|rolfijo|m_atq|m_def|m_pv|m_ini))$/;
  root.addEventListener("change", e => {
    const k = e.target.dataset.k; if (!k) return;
    let v = e.target.value; if (NUM.test(k)) v = v === "" ? 0 : +v;
    setPath(c, k, v);
    if (k === "t.trasfondo" && TRASFONDOS[v]) { c.t.hab[TRASFONDOS[v][0]] = Math.max(1, +(c.t.hab[TRASFONDOS[v][0]] || 0)); c.t.hab[TRASFONDOS[v][1]] = Math.max(1, +(c.t.hab[TRASFONDOS[v][1]] || 0)); }
    if (k === "d.novato") { c.d.forma = v; const nd = S.byId.get(v); if (nd && nd.prev && nd.prev.length && !c.d.bebe) c.d.bebe = nd.prev[0]; c.d.pv = null; }
    if (/^d\.(campeon|perfecto|definitivo)$/.test(k) && !v && c.d.forma === c.d[k]) c.d.forma = c.d.novato;
    c.ejemplo = false; save(); flash();
    if (RERENDER.test(k)) sheet();
  });
  root.addEventListener("input", e => { const k = e.target.dataset.k; if (!k || e.target.tagName === "SELECT") return; let v = e.target.value; if (NUM.test(k)) return; setPath(c, k, v); save(); flash(); });
  $$(".forms button", root).forEach(b => b.addEventListener("click", () => { c.d.forma = b.dataset.forma; c.d.pv = null; save(); sheet(); }));
  $("#sh-pick").addEventListener("change", e => { curId = e.target.value; save(); sheet(); });
  $("#sh-new").addEventListener("click", () => { const n = blankChar(); chars.push(n); curId = n.id; save(); sheet(); });
  $("#sh-dup").addEventListener("click", () => { const n = JSON.parse(JSON.stringify(c)); n.id = "pj" + Math.random().toString(36).slice(2, 8); n.ejemplo = false; n.t.nombre = (n.t.nombre || "Sin nombre") + " (copia)"; chars.push(n); curId = n.id; save(); sheet(); });
  const io = $("#sh-io");
  $("#sh-del").addEventListener("click", () => {
    io.hidden = false;
    io.innerHTML = `<p>¿Borrar la ficha de <b>${esc(c.t.nombre || "Sin nombre")}</b>? No se puede deshacer.</p><div class="row-b"><button class="pill danger" id="io-yes" type="button">Sí, borrar</button><button class="pill" id="io-no" type="button">Cancelar</button></div>`;
    $("#io-no").onclick = () => { io.hidden = true; };
    $("#io-yes").onclick = () => { chars = chars.filter(x => x.id !== c.id); if (!chars.length) chars = [blankChar()]; curId = chars[0].id; save(); sheet(); };
  });
  $("#sh-exp").addEventListener("click", () => {
    const json = JSON.stringify(c, null, 1);
    io.hidden = false;
    io.innerHTML = `<p>Copia este texto y guárdalo donde quieras. Para recuperar la ficha, pégalo en «Importar».</p><textarea id="io-txt" rows="8" readonly>${esc(json)}</textarea><div class="row-b"><button class="pill" id="io-copy" type="button">Copiar</button><button class="pill" id="io-no" type="button">Cerrar</button><span id="io-msg" class="hint"></span></div>`;
    $("#io-no").onclick = () => { io.hidden = true; };
    $("#io-copy").onclick = () => { const ta = $("#io-txt"); navigator.clipboard.writeText(json).then(() => { $("#io-msg").textContent = "Copiado"; }, () => { ta.select(); $("#io-msg").textContent = "Selecciona el texto y cópialo"; }); };
  });
  $("#sh-imp").addEventListener("click", () => {
    io.hidden = false;
    io.innerHTML = `<p>Pega aquí el texto de una ficha exportada, o elige un archivo .json.</p><textarea id="io-txt" rows="8"></textarea><div class="row-b"><input type="file" id="io-file" accept=".json,application/json"><button class="pill" id="io-ok" type="button">Importar</button><button class="pill" id="io-no" type="button">Cancelar</button><span id="io-msg" class="hint"></span></div>`;
    $("#io-no").onclick = () => { io.hidden = true; };
    $("#io-file").onchange = e => { const f = e.target.files[0]; if (!f) return; const r = new FileReader(); r.onload = () => { $("#io-txt").value = r.result; }; r.readAsText(f); };
    $("#io-ok").onclick = () => {
      try {
        const n = JSON.parse($("#io-txt").value);
        if (!n || !n.t || !n.d) throw new Error("x");
        const b = blankChar(); n.t = Object.assign(b.t, n.t); n.d = Object.assign(b.d, n.d); n.id = "pj" + Math.random().toString(36).slice(2, 8); n.ejemplo = false;
        chars.push(n); curId = n.id; save(); sheet();
      } catch (e) { $("#io-msg").textContent = "Ese texto no es una ficha válida. Copia el texto completo que dio «Exportar»."; }
    };
  });
}
let flashT = 0;
function flash() { const s = $("#sh-saved"); if (!s) return; s.textContent = "Guardado"; clearTimeout(flashT); flashT = setTimeout(() => { s.textContent = "Se guarda sola en este navegador"; }, 1200); }

boot();
})();
