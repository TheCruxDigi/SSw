# Cómo usar el bestiario

El bestiario es la mitad del juego. En él viven los 1.317 Digimon de *Lazos de Código*: el compañero de cada jugador, el [[Goblimon]] que acecha en el camino, el Jefe que cierra la aventura y el Legendario que hace temblar el Mundo Digital. Todos usan el mismo formato de ficha: cuando aprendas a leer una, sabrás leerlas todas.

En este capítulo aprenderás a leer una ficha campo a campo, qué significan los roles, las familias y las plantillas de forma (X-Antibody, Modos, Armadura, Híbrido, Bebé…) y cómo aplicar las plantillas de amenaza. También verás cómo se generó el bestiario, con sus fórmulas a la vista, y cómo usarlas para crear tus propios Digimon.

## El bestiario de un vistazo

Cada ficha se **genera por fórmula** a partir de cinco datos: **nivel, rol, atributo, familia y técnicas oficiales**. Nadie ha retocado las cifras a mano: solo se corrigen a mano algunos roles y técnicas, como verás más adelante. Por eso todas las fichas son coherentes entre sí y encajan en el presupuesto de encuentros del capítulo 12. Hay 108 Bebés, 175 Novatos, 278 Campeones, 283 Perfectos, 371 Definitivos y 102 fichas de niveles especiales (Armadura, Híbrido e Indeterminado).

Dos ideas te ahorrarán muchos problemas:

- **Todas las fichas son Estándar.** Cuando sacas un Digimon como enemigo, tú decides si es un esbirro, una élite, un Jefe o un Legendario aplicando una **plantilla de amenaza**.
- **No cambies las cifras.** Si quieres un enemigo más duro o más débil, cambia su plantilla o elige otra ficha. Los números están calibrados con combates simulados.

> **Si es tu primera vez:** para tu primera sesión basta con la sección «Anatomía de una ficha». El resto está aquí para cuando quieras entender por qué una ficha tiene esos números o crear un Digimon propio.

## Anatomía de una ficha

Vamos a desmontar una ficha real: [[MetalGreymon (Vaccine)]], el Perfecto de la línea de [[Agumon]].

```
MetalGreymon (Vaccine) — Perfecto · Máquina (Cíborg) · Tirador · Vacuna
Rango 3 · PV 35 · Atq +4 · Def +3 · Arm 1 · Ini +3 · Dado d10 (VF 5) · Vuela
Debilidad: Eléctrico, Fuego · Resistencia: Veneno, Acero · Triángulo: vence a Virus
Especialidades: fuerza, cálculo, sensores, interfaz; puntería y vigilancia · Amenaza: media
Rasgos: Francotirador (rol); Blindaje (familia); Antivirus (atributo)
Técnicas:
· Disparo — P1 · Distancia · Individual · Acero  [1d10]
· Disparo certero — P1 · Larga · Individual · Acero · Certero
· Giga Destroyer — P3 (Agotadora) · Larga · Individual · Acero · Brutal, Certero  [3d10]
· Trident Arm — P2 · Toque · Individual · Acero · Perforante  [2d10]
· Giga Storm — P2 · Distancia · Zona · Acero · Brutal  [2d10; contra 2+: 1d10]
Evoluciona de: Growlmon, Leomon, Airdramon… · Evoluciona a: WarGreymon, ShineGreymon… · Modos: MetalGreymon: Alterous Mode
```

*(Las listas de evolución están recortadas; la ficha completa las trae enteras.)*

### Primera línea: quién es

**Nombre — Nivel · Familia (Tipo) · Rol · Atributo**, más sus **plantillas de forma** si las tiene y su **amenaza sugerida** si no es Estándar.

- **Nombre:** el oficial, en inglés. Algunos se repiten en los datos (hay seis [[Argomon]], por ejemplo): fíjate en el nivel para distinguirlos.
- **Nivel:** de Bebé I a Definitivo, más tres niveles especiales: Armadura, Híbrido e Indeterminado.
- **Familia (Tipo):** el tipo es el oficial y la familia, una de las 14 en que el juego agrupa los 140 tipos.
- **Rol:** su estilo de combate, uno de 8. Los Bebés no tienen.
- **Atributo:** su lugar en el triángulo Vacuna, Datos y Virus, o fuera de él.

### Segunda línea: las cifras

- **Rango (0–4):** el número que se compara siempre (Bebé 0, Novato 1, Campeón 2, Perfecto 3, Definitivo 4). Los niveles especiales usan el rango de la fila que toman prestada.
- **PV, Atq, Def:** sus puntos de vida, su Ataque y su Defensa. El DJ no tira para impactar. Un PJ ataca con 2d6 + su Atq − la Def del objetivo y se defiende con 2d6 + su Def − el Atq del atacante.
- **Arm:** resta daño a cada impacto. En el bestiario nunca pasa de 2.
- **Ini:** para la tirada de iniciativa.
- **Dado y VF:** el dado de poder del nivel (d4 a d12) y su **valor fijo**, la mitad de sus caras. El VF es el daño de cada dado con daño fijo y aparece en muchas reglas («recupera VF PV»).
- **Vuela / Nada:** solo aparecen si los tiene.

