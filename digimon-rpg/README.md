# Digimon: Lazos de Código

Juego de rol de mesa en español, **no oficial y sin ánimo de lucro**, ambientado en el Mundo Digital de Digimon. Usa 2d6 con tres franjas de resultado (10+, 7–9, 6–). Cada jugador lleva una pareja de Tamer y compañero Digimon, y la digievolución se paga con Chispa y se estabiliza con el Vínculo.

Digimon y todos sus nombres, personajes y técnicas pertenecen a sus propietarios. Este proyecto no está afiliado ni respaldado por ellos. Las reglas, las descripciones y las aventuras son texto original.

## Qué hay aquí

| Carpeta o archivo | Contenido |
|---|---|
| `web/` | La web del manual: lector de capítulos, bestiario con buscador y plantillas de amenaza, constructor de encuentros y ficha de personaje editable. Un botón cambia entre la edición 2d6 y la d20. |
| `d20/` | Edición d20 (beta, basada en el SRD 5.1, CC-BY-4.0): biblia de reglas, catálogo de 63 habilidades especiales, generador de fichas d20 y troceado de capítulos. |
| `fuentes/d20/` | Habilidades especiales elegidas y Sello/Desatado en d20 de cada Digimon. |
| `fuentes/firmas/` | Efectos de Firma (nombre, Sello, Desatado y Eco) de los 1.316 Digimon con Firma. |
| `capitulos/` | Los 19 capítulos del manual en Markdown: fundamentos, personajes, reglas, guía del DJ, personajes pregenerados, 3 aventuras y referencia rápida. |
| `fuentes/biblia_reglas.md` | La biblia de reglas: la referencia técnica completa y la fuente de verdad del sistema. |
| `fuentes/cambios.md` | Cambios aplicados tras la verificación del sistema con simulaciones. |
| `fuentes/descripciones/` | Descripción, tácticas y gancho de aventura de los 1.317 Digimon. |
| `descargas/ficha-lazos-de-codigo.pdf` | Ficha de personaje en PDF rellenable (2 páginas). |
| `tools/spec_fichas.json` | Especificación programable de las fichas del bestiario. |
| `tools/gen.py` | Generador de las 1.317 fichas a partir de la especificación. |
| `tools/build_web.py` | Genera los datos de la web (bestiario y reglas) y copia los capítulos. |
| `tools/make_manifest.py` | Reúne los capítulos y la biblia (como apéndice) con su índice. |
| `tools/make_sheet_pdf.py` | Genera la ficha en PDF rellenable. |

## Cómo regenerar

Los datos de origen de los Digimon (nombre, nivel, tipo, atributo, técnicas oficiales y líneas evolutivas) vienen del conjunto de datos público del proyecto DigimonQL (`data/digimon.json`).

```sh
# 1. Índice de capítulos (con la biblia como apéndice) en un directorio temporal
python3 tools/make_manifest.py capitulos /tmp/caps fuentes/biblia_reglas.md capitulos/resumenes.json

# 2. Fichas del bestiario, reglas y capítulos de la web
python3 tools/build_web.py --spec tools/spec_fichas.json --all ruta/a/all.json --gen tools/gen.py \
  --out web --desc fuentes/descripciones --firmas fuentes/firmas --chapters /tmp/caps

# 3. Edición d20: fichas y capítulos
python3 d20/gen_d20.py web/data/bestiario.json d20/habilidades.json fuentes/d20 web/data/bestiario_d20.json
python3 d20/make_d20_chapters.py d20/biblia_d20.md d20/habilidades.json web/capitulos_d20

# 4. Ficha en PDF
python3 tools/make_sheet_pdf.py descargas/ficha-lazos-de-codigo.pdf
```

`all.json` es la lista de los 1.317 Digimon con los campos `id`, `name`, `level`, `type`, `attribute`, `moves`, `x_antibody`, `is_mode`, `modes`, `prev`, `next` y `background_EN_reference_only`. El perfil en inglés solo lo usa el clasificador de técnicas; nunca se copia ni se traduce.

Para probar la web en local, sírvela con cualquier servidor estático (por ejemplo `python3 -m http.server` dentro de `web/`), porque carga los capítulos y los datos con `fetch`.
