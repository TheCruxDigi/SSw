# Guía de redacción: edición d20 (habilidades especiales y Firmas)

Para cada Digimon del lote escribes tres cosas:
1. **habilidades**: entre 1 y 3 habilidades especiales **del catálogo** (`/home/user/SSw/digimon-rpg/d20/habilidades.json`), con un `detalle` propio.
2. **sello**: el Sello de su Firma, reescrito en reglas d20.
3. **desatado**: el Desatado de su Firma, reescrito en reglas d20. En Bebé I y Bebé II, `null`.

Formato de salida: un JSON `{ id: {"habilidades": [{"id": "...", "detalle": "..."}], "sello": "...", "desatado": "..." } }`.

## 1. Habilidades especiales
- La entrada indica `habilidades_auto`, que el generador ya asigna por familia y tipo (vuelo, visión en la oscuridad, cuerpo artificial…). **No las repitas.**
- Añade de 1 a 3 habilidades **que tengan sentido** para ese Digimon según su franquicia, su diseño y su descripción. Ejemplos:
  - un fantasma (Phantomon, Bakemon): `posesion` o `invisibilidad`;
  - un Digimon psíquico o divino: `telepatia`;
  - un Definitivo que borra datos (Alphamon, Omnimon, Craniamon…): `borrado`;
  - un dragón enorme: `gigante` y `presencia_terrible`;
  - un Digimon con montura (Garurumon, Birdramon…): `monta`;
  - un lagarto de cuevas: `vision_oscuridad`;
  - un murciélago: `vision_ciega`;
  - un topo: `excavar`;
  - un fénix: `renacer`;
  - un hacker: `hackeo`;
  - un mago: `ilusiones`;
  - un camaleón: `camuflaje`;
  - una sirena o un bardo: `musica`;
  - un ángel sanador: `sanador`;
  - un señor oscuro: `aura_oscura`;
  - un virus devorador: `absorber_datos` o `corrupcion`.
- **Escala con el nivel.** Por número:
  - Bebés: 0–1.
  - Novatos: 1.
  - Campeones: 1–2.
  - Perfectos: 2.
  - Definitivos: 2–3.

  Las habilidades potentes (`posesion`, `borrado`, `manipular_tiempo`, `portal`, `vision_verdadera`, `control_mental`, `invocar_aliados`, `regeneracion`, `renacer`, `presencia_terrible`, `gigante`) son solo para Perfectos y Definitivos, salvo una justificación muy clara de la franquicia.
- El `detalle` (máx. 18 palabras) explica **cómo lo hace este Digimon**. Por ejemplo, «Sus alas de murciélago captan el eco de cada movimiento», o «Absorbe los datos de los vencidos con la boca de su pecho». Si cambia un dato de la regla (el elemento del terreno de `dominio_elemental`, el clima de `control_clima`…), dilo aquí.
- **No inventes ids:** usa solo los del catálogo.

## 2. Sello y Desatado en d20
Partes del efecto de Firma de 2d6 (`efecto_2d6`) y lo **traduces al motor d20**, conservando la idea y el sabor. El nombre y el Eco no cambian. Tienes la Firma d20 ya calculada en `firma_d20`: daño, ataque o salvación, y efectos.

**Traducciones habituales:**
| 2d6 | d20 |
|---|---|
| «Con 10+» | «Si el objetivo falla la salvación por 5 o más» (área), o «si la tirada de ataque supera la CA del objetivo por 5 o más» (ataque). |
| «+1 dado» | +1 dado (de su dado de poder). |
| «+1 a la tirada» | +2 al ataque, o −2 a la salvación del objetivo. |
| «Escudo VF» | PG temporales iguales a su BC × 2. |
| «Escudo 2 × VF» | PG temporales iguales a su BC × 4. |
| «zona» (lugar) | Un radio, o el área de la técnica. |
| «1 zona» de movimiento | 3 m; «2 zonas», 6 m. |
| «hasta el final del siguiente asalto» | Hasta el principio de su siguiente turno, o 1 asalto. |
| «Expuesto» | Los ataques contra él tienen ventaja hasta el final de su siguiente turno. |
| «Potenciado» | Ventaja en su próximo ataque. |
| «Ventaja» (2d6) | Ventaja. |
| Estados | Usa los nombres d20 con su salvación: ardiendo (DES), congelado (CON), entumecido (CON), envenenado (CON), aturdido (CON), dormido (SAB), cegado (CON), confundido (SAB), asustado (SAB), hechizado (SAB), sellado (CAR), ralentizado (DES), apresado (FUE), debilitado (CON), roto (FUE), derribado (FUE), provocado (SAB) y marcado (sin salvación). |
| «Peligro: VF al entrar» | 1 dado de poder al entrar o empezar el turno allí. |
| «Ráfaga sin perder dados» | Puede afectar a un segundo objetivo a 3 m del primero con el mismo ataque, o las criaturas en un radio de 3 m hacen la salvación. Sin el cuarto de dados menos. |

**Presupuesto:**
- **Sello:** pequeño y condicionado, como en 2d6.
- **Desatado:** equivale a +2 dados o a un efecto mayor.
- **Límite:** el Sello y el Desatado no suman más de +2 dados en la misma tirada.
- **Control duro:** aturdido, dormido y regresión nunca se aplican sin salvación.
- **Prohibido:** acciones extra, matar al instante y efectos permanentes.

**Extensión:** el Sello y el Desatado, máximo 40 palabras cada uno. Reglas exactas: quién, cuándo y cuánto dura. Español de España.

**Ejemplo, Agumon · Pepper Breath:**
- *2d6:* Sello «Si el objetivo es de un nivel superior, +1 a la tirada»; Desatado «Ráfaga sin perder dados y la zona queda en Llamas…».
- *d20:*

```json
"agumon": {"habilidades":[{"id":"empatia_animal","detalle":"Se entiende con los Digimon reptiles y saurios pequeños a base de gruñidos y gestos."}],
"sello":"Si el objetivo es de un nivel superior al de Agumon, la técnica tiene +2 al ataque: cuanto más grande el rival, más fuerte sopla.",
"desatado":"La llamarada alcanza también a un segundo objetivo a 3 m del primero, sin perder dados, y deja un círculo de 3 m en llamas durante 1 asalto (1d6 de fuego a quien entre o empiece su turno en él)."}
```