### Tercera y cuarta líneas: elementos, especialidades y amenaza

- **Debilidad y Resistencia**, como mucho dos de cada. Contra una debilidad, el atacante suma +1 dado; contra una resistencia, el daño se reduce a la mitad (salvo con Perforante). Es lo que un Tamer descubre con Analizar.
- **Triángulo:** el atributo al que vence.
- **Especialidades:** la de su familia y la de su rol. Fuera de combate, un Digimon tira **2d6 + rango**, con +1 si la tarea entra en una de ellas.
- **Amenaza:** su **índice de amenaza**, **baja (PA ×¾)**, **media** o **alta (PA ×1½)**, que multiplica sus puntos de amenaza en el presupuesto.

### Quinta línea: rasgos

Los rasgos de **rol**, **familia**, **atributo** y **plantillas**. Si un rasgo dice «(incluido)», ya está sumado en las cifras: el +1 Def de Antivirus ya está en el Def +3. Los demás son reglas que debes recordar en mesa: Francotirador da +1 contra objetivos fuera de su zona y Blindaje lo hace inmune a Dormir y Encantar.

### Las técnicas

Se leen así: **nombre — potencia · alcance · área · elemento · palabras clave [dados]**.

- **Técnica básica** (Disparo): su nombre y su elemento dependen de la familia. Siempre P1 y de Toque, salvo en la familia Arcano (a Distancia) y en los Tiradores, que la usan como **Disparo**, a Distancia: por eso MetalGreymon no tiene el Puño mecánico de las Máquinas.
- **Maniobra de rol** (Disparo certero): depende del rol. Los Bebés no tienen.
- **Firma** (Giga Destroyer): la técnica estrella, P3 y **Agotadora** (en su turno siguiente no puede usar ninguna técnica Agotadora, tampoco la misma). Si el Digimon solo tiene una técnica oficial, su Firma es **P2/P3**: P2 a voluntad o P3 Agotadora. Por eso [[Agumon]] imprime «2d6 / 3d6» en Pepper Breath.
- **Efecto de Firma**: bajo las técnicas, la Firma lleva su efecto propio, con nombre, **Sello** (siempre que se usa como Firma), **Desatado** (1 Chispa, 1 vez por combate; un Élite, Jefe o Legendario lo usa gratis 1 vez) y **Eco** (fuera de combate, 1 vez por escena). Las reglas están en el capítulo 8. Un Esbirro no usa ni el Sello ni el Desatado.
- **Las demás técnicas oficiales**, con su potencia.
- **Los dados entre corchetes** son contra un objetivo. En una técnica de área se añaden los dados **contra 2 o más objetivos**, uno menos: Giga Storm tira 2d10 contra uno y 1d10 contra cada uno si alcanza a varios.

### Línea evolutiva, notas y web

**Evoluciona de**, **Evoluciona a** y **Modos** enlazan con las fichas vecinas. Algunas fichas añaden **Notas**: 27 Novatos avisan de que no tienen Bebé II en los datos y te dicen qué hacer. En la web, cada ficha trae además una **descripción** original, consejos **En combate**, un **gancho de aventura** y un desplegable **«Qué hace cada efecto»** con las reglas de sus palabras clave.

## Los roles

El rol cambia las cifras y da un rasgo, una maniobra, una especialidad y, a veces, una **palabra de Firma** que la técnica estrella recibe si le queda hueco.

| Rol | En una frase | Modificadores | Rasgo | Maniobra | Palabra de Firma | Fichas |
|---|---|---|---|---|---|---|
| **Bruto** | Golpea fuerte y aguanta | Atq +1, PV +1 | Arrollador | Arremetida | Brutal | 298 |
| **Tanque** | La muralla del grupo | Def +1, PV +1, Arm +1, Ini −1 | Guardián | Desafío | Provocar | 110 |
| **Ágil** | Rápido y escurridizo | Def +1, PV −1, Ini +2 | Escurridizo | Golpe y fuga | Rápido | 159 |
| **Tirador** | Ataca desde lejos | Atq +1, Def −1, Ini +1 | Francotirador | Disparo certero | Certero | 118 |
| **Místico** | Domina los estados | PV −1 | Maestro de estados | Interferencia | — | 223 |
| **Apoyo** | Cura y protege | Atq −1 | Sanador | Pulso restaurador | — | 39 |
| **Acechador** | Remata a los débiles | Atq +1, PV −1, Ini +2 | Emboscada | Marca de caza | Perforante | 80 |
| **Versátil** | Equilibrado y fiable | Ini +1 | Adaptable | Cambio de guardia | — | 182 |

*«PV +1» es +1 al multiplicador de PV, es decir, +VF puntos de vida.*

Apoyo y Tanque escasean entre los Digimon salvajes. Por eso un jugador puede **fijar el rol** de su compañero (capítulo 5): todas sus formas usan los modificadores, el rasgo, la maniobra y la palabra de Firma de ese rol.

## Las familias y los atributos

La familia decide la **afinidad** (el elemento por defecto de sus técnicas), las **debilidades y resistencias base**, un **rasgo**, la **técnica básica**, la especialidad y qué roles le salen con más facilidad (el primero es su rol **primario**; el segundo, el **secundario**).

| Familia | Afinidad | Débil a | Resiste | Rasgo | Roles afines | Mods |
|---|---|---|---|---|---|---|
| **Dragón** | Fuego | Hielo | Fuego | Corazón de dragón | Bruto, Versátil | — |
| **Saurio** | Neutro | Hielo | Tierra | Piel gruesa | Bruto, Tanque | PV +1 |
| **Bestia** | Neutro | Fuego | Hielo | Manada | Ágil, Acechador | — |
| **Ave** | Viento | Eléctrico | Tierra | Vuelo | Ágil, Tirador | — |
| **Acuático** | Agua | Eléctrico | Fuego | Anfibio | Tanque, Tirador | — |
| **Naturaleza** | Planta | Fuego | Agua | Toxinas y raíces | Místico, Acechador | — |
| **Máquina** | Acero | Eléctrico | Veneno | Blindaje | Tanque, Tirador | Arm +1, Ini −1 |
| **Juguete** | Mental | Fuego | Mental | Relleno | Místico, Apoyo | — |
| **Sagrado** | Luz | Oscuridad | Luz | Aura sagrada | Místico, Apoyo | — |
| **Caballero** | Acero | Oscuridad | Acero | Honor | Versátil, Tanque | — |
| **Oscuro** | Oscuridad | Luz | Oscuridad | Hambre oscura | Acechador, Místico | — |
| **Arcano** | Mental | Acero | Mental | Hechicería | Místico, Apoyo | — |
| **Elemental** | Según su tipo | Según su tipo | Según su tipo | Cuerpo elemental | Bruto, Místico | — |
| **Anomalía** | Neutro | — | — | Adaptación | Versátil, Bruto | — |

*Los Caballeros de tipo Dark Knight invierten debilidad y resistencia: débiles a la Luz, resisten la Oscuridad.*

El **atributo** da un pequeño modificador (incluido) y te sitúa en el triángulo: +1 a las tiradas del PJ si su atributo vence al del rival, −1 si pierde.

| Atributo | Modificador | Rasgo | Triángulo |
|---|---|---|---|
| **Vacuna** | Def +1 | Antivirus | Vence a Virus |
| **Datos** | PV +1, Ini +1 | Procesamiento | Vence a Vacuna |
| **Virus** | Atq +1 | Agresión | Vence a Datos |
| **Libre** | PV +1 | Libre | Neutral |
| **Variable** | Ninguno fijo | Mutable: cada escena elige ser Vacuna, Datos o Virus | El que elija |
| **Desconocido** y **SIN DATOS** | Def +1 | Ilegible: Analizar contra él tiene −1 | Neutral |
| **Ninguno** (Bebés) | — | — | Neutral |

## Las plantillas de forma

Algunas fichas llevan una **plantilla de forma**: una marca de que ese Digimon es algo especial. No las confundas con las plantillas de amenaza: **las de forma ya están aplicadas en la ficha**. Solo tienes que recordar su rasgo.

| Plantilla | Se aplica a | Modificadores (incluidos) | Rasgo | Fichas |
|---|---|---|---|---|
| **X-Antibody** | Las variantes «(X Antibody)» | Atq +1, PV +1 | Anticuerpo X | 120 |
| **Modo Supremo** | Modos con marca suprema (*Burst Mode*, *Crimson Mode*, *GX*…) | Atq +1, Def +1, PV +1 | Poder desatado | 22 |
| **Modo Oscuro** | Modos con marca oscura (*Ruin Mode*, *Rage Mode*, *Falldown Mode*…) | Atq +1, Def +1, PV +1 | Descontrol | 16 |
| **Modo alterno** | El resto de Modos | — | Cambio de modo | 24 |
| **Fusión de Espíritus** | Híbridos de clase Fusión | Atq +1, Def +1 | Fusión de Espíritus | 6 |
| **Híbrido** | Nivel Híbrido | — | Espíritu legendario | 32 |
| **Armadura** | Nivel Armadura | — | Poder del Digi-Huevo | 67 |
| **Bebé** | Bebé I y Bebé II | — | Bebé | 108 |

**X-Antibody.** [[WarGreymon (X Antibody)]] tiene PV 48 y Atq +5; [[WarGreymon]], PV 42 y Atq +4. La variante X tiene además sus propias técnicas, así que su elemento y sus debilidades cambian. Su rasgo **Anticuerpo X** lo hace inmune a Sellar y a Ejecutar y, una vez por combate, le deja repetir una tirada de Defensa (si es PJ) u obligar a un PJ a repetir un 10+ contra él (si es PNJ).

**Modos.** El nombre decide la plantilla. [[ShineGreymon]] tiene PV 48, Atq +5 y Def +5; [[ShineGreymon: Burst Mode]] sube a PV 54, Atq +6 y Def +6, y su rasgo **Poder desatado** deja lista su Firma al entrar en el modo. [[ShineGreymon: Ruin Mode]] tiene las mismas cifras, pero su rasgo es **Descontrol**: +1 dado de daño en todas sus técnicas (no está impreso en los corchetes: súmalo al tirar) y −1 Def contra la Luz. Un compañero solo llega a un Modo Oscuro por digievolución oscura, y entonces lo controla el DJ. Los Modos alternos, como [[Imperialdramon: Dragon Mode]] e [[Imperialdramon: Fighter Mode]], comparten cifras y cambian de técnicas; pasar de uno a otro **gasta el movimiento** y conserva el daño recibido. Ojo: varios Híbridos figuran como «modo» en los datos, pero no usan estas plantillas.

**Armadura.** El nivel Armadura usa la **fila de Campeón**: [[Flamedramon]] tiene PV 36, Atq +3 y Def +2, como un Campeón de su familia, rol y atributo. Su rasgo **Poder del Digi-Huevo** le da resistencia al elemento de su Firma (incluida), funciona aunque la digievolución normal esté bloqueada y le impide digievolucionar desde esa forma. Los huevos dorados son la excepción: [[GoldVeedramon]] y el [[Rapidmon]] de nivel Armadura usan la fila de Perfecto, y [[Magnamon]], la de Definitivo.

**Híbridos.** Son la transformación de un Tamer con un Espíritu (capítulo 13). Su atributo es siempre **Variable** y cada clase usa una fila:

| Espíritu | Fila | Ejemplo | Cifras |
|---|---|---|---|
| Forma base | Novato | [[Flamemon]] | PV 21 · Atq +1 · Def +1 |
| Humano | Campeón | [[Agunimon]] | PV 32 · Atq +3 · Def +2 |
| Bestia | Perfecto | [[BurningGreymon]] | PV 35 · Atq +3 · Def +3 |
| Fusión | Perfecto + plantilla Fusión | [[Aldamon]] | PV 35 · Atq +4 · Def +4 |
| Unificado | Definitivo | [[EmperorGreymon]] | PV 42 · Atq +4 · Def +4 |

BurningGreymon y Aldamon son Perfectos, Versátiles y Variables: el +1 Atq y el +1 Def de Aldamon vienen de la plantilla Fusión.

**Bebé.** Bebé I tiene **6 PV** y Bebé II, **10**, siempre con d4 (VF 2) y Atq, Def, Arm e Ini a 0. No tienen rol, rasgo de familia, debilidades ni resistencias; su familia solo aporta la técnica básica y la afinidad. El rasgo **Bebé** les impide usar P3, les da +2 para esconderse o huir y hace que sus técnicas no apliquen control duro ni Ejecutar. En Bebé I todas sus técnicas son P1; en Bebé II, la primera es P2. Así, [[Botamon]] escupe Acid Bubbles a 1d4 y [[Koromon]] lanza Foam a 2d4 con Cegar.

**Indeterminado.** Es el nivel `Unknown` de los datos (no lo confundas con el atributo Desconocido). [[Calumon]] y [[Burpmon]] usan la fila de Novato y [[NEO]], la de Definitivo. Calumon y Burpmon no tienen técnicas oficiales, así que reciben la Firma genérica **Descarga de datos**: P2/P3 · Distancia · Individual, con la afinidad de su familia.

## Cómo aplicar las plantillas de amenaza

Las reglas completas de cada plantilla y la anatomía de un Jefe están en el capítulo 12. Este es el procedimiento:

1. **Elige la ficha** según la historia y el nivel de referencia del grupo.
2. **Mira su amenaza sugerida.** El bestiario sugiere Legendario en 126 fichas, Jefe en 27 y Esbirro en 20. Es solo una sugerencia, aunque la plantilla Legendario está pensada para los grandes poderes de esa lista.
3. **Elige la plantilla** según su papel: carne de cañón (Esbirro), rival de igual a igual (Estándar), veterano peligroso (Élite), clímax (Jefe) o fuerza de la naturaleza (Legendario).
4. **Ajusta las cifras** con la tabla que sigue a esta lista. **N** es el número de parejas Tamer-Digimon.
5. **Añade sus reglas:** daño fijo y Firma como P2 del Esbirro, reacción de la Élite, fases y Furia del Jefe, Dominio del Legendario.
6. **Calcula sus PA:** PA de la plantilla × factor por diferencia de rango con el nivel de referencia (−3 o menos ×⅛, −2 ×¼, −1 ×½, 0 ×1, +1 ×2, +2 ×5, +3 o más ×15) × modificador de su índice de amenaza.

Los ajustes de cada plantilla, en resumen:

| Plantilla | PV | Atq | Def | Arm | Ini | Acciones por asalto | PA | Además |
|---|---|---|---|---|---|---|---|---|
| **Esbirro** | PV ÷ 4, hacia arriba | −1 | −1 | +0 | +0 | 1 | ¼ | Firma como P2; daño fijo |
| **Estándar** | PV | +0 | +0 | +0 | +0 | 1 | 1 | — |
| **Élite** | PV × 1,5, hacia abajo | +1 | +1 | +0 | +1 | 1 | 2 | 1 reacción por asalto |
| **Jefe** | PV × (N + 2) ÷ 2, hacia abajo | +1 | +1 | +1 | +2 | N ÷ 2, hacia arriba | N | Anatomía de un Jefe |
| **Jefe con Refuerzo I** | PV × (N + 3) ÷ 2, hacia abajo | +1 | +1 | +1 | +2 | N ÷ 2, hacia arriba, + 1 | N, contando un nivel más | Anatomía de un Jefe |
| **Jefe con Refuerzo II** | PV × (N + 3) ÷ 2, hacia abajo | +1 | +1 | +1 | +2 | N | N, contando un nivel más | +1 dado en todas sus técnicas |
| **Legendario** | PV × (N + 3) ÷ 2, hacia abajo | +1 | +1 | +1 | +2 | N ÷ 2, hacia arriba | 2N | +1 dado, 3 fases y Dominio |

Así queda [[MetalGreymon (Vaccine)]] para **4 parejas** con nivel de referencia **Perfecto** (diferencia 0, índice medio):

| Plantilla | PV | Atq | Def | Arm | Ini | Acciones | Además | PA |
|---|---|---|---|---|---|---|---|---|
| Esbirro | 9 | +3 | +2 | 1 | +3 | 1 | Giga Destroyer como P2; daño fijo | ¼ |
| Estándar | 35 | +4 | +3 | 1 | +3 | 1 | — | 1 |
| Élite | 52 | +5 | +4 | 1 | +4 | 1 | 1 reacción por asalto | 2 |
| Jefe | 105 | +5 | +4 | 2 | +5 | 2 | Anatomía de un Jefe | 4 |
| Jefe con Refuerzo I | 122 | +5 | +4 | 2 | +5 | 3 | Cuenta un nivel más | 8 |

Los PV salen así: 35 ÷ 4 = 8,75, hacia arriba, 9; 35 × 1,5 = 52,5, hacia abajo, 52; 35 × (4 + 2) ÷ 2 = 105; 35 × (4 + 3) ÷ 2 = 122,5, hacia abajo, 122. El Refuerzo II (N acciones y +1 dado) es para los Jefes Definitivos de Vínculo 5, o de Vínculo 4 con el Definitivo desbloqueado.

> **Ejemplo:** el grupo de Lía tiene 4 parejas a Vínculo 3, así que el Jefe de la aventura es un Perfecto con Refuerzo I. La DJ elige a MetalGreymon (Vaccine), corrompido por una Aguja de Control: 122 PV, 3 acciones por asalto, umbral de fase en 61 PV y Guardia de carga 17. Para el presupuesto cuenta un nivel por encima: 4 × 2 × 1 = **8 PA**, justo **2N (Épico)**. Como esbirro, en cambio, usaría Giga Destroyer como P2 con daño fijo: 2 dados × VF 5 = 10, que se quedan en 5 si el PJ saca 7–9 al defenderse. Con 6–, Brutal suma un dado y cada dado vale VF + 1: 3 × 6 = 18 (antes de restar Arm).

Dos recordatorios. **Los compañeros nunca usan plantillas de amenaza**: un compañero que llega a [[Gallantmon]] usa su ficha base. Y las plantillas de forma y de amenaza **se suman**: un [[ShineGreymon: Ruin Mode]] como Jefe conserva su dado extra de Descontrol, y la Furia le añade otro.

## Cómo se genera el bestiario

Detrás de cada ficha hay una especificación exacta, `spec_fichas.json`, y un generador de referencia que crea las 1.317 fichas y comprueba todas las reglas de validación: si una falla, se detiene. No necesitas nada de esto para jugar, pero saber de dónde salen los números te ayuda a confiar en ellos y a crear Digimon nuevos.

El orden es siempre el mismo: fila de nivel, familia, técnicas (primera pasada), rol, técnicas (segunda pasada), plantillas de forma, estadísticas, elementos, rasgos, amenaza y, por último, correcciones manuales y validación.

### La tabla base por nivel

| Fila | Rango | Dado | VF | PV base | Atq, Def e Ini base | Potencia máx. | Umbral de Ejecutar | Peligro contra Tamers | Guardia de carga |
|---|---|---|---|---|---|---|---|---|---|
| Bebé I | 0 | d4 | 2 | 6 (fijo) | 0 | P1 | 4 | 1 | — |
| Bebé II | 0 | d4 | 2 | 10 (fijo) | 0 | P2 | 4 | 1 | — |
| Novato | 1 | d6 | 3 | 21 | +1 | P3 | 6 | 1 | 10 |
| Campeón | 2 | d8 | 4 | 28 | +2 | P3 | 8 | 2 | 14 |
| Perfecto | 3 | d10 | 5 | 35 | +3 | P3 | 10 | 3 | 17 |
| Definitivo | 4 | d12 | 6 | 42 | +4 | P3 | 12 | 4 | 21 |

El **umbral de Ejecutar** es 2 × VF. El **Peligro contra Tamers** es el Aguante que quita un ataque de ese nivel (+1 si es P3). La **Guardia de carga**, la mitad de los PV base, solo la usan los Jefes.

### Las fórmulas

```
Dado = d(4 + 2 × rango)                   (Bebés: d4)
VF   = caras del dado ÷ 2
PV   = VF × (7 + rol + familia + atributo + plantillas)   (Bebé I: 6; Bebé II: 10)
Atq  = rango + rol + atributo + plantillas
Def  = rango + rol + atributo + plantillas
Arm  = rol + familia + plantillas, como máximo 2          (Bebés: 0)
Ini  = rango + rol + atributo + familia + plantillas
Daño medio de una técnica = nº de dados × (caras + 1) ÷ 2
```

Como los PV se multiplican por el VF, un +1 al multiplicador vale +3 PV en un Novato y +6 en un Definitivo. Compruébalo con [[MetalGreymon (Vaccine)]]: PV = 5 × (7 + 0) = 35; Atq = 3 + 1 (Tirador) = +4; Def = 3 − 1 (Tirador) + 1 (Vacuna) = +3; Arm = 1 (Máquina); Ini = 3 + 1 (Tirador) − 1 (Máquina) = +3.

### Cómo se elige el rol

El generador reparte puntos y gana el rol con más:

- **+3** al rol primario de su familia y **+1** al secundario.
- **+4** si su tipo es una excepción de un rol (Cyborg → Tirador, Holy Knight → Versátil, Pixie → Apoyo, Dinosaur → Bruto…).
- **Evidencia de sus técnicas**, que cuenta doble en la Firma: una técnica de apoyo da +3 a Apoyo; un Toque detectado por una palabra, +1 a Bruto; una Distancia o Larga detectada por una palabra, +1 a Tirador; y cada palabra clave encontrada por raíz suma 1 a su rol afín (Dormir, Encantar, Confundir, Sellar, Regresión, Atrapar, Ralentizar, Debilitar, Asustar o Cegar a Místico; Invocar, Drenar, y Curar o Mejora en una técnica de daño, también a Místico; Perforante, Certero, Ejecutar u Ocultar a Acechador; Rápido a Ágil; Provocar, Contraataque o Escudo en una técnica de daño a Tanque; Brutal, Romper, Derribar o Aturdir a Bruto).
- **Extras:** +2 a Versátil si es Definitivo con técnicas de Toque y de Distancia; +4 a Apoyo si más de la mitad de sus técnicas son de apoyo; +1 a Bruto si es un Elemental de tipo Fire.

Los empates los gana el rol primario de la familia; después, el rol de la excepción de tipo, y si aún hay empate, un orden fijo (Bruto, Versátil, Tirador, Místico, Ágil, Acechador, Tanque, Apoyo). Los Híbridos solo reciben +3 a Versátil más la evidencia de sus técnicas, y 24 Digimon icónicos tienen el rol fijado a mano. MetalGreymon (Vaccine) empieza con Tanque 3 y Tirador 1 por ser Máquina, su tipo Cyborg suma +4 a Tirador y termina con Tirador 8, Bruto 4, Tanque 3 y Acechador 1.

### Cómo se leen las técnicas

Un **clasificador** convierte el nombre oficial en mecánica buscando **raíces en inglés**: *breath* o *cannon* indican Distancia; *punch* o *sword*, Toque; *burn*, Quemar; *storm* o *quake*, Zona. Si el nombre no basta, mira un fragmento del perfil oficial en inglés, que **solo sirve para clasificar y nunca se copia ni se traduce**.

- **Firma:** la primera técnica, salvo que otra tenga una palabra de potencia máxima (*giga*, *final*, *ultimate*, *nova*, *omega*…) o que la primera sea de apoyo. En los datos, MetalGreymon empieza por Trident Arm, pero Giga Destroyer lleva *giga* y se queda la Firma.
- **Potencia:** Firma P3 (P2/P3 si es la única), segunda P2, tercera P2 desde rango 3 y el resto P1. Fuera de la Firma, una palabra menor (*petit*, *mini*, *baby*…) baja una potencia.
- **Apoyo:** si el nombre habla de curar, proteger, mejorar o purificar y no tiene palabras de daño, la técnica no hace daño ni lleva tirada.
- **Alcance:** Larga, luego Distancia fuerte, Toque, el contexto y Distancia débil. Si nada decide, la Firma es de Distancia y las demás dependen del rol primario de la familia.
- **Elemento:** primero las frases y luego las palabras sueltas, por este orden: Veneno, Hielo, Eléctrico, Fuego, Agua, Planta, Oscuridad, Luz, Cósmico, Mental, Viento, Tierra y Acero. Si no hay ninguna, la afinidad de la familia (salvo en Toque) o Neutro.
- **Área:** Total solo en la Firma de rango 4; si no, Zona, Ráfaga o Individual. Una técnica de daño P1 siempre es Individual.
- **Palabras clave:** como mucho dos. Del nombre se toma solo la primera palabra de cada categoría (apoyo, daño, estado y táctica), según el orden de efectos; si aún queda hueco, se buscan en el contexto. En la segunda pasada, una técnica sin estado recibe el **estado por defecto de su elemento** y la Firma, la **palabra de Firma de su rol**, si les cabe; además, la Firma de Distancia de un Tirador pasa a Larga. Ejecutar solo va en técnicas Individuales (en una de área pasa a Brutal).
- **Correcciones manuales:** 74 técnicas y 24 Digimon tienen valores fijados a mano. Siempre ganan.

### Elementos y amenaza

El **elemento principal** es el más repetido entre sus técnicas oficiales, sin contar Neutro (si empatan, el de la técnica que va antes). Las **debilidades** son las de su familia más el primer elemento de esta lista que vence a su elemento principal y que no esté ya entre las debilidades ni las resistencias de su familia: Agua, Fuego, Planta, Eléctrico, Veneno, Viento, Tierra, Hielo, Acero, Mental, Luz, Oscuridad y Cósmico. Las **resistencias** son las de su familia más su elemento principal (salvo Neutro y Cósmico). Lo repetido en ambas listas se tacha y quedan como mucho dos de cada. MetalGreymon (Vaccine) es Máquina (débil a Eléctrico, resiste Veneno) y su elemento principal es Acero, al que vence el Fuego: débil a Eléctrico y Fuego, resiste Veneno y Acero.

La **amenaza sugerida** sale de tres listas cerradas (Legendarios, Jefes y esbirros). El **índice de amenaza** combina su **ofensiva** (dados de su Firma y de su mejor otra técnica, probabilidad de que la Defensa del PJ falle, área de la Firma) con sus **PV efectivos** (PV, Arm, resistencias, curación y lo difícil que es impactarla), frente a una pareja media de su rango. La ofensiva cuenta al cuadrado: en las simulaciones, el riesgo de derrota depende más del daño que del aguante. Las fichas de cada nivel se dividen en tres tercios: **baja**, **media** y **alta**. Los Bebés, que no tienen rol, son siempre «media». Por eso [[WarGreymon]] es «baja» y [[ShineGreymon]], con más Atq y más PV, es «alta».

### La validación

Ninguna ficha se publica si se sale de estos márgenes:

| Fila | PV | Atq | Def | Arm |
|---|---|---|---|---|
| Bebé I y II | 6 y 10 | +0 a +2 | +0 a +2 | 0 |
| Novato | 15–36 | +0 a +5 | +0 a +4 | 0–2 |
| Campeón | 20–48 | +1 a +6 | +1 a +5 | 0–2 |
| Perfecto | 25–60 | +2 a +7 | +2 a +6 | 0–2 |
| Definitivo | 30–72 | +3 a +8 | +3 a +7 | 0–2 |

Además: como mucho una P3 (o P2/P3) por ficha y dos palabras clave por técnica; ningún Bebé con P3, Ejecutar ni control duro; Total solo en la Firma de rango 4; Ejecutar solo en técnicas Individuales; las técnicas de apoyo no hacen daño; y toda ficha tiene técnica básica y maniobra de rol (los Bebés, solo básica). Con todo esto, un duelo entre dos Digimon del mismo nivel dura de media unos tres asaltos.

## Crear tus propios Digimon

El guardián de una región o el villano original de tu campaña encajará en el presupuesto como cualquier ficha oficial si lo creas con las mismas fórmulas. El capítulo 12 trae una versión rápida; esta es la completa:

1. **Concepto y nivel:** el nivel te da la fila.
2. **Tipo y familia:** elige un tipo oficial; su familia te da afinidad, debilidad, resistencia, rasgo, técnica básica y especialidad.
3. **Atributo.**
4. **Técnicas:** una o varias, con nombre en inglés, clasificadas con las reglas anteriores. Si un nombre no deja claro qué hace, decide tú, como haría una corrección manual.
5. **Rol:** cuenta los puntos o, sencillamente, elígelo.
6. **Plantillas de forma**, si las tiene, y **cifras** con las fórmulas.
7. **Elementos:** necesitas saber qué vence a qué.

| Elemento | Estado por defecto | Vence a |
|---|---|---|
| Veneno | Veneno | Planta |
| Hielo | Congelar | Planta, Viento |
| Eléctrico | Paralizar | Agua, Viento |
| Fuego | Quemar | Planta, Hielo, Acero |
| Agua | Ralentizar | Fuego, Tierra |
| Planta | Atrapar | Agua, Tierra |
| Luz | Cegar | Oscuridad |
| Oscuridad | Asustar | Luz, Mental |
| Cósmico | Ralentizar | Tierra, Acero |
| Mental | Confundir | Veneno, Cósmico |
| Viento | Empujar | Planta, Veneno |
| Tierra | Derribar | Eléctrico, Veneno, Fuego |
| Acero | — | Hielo, Mental |
| Neutro | — | — |

8. **Rasgos, técnica básica, maniobra y especialidades** de su rol, familia, atributo y plantillas.
9. **Valida** con los márgenes y las reglas de la sección anterior.
10. **Índice de amenaza:** copia el de una ficha del mismo nivel, familia, rol y atributo, con una Firma parecida. Ante la duda, «media».

### Ejemplo completo: Mudgatormon

Mudgatormon es una criatura original: un caimán de barro que duerme bajo los pantanos del sur y despierta cuando alguien enturbia sus aguas. Es **Perfecto**, de tipo **Reptile** (familia **Saurio**) y **Virus**, con tres técnicas: **Mud Crusher**, **Swamp Quake** y **Tail Hammer**.

- **Mud Crusher** es la Firma (ninguna técnica lleva palabras de potencia máxima) y es P3. *Crusher* da Toque y Brutal; *mud* da Tierra. De sus dos estados posibles (Ralentizar por *mud*, Romper por *crusher*) se queda el primero del orden de efectos: Ralentizar.
- **Swamp Quake** es P2. *Quake* da Distancia, Tierra, Zona y Derribar.
- **Tail Hammer** es P2 por ser la tercera técnica de un rango 3. *Tail* y *hammer* dan Toque; *hammer* da Acero y Aturdir, que va antes que el Derribar de *tail*.

**Rol:** Saurio da Bruto 3 y Tanque 1. Mud Crusher, que cuenta doble, suma Bruto +4 (Toque y Brutal) y Místico +2 (Ralentizar); Swamp Quake, Tirador +1 y Bruto +1; Tail Hammer, Bruto +2. Total: Bruto 10. Su Firma ya lleva Brutal, la palabra de Firma del Bruto.

**Cifras:** PV = 5 × (7 + 1 Bruto + 1 Saurio) = 45. Atq = 3 + 1 Bruto + 1 Virus = +5. Def +3, Arm 0, Ini +3. Todo dentro de los márgenes.

**Elementos:** Tierra aparece dos veces, así que es su elemento principal. Saurio es débil al Hielo y el Agua vence a la Tierra; Saurio ya resiste la Tierra.

**Índice:** [[Azhdarmon]] es Perfecto, Saurio, Bruto y Virus, con las mismas cifras y una Firma P3 Individual: amenaza alta. Mudgatormon también lo es (el generador de referencia lo confirma).

```
Mudgatormon — Perfecto · Saurio (Reptil) · Bruto · Virus
Rango 3 · PV 45 · Atq +5 · Def +3 · Arm 0 · Ini +3 · Dado d10 (VF 5)
Debilidad: Hielo, Agua · Resistencia: Tierra · Triángulo: vence a Datos
Especialidades: aguante, fuerza, morder; fuerza y romper cosas · Amenaza: alta (PA ×1½)
Rasgos: Arrollador (rol); Piel gruesa (familia); Agresión (atributo)
Técnicas:
· Mordisco — P1 · Toque · Individual · Neutro  [1d10]
· Arremetida — P1 · Toque · Individual · Neutro · Derribar
· Mud Crusher — P3 (Agotadora) · Toque · Individual · Tierra · Brutal, Ralentizar  [3d10]
· Swamp Quake — P2 · Distancia · Zona · Tierra · Derribar  [2d10; contra 2+: 1d10]
· Tail Hammer — P2 · Toque · Individual · Acero · Aturdir  [2d10]
Evoluciona de: — · Evoluciona a: —
```

Un Mudgatormon (X Antibody) tendría PV 50 y Atq +6. Y si tienes prisa, usa la ficha de Azhdarmon con otro nombre y otra descripción: las cifras son las mismas.

**Errores frecuentes:** subir una cifra «a ojo» (si debe ser más duro, dale una plantilla de amenaza); darle dos P3 o tres palabras clave a una técnica; poner Total fuera de la Firma de un Definitivo o Ejecutar en un área; pasar de Arm 2; o dar la plantilla Legendario a un compañero.

> **Consejo para el DJ:** escribe tú la descripción de tus criaturas. Bastan una o dos frases con su aspecto, una costumbre y un gancho. «Duerme bajo el lodo y solo despierta si alguien enturbia el agua» ya le regala a tu mesa una escena entera.

## El bestiario en la web

La web del manual tiene todo el bestiario a mano y hace las cuentas por ti:

- **Buscador:** por nombre, tipo o técnica.
- **Filtros:** nivel, atributo, familia, rol, elemento, grupo (Legendarios, X-Antibody o Modos) y una casilla para ver solo los que vuelan. Puedes ordenar por nivel, nombre, PV o Ataque, y los filtros se recuerdan en tu navegador.
- **Ficha:** los botones **Estándar, Esbirro, Élite, Jefe, Jefe · Refuerzo I, Jefe · Refuerzo II y Legendario** recalculan sus cifras y muestran las reglas de la plantilla. En Jefes y Legendarios puedes indicar el número de parejas, y la ficha te dice cuántos PA vale.
- **Constructor de encuentros:** el botón «Añadir al encuentro» lleva la ficha a tu combate, con su plantilla, y suma los PA y la dificultad.

Si un nombre aparece repetido, como los dos [[Rapidmon]], mira el nivel: uno es Perfecto y el otro, Armadura.

## Lo esencial

- Las 1.317 fichas salen de la misma fórmula: **nivel, familia, rol, atributo y técnicas oficiales**. Todas son **Estándar**. No cambies sus cifras.
- Lee la ficha por líneas: identidad, cifras, elementos y triángulo, especialidades y amenaza, rasgos, técnicas y evolución.
- **Roles** y **familias** modifican cifras y dan rasgos; el **atributo** te coloca en el triángulo.
- Las **plantillas de forma** (X-Antibody, Modos, Armadura, Híbrido, Fusión, Bebé) ya están en la ficha: recuerda sus rasgos.
- Las **plantillas de amenaza** las aplicas tú. PA = PA de la plantilla × factor de rango × índice de amenaza.
- **PV = VF × (7 + modificadores)**; **Atq y Def = rango + modificadores**; **Arm, como máximo 2**.
- Para crear un Digimon, sigue la especificación, valida sus cifras y copia el índice de una ficha parecida.
- La web tiene **buscador, filtros, botones de plantilla y constructor de encuentros**.
