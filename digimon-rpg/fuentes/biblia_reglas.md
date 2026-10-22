# DIGIMON: LAZOS DE CÓDIGO
## Juego de rol no oficial de aventuras en el Mundo Digital — BIBLIA DE REGLAS v1.1

> **Aviso:** *Digimon: Lazos de Código* es una **obra de fans, no oficial y sin ánimo de lucro**. Digimon y todos sus nombres, personajes, técnicas e imágenes pertenecen a sus propietarios. Este proyecto no está afiliado ni respaldado por ellos. Todo el texto de reglas es original. Los nombres de los Digimon y de sus técnicas se usan tal cual, como referencia. Los perfiles oficiales **nunca** se copian ni se traducen.

**Qué es este documento.** Es la **fuente de verdad** para quienes redacten los capítulos del manual, el bestiario, la ficha editable y las aventuras. Si un capítulo contradice esta biblia, manda la biblia. Si la biblia contradice `spec_fichas.json` en una cifra del bestiario, manda el JSON, y hay que corregir la biblia. Esta versión 1.1 corresponde a `spec_fichas.json` 1.1; la lista de cambios respecto a la 1.0 está en `design/cambios.md`.

**Etiquetas:** **[N]** núcleo (las reglas de una campaña normal; la **primera sesión** usa solo el subconjunto marcado como *Núcleo de primera sesión*, 1.1) · **[A]** avanzado (se añade cuando el grupo domina el núcleo) · **[O]** módulo opcional.

**Índice**
0. Decisiones de diseño (de dónde sale cada pieza)
1. El sistema en una página
2. Resolución
3. El Tamer
4. El compañero Digimon
5. Chispa, Vínculo y digievolución
6. Combate
7. Estados alterados
8. Triángulo de atributos
9. Familias de tipos (los 140 tipos)
10. Elementos
11. Vocabulario de técnicas (potencias, alcances, áreas, palabras clave)
12. Roles de combate y técnicas aprendibles
13. Programas (Tarjetas de modificación)
14. Objetos, equipo y Bits
15. Digivices
16. Emblemas
17. Progresión
18. Exploración, relaciones y Mundo Digital
19. Amenazas: esbirros, élites, jefes, legendarios y hordas
20. Reglas opcionales avanzadas (Armadura, Espíritus, DNA, Modos, X-Antibody, Digimon salvajes, corrupción…)
21. Especificación de fichas (resumen de `spec_fichas.json`) y ejemplos calculados
22. Hoja de referencia rápida y notas para redactores

---

## 0. Decisiones de diseño

El sistema parte de la propuesta **A** («Chispa Digital», 2d6 con franjas), que fue la mejor valorada en accesibilidad y especificación programable, y le injerta lo mejor de **C** y **B**. También corrige los riesgos que señalaron los jueces.

| Pieza | Origen | Por qué |
|---|---|---|
| 2d6 + modificador, franjas 10+ / 7–9 / 6–, el DJ no tira para impactar | A | Se aprende en 15 minutos y el DJ lleva seis Digimon sin hacer cuentas. |
| Dado de Poder d4 → d12 según el nivel; daño con dados de poder | A | Digievolucionar se nota en la mano. |
| **PV = VF × (7 + modificadores)**, proporcionales al nivel | C (corrige A) | Los golpes necesarios para tumbar a un igual no cambian con el nivel. Ningún Definitivo tiene menos PV que la base de un Perfecto por culpa de un modificador fijo. |
| Armadura plana, como máximo 2 (no crece con el nivel) | Juez 3 | Evita los Tanques Máquina de 8–10 turnos. |
| **Sin Energía:** P1 y P2 a voluntad, P3 *Agotadora* (tras usarla, el turno siguiente no se puede usar otra técnica Agotadora) | Juez 1 y 3 | Quita contabilidad a jugadores y DJ. |
| **Dado de Vínculo** (Ventaja una vez por asalto) y **Resonancia** (un 6 da Chispa) | C, adaptado a 2d6 | El Tamer decide algo en cada asalto: es el «¡brilla el Digivice!». |
| La Chispa se gana fallando, en Crisis y por el Emblema; cuesta 2 por nivel; detonante la primera vez | A | La digievolución nace de la adversidad. A Vínculo 1 nunca se digievoluciona en el asalto 1 sin una Crisis. Desde Vínculo 2, la Chispa inicial ya paga un nivel en el asalto 1, y el presupuesto de encuentro lo cuenta con el **nivel de referencia** (19.2). |
| **Hambriento** y **regresión a Bebé II** tras grandes saltos | C y B | Fidelidad (Koromon después de la batalla) y coste narrativo. |
| Ataque conjunto, Sendas del Tamer, anatomía de jefe (fases, Firma telegrafiada, Guardia de carga, punto débil, objetivos de escena), combos elementales, lista de voladores, validación automática | B | Profundidad táctica para veteranos, separada en capas. |
| Dominios de los grupos legendarios, viajes con papeles, clima, regiones, Engranajes Negros, pruebas de grupo, menú de costes y jugadas del DJ | A | Sabor y herramientas de DJ. |
| Clasificación de técnicas en dos pasadas (nombre y, después, contexto del perfil); debilidades derivadas del elemento principal; plantilla Legendario solo para PNJ; Tarjetas Digimon | C | Más precisión sin perder el determinismo. Los compañeros pueden llegar a Gallantmon. |
| Lista curada de Legendarios (no por tipo, por id), `overrides`, rangos de validación | A, B y jueces | Evita inflar el bestiario de jefes y permite corregir a mano las técnicas icónicas. |
| Golpe aguantado, regla de espejo, Jefe reforzado según el Vínculo, índice de amenaza por ficha | Verificadores (ronda 3) | Ningún compañero cae de un solo golpe; los estados funcionan contra PNJ; el Jefe sigue siendo un clímax cuando la Chispa inicial ya paga la digievolución. |

**Calibración (versión 1.1; motor `work_final/r3_sim.py` con las fichas reales de `gen.py`; 4 parejas de las líneas Adventure, Tamers y Savers, con Orden y Dado de Vínculo en cada asalto, sin programas, sin objetos y sin Firma telegrafiada):**
- **Vínculo 1:** un encuentro Fácil dura 2,1–2,6 asaltos, uno Normal 2,7–3,0 y uno Difícil 3,4–3,7, sin derrotas. Los compañeros que digievolucionan lo hacen de media entre los asaltos 1,5 y 1,8, siempre tras una Crisis.
- **Jefe de la aventura** (19.2): Vínculo 1, 5,0–5,3 asaltos y 1–3 % de derrota; Vínculo 2, 3,6–3,8 asaltos y 2–10 %; Vínculo 3, 4,3–4,7 asaltos y 16–28 %; Vínculo 4, 3,0–4,8 asaltos y 3–27 %; Vínculo 5, 2,9–4,1 asaltos y 0–10 %. Un **Legendario** de clímax contra Vínculo ★ dura 3,8–4,4 asaltos, con un 7–22 % de derrota.
- La diferencia entre dos Jefes del mismo nivel es mayor que la diferencia entre tramos (Myotismon como Jefe a Vínculo 3: 60–97 % de derrota; Etemon: 0 %). Por eso cada ficha lleva un **índice de amenaza** que corrige su PA (19.2).
- Un enemigo un nivel por encima del nivel de referencia que el grupo no puede alcanzar en el combate es casi imposible (75 % de derrota a Vínculo 2 contra un Jefe Perfecto sin el Perfecto desbloqueado). Dos niveles por encima es imposible sin digievolucionar: así está pensado, y la huida siempre es una opción.

---

## 1. El sistema en una página [N]

**El grupo.** Cada jugador lleva una **pareja**: un **Tamer** (un chico o una chica humanos, de unos 10 a 17 años) y su **compañero Digimon**. El **Director de Juego (DJ)** describe el Mundo Digital y lleva a todos los demás. Grupo típico: de 3 a 5 parejas.

**La tirada.** Cuando el resultado es incierto, tira **2d6 y suma un modificador**:
- Tu Tamer actúa: **atributo + habilidad** (p. ej., Destreza +1 y Sigilo +1 → 2d6 + 2).
- Tu Digimon ataca: **su Ataque − la Defensa del objetivo**.
- Tu Digimon se defiende: **su Defensa − el Ataque del enemigo**. *(Los jugadores tiran siempre; el DJ solo tira el daño. Por eso, cuando una regla da un bono o un penalizador a la tirada de un PNJ, se aplica con el signo cambiado a la tirada del PJ que se le opone: es la **regla de espejo**, 2.1.)*

| Resultado | Significa | En combate |
|---|---|---|
| **10+** | Lo consigues limpiamente. | Atacando: daño y todos los efectos. Defendiendo: lo evitas. |
| **7–9** | Lo consigues con un coste, a medias o con una complicación. | Atacando: daño sin estados. Defendiendo: recibes la mitad del daño. |
| **6–** | No sale y algo se complica. **Tu Tamer gana 1 Chispa** (como mucho 1 por asalto en combate y 1 por escena fuera de combate). | Atacando: fallas. Defendiendo: daño completo y efectos. |

Doble seis siempre es 10+ (crítico). Doble uno siempre es 6– (pifia).

**El asalto.** Las parejas que ganan la iniciativa actúan primero (*fase rápida*), luego todos los enemigos (*fase enemiga*) y luego el resto (*fase lenta*). En su turno, cada pareja hace **una acción de Tamer** (dar una Orden, usar un programa o un objeto, Analizar, Animar…) y **una acción de Digimon** (normalmente una técnica), y cada uno puede moverse una zona.

**El Dado de Vínculo.** Una vez por asalto, tu Tamer puede añadir un dado de otro color a una tirada de su compañero: tiras 3d6 y te quedas con los 2 mejores. **Si ese dado saca un 6, ganas 1 Chispa.**

**Técnicas.** P1 (1 dado de poder) y P2 (2 dados) se usan siempre que quieras. P3, la *Firma*, tira 3 dados, pero es *Agotadora*: en el turno siguiente tu compañero no puede usar otra técnica Agotadora. El dado crece con el nivel: Bebé d4, Novato d6, Campeón d8, Perfecto d10, Definitivo d12.

**Digievolución.** Gasta **2 Chispa por cada nivel por encima de tu nivel estable** (al principio, Novato). Tu compañero toma la ficha de la nueva forma, con todos sus PV, hasta el final de la escena. Si esa forma cae a 0 PV, vuelve a la forma desde la que digievolucionó (su *forma de partida*) con los PV que tenía y queda *Agotado*. La primera vez que alcanza cada nivel hace falta, además, un momento dramático.

**Triángulo.** Vacuna vence a Virus, Virus vence a Datos y Datos vence a Vacuna: **+1 a tus tiradas** contra el atributo que vences, y −1 contra el que te vence.

Con esto ya se puede jugar. Todo lo demás son detalles, opciones y listas.

### 1.1 Núcleo de primera sesión
Lo único que hay que enseñar para jugar la primera sesión (unos 15 minutos), con parejas pregeneradas (22.3):
- Este capítulo 1 y la escena (2.14).
- La tirada, las franjas, la dificultad, la Ventaja, la Ayuda y los críticos (2.1–2.6).
- **Atacar** y **Defenderse** (6.6–6.8) con la técnica básica, la P2 y la Firma de la ficha.
- Cuatro acciones de Tamer: **Orden**, **Analizar**, **Animar** y **Usar un objeto** (6.5).
- La **Chispa**, el Dado de Vínculo y la **digievolución a Campeón** con su detonante (5.1, 5.3, 5.4–5.6).
- Seis estados: **Quemar, Paralizar, Atrapar, Asustar, Aturdir y Expuesto**.

El resto del núcleo [N] (programas, más estados, Sendas con talentos, Emblemas, el Jefe completo…) entra en las sesiones 2 a 4, a medida que aparece. Lo marcado [A] y [O], después.

---

## 2. Resolución [N]

### 2.1 La tirada
**2d6 + modificador total.** En situaciones normales, el modificador total queda entre −4 y +6.
- **Tamer:** 2d6 + **atributo** (−1 a +3) + **habilidad** (0 sin entrenar, +1 entrenada, +2 experta) + situación.
- **Digimon en combate:** 2d6 + **Atq propio − Def del objetivo** (al atacar) o 2d6 + **Def propia − Atq del atacante** (al defender) + situación.
- **Digimon fuera de combate:** 2d6 + **rango** (Bebé 0, Novato 1, Campeón 2, Perfecto 3, Definitivo 4) **+1 si la acción es la especialidad de su familia o de su rol** (cap. 9 y 12).
- **Tamer contra un Digimon** (esconderse de él, engañarlo, huir o perseguir a pie, el programa Candado): resta **siempre** el **rango** del Digimon (no su Def ni su Ini).
- **Tirada enfrentada** (dos PJ entre sí, o un PJ contra un PJ rival): tiran ambos; gana el resultado más alto. Si empatan, gana quien tenga el modificador más alto; si también empatan en eso, ambos consiguen un éxito parcial (o el DJ decide, con un coste para los dos).
- **Regla de espejo:** el DJ no tira para impactar, así que **todo modificador a una tirada de un PNJ se aplica con el signo cambiado a la tirada del PJ que se le opone**. −X a los ataques de un PNJ = +X a la Defensa del PJ; +X al ataque de un PNJ = −X a la Defensa del PJ; «los ataques contra él tienen +X» = +X al ataque del PJ si el objetivo es un PNJ, y −X a la Defensa del PJ si el objetivo es un PJ; Ventaja de un PNJ = Desventaja del PJ, y al revés. La traducción de cada estado está en 11.4.

### 2.2 Franjas
**10+ éxito total · 7–9 éxito parcial · 6– fallo.** Siempre se leen desde el punto de vista de quien tira.

### 2.3 Dificultades
Los umbrales no cambian nunca (7 y 10). La dificultad es un **modificador** que el DJ anuncia **antes** de tirar.

| Dificultad | Mod. | Ejemplo |
|---|---|---|
| Trivial | sin tirada | Abrir una puerta normal. |
| Fácil | +1 | Trepar a un árbol con ramas bajas. |
| Normal | 0 | Convencer a un Digimon neutral de que os deje pasar. |
| Difícil | −1 | Hackear una terminal del Mundo Digital. |
| Muy difícil | −2 | Cruzar a nado un río de datos crecido. |
| Heroica | −3 | Saltar de un Birdramon en vuelo a otro. |
| Imposible | — | No se puede sin un plan, un programa o una digievolución. |

### 2.4 Ventaja y desventaja
Por una posición narrativa clara (atacar por sorpresa, terreno ideal, estar herido…) el DJ concede **Ventaja** (tira 3d6 y quédate con los 2 mejores) o impone **Desventaja** (3d6 y quédate con los 2 peores). No se acumulan: una Ventaja y una Desventaja se anulan. El Dado de Vínculo (5.3) es una forma de Ventaja.

### 2.5 Ayuda
Otro personaje que describa cómo ayuda da **+1** (máximo +2 en total por varias ayudas). Si la tirada sale 6–, quien ayudó comparte la consecuencia. Fuera de combate, un Tamer y su propio compañero pueden ayudarse. **En combate**, la ayuda del Tamer a su compañero es la **Orden** (6.5), que no se suma a esta Ayuda; la Ayuda de este apartado solo se usa entre compañeros distintos o fuera de combate.

### 2.6 Críticos y pifias
- **Doble seis:** siempre cuenta como 10+, aunque los modificadores lo bajen. En ataque: **+1 dado de daño** y se aplican todos los efectos de la técnica. En defensa: **contraataque gratuito**, el atacante recibe 1 dado de poder de daño de tu compañero (sin tirada; ignora la Arm). Fuera de combate, el DJ añade un beneficio extra.
- **Doble uno:** siempre cuenta como 6– y la jugada del DJ es dura.

### 2.7 Límite de modificadores situacionales
Los bonificadores **situacionales** (Orden, Ayuda, programas, Marcado, triángulo, Certero, rasgos que dan +1 a la tirada…) suman **como mucho +3**, y los penalizadores, **como mucho −3**. Atq, Def, atributos, habilidades, dificultad y rango no cuentan para este límite. *Esta regla debe aparecer en la hoja de referencia: es la que impide que un Tirador Virus con X-Antibody impacte siempre.*

### 2.8 Probabilidades de referencia (2d6)

| Mod. total | 7+ (al menos parcial) | 10+ (total) | con Ventaja: 7+ | con Ventaja: 10+ |
|---|---|---|---|---|
| −3 | 16,7 % | 2,8 % | 35,6 % | 7,4 % |
| −2 | 27,8 % | 2,8 % | 52,3 % | 7,4 % |
| −1 | 41,7 % | 8,3 % | 68,1 % | 19,9 % |
| 0 | 58,3 % | 16,7 % | 80,6 % | 35,6 % |
| +1 | 72,2 % | 27,8 % | 89,4 % | 52,3 % |
| +2 | 83,3 % | 41,7 % | 94,9 % | 68,1 % |
| +3 | 91,7 % | 58,3 % | 98,1 % | 80,6 % |
| +4 | 97,2 % | 72,2 % | 99,5 % | 89,4 % |

*(El doble seis siempre es 10+ y el doble uno siempre es 6–: con −3 y −2, el 10+ solo llega por crítico.)*

### 2.9 Éxito parcial (7–9): menú de costes
El DJ ofrece uno, o el jugador elige entre dos:
- **Tarda más:** el reloj de amenaza avanza 1.
- **Cuesta algo:** un objeto, 1 Carga del Digivice, 1 Aguante o 1 Chispa.
- **Resultado reducido:** consigues la mitad, o solo durante un rato.
- **Complicación:** alguien te ve, algo se rompe o aparece un problema nuevo.
- **Posición peligrosa:** la próxima tirada relacionada tiene −1.
- **Separación:** lo consigues, pero te alejas del grupo (o de tu compañero).

### 2.10 Jugadas del DJ (cuando sale 6–)
**Suaves** (avisan): mostrar una amenaza que se acerca, ofrecer una oportunidad con coste, separar al grupo, revelar una verdad incómoda, **anunciar el próximo ataque contra un Tamer** (telegrafiar).
**Duras** (golpean): infligir daño o un estado, quitar un objeto, avanzar un reloj 2 segmentos, capturar a alguien, hacer que un enemigo actúe de inmediato, cumplir un ataque telegrafiado contra un Tamer.
*Regla de oro:* tras un 6– **siempre cambia algo**; nunca «no pasa nada». Con un DJ primerizo, la jugada por defecto en combate es: *el compañero queda Expuesto* (−1 Def hasta el final de su próximo turno, 7.3).

### 2.11 Relojes de progreso
Para tareas largas o amenazas (hackear una Torre Oscura, el despertar de un Señor Demonio, una persecución, un objetivo de escena en combate), dibuja un reloj de **4, 6 u 8 segmentos**.
- Tirada de progreso: **10+ marca 2**, **7–9 marca 1**, **6– no marca** (y avanza el reloj de amenaza, si lo hay).
- Los relojes de amenaza avanzan con los fallos, con el paso del tiempo o con las jugadas duras.

### 2.12 Pruebas de grupo
Cuando todos hacen lo mismo (escalar, esconderse, cruzar la ciénaga), tiran todos. **Si al menos la mitad saca 7+, el grupo lo consigue**; cada 6– individual sufre una consecuencia menor (−1 Aguante, pierde algo, se rezaga). Si **todos** sacan 10+, el grupo obtiene además un beneficio (un atajo, una ventaja en la escena siguiente).

### 2.13 Digimon fuera de combate
Los compañeros también actúan fuera de combate: volar con alguien a cuestas, olfatear un rastro, abrir un camino a golpes, iluminar una cueva. Tiran **2d6 + rango (+1 especialidad)**; la ficha imprime el rango y las dos especialidades (familia y rol). Una forma digievolucionada en una escena tranquila tiene su rango, pero el compañero queda Hambriento al terminar (5.7).

### 2.14 Escena y combate
- Una **escena** es un tramo continuo de acción en un lugar y con un objetivo: cruzar el bosque, interrogar a un Gekomon, pelear contra Ogremon.
- Un **combate** es siempre una escena completa y termina cuando no quedan enemigos activos. Un combate que enlaza con otro sin pausa (llegan refuerzos, el grupo sigue corriendo y le sale otro enemigo) forma parte de **la misma escena**: la forma temporal sigue activa, no se renuevan los límites «por escena» y el Hambriento llega al final.
- **La escena termina cuando el DJ corta:** cambio de lugar, paso de tiempo o descanso. Al terminar se aplican los efectos «al final de la escena» (fin de la forma temporal, Hambriento, regresión, Escudos, Romper) y se renuevan los límites «por escena».
- Los límites «por combate» se renuevan con cada combate, aunque sea en la misma escena.

---

## 3. El Tamer [N]

### 3.1 Creación en 9 pasos (unos 20 minutos; creación rápida en 5)
1. **Concepto:** nombre, edad, aspecto y una pregunta: *¿qué te falta en tu vida?* (es la semilla de tu Emblema).
2. **Atributos:** reparte **+2, +1, +1 y 0** entre Valor, Astucia, Corazón y Destreza.
3. **Trasfondo:** elige uno (3.4). Te da 2 habilidades entrenadas, un objeto y un rasgo.
4. **Habilidades:** entrena **2 habilidades más** (+1). Puedes renunciar a una de ellas para hacer **experta (+2)** una habilidad que ya tengas entrenada.
5. **Senda:** elige tu papel en combate (3.5) y su talento inicial.
6. **Rasgos personales:** elige o tira una cualidad y un defecto (3.6).
7. **Emblema:** elige tu virtud (cap. 16). Milagros y Destino son Emblemas dorados de trama: no se eligen al crear el personaje.
8. **Compañero Digimon** (cap. 4):
   - elige un **Novato** y ponle nombre si quieres;
   - anota su **Bebé II** (de su lista *prev*; si no tiene, 4.2);
   - anota un **Campeón probable** de su lista *next*;
   - elige o tira su **personalidad** (4.4, 1d12);
   - si quieres, **fija su rol** (4.1); si es Versátil, elige ya su especialidad (12.3).
9. **Digivice, programas y equipo:** elige un modelo de Digivice (cap. 15), **3 programas de Nivel 1** (cap. 13), el objeto del trasfondo, **2 objetos del equipo del Tamer** (tabla 14.3) de hasta 60 Bits cada uno, **1 Disco de recuperación S**, **2 Carnes digitales** y **100 Bits**. Empiezas con **Vínculo 1, Chispa 1** y la **Carga llena**. Calcula los valores derivados (3.7).

**Creación rápida** (para la primera sesión o para quien llega tarde): usa una pareja pregenerada (22.3), o haz solo los pasos 1, 3 y 8 y toma tu Senda como **paquete cerrado** con el Digivice clásico:

| Senda | Atributos (VAL / AST / COR / DES) | Programas | Equipo |
|---|---|---|---|
| Estratega | +1 / +2 / +1 / 0 | Velocidad, Escáner, Puntería | Silbato, Prismáticos |
| Técnico | 0 / +2 / +1 / +1 | Potencia, Guardia, Antídoto | Linterna, Navaja multiusos |
| Protector | +2 / 0 / +1 / +1 | Guardia, Antídoto, Ancla de suelo | Botiquín, Cuerda |
| Batidor | +1 / +1 / 0 / +2 | Velocidad, Utilidad, Bengala | Cuerda, Brújula |
| Inspirador | +1 / 0 / +2 / +1 | Potencia, Enfoque, Guardia | Silbato, Linterna |

Las 2 habilidades del paso 4 también vienen dadas por la Senda: Táctica y Saber Digital (Estratega), Tecnología y Saber Digital (Técnico), Medicina y Atletismo (Protector), Atletismo y Observación (Batidor), Empatía y Persuasión (Inspirador). Si una ya la tienes por el trasfondo, pasa a experta (+2).

### 3.2 Atributos del Tamer

| Atributo | Para qué sirve | Ejemplos | Deriva |
|---|---|---|---|
| **Valor (VAL)** | Coraje y cuerpo | Plantar cara al miedo, aguantar, levantar, intimidar | Aguante |
| **Astucia (AST)** | Mente y técnica | Analizar, hackear, planificar, recordar | Carga |
| **Corazón (COR)** | Empatía y voluntad | Animar, convencer, calmar a un Digimon salvaje, resistir la desesperación | — |
| **Destreza (DES)** | Agilidad y reflejos | Esquivar, correr, sigilo, puntería, trabajos manuales finos | Defensa del Tamer |

Máximo +2 al crear el personaje y +3 a lo largo de la campaña. **Defecto marcado** (opcional, al crear el personaje): baja a −1 el atributo que tenía 0 y sube en +1 otro que no pase de +2; es el único modo de tener un atributo a −1.

### 3.3 Habilidades (12)
Cada habilidad se combina con el atributo que pida la situación (el DJ lo sugiere y el jugador puede argumentar otro).

| Habilidad | Uso típico | Atributo habitual |
|---|---|---|
| Atletismo | Correr, trepar, nadar, saltar, esquivar | VAL / DES |
| Sigilo | Esconderse, moverse sin ruido | DES |
| Tecnología | Ordenadores, Digivice, máquinas, hackear | AST |
| Saber Digital | Conocer Digimon, leyendas y el Mundo Digital | AST |
| Observación | Buscar, notar, investigar pistas | AST / COR |
| Supervivencia | Orientarse, rastrear, acampar, buscar comida | AST / VAL |
| Medicina | Primeros auxilios, cuidar de personas y Digimon | AST / COR |
| Persuasión | Convencer, negociar, liderar | COR |
| Engaño | Mentir, disimular, actuar | COR / AST |
| Empatía | Leer emociones, calmar, hablar con Digimon salvajes | COR |
| Táctica | Mandar en combate, planear emboscadas | AST / VAL |
| Arte | Música, cocina, dibujo, actuación | COR / DES |

### 3.4 Trasfondos (10)

| Trasfondo | Habilidades | Objeto | Rasgo |
|---|---|---|---|
| **Deportista** | Atletismo, Táctica | Balón o raqueta | *Fondo físico:* +2 Aguante. |
| **Cerebrito** | Saber Digital, Observación | Portátil | *Lo leí en algún sitio:* 1 vez por sesión, pregunta al DJ un dato útil y te lo dirá con sinceridad. |
| **Manitas** | Tecnología, Observación | Caja de herramientas | *Ingenio:* +1 Carga máxima. |
| **Hermano/a mayor** | Empatía, Medicina | Botiquín | *Protector:* +1 a cualquier tirada para proteger a alguien más débil o más joven. |
| **Explorador/a** | Supervivencia, Atletismo | Cuerda y brújula | *Siempre preparado:* 1 vez por sesión, saca de la mochila un objeto común razonable. |
| **Artista** | Arte, Persuasión | Instrumento o utensilios de cocina | *Inspiración:* en un descanso corto, todos los compañeros del grupo recuperan VF PV extra. |
| **Pícaro/a** | Sigilo, Engaño | Tirachinas o ganzúas | *Huidizo:* +1 a las tiradas de Defensa de tu Tamer. |
| **Líder nato** | Persuasión, Táctica | Silbato | *Al mando:* tu Orden puede darse a cualquier compañero del grupo, no solo al tuyo. |
| **Chico/a de campo** | Supervivencia, Empatía | Navaja multiusos | *Mano con los animales:* los Digimon salvajes empiezan un paso más amistosos contigo. |
| **Gamer** | Saber Digital, Tecnología | Consola portátil | *Me sé este jefe:* +1 a Analizar; 1 vez por combate puedes repetir una tirada de Analizar. |

**Objetos de trasfondo.** El portátil, el botiquín, el silbato, la navaja multiusos, la cuerda y la brújula usan su regla de 14.3. Los demás dan **+1 a una tirada por sesión** en la que encajen claramente: balón o raqueta (Atletismo), caja de herramientas (Tecnología para reparar), instrumento o utensilios de cocina (Arte), tirachinas (puntería del Tamer o distraer a un Digimon) o ganzúas (abrir cerraduras), consola portátil (Saber Digital).

### 3.5 Sendas del Tamer (arquetipos de combate)
La Senda es un paquete ya hecho que responde a *¿cómo ayudo a mi compañero en combate?*. Da un **talento inicial** y ordena los talentos que se eligen al subir de nivel (17.3). Desde el nivel 6 se puede tomar un talento de otra Senda.

| Senda | Estilo | Talento inicial |
|---|---|---|
| **Estratega** | Coordina a todo el equipo y multiplica las Órdenes | *¡Flanqueo!:* nueva Orden. Tu compañero y un aliado que ataquen al mismo enemigo este asalto tienen +1 contra él (para tu compañero, en lugar del +1 de la Orden normal). |
| **Técnico** | Maestro de programas y del entorno digital | *Memoria ampliada:* +2 Carga máxima y conoces 1 programa de Nivel 1 más. |
| **Protector** | Escudo emocional de su compañero | *Vínculo protector:* +1 Aguante; mientras estéis en la misma zona, tu compañero tiene +1 Def contra técnicas de área. |
| **Batidor** | Terreno, movilidad y emboscadas | *Ojo para el terreno:* al empezar cada combate, da Cobertura o Altura a una zona, o quita Terreno difícil de una. |
| **Inspirador** | Emoción, Chispa y digievolución | *Llama del vínculo:* al empezar cada combate, si tienes menos Chispa que tu Vínculo, sube hasta tu Vínculo. |

### 3.6 Rasgos personales
Elige (o tira 1d12) **una cualidad** y **un defecto**. La cualidad da **+1** a las tiradas fuera de combate en las que encaje claramente (como mucho una vez por escena). El defecto da **1 Chispa** una vez por sesión, cuando cause un problema real. *(«Cualidad» se usa para no confundirla con la virtud del Emblema.)*

| d12 | Cualidad | Defecto |
|---|---|---|
| 1 | Valiente | Impulsivo/a |
| 2 | Observador/a | Despistado/a |
| 3 | Generoso/a | Cabezota |
| 4 | Ingenioso/a | Miedoso/a (a algo concreto) |
| 5 | Leal | Celoso/a |
| 6 | Paciente | Mandón/a |
| 7 | Alegre | Llorón/a |
| 8 | Responsable | Perezoso/a |
| 9 | Curioso/a | Bocazas |
| 10 | Tranquilo/a | Orgulloso/a |
| 11 | Sincero/a | Desconfiado/a |
| 12 | Trabajador/a | Glotón/a |

### 3.7 Valores derivados del Tamer
- **Aguante = 6 + VAL** (+2 *Fondo físico*, +1 *Vínculo protector*; mínimo 4). Son los «puntos de vida» del Tamer. A 0 queda fuera de combate (6.11).
- **Defensa del Tamer** (tirada): **2d6 + DES + Atletismo − Atq del atacante**.
- **Carga del Digivice = 3 + AST + modificador del Digivice** (+ talentos y trasfondo). Se gasta en programas. Se recupera entera con un descanso largo y 2 puntos con uno corto.
- **Vínculo = 1** al empezar (máximo 5, y ★ con el arco del Emblema).
- **Chispa:** **1** al crear el personaje; máximo **3 + Vínculo**. Al empezar cada sesión, si tienes menos que tu Vínculo, sube hasta tu Vínculo.
- **Dado de Vínculo:** 1 por asalto (5.3).
- **Nivel de Tamer = 1** y 0 XP.

---

## 4. El compañero Digimon [N]

### 4.1 Principio: la ficha del compañero es la del bestiario
Cada forma del compañero usa **la ficha de su especie en el bestiario** (generada con `spec_fichas.json`), más:
- **Rol fijado** (opcional, al crearlo): el jugador puede fijar uno de los 8 roles; todas sus formas usarán los modificadores, el rasgo, la maniobra y la palabra de Firma de ese rol en lugar de los del bestiario. Así un jugador puede llevar un Apoyo o un Tanque aunque su línea no los tenga, y los PV crecen siempre al subir de nivel (ejemplo en 21.10).
- **Avances del compañero** (17.4), que se aplican a **todas** sus formas.
- **Técnicas heredadas o aprendidas** (12.4).
- **Personalidad** (4.4).
- Su **forma Bebé II**, su **forma Novato** y las **formas desbloqueadas** de cada nivel.

Los compañeros **nunca** usan las plantillas de amenaza (Élite, Jefe, Legendario): un compañero que llega a Gallantmon usa la ficha base de Gallantmon.

### 4.2 Elegir el Novato inicial
- Elige **un Novato del bestiario** con el visto bueno del DJ. No se permiten Legendarios ni las formas que solo existen como preludio de un Legendario (p. ej., Lucemon), salvo por una razón de campaña.
- Anota su **forma Bebé II** (de su lista *prev*): es la forma a la que vuelve cuando es derrotado o tras un gran esfuerzo. **Si no tiene ninguna** (27 Novatos del bestiario, como Neemon, Hyemon u Otamamon (Red); su ficha lo indica en *Notas*), el jugador elige con el DJ un Bebé II de la misma familia o de aspecto parecido, o usa la ficha genérica de Bebé II (10 PV, d4, técnica básica de su familia).
- Elige un **Campeón probable** de su lista *next*. Es solo una intención: la primera digievolución se decide en la escena (5.6).

**Novatos recomendados** (cifras del bestiario generado con `spec_fichas.json` 1.1; «rol» = el del bestiario, que el jugador puede cambiar). **Frágil** = 21 PV o menos y Def +1: aguanta poco hasta que digievoluciona; conviene que juegue a distancia o detrás de un Tanque.

| Novato | Bebé II | Familia | Rol | Atrib. | PV | Atq | Def | Ini | Firma | Por qué elegirlo |
|---|---|---|---|---|---|---|---|---|---|---|
| Agumon | Koromon | Saurio | Bruto | Vacuna | 27 | +2 | +2 | +1 | Pepper Breath (Fuego) | El clásico: duro, pega fuerte y su línea llega a WarGreymon. |
| Gabumon | Tsunomon | Saurio | Bruto | Datos | 30 | +2 | +1 | +2 | Blue Blaster (Fuego) | El más resistente de los Novatos; línea de lobos y hielo. |
| Biyomon | Yokomon | Ave | Tirador | Vacuna | 21 | +2 | +1 | +2 | Spiral Twister (Fuego, Larga) | **Frágil.** Vuela y dispara desde lejos. |
| Tentomon | Motimon | Naturaleza | Tirador | Vacuna | 21 | +2 | +1 | +2 | Super Shocker (Eléctrico, Larga) | **Frágil.** Paraliza a distancia y vuela. |
| Palmon | Tanemon | Naturaleza | Místico | Datos | 21 | +1 | +1 | +2 | Poison Ivy (Planta) | **Frágil.** Atrapa y envenena: ideal para quien disfruta del control. |
| Gomamon | Bukamon | Acuático | Tanque | Vacuna | 24 | +1 | +3 | +0 | Marching Fishes (Agua, Zona) | Muralla del grupo; invoca bancos de peces. |
| Patamon | Tokomon | Bestia | Ágil | Datos | 21 | +1 | +2 | +4 | Air Shot (Viento) | Rápido y escurridizo; línea sagrada. |
| Salamon | Nyaromon | Bestia | Ágil | Vacuna | 18 | +1 | +3 | +3 | Puppy Howl (Mental) | Defensa muy alta; línea de ángeles. |
| Veemon | DemiVeemon | Dragón | Bruto | Libre | 27 | +2 | +1 | +1 | Boom Boom Punch (Toque) | Puñetazos y Digi-Huevos (Armadura [O]). |
| Hawkmon | Poromon | Ave | Ágil | Libre | 21 | +1 | +2 | +3 | Pecking Beak (Toque) | Vuela; buen candidato a Armadura y DNA [O]. |
| Armadillomon | Upamon | Bestia | Ágil | Libre | 21 | +1 | +2 | +3 | Scratch Beat (Toque) | Fácil de llevar; buenas formas Armadura [O]. |
| Wormmon | Minomon | Naturaleza | Místico | Libre | 21 | +1 | +1 | +1 | Sticky Net (Planta) | **Frágil.** Atrapa y ciega; el amigo leal por excelencia. |
| Guilmon | Gigimon | Saurio | Bruto | Virus | 27 | +3 | +1 | +1 | Rock Breaker (Toque) | El mayor Ataque de los Novatos; rompe armaduras. |
| Terriermon | Gummymon | Bestia | Tirador | Vacuna | 21 | +2 | +1 | +2 | Terrier Tornado (Viento, Larga) | **Frágil.** Desplaza enemigos desde lejos; línea de artillería. |
| Renamon | Viximon | Bestia | Ágil | Datos | 21 | +1 | +2 | +4 | Diamond Storm (Tierra, Ráfaga) | Golpea a dos objetivos (3d6 a uno solo, 2d6 a cada uno de dos) y se oculta con Kohenkyo. |
| Impmon | Yaamon | Oscuro | Acechador | Virus | 18 | +3 | +1 | +3 | Summon (Oscuridad) | **Frágil.** Remata a los debilitados; arco de redención. |
| Lalamon | Budmon | Naturaleza | Apoyo | Datos | 24 | +0 | +1 | +2 | Seed Blast (Planta) | Canta (Sing a Song duerme a un rival) y apoya al grupo. |
| Falcomon | Pinamon | Ave | Bruto | Vacuna | 24 | +2 | +2 | +1 | Scratch Smash (Toque) | Ave luchadora y ninja. |
| Kotemon | Kapurimon | Saurio | Bruto | Datos | 30 | +2 | +1 | +2 | Thunder Kote (Eléctrico) | Espadachín duro de roer. |
| Lunamon | Moonmon | Bestia | Ágil | Datos | 21 | +1 | +2 | +4 | Luna Claw (Cósmico, Toque) | Pareja ideal con Coronamon; ruta al Olimpo XII. |
| Coronamon | Sunmon | Bestia | Bruto | Vacuna | 24 | +2 | +2 | +1 | Corona-Knuckles (Fuego, Toque) | Pareja ideal con Lunamon; puños de fuego que aturden. |
| Gotsumon | Motimon | Elemental | Bruto | Datos | 27 | +2 | +1 | +2 | Rock Fist (Tierra) | Resiste la Tierra y es inmune a Derribar; tozudo y entrañable. |
| Betamon | Bukamon | Acuático | Tanque | Virus | 24 | +2 | +2 | +0 | Electric Shock (Eléctrico) | Anfibio resistente con descargas. |

*(Los redactores deben comprobar cada Bebé II en la lista* prev *del bestiario: cuando un Novato tenga varias, el jugador elige. En la ficha, el nombre de la técnica de Coronamon se imprime «Corona-Knuckles»: el dato original lleva un carácter de media anchura, «CoronaｰKnuckles», que se conserva en* `nombre_dato`*.)*

### 4.3 Línea evolutiva
- Cada nivel nuevo se elige de la lista *next* de la forma actual (o de otra, si el DJ lo justifica con la historia).
- Las formas alcanzadas quedan **desbloqueadas**. Se pueden tener varias ramas (Greymon y, en una noche de rabia, SkullGreymon).
- El avance **Rama alternativa** (17.4) desbloquea otra forma del mismo nivel sin repetir el detonante.
- Cambiar de forma dentro del mismo nivel fuera de combate es gratis. En combate, cuesta lo mismo que digievolucionar a ese nivel (0 si el nivel es estable). En ambos casos **conserva el daño**: PV = PV máximos de la nueva forma − daño acumulado, como el Modo alterno (20.4).

### 4.4 Personalidad (d12)
Una vez por sesión, cuando la personalidad del compañero cause un problema real, **su Tamer gana 1 Chispa**.

| d12 | Rasgo | d12 | Rasgo |
|---|---|---|---|
| 1 | Glotón | 7 | Leal hasta el extremo |
| 2 | Valiente e impulsivo | 8 | Bromista |
| 3 | Miedoso | 9 | Serio y responsable |
| 4 | Orgulloso | 10 | Cariñoso y pegajoso |
| 5 | Curioso | 11 | Perezoso |
| 6 | Gruñón | 12 | Tímido |

### 4.5 Comer
Los Digimon comen muchísimo. Cada día, el compañero necesita **1 comida** (Carne digital, ración, fruta de datos o una comida en una aldea). Si no come, empieza el día **Hambriento** (7.3). Digievolucionar temporalmente también da hambre (5.7).

### 4.6 Cómo crece el compañero
- **Nivel de forma:** con Chispa sube temporalmente de nivel (cap. 5); con el Vínculo, esos niveles se vuelven estables (5.9). Cada nivel cambia su dado de poder (d6 → d8 → d10 → d12), su rango (+1 a Atq, Def e Ini) y sus PV (VF × 7 más modificadores).
- **Avances del compañero** (17.4) en los niveles de Tamer 3, 5, 7, 9 y 10: Atq, Def, PV, Ini, técnicas heredadas, perfeccionadas o nuevas, afinidades y ramas alternativas. Se aplican a todas sus formas.
- **Rol fijado:** mantiene el mismo estilo de combate en toda la línea, para que el crecimiento sea continuo.
- **Lo que no cambia nunca:** su personalidad, su forma Bebé II y su historia con el Tamer.

---

## 5. Chispa, Vínculo y digievolución [N]

### 5.1 La Chispa
La Chispa es la emoción del Tamer que fluye por el Digivice. Se anota con fichas o con marcas. **Máximo = 3 + Vínculo.** Al empezar cada sesión, si tienes menos que tu Vínculo, sube hasta tu Vínculo.

**Cómo se gana**

| Disparador | Chispa | Límite |
|---|---|---|
| **Fallo dramático:** cualquier 6– del Tamer o de su compañero en una situación de tensión (la iniciativa no cuenta) | +1 | 1 por asalto en combate; 1 por escena fuera de combate |
| **Resonancia:** el Dado de Vínculo saca un 6 (desde Vínculo 4, un 5 o un 6) | +1 | 1 por asalto |
| **Crisis:** el compañero baja por primera vez en el combate a la mitad de sus PV o menos (en cualquier forma), el Tamer pierde Aguante por primera vez en el combate o el DJ telegrafía un ataque contra el Tamer | +1 | 1 por combate |
| **Emblema:** el Tamer actúa según la virtud de su Emblema asumiendo un riesgo o un coste real | +1 | 1 por escena |
| **Personalidad o defecto:** la personalidad del compañero o el defecto del Tamer causan un problema real | +1 | 1 por sesión cada uno |
| **Animar** con éxito (opción del menú) | +1 | 1 por combate |
| **Furia de un Jefe** (19.4) | +1 a cada Tamer | — |
| **Premio del DJ** por un momento épico del grupo | +1 | a discreción |

**En qué se gasta**

| Uso | Coste |
|---|---|
| **Digievolucionar** | **2 por cada nivel por encima del nivel estable** (+1 si está Hambriento) |
| Digievolución de emergencia (5.8) | coste normal +1 |
| Segundo aliento: digievolucionar estando Agotado | coste normal +2 |
| **Esfuerzo:** +1 a una tirada ya hecha, antes de que el DJ narre el resultado | 1 (máx. +2 por tirada; cuenta para el límite de +3) |
| **Último aliento:** el compañero iba a quedar Derrotado; se queda a 1 PV | 2 (1 por combate) |
| **Ataque conjunto** (6.10) | 1 cada Tamer |
| Resonancia del Emblema (nivel 5 y Vínculo 3+, cap. 16) | 2 (1 por sesión) |
| Recuperar la forma estable tras una derrota o una regresión, en una escena tranquila (o al empezar un combate, si está en regresión, 5.7) | 1 |
| Armadura, DNA, Modos y Espíritus [O] | ver cap. 20 |

La tensión es deliberada: *¿gasto la Chispa en empujar esta tirada o la guardo para digievolucionar?*

### 5.2 El Vínculo
El Vínculo (1–5, y ★) mide la confianza entre Tamer y compañero. **Sube cuando el Tamer alcanza el nivel indicado *y* la pareja vive un Momento de Vínculo** (5.11). Si llegas al nivel sin el momento, el Vínculo espera.

| Vínculo | Nivel de Tamer | Nivel **estable** | Nivel **máximo** (temporal) | Chispa máx. | Resonancia |
|---|---|---|---|---|---|
| 1 | 1–2 | Novato | Campeón | 4 | 6 |
| 2 | 3–4 | Novato | Perfecto | 5 | 6 |
| 3 | 5–6 | Campeón | Perfecto | 6 | 6 |
| 4 | 7–8 | Campeón | Definitivo | 7 | 5–6 |
| 5 | 9–10 | Perfecto | Definitivo | 8 | 5–6 |
| ★ | 10 + arco del Emblema cerrado | Definitivo | Modo Supremo [O] | 9 | 5–6 |

**Coste = 2 Chispa por nivel por encima del estable.** Vínculo 1: Campeón = 2. Vínculo 2: Campeón = 2 y Perfecto = 4 en total (de golpe o en dos pasos de 2). Vínculo 4 (estable Campeón): Perfecto = 2 y Definitivo = 4. Ir a una forma de nivel igual o inferior al estable es gratis, pero **no restaura PV** (5.4), **salvo que el compañero esté Derrotado o en regresión a Bebé II**: entonces solo vuelve a su forma estable con un descanso (corto con comida para la regresión, largo para la derrota) o pagando 1 Chispa (5.1).

### 5.3 El Dado de Vínculo y la Resonancia
- **Una vez por asalto**, sin gastar su acción y aunque no sea su turno, el Tamer (consciente y como mucho a 1 zona de su compañero) puede añadir el **Dado de Vínculo (DV)**, un d6 de otro color, a una tirada de **ataque o de Defensa** de su compañero: **tira 3d6 y quédate con los 2 mejores** (es una Ventaja).
- Si la tirada ya tenía Ventaja, el DV da **+1** en su lugar (cuenta para el límite de +3). Si tenía Desventaja, ambas se anulan: tira 2d6 normales y el DV aparte, solo para la Resonancia.
- **Resonancia:** si el DV saca un **6** (desde Vínculo 4, un 5 o un 6), el Tamer gana **1 Chispa** (máximo 1 por asalto). *«¡El Digivice brilla!»*
- Fuera de combate, una vez por escena, el DV puede darse a una tirada del compañero o a una tirada conjunta de la pareja. Solo da Chispa si la escena es de tensión.

### 5.4 Cómo se digievoluciona
- **Cuándo:** acción gratuita del Tamer, **una vez por asalto**, al comienzo del turno de la pareja (o en cualquier momento dramático fuera de combate). El Tamer debe estar consciente y como mucho a 1 zona de su compañero.
- **Saltos («warp»):** se pueden saltar niveles en una sola digievolución pagando la suma.
- **Límite:** nunca por encima del nivel máximo de tu Vínculo, salvo con la digievolución forzada (5.10) o con objetos de trama.
- **Forma de partida:** la forma desde la que digievoluciona el compañero. Normalmente es la estable, pero puede ser una inferior (con Vínculo 3 puede ir por ahí como Agumon y digievolucionar desde Agumon).
- **Efectos:**
  1. El compañero adopta la **ficha del bestiario** de la nueva forma (con su rol fijado y sus avances).
  2. **PV al máximo** de la nueva forma y su Firma lista. Solo lo consigue una digievolución **pagada con Chispa** a un nivel superior al estable, y como mucho **una vez por forma y escena**: si vuelve a una forma que ya usó en esta escena, entra con los PV que tenía al dejarla (y si esa forma cayó a 0, ver *Segundo aliento*, 5.5).
  3. **Se eliminan todos sus estados**, salvo Hambriento.
  4. Se **guardan los PV** que tenía la forma de partida. Si sube de una forma temporal a otra superior, solo paga los niveles nuevos y los PV guardados siguen siendo los de la forma de partida original.
- **Formas iguales o inferiores a la estable:** cambiar a ellas es gratis, pero **conserva el daño** (PV = PV máximos de la nueva forma − daño acumulado), igual que el Modo alterno. Así no hay bucles de curación gratis.
- **Duración:** hasta el final de la escena, hasta que el Tamer la deshaga (gratis: vuelve a la forma de partida con los PV guardados) o hasta que la forma caiga a 0 PV.

### 5.5 Capas de forma, regresión y Agotado
- **Fin normal** (fin de escena o voluntario): vuelve a la **forma de partida** con los PV guardados, sin penalización (pero queda Hambriento, 5.7).
- **Fin por 0 PV:** vuelve **directamente a la forma de partida** con los PV guardados y queda **Agotado**: −1 a todas sus tiradas y no puede digievolucionar en esta escena salvo con *Segundo aliento* (+2 Chispa). Agotado se elimina con un descanso corto. El daño sobrante del impacto que tumbó la forma temporal se pierde (salvo en la emergencia, 5.8).
- **Segundo aliento: volver a una forma ya usada no cura del todo:** si vuelve a una forma que ya cayó a 0 en esta escena, entra con **la mitad** de sus PV máximos (no con todos).
- **Forma estable:** el compañero puede pasar las escenas en cualquier forma igual o inferior a su nivel estable, sin coste (conservando el daño, 5.4). **Si la forma en la que está cae a 0 y no es una forma temporal, queda Derrotado** (6.12), sea cual sea su nivel: no hay una segunda cascada a un nivel menos. Así cada compañero tiene como mucho dos barras de PV: la forma temporal y la de partida.

### 5.6 La primera vez (detonantes)
La primera vez que un compañero alcanza un nivel, hace falta un detonante dramático **además** de la Chispa:
- **Campeón:** una **Crisis** (5.1) en esta escena.
- **Perfecto:** el **Emblema despierta**: en esta escena, el Tamer ha ganado Chispa por su Emblema.
- **Definitivo:** un **Momento de Vínculo** en la escena o una situación desesperada para todo el grupo.

El jugador elige la forma de la lista *next* (con el DJ) y queda **desbloqueada**: a partir de entonces basta con la Chispa. *La primera digievolución a Campeón no puede ocurrir en el asalto 1 antes de una Crisis: el Tamer empieza con 1 Chispa y necesita 2, y además el detonante. Desde Vínculo 2, en cambio, la Chispa inicial (= Vínculo) ya paga un nivel en el asalto 1: el presupuesto de encuentro lo tiene en cuenta (nivel de referencia, 19.2).*

### 5.7 Hambriento y regresión a Bebé
- **Hambriento:** al terminar una escena en la que usó una forma temporal, el compañero queda Hambriento (7.3): −1 a sus tiradas fuera de combate, y digievolucionar le cuesta +1 Chispa. Se elimina comiendo (1 Carne digital, una ración o una comida en una aldea). La Armadura [O] no da hambre.
- **Regresión a Bebé II («Koromon después de la batalla»):** si en la escena el compañero estuvo **2 o más niveles por encima de su nivel estable**, o hizo DNA [O], o una digievolución forzada u oscura, al terminar la escena vuelve a su **forma Bebé II** hasta un descanso corto con comida. Mientras tanto viaja en brazos de su Tamer. Si empieza un combate, el Tamer puede devolverlo a su forma estable como acción gratuita pagando **1 Chispa**.

### 5.8 Digievolución de emergencia
Cuando un impacto va a dejar a tu compañero a 0 PV, puedes digievolucionar **como reacción** (6.3) pagando el coste normal **+1 Chispa**, aunque no sea vuestro turno y aunque ya hayas digievolucionado en este asalto.
- La Chispa que gane tu Tamer con **ese mismo impacto** (el 6– en la Defensa, la Crisis) se gana **antes** de resolver el 0 PV y puede pagar la emergencia; ese impacto cuenta como la **Crisis** que hace de detonante del primer Campeón.
- El daño de ese impacto se aplica a la nueva forma, que entra con sus PV completos (y con el golpe aguantado, 6.8). Si la nueva forma cae a 0 con ese mismo impacto, **el daño sobrante pasa a la forma de partida**, que queda Agotada (5.5).

### 5.9 Estabilización
Una forma es **estable** cuando su nivel es igual o inferior al nivel estable del Vínculo (5.2). En cuanto el Vínculo sube, las formas desbloqueadas de ese nivel pasan a ser estables: se usan sin Chispa, no dan hambre y su caída a 0 sigue la regla de forma estable (5.5). Con el Vínculo, la digievolución deja de ser un estallido para convertirse en el día a día de la pareja.

### 5.10 Digievolución forzada, sobrecarga y digievolución oscura [A]
Si quieres superar tu nivel máximo, digievolucionar con 1 o 2 Chispa menos de lo necesario, o si el **DJ declara** que el Tamer actúa movido por la ira, el odio o la desesperación, paga la Chispa que puedas y tira **2d6 + Vínculo**. Límites: **como mucho 1 nivel por encima del máximo** del Vínculo y hay que pagar **al menos la mitad del coste** (redondeando hacia arriba).
- **10+ (sobrecarga controlada):** lo consigues durante **2 asaltos**; después, la forma termina como si hubiera caído a 0 (Agotado). Al terminar la escena, regresión a Bebé II.
- **7–9 (descontrol):** lo consigues, pero el compañero queda **Descontrolado** (7.3): actúa en la fase enemiga y el DJ elige sus objetivos (pueden ser aliados). El Tamer lo recupera con *Animar* (10+).
- **6– (digievolución oscura):** el compañero adopta una **forma oscura** de su línea (SkullGreymon, Megidramon, ChaosGallantmon, BlackWarGreymon…, con la plantilla *Modo Oscuro* si es un modo). La controla el DJ hasta que caiga a 0 PV o el Tamer la calme con *Animar* 10+. Después queda Derrotado (Bebé II) y el Tamer gana 1 punto de Corrupción [O] si se usa ese módulo.

### 5.11 Momentos de Vínculo
Escenas en las que Tamer y compañero se enfrentan juntos a algo que pone a prueba su relación: un sacrificio, una reconciliación tras una pelea, superar el miedo del otro, un secreto compartido. Los propone el jugador o el DJ; como referencia, uno cada dos sesiones. Permiten subir el Vínculo (5.2), cuentan como detonante del Definitivo y dan 1 XP (17.1).

### 5.12 Resumen de variantes de digievolución
| Variante | Dónde | Núcleo / módulo |
|---|---|---|
| Normal (Bebé → Novato → Campeón → Perfecto → Definitivo), saltos y emergencia | 5.4–5.8 | [N] |
| Forzada, sobrecarga y oscura | 5.10 | [A] |
| Armadura (Digi-Huevos) | 20.1 | [O] |
| Espíritus (Híbridos) | 20.2 | [O] |
| DNA / Jogress | 20.3 | [O] |
| Modos (alternativos, supremos y oscuros) | 20.4 | [O] |
| X-Antibody | 20.5 | [O] |
| Bloqueos (Agujas de Control, Torres Oscuras, Sellado) | 20.8 | [O] |

---

## 6. Combate [N]

### 6.1 Zonas
El DJ describe el escenario en **3 a 6 zonas** con nombre y, a veces, un rasgo («Claro», «Río —agua—», «Acantilado —altura—», «Ruinas —cobertura—»).
- **Mapa:** dibuja las zonas como recuadros unidos por líneas. **Adyacente** = unida por una línea. Si no se dice otra cosa, las zonas van en fila (cada una es adyacente a la anterior y a la siguiente).
- **Misma zona:** todos pueden alcanzarse con técnicas de *Toque*.
- **Trabado:** si en tu zona hay un enemigo que te atacó con Toque (o al que atacaste con Toque), estáis trabados. Usar una técnica de Distancia o Larga estando trabado: **−1**. Salir de la zona estando trabado provoca un **ataque de retirada** (P1 gratuito del enemigo, al que respondes con tu Defensa), salvo que uses la acción *Retirarse*.
- **Rasgos de zona:** *Cobertura* (+1 Def contra Distancia y Larga) · *Altura* (+1 al atacar a quien está debajo) · *Agua* (los Acuáticos ganan su rasgo; los objetivos en ella cuentan como Empapados para los combos [A]) · *Terreno difícil* (moverse por ella cuesta la acción, salvo a quien vuela) · *Peligro* (VF del causante o 2 de daño al entrar o al empezar el turno en ella; a los Tamers, 1 Aguante) · *Oscuridad* (−1 a Distancia y Larga; nadie puede usar Larga) · *Estrecha* (no caben Digimon de nivel Perfecto o superior salvo que vuelen o sean pequeños; lo decide el DJ).
- **Vuelo:** quien vuela ignora el Terreno difícil y las técnicas de Toque de quien no vuela tienen −2 contra él, salvo que estén trabados. Un Derribado que volaba cae a tierra.
- **Opción de casillas** [O]: ver 20.10.

### 6.2 Iniciativa por fases
Al empezar el combate, cada jugador tira por su pareja **2d6 + Ini de su compañero − Ini del enemigo más rápido**.
- **10+:** fase rápida y **+1 a su primera tirada** del combate.
- **7–9:** fase rápida.
- **6–:** fase lenta (esta tirada no da Chispa).

**Orden del asalto (se repite igual cada asalto):**
1. **Inicio del asalto:** efectos de «al empezar el asalto» (Dominios, regeneración, 3.ª acción de un Jefe).
2. **Fase rápida:** las parejas que ganaron la iniciativa, en el orden que prefieran.
3. **Fase enemiga:** todos los PNJ, en el orden que elija el DJ (1.ª acción de los Jefes).
4. **Fase lenta:** el resto de parejas.
5. **Final del asalto:** 2.ª acción de los Jefes; terminan los efectos «hasta el final del asalto».

**Sorpresa:** si los PNJ son sorprendidos, no actúan en el primer asalto. Si lo son los PJ, todos van a la fase lenta en el primer asalto y tienen −1 a la Defensa durante ese asalto. Un estado *Ralentizado* manda a un PJ a la fase lenta y a un PNJ al final de la fase enemiga.

### 6.3 El turno de la pareja
En su fase, cada pareja tiene:
- **Tamer:** 1 *acción de Tamer* + moverse 1 zona.
- **Digimon:** 1 *acción* + moverse 1 zona (antes o después de la acción).
- **Gratis:** hablar, gritar ánimos, **digievolucionar** (una vez por asalto, 5.4), usar el **Dado de Vínculo** (una vez por asalto, 5.3), soltar un objeto.
- Para dar Órdenes, usar programas o el Dado de Vínculo, **el Tamer debe estar como mucho a 1 zona de su compañero** (alcance del Digivice).
- **Reacción:** efecto que se usa fuera de tu turno en respuesta a un hecho: la digievolución de emergencia (5.8), el Instinto protector (6.11), el rasgo *Guardián* (12.1), el talento *Cortafuegos personal* (17.3), la de una Élite (19.1). Cada Digimon y cada Tamer tiene **1 reacción por asalto**, salvo que el texto diga otra cosa. Un Digimon Paralizado, Dormido o Aturdido no puede reaccionar (su Tamer sí); un Tamer Dormido, Aturdido o a 0 Aguante, tampoco.

### 6.4 Acciones del Digimon
| Acción | Efecto |
|---|---|
| **Técnica** | Usa una técnica (de ataque o de apoyo). **Agotadora** afecta al Digimon: tras usar una técnica Agotadora (P3, P2/P3 usada como P3, técnica de apoyo con Curar o Escudo, maniobra Pulso restaurador), en su siguiente turno no puede usar **ninguna** técnica Agotadora. |
| **Defender** | Hasta tu próximo turno, +2 a tus tiradas de Defensa. Si lo hace un PNJ, −2 a los ataques contra él. |
| **Proteger** | Elige un aliado (o un Tamer) de tu zona. Hasta tu próximo turno, los ataques individuales contra él te tienen a ti como objetivo, con +1 Def contra ellos. |
| **Cargar** | Prepara una técnica con *Cargado* (11.4). |
| **Correr** | Muévete 1 zona más (2 en total). |
| **Maniobra** | Algo creativo sin técnica: empujar, agarrar, derribar, usar el entorno, liberar a un aliado. Tirada 2d6 + Atq − Def: **10+** aplicas un estado simple (Derribar, Empujar, Atrapar o Marcar); **7–9** lo aplicas, pero quedas Expuesto; **6–** fallas. |
| **Maniobra de rol** | La técnica genérica de su rol (12.2): siempre disponible. |
| **Retirarse** | Sales de una zona en la que estás trabado sin provocar ataque de retirada. |

### 6.5 Acciones del Tamer
| Acción | Tirada | Efecto |
|---|---|---|
| **Orden** | No | +1 a la próxima tirada de tu compañero en este asalto (ataque o Defensa). Una **Orden especial** (de talento) **sustituye** a ese +1, salvo que diga lo contrario; no se puede dar la **misma** Orden especial dos asaltos seguidos. Una sola Orden por asalto (salvo *Doble orden*). |
| **Orden táctica** [A] | AST + Táctica | **10+:** +2 a la próxima tirada del compañero, que además puede moverse 1 zona extra. **7–9:** +1. **6–:** nada, y el enemigo se fija en ti (ataque telegrafiado contra tu Tamer). |
| **Usar un programa** | Normalmente no | Gasta Carga y aplica el efecto (cap. 13). |
| **Usar un objeto** | No | Discos, chips… (cap. 14). Sobre tu compañero, si está en tu zona o en una adyacente. |
| **Analizar** | AST + Saber Digital | **10+:** conoces la ficha entera del objetivo (PV actuales, Atq, Def, debilidades, rasgos, punto débil si es Jefe) y los aliados tienen +1 en su próximo ataque contra él. **7–9:** su nivel, atributo, una debilidad y sus PV aproximados. **6–:** dato incompleto o confuso. |
| **Animar** | COR + Empatía | **10+** elige dos; **7–9** elige uno: el compañero se libra de un estado mental (Asustado, Confundido, Encantado, Dormido; Descontrolado y forma oscura, solo con 10+) / su Firma queda lista aunque la usara en su turno anterior / ganas 1 Chispa (1 por combate). |
| **Ponerse a cubierto** | No | Tu Tamer tiene +2 a su Defensa hasta tu próximo turno y deja de estar Expuesto. |
| **Actuar en el entorno** | Según la habilidad | Rescatar a alguien, hackear una puerta, avanzar un reloj de objetivo de escena, cortar una cuerda, encender una luz… |

### 6.6 Atacar
1. Declara la técnica y el objetivo (u objetivos) dentro de su alcance.
2. **El DJ anuncia el modificador neto** (Atq − Def del objetivo ± triángulo ± estados del PNJ por la regla de espejo); el jugador no necesita conocer la ficha del enemigo. Tira **2d6 + ese modificador** + sus situacionales (Orden, Certero, Dado de Vínculo…). *Analizar* sigue siendo útil: revela PV, debilidades, rasgos y punto débil.
   - Si la técnica afecta a varios objetivos, **tira una sola vez** y compara el resultado con cada uno (el DJ dice la franja de cada uno).
3. Resultado:
   - **10+ — Impacto total:** daño completo y **todos los efectos** de la técnica.
   - **7–9 — Impacto:** daño completo, pero **sin estados** (los efectos de daño, como Perforante o Drenar, sí se aplican). *Alternativa:* puedes cambiar todo el daño por aplicar el estado, salvo que sea de control duro (Aturdir, Dormir, Regresión).
   - **6– — Fallo:** no hay daño. El DJ hace una jugada (lo habitual: el compañero queda **Expuesto**) y tu Tamer gana 1 Chispa (fallo dramático; como mucho 1 por asalto).

### 6.7 Defenderse (cuando un PNJ te ataca)
El DJ declara la técnica y el objetivo, y anuncia el modificador neto. El jugador cuyo compañero es atacado tira **2d6 + Def − Atq del atacante** + modificadores (incluidos los del PNJ con el signo cambiado, 2.1).
- **10+ — Lo evitas:** sin daño ni efectos.
- **7–9 — Lo mitigas:** recibes **la mitad del daño** (redondeo hacia abajo) y ningún estado (salvo que el atacante tenga el **rol** Místico: entonces sufres los estados que no son de control duro).
- **6– — Te alcanza:** daño completo y todos los efectos. Tu Tamer gana 1 Chispa (como mucho 1 por asalto).

**Áreas de un PNJ:** contra una técnica de área, **cada PJ afectado tira su propia Defensa** (y cada uno puede usar su Dado de Vínculo). El DJ tira el daño **una vez** y lo aplica a cada uno según su resultado (mitad con 7–9; nada con 10+).

*PNJ contra PNJ* (un aliado del DJ contra un enemigo): el DJ tira el ataque como si fuera un PJ; el defensor no tira.

### 6.8 Daño (orden de cálculo)
1. **Dados:** tantos dados de poder (del atacante) como la potencia de la técnica (P1 = 1, P2 = 2, P3 = 3).
2. **Más dados:** +1 por cada uno de estos: *Debilidad* del objetivo al elemento · *Brutal* con 10+ · crítico · *Potenciado+* (Mejora P2 o P3) o programa Potencia · el atacante es de **rango superior** al objetivo (no se acumula por más rangos) · Legendario (plantilla) · *Cargado* · *Retroceso* · Furia de un Jefe · rasgos que lo indiquen.
3. **Menos dados:** −1 si la técnica es de área (Ráfaga, Zona o Total) **y alcanza de verdad a 2 o más objetivos**; contra uno solo cuenta como Individual. Mínimo 1 dado.
4. **Suma** los dados y los modificadores fijos.
5. **Resta la Arm** del objetivo (salvo *Perforante*).
6. **Divide a la mitad** por cada uno: el defensor sacó 7–9 · el objetivo *Resiste* el elemento (salvo Perforante) · **por cada rango** que el objetivo esté por encima del atacante. Redondeo hacia abajo cada vez.
7. **Mínimo 1** si hubo impacto.
8. **Golpe aguantado:** un solo impacto de un PNJ **no puede quitar a un compañero más de la mitad de sus PV máximos** (redondeo hacia arriba). Ningún compañero cae de un solo golpe desde PV máximos.
9. Los **Escudos** absorben el daño antes que los PV.

**Daño fijo opcional** (para DJ que no quieran tirar daño): cada dado vale su **VF** (la mitad de sus caras: d4 = 2, d6 = 3, d8 = 4, d10 = 5, d12 = 6) y **VF + 1** en un 10+ del atacante o en un 6– del defensor. **Es la regla por defecto para esbirros y pelotones.**

*Escala épica:* la escala compara el **rango** de la fila que usa cada ficha (Bebé 0, Novato 1, Campeón 2, Perfecto 3, Definitivo 4; una forma Armadura tiene rango 2, Rapidmon (Armadura) 3, Magnamon y NEO 4; un Híbrido, el de su clase). Un Novato que golpea a un Campeón hace la mitad de daño; a un Definitivo, la octava parte. Un Definitivo que golpea a un Novato suma 1 dado. Por eso digievolucionar cambia el combate de golpe.

### 6.9 PV, Arm y Escudo
- **PV:** al llegar a 0, la forma cae (6.12 y 5.5).
- **Arm (armadura plana):** se resta a cada impacto. Máximo 2 en la ficha; con programas o chips, 3 como mucho. *(En todo el libro, la estadística se llama siempre «Arm»; «Armadura» es el nivel de los Digi-Huevos, 20.1.)*
- **Escudo:** PV temporales que se pierden primero; no se acumulan (se queda el mayor) y desaparecen al final de la escena.
- **Curación:** nunca por encima de los PV máximos de la forma actual.

### 6.10 Ataque conjunto [A]
El gran momento de equipo del anime.
- **Requisitos:** dos parejas; cada Tamer paga **1 Chispa**. Al empezar el turno de una pareja, otra que aún no haya actuado en este asalto se une (actúa ahora).
- Los dos compañeros gastan su acción en **una técnica combinada** (una técnica de cada uno, P3 incluidas si están listas) contra un objetivo al alcance de ambos.
- **Una sola tirada** con el mejor Atq de los dos, **+1** (situacional). Solo uno de los dos Tamers puede usar su Dado de Vínculo.
- **Daño:** la suma de los dados de ambas técnicas (cada una con su dado de poder); Armadura y Resistencias se aplican **una sola vez** al total. Se aplican las palabras clave de las dos (las áreas incluidas, a elección de los jugadores).
- Los dos Tamers conservan sus acciones. Un Ataque conjunto con éxito cuenta como detonante del DNA [O] la primera vez.

### 6.11 Los Tamers en combate
- Los Tamers **no hacen daño a los Digimon** (salvo con programas, objetos u opciones concretas).
- **Un PNJ solo ataca a un Tamer si:** (a) el DJ lo **telegrafió** en el asalto anterior («Devimon mira a Sora…») o es una jugada dura tras un 6– del propio Tamer; (b) el Tamer está **Expuesto** y en la zona del atacante; o (c) es una técnica de Zona o Total y el atacante elige incluir a **cualquier Tamer de esa zona**. **Como mucho un ataque contra cada Tamer por asalto.**
- **Cómo queda Expuesto un Tamer:** (a) termina su turno en una zona en la que hay un enemigo sin estar *a cubierto* (acción *Ponerse a cubierto* o rasgo de zona Cobertura); (b) saca 6– en una acción de Tamer durante un combate; o (c) lo decide una jugada del DJ. Expuesto dura hasta el final de su próximo turno (7.3).
- **Defensa del Tamer:** 2d6 + DES + Atletismo − Atq del atacante.
- **Peligro (pérdida de Aguante)** = **max(1, rango del atacante)**: Bebé y Novato **1**, Campeón **2**, Perfecto **3**, Definitivo **4**; **+1** si es una técnica P3. Con 7–9 en la Defensa, la mitad (mínimo 1); con 10+, nada.
- **Instinto protector:** reacción gratuita, una vez por asalto: si el compañero está en la zona de su Tamer y no está trabado, puede **interponerse**: el ataque le apunta a él en lugar de a su Tamer.
- **Estados en los Tamers** (cuando un área o una jugada dura se los aplica):

| Estado | Efecto en un Tamer |
|---|---|
| Quemar, Veneno, daño de una invocación | 1 Aguante al inicio de su turno (en lugar de VF PV), mientras dure |
| Congelar, Atrapar, Paralizar | No puede moverse |
| Dormir, Aturdir | Pierde su acción de Tamer y no puede usar el Dado de Vínculo |
| Cegar | −2 a su Defensa y no puede Analizar |
| Asustar, Confundir, Encantar | No puede dar Órdenes |
| Cualquier otro | No afecta a los Tamers |
- **Peligros del entorno** (caer, quemarse, una avalancha): Leve 1, Serio 2, Grave 3, Mortal 5 de Aguante.
- **Aguante 0:** el Tamer queda **fuera de combate** (inconsciente o incapaz de seguir): no tiene acciones de Tamer ni Dado de Vínculo. **El jugador sigue jugando con su compañero**, que gana una Crisis (1 Chispa para su Tamer, utilizable cuando despierte) y puede usar Proteger sobre su Tamer como acción gratuita una vez. Otro Tamer puede reanimarlo con una acción (COR o AST + Medicina, 7+): vuelve con 1 Aguante. Al terminar la escena, todo Tamer a 0 recupera 1 Aguante y queda **Herido** (−1 a las tiradas físicas) hasta un descanso largo. *Tono:* en Digimon, los Tamers no mueren salvo que la mesa lo pacte para un momento muy concreto.

### 6.12 Derrota
- **Forma temporal a 0 PV:** vuelve a su forma de partida con sus PV guardados y queda Agotado (5.5).
- **Cualquier otra forma a 0 PV** (la estable o una inferior, de cualquier nivel): queda **Derrotado**: vuelve a su forma Bebé II, inconsciente, y no puede actuar el resto del combate. Tras el combate despierta como Bebé II; vuelve a su forma estable con un descanso largo o gastando 1 Chispa en una escena tranquila. No hay cascada de un nivel en un nivel.
- **PNJ a 0 PV:** su cuerpo se deshace en datos y normalmente deja un **Digi-Huevo** que renacerá en la Ciudad del Comienzo. Los esbirros pueden simplemente huir.
- **Rendición:** los PNJ estándar suelen huir o rendirse al quedar a ¼ de sus PV si su líder ha caído (lo decide el DJ).
- *Módulo de Borrado* [O] (20.12): muerte permanente.

### 6.13 Huida
Si el grupo quiere escapar, cada pareja tira **2d6 + Ini de su compañero − Ini del perseguidor más rápido** (o DES + Atletismo − rango del perseguidor más rápido, si el Tamer huye a pie y solo):
- **10+:** escapa limpiamente.
- **7–9:** escapa, pero paga un coste (recibe un ataque P1, deja algo atrás o se separa del grupo).
- **6–:** no escapa; pasa a una persecución (18.4) o sigue el combate en mala posición.
Quien vuela, en terreno abierto, tiene Ventaja. *El DJ debe ofrecer siempre la huida cuando el encuentro supera el presupuesto Épico.*

### 6.14 Recuperación
- **Descanso corto** (una comida o una hora tranquila): los compañeros recuperan **la mitad de sus PV máximos**; los Tamers recuperan 2 Aguante y 2 Carga; se eliminan *Agotado* y, si hay comida, *Hambriento* y la regresión a Bebé II.
- **Descanso largo** (una noche en lugar seguro): todo al máximo; los Derrotados vuelven a su forma estable.
- **Curación fuera de combate:** las técnicas con Curar y los objetos funcionan igual.

### 6.15 Rutina de los PNJ (para aligerar al DJ)
- Un PNJ usa su **Firma en su primer turno** si la tiene lista y vuelve a usarla en cuanto puede (cada dos turnos, porque es Agotadora; un Jefe, en asaltos alternos, 19.4). En los turnos intermedios, su técnica P2 o su maniobra de rol.
- Los esbirros y los pelotones usan **daño fijo**. Para los demás, el DJ puede tirar daño o usar daño fijo.
- **Consejos de mesa:** telegrafía los golpes que pueden dejar fuera de combate a un compañero o a un Tamer; no encadenes dos estados de control (Aturdir, Dormir, Congelar, Atrapar) sobre la misma pareja en el mismo asalto; ofrece siempre una salida (huir, negociar, un objetivo de escena).

---

## 7. Estados alterados [N]

### 7.1 Reglas generales
- Un estado se aplica con un **10+ en el ataque del PJ** o con un **6– en la Defensa del PJ** (si lo aplica un PNJ). Si el atacante tiene el **rol** Místico (rasgo *Maestro de estados*), también con **7–9**, salvo los de control duro.
- **Duración «1 turno»** = hasta el final del **siguiente turno del afectado**. «2 turnos» = hasta el final de su segundo turno. Para un **Jefe o Legendario**, su turno es el asalto completo: sus estados avanzan una vez por asalto (al inicio de su 1.ª acción) y sus duraciones se cuentan en asaltos (19.4).
- El mismo estado **no se acumula**: si se vuelve a aplicar, se renueva la duración. **Invocaciones:** cada usuario mantiene como mucho una activa; crear otra disipa la anterior.
- **Digievolucionar elimina todos los estados** salvo Hambriento.
- **Control duro:** Aturdir, Dormir y Regresión. Nunca se aplican con 7–9. Los Jefes los sufren de forma limitada (19.4).
- **Daño por turno** (Quemar, Veneno, invocaciones): usa el **VF del causante**, se divide a la mitad por cada rango que el afectado supere al causante (mínimo 1) y a un Jefe se le aplica una vez por asalto.
- **Estados contra PNJ:** como el DJ no tira para impactar, los estados que modifican tiradas se traducen con la **regla de espejo** (2.1; tabla en 11.4). **Estados en Tamers:** 6.11.
- **Inmunidades** por familia, rol o plantilla: se indican en el rasgo correspondiente.

### 7.2 Estados de las palabras clave
Los 20 estados que aplican las técnicas (Quemar, Congelar, Paralizar, Veneno, Aturdir, Dormir, Cegar, Confundir, Asustar, Encantar, Sellar, Regresión, Ralentizar, Atrapar, Debilitar, Romper, Marcar, Derribar, Empujar y Provocar) tienen su regla exacta en el capítulo 11.4 (grupo *Estado*), junto con su traducción cuando los sufre un PNJ.

### 7.3 Otros estados y condiciones
| Estado | Regla | Termina |
|---|---|---|
| **Expuesto** | −1 Def: −1 a sus tiradas de Defensa si es un PJ; +1 a los ataques de los PJ contra él si es un PNJ (también un Jefe tras romperle la Guardia de carga). Un Tamer Expuesto puede ser atacado (6.11). | Al final de su próximo turno (un Jefe: al final del asalto siguiente), o al Ponerse a cubierto. |
| **Agotado** | −1 a todas sus tiradas; no puede digievolucionar en esta escena (salvo con Segundo aliento). *(No confundir con «Agotadora», la propiedad de las técnicas P3.)* | Descanso corto. |
| **Hambriento** | −1 a sus tiradas fuera de combate; digievolucionar cuesta +1 Chispa. No lo elimina la digievolución. | Al comer. |
| **Derrotado** | Inconsciente en forma Bebé II; no actúa el resto del combate. | Descanso largo, o 1 Chispa en una escena tranquila. |
| **Trabado** | −1 a Distancia y Larga; salir de la zona provoca un ataque de retirada. | Al salir de la zona o al caer el enemigo. |
| **Oculto** | No puede ser objetivo de técnicas de Distancia ni Larga; su primer ataque tiene +2. | Al atacar, o si lo revelan (Bengala, Analizar 10+). |
| **Potenciado** / **Potenciado+** | Potenciado (Mejora P1): +1 a la tirada de su próximo ataque. Potenciado+ (Mejora P2 o P3): además, +1 dado de daño. *El programa Potencia no aplica ningún estado: da +1 dado a la próxima técnica de este asalto y no lo eliminan Purificar ni Purgado.* | Tras ese ataque. |
| **Descontrolado** | Actúa en la fase enemiga; el DJ elige sus objetivos (pueden ser aliados). | Animar 10+, o al terminar la forma. |
| **Empapado** [A] | Condición para combos (20.9): está en una zona de Agua, bajo la lluvia o ha recibido una técnica de Agua este asalto. | Al salir del agua o al final del asalto. |
| **Herido** (Tamer) | −1 a las tiradas físicas del Tamer. | Descanso largo. |

---

## 8. Triángulo de atributos [N]

### 8.1 El triángulo
**Vacuna vence a Virus · Virus vence a Datos · Datos vence a Vacuna.**
- Si tu atributo vence al del rival: **+1 a tus tiradas contra él** (al atacar y al defenderte de él).
- Si el suyo vence al tuyo: **−1**.
- **Libre, Desconocido, SIN DATOS y Ninguno** son neutrales: ni dan ni reciben ventaja.
- **Variable** elige al empezar cada escena ser Vacuna, Datos o Virus.
- El triángulo es un modificador situacional (cuenta para el límite de ±3).

### 8.2 Modificadores por atributo (ya incluidos en la ficha)
| Atributo | En los datos | Vence a | Pierde contra | Modificadores | Rasgo |
|---|---|---|---|---|---|
| **Vacuna** | `Vaccine` | virus | datos | Def +1 | *Antivirus:* +1 Def (incluido). |
| **Datos** | `Data` | vacuna | virus | PV +VF, Ini +1 | *Procesamiento:* +1 Ini y +VF PV (incluidos). |
| **Virus** | `Virus` | datos | vacuna | Atq +1 | *Agresión:* +1 Atq (incluido). |
| **Libre** | `Free` | — (neutral) | — | PV +VF | *Libre:* Fuera del triángulo: no da ni recibe ventaja. +VF PV (incluido). |
| **Variable** | `Variable` | elige cada escena | elige cada escena | — | *Mutable:* Al empezar cada escena elige ser Vacuna, Datos o Virus: usa ese triángulo y ese modificador hasta el final de la escena (no incluido en la ficha). |
| **Desconocido** | `Unknown` | — (neutral) | — | Def +1 | *Ilegible:* Fuera del triángulo. +1 Def (incluido). Analizar contra él tiene −1. |
| **SIN DATOS** | `NO DATA` | — (neutral) | — | Def +1 | *Ilegible:* Fuera del triángulo. +1 Def (incluido). Analizar contra él tiene −1. |
| **Ninguno** | `None` | — (neutral) | — | — | — |

*«PV +VF» significa +1 al multiplicador de PV (la ficha suma un VF más). Los Bebés aplican los modificadores de atributo, pero no los de rol ni familia.*

---

## 9. Familias de tipos [N]

Los 140 tipos oficiales se agrupan en **14 familias**. La familia da al Digimon un **rasgo**, una **afinidad elemental** (el elemento por defecto de sus técnicas de distancia sin elemento claro), **debilidades y resistencias**, una **especialidad** (+1 a sus tiradas fuera de combate cuando encaje), los **roles más probables**, una **técnica básica** y, a veces, modificadores numéricos.

### 9.1 Las 14 familias
| Familia | Qué agrupa | Afinidad | Debilidad | Resistencia | Rasgo | Especialidad | Roles probables | Técnica básica | Mods |
|---|---|---|---|---|---|---|---|---|---|
| **Dragón** | Dragones y hombres dragón: potencia bruta y orgullo. | Fuego | Hielo | Fuego | *Corazón de dragón:* Con la mitad de sus PV o menos, +1 a sus tiradas de ataque. | fuerza, intimidar, volar si tiene alas | Bruto / Versátil | Garra de dragón (Neutro) | — |
| **Saurio** | Reptiles y dinosaurios: piel dura y mandíbulas fuertes. | Neutro | Hielo | Tierra | *Piel gruesa:* +VF PV (incluido en la ficha). | aguante, fuerza, morder | Bruto / Tanque | Mordisco (Neutro) | PV +VF |
| **Bestia** | Mamíferos y bestias míticas: instinto de manada. | Neutro | Fuego | Hielo | *Manada:* +1 al atacar a un objetivo que un aliado ya ha atacado en este asalto. | rastrear, olfato, correr | Ágil / Acechador | Zarpazo (Neutro) | — |
| **Ave** | Aves y hombres ave: dominan el cielo. | Viento | Eléctrico | Tierra | *Vuelo:* Vuela: ignora el terreno y las técnicas de Toque de quien no vuela tienen −2 contra ella, salvo que esté trabada con el atacante. | volar, otear, orientarse | Ágil / Tirador | Picotazo (Neutro) | — |
| **Acuático** | Criaturas marinas y anfibias. | Agua | Eléctrico | Fuego | *Anfibio:* Nada. En zonas con agua o bajo la lluvia, +1 Def y se mueve sin penalización. | nadar, bucear, corrientes | Tanque / Tirador | Coletazo (Agua) | — |
| **Naturaleza** | Insectos y plantas: venenos, raíces y caparazones. | Planta | Fuego | Agua | *Toxinas y raíces:* Inmune a Veneno. +1 a la tirada con técnicas de Veneno o Atrapar. Los insectos (Insectoid, Ancient Insectoid) vuelan. | sigilo en la naturaleza, plantas, camuflaje | Místico / Acechador | Picadura (Neutro) | — |
| **Máquina** | Cíborgs, máquinas y armas vivientes. | Acero | Eléctrico | Veneno | *Blindaje:* +1 Arm y −1 Ini (incluidos). Inmune a Dormir y Encantar. | fuerza, cálculo, sensores, interfaz | Tanque / Tirador | Puño mecánico (Acero) | Arm +1, Ini -1 |
| **Juguete** | Marionetas, juguetes y comida con vida. | Mental | Fuego | Mental | *Relleno:* Una vez por combate reduce a la mitad el daño de un impacto. Inmune a Asustar. | distraer, actuar, engañar | Místico / Apoyo | Golpe de juguete (Neutro) | — |
| **Sagrado** | Ángeles, bestias sagradas y deidades. | Luz | Oscuridad | Luz | *Aura sagrada:* +1 dado de daño con técnicas de Luz contra la familia Oscuro (no contra el Modo Oscuro de otra familia). Los ángeles y las aves sagradas vuelan. | detectar el mal, consolar, saber antiguo | Místico / Apoyo | Golpe sagrado (Luz) | — |
| **Caballero** | Caballeros y guerreros de código y honor. | Acero | Oscuridad | Acero | *Honor:* Inmune a Asustar y Encantar. +1 Def mientras usa Proteger. (Tipo Dark Knight: debilidad Luz y resistencia Oscuridad.) | proteger, etiqueta, juramentos | Versátil / Tanque | Tajo (Acero) | — |
| **Oscuro** | Demonios, no muertos, fantasmas y bestias oscuras. | Oscuridad | Luz | Oscuridad | *Hambre oscura:* Cuando su ataque saca 10+ (o el defensor saca 6–), recupera VF PV. | intimidar, ver en la oscuridad, ocultarse | Acechador / Místico | Zarpa sombría (Oscuridad) | — |
| **Arcano** | Magos, hadas y espíritus. *(En la versión 1.0 se llamaba «Místico»; se renombra para no confundirla con el rol Místico.)* | Mental | Acero | Mental | *Hechicería:* Sus técnicas de alcance Distancia pueden usarse con alcance Larga. Inmune a Confundir. | magia, saber arcano, ilusiones | Místico / Apoyo | Proyectil arcano (Mental) | — |
| **Elemental** | Cuerpos hechos de fuego, hielo, roca o luz estelar. | según el tipo | según el tipo | según el tipo | *Cuerpo elemental:* Resistencia al daño de su propio elemento (incluida en la ficha) e inmune al estado por defecto de ese elemento. No es inmune al daño: un grupo con técnicas de ese elemento no se queda sin opciones. Por tipo: Fire → Fuego (débil a Agua); Ice-Snow → Hielo (débil a Fuego); Mineral → Tierra (débil a Planta); Ore → Tierra (débil a Planta); Ancient Mineral → Tierra (débil a Planta); Galaxy → Cósmico (débil a Oscuridad); Minor → Cósmico (débil a Oscuridad); Major → Cósmico (débil a Oscuridad); Super Major → Cósmico (débil a Oscuridad). | su elemento | Bruto / Místico | Golpe elemental (afinidad de la familia) | — |
| **Anomalía** | Mutantes, compuestos, invasores y lo inclasificable (incluye las crías Slime y Lesser). | Neutro | — | — | *Adaptación:* Tras recibir daño de un elemento, gana Resistencia a ese elemento hasta el final del combate (solo a uno a la vez). | adaptarse, infiltrarse en sistemas, imitar | Versátil / Bruto | Embestida (Neutro) | — |

### 9.2 Asignación de los 140 tipos
Cada tipo pertenece a **exactamente una** familia. Se indica el nombre oficial en inglés (tal como aparece en los datos) y su traducción.

- **Dragón** (21 tipos, 116 Digimon): Dragon Man (Hombre Dragón), Dark Dragon (Dragón Oscuro), Mini Dragon (Minidragón), Dragon (Dragón), Holy Dragon (Dragón Sagrado), Beast Dragon (Dragón Bestia), Evil Dragon (Dragón Maligno), Bird Dragon (Dragón Ave), Rock Dragon (Dragón de Roca), Armored Dragon (Dragón Acorazado), Shining Dragon (Dragón Resplandeciente), Baby Dragon (Dragón Bebé), Mythical Dragon (Dragón Mítico), Machine Dragon (Dragón Máquina), Sky Dragon (Dragón Celeste), Ancient Dragon (Dragón Ancestral), Ancient Dragon Man (Hombre Dragón Ancestral), Ocean Dragon (Dragón Oceánico), Earth Dragon (Dragón de Tierra), Fire Dragon (Dragón de Fuego), Dragon Warrior (Guerrero Dragón).
- **Saurio** (7 tipos, 58 Digimon): Dinosaur (Dinosaurio), Reptile (Reptil), Reptile Man (Hombre Reptil), Ceratopsian (Ceratopsio), Pterosaur (Pterosaurio), Plesiosaur (Plesiosaurio), Stegosaur (Estegosaurio).
- **Bestia** (8 tipos, 134 Digimon): Beast (Bestia), Beast Man (Hombre Bestia), Mammal (Mamífero), Ancient Beast (Bestia Ancestral), Mythical Beast (Bestia Mítica), Mysterious Beast (Bestia Misteriosa), Rare Animal (Animal Raro), Ancient Mythical Beast (Bestia Mítica Ancestral).
- **Ave** (8 tipos, 43 Digimon): Bird (Ave), Giant Bird (Ave Gigante), Baby Bird (Polluelo), Bird Man (Hombre Ave), Ancient Bird (Ave Ancestral), Mysterious Bird (Ave Misteriosa), Mini Bird (Minipájaro), Ancient Bird Man (Hombre Ave Ancestral).
- **Acuático** (12 tipos, 74 Digimon): Aquatic (Acuático), Aquatic Beast Man (Hombre Bestia Acuático), Ancient Aquatic Beast Man (Hombre Bestia Acuático Ancestral), Sea Beast (Bestia Marina), Sea Animal (Animal Marino), Mollusk (Molusco), Crustacean (Crustáceo), Ancient Crustacean (Crustáceo Ancestral), Amphibian (Anfibio), Ancient Fish (Pez Ancestral), Tropical Fish (Pez Tropical), Marine Man (Hombre Marino).
- **Naturaleza** (9 tipos, 80 Digimon): Insectoid (Insectoide), Ancient Insectoid (Insectoide Ancestral), Larva, Parasite (Parásito), Vegetation (Vegetal), Carnivorous Vegetation (Planta Carnívora), Ancient Vegetation (Vegetal Ancestral), Seed (Semilla), Bulb (Bulbo).
- **Máquina** (9 tipos, 176 Digimon): Cyborg (Cíborg), Machine (Máquina), Weapon (Arma), Mine (Mina), Enhancement (Potenciado), Armor (Armadura), CRT (Pantalla CRT), LCD (Pantalla LCD), 9000.
- **Juguete** (3 tipos, 57 Digimon): Puppet (Marioneta), Food (Comida), Musical Instrument (Instrumento Musical).
- **Sagrado** (16 tipos, 113 Digimon): Angel (Ángel), Mini Angel (Miniángel), High Angel (Arcángel), Super Angel (Superángel), Great Angel (Gran Ángel), Seraph (Serafín), Cherub (Querubín), Dominion (Dominación), Principality (Principado), Virtue (Virtud), Holy Beast (Bestia Sagrada), Holy Bird (Ave Sagrada), Deity (Deidad), God Beast (Bestia Divina), Tathāgata, Monk (Monje).
- **Caballero** (8 tipos, 60 Digimon): Holy Knight (Caballero Sagrado), Dark Knight (Caballero Oscuro), Beast Knight (Caballero Bestia), Magic Knight (Caballero Mágico), Ancient Holy Knight (Caballero Sagrado Ancestral), Holy Sword (Espada Sagrada), Warrior (Guerrero), Magic Warrior (Guerrero Mágico).
- **Oscuro** (10 tipos, 116 Digimon): Demon (Demonio), Dark Angel (Ángel Caído), Evil King (Rey Maligno), Little Devil (Diablillo), Demon God (Dios Demonio), Wicked God (Dios Perverso), Avatar, Undead (No Muerto), Ghost (Fantasma), Dark Beast (Bestia Oscura).
- **Arcano** (6 tipos, 69 Digimon): Wizard (Mago), Pixie (Hada), Ancient Pixie (Hada Ancestral), Ancient (Ancestral), Spirit (Espíritu), Smoke (Humo).
- **Elemental** (9 tipos, 29 Digimon): Fire (Fuego), Ice-Snow (Hielo y Nieve), Mineral, Ore (Mena), Ancient Mineral (Mineral Ancestral), Galaxy (Galaxia), Minor (Menor (estelar)), Major (Mayor (estelar)), Super Major (Supermayor).
- **Anomalía** (14 tipos, 192 Digimon): Mutant (Mutante), Unidentified (No Identificado), Composite (Compuesto), Alien (Alienígena), Alien Humanoid (Humanoide Alienígena), Invader (Invasor), Unanalyzable (Inanalizable), Abnormal (Anómalo), Unique (Único), NO DATA (SIN DATOS), Ancient Mutant (Mutante Ancestral), Slime (Limo), Lesser (Menor), Perfect (Perfección).

**Total: 140 tipos** (comprobado contra `types.txt`: ninguno sin familia ni repetido).

### 9.3 Vuelo y nado
**Vuelan:** la familia Ave; los tipos Insectoid, Ancient Insectoid, Sky Dragon, Holy Dragon, Bird Dragon, Pterosaur, Angel, Mini Angel, High Angel, Super Angel, Great Angel, Cherub, Seraph, Virtue, Dominion, Principality, Dark Angel, Pixie, Ancient Pixie, Ghost, Holy Bird, Smoke, Spirit; y, una a una (la especificación usa sus **ids**, porque los nombres se repiten), Patamon, WarGreymon, WarGreymon (X Antibody), BlackWarGreymon, MetalGarurumon, Omnimon, Imperialdramon: Dragon Mode, Imperialdramon: Fighter Mode, Imperialdramon: Paladin Mode, MetalGreymon (Vaccine), Myotismon, MaloMyotismon, Beelzemon: Blast Mode, Magnamon, UlforceVeedramon, Gallantmon: Crimson Mode, Pegasusmon, Nefertimon, Airdramon, Megadramon, Gigadramon, Piedmon, Lucemon: Chaos Mode, Seraphimon, Rosemon, Lilamon, Kabuterimon, MegaKabuterimon (Red), MegaKabuterimon (Blue), Flymon, Etemon, Tentomon, Biyomon, Hawkmon, Falcomon, Lunamon, Kudamon, Sakuyamon, Taomon, Ravemon: Burst Mode, Ravemon. **Nadan:** la familia Acuático y los tipos Amphibian, Plesiosaur, Ocean Dragon, Sea Beast, Sea Animal. *(El DJ puede conceder vuelo o nado a cualquier forma con alas o aletas evidentes mediante un override.)*

---

## 10. Elementos [N]

Lista cerrada de **14 elementos**. Cada técnica tiene uno. El elemento decide las **debilidades** (+1 dado de daño) y las **resistencias** (mitad de daño) y da un **estado por defecto** a las técnicas que no tienen ningún estado propio.

| Elemento | Qué representa | Estado por defecto | Vence a (deriva debilidades) | Raíces de ejemplo en el nombre (inglés) |
|---|---|---|---|---|
| **Neutro** | Golpes, garras, embestidas y energía sin naturaleza definida. | — | — | — |
| **Veneno** | Ácidos, toxinas, gases, basura y, sí, caca. | Veneno | Planta | poison, venom, toxic, toxin, acid, sludge, poop, excrement |
| **Hielo** | Escarcha, nieve, ventisca y frío absoluto. | Congelar | Planta, Viento | ice, icy, frozen, freez, frost, snow, blizzard, hail |
| **Eléctrico** | Rayos, plasma, magnetismo y descargas. | Paralizar | Agua, Viento | thunder, lightning, electr, elec, spark, plasma, volt, shock |
| **Fuego** | Llamas, calor, magma y explosiones solares. | Quemar | Planta, Hielo, Acero | fire, fires, fireball, flame, flaming, flare, blaze, blazing |
| **Agua** | Burbujas, olas, presión y corrientes. | Ralentizar | Fuego, Tierra | water, aqua, hydro, bubble, wave, waves, ocean, sea |
| **Planta** | Enredaderas, pétalos, semillas y esporas. | Atrapar | Agua, Tierra | leaf, leaves, flower, ivy, seed, vine, thorn, rose |
| **Luz** | Lo sagrado, láseres, estrellas y fotones. | Cegar | Oscuridad | holy, heaven, light, lights, licht, shining, shine, divine |
| **Oscuridad** | Sombras, maldiciones, muerte y el lado oscuro de los datos. | Asustar | Luz, Mental | dark, death, hell, evil, shadow, night, black, nightmare |
| **Cósmico** | Meteoros, gravedad, tiempo, estrellas y el espacio profundo. | Ralentizar | Tierra, Acero | meteor, galaxy, galactic, cosmic, cosmo, space, planet, black hole |
| **Mental** | Mente, sonido, música, ilusiones, magia y emociones. | Confundir | Veneno, Cósmico | love, charm, dream, lullaby, song, songs, symphony, sonic |
| **Viento** | Tornados, alas, vendavales y presión de aire. | Empujar | Planta, Veneno | wind, tornado, storm, gale, hurricane, typhoon, cyclone, whirlwind |
| **Tierra** | Rocas, terremotos, arena y cristal. | Derribar | Eléctrico, Veneno, Fuego | rock, rocks, stone, earth, quake, gaia, terra, sand |
| **Acero** | Espadas, misiles, cañones y metal. | — | Hielo, Mental | metal, iron, steel, blade, sword, saber, sabre, slash |

**Debilidades y resistencias de cada ficha:** las de su familia, más las derivadas del **elemento principal** de sus técnicas: es débil al primer elemento (en el orden Agua, Fuego, Planta, Eléctrico, Veneno, Viento, Tierra, Hielo, Acero, Mental, Luz, Oscuridad, Cósmico) que vence a su elemento principal **y que no esté ya entre las debilidades o resistencias de su familia**, y resiste su propio elemento principal (salvo Neutro y Cósmico). Lo que aparezca en ambas listas se anula. Como máximo 2 de cada. Así, dos Digimon de la misma familia pueden tener debilidades distintas, y todos los elementos pueden ser debilidad de alguna ficha. La columna «Vence a» **solo sirve para derivar debilidades**: el +1 dado lo da la debilidad de la ficha objetivo, no el elemento del atacante.

**Raíces en el contexto:** para clasificar por el perfil inglés, cada elemento tiene una lista propia de raíces de contexto, sin palabras ambiguas (*fire* como verbo, *arm*, *time*, *nature*, *light*, *air*); la lista exacta está en `spec_fichas.json` (`elementos[*].raices_contexto`).

**Clima y terreno** pueden modificar elementos (18.3): tormenta eléctrica (+1 dado a Eléctrico), calor de servidor (+1 dado a Fuego y −1 dado a Hielo), etc.

---

## 11. Vocabulario de técnicas [N]

### 11.1 Anatomía de una técnica
Toda técnica, oficial o genérica, se describe con el mismo vocabulario cerrado:

> **Nombre** — Potencia (P1/P2/P3; P2/P3 versátil) [Agotadora] · Alcance · Área · Elemento · hasta 2 palabras clave · [dados de daño ≈ media]

Ejemplo: **Pepper Breath** — P2/P3 (Agotadora como P3) · Distancia · Individual · Fuego · Quemar, Brutal · [2d6 / 3d6]. Los nombres de las técnicas se escriben siempre en su forma oficial; la regla se redacta con palabras propias.

### 11.2 Potencias y dado de poder
| Potencia | Dados | Uso | Para qué |
|---|---|---|---|
| **P1 Ligera** | 1 | A voluntad | Técnica básica, maniobras de rol y técnicas menores. |
| **P2 Fuerte** | 2 | A voluntad | La técnica de diario. |
| **P3 Firma** | 3 | **Agotadora**: tras usarla, el Digimon no puede usar ninguna técnica Agotadora en su siguiente turno (un Jefe, en el asalto siguiente) | La técnica emblemática; las fichas tienen como mucho una. |
| **P2/P3 versátil** | 2 o 3 | Como P2 a voluntad; como P3, Agotadora | Firma de los Digimon con una sola técnica oficial. |

**Asignación en el bestiario:** Bebé I, todas P1. Bebé II, la primera P2 y el resto P1. Con una sola técnica oficial, Firma P2/P3. Con varias, Firma P3, la segunda P2, la tercera P2 si el rango es 3 o más (si no, P1) y el resto P1. Una técnica que no sea la Firma y lleve una «palabra menor» (petit, mini, baby, bubbles…) baja una potencia. **Una técnica de daño P1 es siempre Individual** (el clasificador descarta su área). Sin técnicas oficiales: Firma genérica *Descarga de datos* (P2/P3 · Distancia · afinidad de la familia).

**Como mucho una P3 por ficha, también con técnicas prestadas:** una técnica heredada que era Firma (P3 o P2/P3) se hereda como **P2**, salvo que sustituya a la Firma de la forma actual (12.4); el programa Tarjeta Digimon usa la técnica como **P2 como máximo** (13.2).

**Dado de poder y daño medio por nivel** (antes de Arm). Las técnicas de área tiran un dado menos **solo cuando alcanzan de verdad a 2 o más objetivos**; contra uno solo usan las columnas normales:

| Nivel | Dado | VF | P1 | P2 | P3 | P2 contra 2+ objetivos | P3 contra 2+ objetivos |
|---|---|---|---|---|---|---|---|
| Bebé | d4 | 2 | 2.5 | 5.0 | — | 2.5 | — |
| Novato | d6 | 3 | 3.5 | 7.0 | 10.5 | 3.5 | 7.0 |
| Campeón | d8 | 4 | 4.5 | 9.0 | 13.5 | 4.5 | 9.0 |
| Perfecto | d10 | 5 | 5.5 | 11.0 | 16.5 | 5.5 | 11.0 |
| Definitivo | d12 | 6 | 6.5 | 13.0 | 19.5 | 6.5 | 13.0 |

*Fórmula:* Daño = suma de los dados de poder del atacante. Nº de dados = potencia (P1 = 1, P2 = 2, P3 = 3) + extras (+1 por cada uno: debilidad del objetivo al elemento, Brutal con 10+, crítico, Potenciado+ o programa Potencia, atacante de rango superior al objetivo, plantilla Legendario, Cargado, Retroceso, Furia del Jefe) − 1 solo si la técnica alcanza de verdad a 2 o más objetivos (contra uno solo, una técnica de área cuenta como Individual); mínimo 1 dado. Después: − Arm del objetivo (salvo Perforante). Después, mitad (redondeo abajo) por cada uno: el defensor PJ sacó 7–9; el objetivo resiste el elemento (salvo Perforante); cada rango que el objetivo esté por encima del atacante. Mínimo 1 si hubo impacto. **Golpe aguantado:** un solo impacto de un PNJ no quita a un compañero más de la mitad de sus PV máximos (redondeo arriba). Los Escudos absorben antes que los PV.

### 11.3 Alcances y áreas
| Alcance | Regla |
|---|---|
| **Toque** | Un objetivo en tu zona. Al usarla quedas trabado con él. **Con área, el área está en tu zona:** Toque + Ráfaga = 2 objetivos de tu zona; Toque + Zona o Total = todos los enemigos de tu zona (quedas trabado con todos). |
| **Distancia** | Un objetivo (o el área) en tu zona o en una adyacente. Estando trabado: −1 a la tirada. |
| **Larga** | Hasta 2 zonas de distancia. Estando trabado: −1 a la tirada. |
| **Personal** | Solo el usuario (técnicas de apoyo sobre sí mismo). **Personal + Zona** = centrada en el usuario: afecta a su zona. |

| Área | Dados | Regla |
|---|---|---|
| **Individual** | 0 | Un objetivo. |
| **Ráfaga** | −1 si alcanza a 2 | Hasta 2 objetivos distintos dentro del alcance. Una sola tirada, comparada con la Def de cada objetivo. |
| **Zona** | −1 si alcanza a 2+ | Todos los enemigos de una zona dentro del alcance y, a elección del atacante, **cualquier Tamer de esa zona** (como mucho 1 ataque contra cada Tamer por asalto). Una sola tirada. |
| **Total** | −1 si alcanza a 2+ | Todos los enemigos dentro del alcance. En el bestiario solo aparece en la Firma de rango 4; un Jefe o un Legendario (plantilla) puede usar su Firma de Zona como Total. No admite control duro. |

Si un PJ usa una técnica de área, la resuelve con **una sola tirada** y el DJ la compara con la Def de cada objetivo. Si la usa un PNJ, **cada PJ afectado tira su propia Defensa** y el DJ tira el daño una vez (6.7). La ficha imprime los dados de una técnica de área **contra un objetivo y contra 2 o más** («2d10; contra 2+: 1d10»).

### 11.4 Palabras clave de efecto (35)
Cada técnica lleva **como máximo 2**. Se agrupan en: **Daño** (modifican el impacto), **Estado** (aplican un estado con 10+ del atacante o 6– del defensor), **Apoyo** (sin tirada ni daño cuando la técnica es de apoyo) y **Táctica** (posición y tiempo). *VF* es el valor fijo del dado del usuario (la mitad de sus caras). En la columna «Se activa»: *al usarla* = funciona impacte o no; *al impactar* = con 7+ del atacante (o 7–9 / 6– del defensor); «Místico» = el **rol** Místico.

**Daño (7)**

| Palabra | Se activa | Regla exacta | Duración | Valor | Control duro |
|---|---|---|---|---|---|
| **Perforante** | al impactar | Ignora la Armadura y la Resistencia elemental del objetivo. | inmediata | — | — |
| **Brutal** | con 10+ (o 6– del defensor) | Con 10+ del atacante (o 6– del defensor): +1 dado de daño. | inmediata | — | — |
| **Certero** | al usarla | +1 a la tirada de ataque del PJ; si la usa un PNJ, −1 a la tirada de Defensa del PJ. Ignora Cobertura y Oculto. | inmediata | — | — |
| **Drenar** | al impactar | El usuario recupera PV iguales a la mitad del daño infligido (tras reducciones). | inmediata | — | — |
| **Retroceso** | al usarla | +1 dado de daño; el usuario sufre VF de daño (ignora Arm) tras resolverla, impacte o no. | inmediata | — | — |
| **Ejecutar** | con 10+ (o 6– del defensor) | Solo en técnicas Individuales (en una técnica de área, el clasificador la cambia por Brutal). Con 10+ (o 6– del defensor): si tras el daño el objetivo queda con PV ≤ 2 × VF del usuario, cae a 0. Jefes y Legendarios son inmunes (en su lugar, +1 dado). | inmediata | 2*vf | — |
| **Cargado** | requiere preparación | Requiere preparación: el usuario gasta una acción en Cargar (−1 Def hasta su próximo turno). En su siguiente turno la lanza con +1 a la tirada y +1 dado. Si queda Aturdido, Dormido o Sellado, pierde la carga. Los Jefes la telegrafían (Guardia de carga). | 1 turno | — | — |

**Estado (20)**

| Palabra | Se activa | Regla exacta | Duración | Valor | Control duro |
|---|---|---|---|---|---|
| **Quemar** | 10+ del atacante / 6– del defensor (Místico: 7–9) | Quemado: al inicio de cada uno de sus turnos (un Jefe: una vez por asalto) pierde VF PV (VF del causante, a la mitad por cada rango que el afectado supere al causante; mínimo 1). Una técnica de Agua o Hielo que le alcance lo apaga. | 2 turnos | vf | — |
| **Congelar** | 10+ del atacante / 6– del defensor (Místico: 7–9) | Congelado: no puede moverse ni usar técnicas de Toque; −2 Def. El daño de Fuego lo descongela. | 1 turno | — | — |
| **Paralizar** | 10+ del atacante / 6– del defensor (Místico: 7–9) | Paralizado: en su turno solo puede moverse o actuar (no ambas); −1 a sus ataques; sin reacciones. | 2 turnos | — | — |
| **Veneno** | 10+ del atacante / 6– del defensor (Místico: 7–9) | Envenenado: al final de cada uno de sus turnos (un Jefe: una vez por asalto) pierde VF PV (VF del causante, a la mitad por cada rango que el afectado supere al causante; mínimo 1); no puede recuperar PV con Curar ni con objetos. | 3 turnos | vf | — |
| **Aturdir** | 10+ del atacante / 6– del defensor (Místico: 7–9) | Aturdido: pierde su próxima acción (puede moverse). Control duro: nunca con 7–9; a un Jefe solo le quita una acción del asalto. | 1 turno | — | sí |
| **Dormir** | 10+ del atacante / 6– del defensor (Místico: 7–9) | Dormido: pierde sus turnos; los ataques contra él tienen +2; despierta al recibir daño o si un aliado gasta su acción. Control duro. | hasta 2 turnos | — | sí |
| **Cegar** | 10+ del atacante / 6– del defensor (Místico: 7–9) | Cegado: −2 a sus ataques; no puede usar técnicas de alcance Larga. | 1 turno | — | — |
| **Confundir** | 10+ del atacante / 6– del defensor (Místico: 7–9) | Confundido: al empezar su turno tira 1d6; con 1–2 usa su técnica P1 contra la criatura más cercana (la elige el DJ, puede ser aliada) y pierde la acción; con 3–6, −1 a sus tiradas. | 2 turnos | — | — |
| **Asustar** | 10+ del atacante / 6– del defensor (Místico: 7–9) | Asustado: no puede acercarse a la fuente ni usar técnicas de Toque contra ella; −1 a cualquier ataque contra ella. | 2 turnos | — | — |
| **Encantar** | 10+ del atacante / 6– del defensor (Místico: 7–9) | Encantado: no puede atacar a la fuente; si no hay otro objetivo, usa Defender. | 1 turno | — | — |
| **Sellar** | 10+ del atacante / 6– del defensor (Místico: 7–9) | Sellado: no puede usar técnicas P3, digievolucionar ni cambiar de modo; su Tamer no puede usarle programas. | 1 turno | — | — |
| **Regresión** | 10+ del atacante / 6– del defensor (nunca con 7–9) | Contra un compañero en forma temporal: esa forma termina y vuelve a su forma de partida con los PV guardados (sin quedar Agotado); si estaba en una forma estable, queda Sellado 2 turnos. Contra un PNJ: queda Sellado y Debilitado 1 turno (el DJ puede narrar que pierde su forma un instante). Jefes y Legendarios: solo Sellado 1 turno. Los Bebés no la aplican. | inmediata (o Sellado) | — | sí |
| **Ralentizar** | 10+ del atacante / 6– del defensor (Místico: 7–9) | Ralentizado: pasa a la fase lenta (un PNJ actúa el último); no puede Correr; −1 Def. | 2 turnos | — | — |
| **Atrapar** | 10+ del atacante / 6– del defensor (Místico: 7–9) | Atrapado: no puede moverse; −1 a sus ataques. Liberarse cuesta su acción (PJ: 2d6 + Atq − Atq del captor, 7+; PNJ: automático). Se libera si el captor cae, queda Aturdido o se aleja. | hasta liberarse | — | — |
| **Debilitar** | 10+ del atacante / 6– del defensor (Místico: 7–9) | Debilitado: −1 a sus ataques y su daño total se reduce en VF del causante (mínimo 1). | 2 turnos | vf | — |
| **Romper** | 10+ del atacante / 6– del defensor (Místico: 7–9) | Roto: −2 Arm (mínimo 0); si ya tenía 0, −1 Def. Dura toda la escena. No se acumula. | escena | — | — |
| **Marcar** | 10+ del atacante / 6– del defensor (Místico: 7–9) | Marcado: el siguiente ataque contra él, de cualquiera, tiene +2. | hasta el próximo ataque | — | — |
| **Derribar** | 10+ del atacante / 6– del defensor (Místico: 7–9) | Derribado: debe gastar su movimiento en levantarse; las técnicas de Toque contra él tienen +1. Si volaba, cae a tierra. | hasta levantarse | — | — |
| **Empujar** | 10+ del atacante / 6– del defensor (Místico: 7–9) | Lo desplaza 1 zona (a elección del atacante) y deja de estar trabado; si choca contra algo sólido o cae en una zona de Peligro, +VF de daño. | inmediata | vf | — |
| **Provocar** | 10+ del atacante / 6– del defensor (Místico: 7–9) | Provocado: en su próximo turno debe atacar al usuario; si ataca a otro, −2 a esa tirada. | 1 turno | — | — |

**Apoyo (4)**

| Palabra | Se activa | Regla exacta | Duración | Valor | Control duro |
|---|---|---|---|---|---|
| **Curar** | sin tirada (en técnica de apoyo) | Un aliado (o el usuario) recupera PV iguales a los dados de poder de la técnica (P1: 1 dado; P2: 2; P3: 3). Si es de área, todos los aliados de una zona con −1 dado. **Una técnica de apoyo con Curar es Agotadora.** En una técnica de daño, el usuario recupera 1 dado al impactar. | inmediata | dados | — |
| **Escudo** | sin tirada (en técnica de apoyo) | Un aliado (o el usuario) gana Escudo = VF × potencia (P1 = VF, P2 = 2 VF, P3 = 3 VF) hasta el final de la escena. Los Escudos no se acumulan: se queda el mayor. **Una técnica de apoyo con Escudo es Agotadora.** | escena | vf*potencia | — |
| **Mejora** | sin tirada (en técnica de apoyo) | P1: el aliado queda **Potenciado** (+1 a la tirada de su próximo ataque). P2: queda **Potenciado+** (+1 a la tirada y +1 dado). P3: Potenciado+ para todos los aliados de una zona. *(No confundir con los Avances del compañero, 17.4.)* | hasta su próximo ataque | — | — |
| **Purificar** | sin tirada (en técnica de apoyo) | Elimina estados negativos: uno (P1), todos los de un aliado (P2) o todos los de los aliados de una zona (P3). En una técnica de daño, además elimina Escudo y Potenciado del objetivo y da +1 dado contra la familia Oscuro. | inmediata | — | — |

**Táctica (4)**

| Palabra | Se activa | Regla exacta | Duración | Valor | Control duro |
|---|---|---|---|---|---|
| **Rápido** | al usarla | Antes de usarla, el usuario puede moverse 1 zona extra sin provocar ataques de retirada. | inmediata | — | — |
| **Contraataque** | requiere preparación | Se prepara (gasta la acción). Hasta su próximo turno, la primera vez que un enemigo le ataque y falle (Defensa del PJ 10+ / ataque del PJ 6– contra un PNJ que la tenga preparada), el atacante recibe el daño de la técnica sin tirada. | hasta su próximo turno | — | — |
| **Invocar** | al impactar (7+) | Si la técnica impacta, crea una invocación (enjambre, banco de peces, piezas…) en una zona a su alcance durante 2 asaltos: al inicio de cada turno del usuario inflige VF de daño (menos Arm) a un enemigo de esa zona; ese daño se divide a la mitad por cada rango que el objetivo supere al usuario. **Cada usuario mantiene como mucho una invocación activa:** crear otra disipa la anterior. Una técnica de área enemiga sobre esa zona la disipa. | 2 asaltos | vf | — |
| **Ocultar** | al usarla | Al usarla (impacte o no; en una técnica de apoyo, sin tirada), el usuario queda Oculto hasta que ataque: no puede ser objetivo de técnicas de Distancia ni Larga, y su primer ataque tiene +2. | hasta que ataque | — | — |

**Reglas comunes:**
- **Técnicas de apoyo:** no hacen daño ni piden tirada; afectan al usuario o a un aliado a su alcance (Personal = solo el usuario). **No llevan estados ni tácticas** (salvo un override documentado, como Kohenkyo de Renamon con Ocultar). Si llevan Curar o Escudo, son **Agotadoras**. Una técnica de apoyo sin palabra con valor (Kohenkyo) imprime la potencia como «—».
- **Palabra de apoyo en una técnica de daño:** hace su daño y, al impactar, el efecto de apoyo recae sobre el usuario: *Curar*, 1 dado; *Escudo*, VF; *Mejora*, Potenciado (P1); *Purificar*, un estado propio, y además +1 dado contra la familia Oscuro.
- **Valor numérico:** las palabras con valor (Quemar, Veneno, Debilitar, Empujar, Invocar, Escudo, Curar, Ejecutar) lo calculan con el VF o los dados del usuario; no hay que anotar nada más en la ficha.

**Cuando el estado lo sufre un PNJ (regla de espejo, 2.1):**

| Estado | En un PNJ | En un PJ |
|---|---|---|
| Paralizar | +1 a la Defensa del PJ contra sus ataques; no tiene reacciones | −1 a sus ataques; sin reacciones |
| Cegar | +2 a la Defensa del PJ contra sus ataques; no usa Larga | −2 a sus ataques; no usa Larga |
| Atrapar | +1 a la Defensa del PJ contra sus ataques; se libera automáticamente gastando su acción | −1 a sus ataques; liberarse cuesta su acción y una tirada |
| Debilitar | +1 a la Defensa del PJ contra sus ataques y su daño total se reduce en VF del causante | −1 a sus ataques y −VF a su daño |
| Confundir | con 3–6 en el d6, +1 a la Defensa del PJ contra sus ataques | con 3–6, −1 a sus tiradas |
| Asustar | +1 a la Defensa del PJ que es la fuente contra sus ataques | −1 a sus ataques contra la fuente |
| Provocar | si ataca a otro que no sea el usuario, ese PJ tiene +2 a su Defensa | si ataca a otro, −2 a esa tirada |
| Encantar | no ataca a la fuente; si no tiene otro objetivo, usa Defender (−2 a los ataques de los PJ contra él hasta su próximo turno) | no ataca a la fuente; si no hay otro objetivo, usa Defender (+2 a su Defensa) |
| Dormir | +2 al ataque del PJ contra él | −2 a su Defensa |
| Congelar | +2 al ataque del PJ contra él | −2 a su Defensa |
| Ralentizar | +1 al ataque del PJ contra él | −1 a su Defensa |
| Marcar | +2 al próximo ataque de un PJ contra él | −2 a su próxima Defensa |
| Derribar | +1 a las técnicas de Toque de los PJ contra él | −1 a su Defensa contra Toque |
| Romper (si ya tenía 0 Arm) | +1 al ataque del PJ contra él | −1 a su Defensa |
| Expuesto (7.3) | +1 a los ataques de los PJ contra él | −1 a su Defensa |

Los demás estados (Quemar, Veneno, Aturdir, Sellar, Regresión, Empujar) no modifican tiradas y funcionan igual en PJ y PNJ.

### 11.5 Técnica básica
Todo Digimon tiene una técnica básica **P1 · Toque · Individual**, sin palabras clave, además de sus técnicas oficiales. Su nombre y su elemento dependen de la familia (tabla del 9.1); los Tiradores la usan como **Disparo** (Distancia) y la familia Arcano la tiene a Distancia.

---

### 11.6 Efectos de Firma
Cada Firma del bestiario tiene, además de sus dados y palabras clave, un **efecto de Firma** propio con nombre y tres partes (la ficha lo imprime bajo sus técnicas; la lista completa está en `fuentes/firmas/`):

| Parte | Cuándo | Qué hace |
|---|---|---|
| **Sello** | Siempre que el Digimon usa su Firma **como Firma** (P3, o P2/P3 usada como P3). En los Bebés, cada vez que la usan. | Un añadido pequeño y temático: un efecto con 10+, +1 dado bajo una condición estrecha, una ventaja táctica o un terreno breve. Se suma a las palabras clave. |
| **Desatado** | Al declarar la Firma como P3, el Tamer gasta **1 Chispa**. **1 vez por combate.** Un PNJ Élite, Jefe o Legendario lo usa gratis 1 vez por combate (el Jefe, en la primera Firma tras su Furia; los demás, cuando el DJ quiera). Los Bebés no tienen. | El gran momento: equivale más o menos a +1 dado (área mayor, estado también con 7–9, Escudo o curación para la zona, Perforante y Certero…). |
| **Eco** | Fuera de combate, **1 vez por escena**. | Un permiso narrativo ligado a la técnica (encender, congelar, abrir, revelar, calmar…) y, si hay tirada, **Ventaja** en una en la que encaje. Abre una vía; nunca resuelve solo el obstáculo central de la aventura. |

**Límites.** Una Firma heredada como P2 (12.4) y la Tarjeta Digimon (13.2) conservan solo el Eco. Los Esbirros no usan Sello ni Desatado. Los estados que añade un efecto de Firma siguen 7.1 (el control duro, nunca con 7–9). El Sello y el Desatado juntos no dan más de **+1 dado** en una tirada, y ese dado **no se suma al de la Furia** de un Jefe (se queda el mayor). Los valores usan el VF del usuario.

## 12. Roles de combate y técnicas aprendibles

### 12.1 Los 8 roles [N]
El rol resume cómo pelea un Digimon. Modifica sus estadísticas, le da un **rasgo**, una **maniobra de rol** siempre disponible y, en algunos casos, una **palabra de Firma** que se añade a su técnica emblemática si le queda hueco.

| Rol | Estilo | Atq | Def | PV | Arm | Ini | Rasgo | Palabra de Firma |
|---|---|---|---|---|---|---|---|---|
| **Bruto** | Golpea fuerte y aguanta. Vive en el cuerpo a cuerpo. | +1 | 0 | +1 VF | 0 | 0 | *Arrollador:* Una vez por asalto, cuando deja a un enemigo a 0 PV con una técnica, puede moverse 1 zona y usar su técnica básica contra otro enemigo como acción gratuita. | Brutal |
| **Tanque** | Muralla del grupo: protege, provoca y resiste. | 0 | +1 | +1 VF | +1 | −1 | *Guardián:* Una vez por asalto puede usar Proteger como reacción sobre un aliado (Digimon o Tamer) de su zona, aunque ya haya actuado. | Provocar |
| **Ágil** | Rápido y escurridizo; elige dónde y cuándo pelear. | 0 | +1 | -1 VF | 0 | +2 | *Escurridizo:* Tras su acción puede moverse 1 zona extra y nunca sufre ataques de retirada. | Rápido |
| **Tirador** | Ataca desde lejos con precisión. | +1 | −1 | 0 | 0 | +1 | *Francotirador:* +1 a sus tiradas de ataque contra objetivos que no estén en su zona. Su técnica básica es de Distancia y su Firma de Distancia pasa a Larga. | Certero |
| **Místico** | Domina los estados alterados y la energía extraña. | 0 | 0 | -1 VF | 0 | 0 | *Maestro de estados:* Sus estados que no son de control duro también se aplican con 7–9 (su ataque de PJ con 7–9, o la Defensa del PJ con 7–9 si el Místico es PNJ). Es un rasgo del **rol** Místico, no de la familia Arcano. | — |
| **Apoyo** | Cura, protege y potencia a sus aliados. | −1 | 0 | 0 | 0 | 0 | *Sanador:* Sus técnicas de apoyo (Curar, Escudo, Mejora, Purificar) afectan a un aliado adicional dentro del alcance. El objetivo principal (solo él) suma +VF a la curación o al Escudo. | — |
| **Acechador** | Cazador oportunista que remata a los debilitados. | +1 | 0 | -1 VF | 0 | +2 | *Emboscada:* +1 dado de daño contra objetivos que aún no han actuado en el combate, que están Derribados, Atrapados, Cegados o Marcados, o si ataca desde Oculto. | Perforante |
| **Versátil** | Equilibrado y fiable; se adapta a lo que pida el combate. | 0 | 0 | 0 | 0 | +1 | *Adaptable:* Una vez por combate puede repetir una tirada propia de ataque o de Defensa (o, si es PNJ, obligar a un PJ a repetir un 10+ obtenido contra él). | — |

*PV «+1 VF» = el multiplicador de PV sube en 1 (Bruto Novato: 3 × 8 = 24 en lugar de 21).*

### 12.2 Maniobras de rol
Técnicas genéricas que cualquier Digimon de ese rol tiene siempre (las 438 especies con una sola técnica oficial ganan así identidad táctica):

| Rol | Maniobra | Ficha | Uso | Regla |
|---|---|---|---|---|
| Bruto | **Arremetida** | P1 · Toque · Individual · Neutro · Derribar | a voluntad | Antes de atacar se mueve 1 zona hacia el objetivo sin provocar ataques de retirada; ataque P1 de Toque con Derribar. |
| Tanque | **Desafío** | sin daño · Toque · Zona · Neutro · Provocar | a voluntad | Sin daño. Afecta a los enemigos de su propia zona (Toque + Zona). Una sola tirada de ataque comparada con la Def de cada uno: con 7+ queda Provocado. Si la usa un PNJ, cada PJ de su zona tira Defensa y queda Provocado con 6–. |
| Ágil | **Golpe y fuga** | P1 · Toque · Individual · Neutro · — | a voluntad | Ataque P1 de Toque; después se mueve 1 zona y deja de estar trabado. |
| Tirador | **Disparo certero** | P1 · Larga · Individual · afinidad de la familia · Certero | a voluntad | Ataque P1 de alcance Larga con Certero. El elemento es la afinidad de su familia. |
| Místico | **Interferencia** | sin daño · Distancia · Individual · Mental · Debilitar o Ralentizar | a voluntad | Sin daño. Tirada de ataque: aplica Debilitar o Ralentizar (a elegir antes de tirar). |
| Apoyo | **Pulso restaurador** | P1 · Distancia · Individual · Neutro · Curar o Purificar | Agotadora | Sin tirada. Un aliado recupera 1 dado de poder de PV o se libra de un estado. Agotadora (6.4). |
| Acechador | **Marca de caza** | sin daño · Larga · Individual · Neutro · Marcar | a voluntad | Sin tirada. Un enemigo a la vista queda Marcado hasta el final del siguiente asalto o hasta que reciba un ataque. |
| Versátil | **Cambio de guardia** | P1 · Toque · Individual · Neutro · — | a voluntad | Ataque P1 de Toque con +1 a la tirada; hasta su próximo turno tiene +1 Def. |

### 12.3 Especialidades fuera de combate
Además de la de su familia, cada rol da una especialidad (+1 a 2d6 + rango): **Bruto** fuerza y romper cosas · **Tanque** cargar peso, resistir y proteger · **Ágil** correr, saltar y esquivar · **Tirador** puntería y vigilancia · **Místico** percibir datos, magia y lo extraño · **Apoyo** curar, consolar y reparar · **Acechador** sigilo y rastreo · **Versátil** una a elección del jugador al crear el compañero.

### 12.4 Técnicas aprendibles [N]
Las técnicas oficiales de cada forma vienen con su ficha. El crecimiento propio del compañero se expresa con:
- **Técnica heredada** (avance, 17.4): una técnica de una forma inferior se puede usar en todas las superiores **con el dado de la forma actual** y su potencia original; **si era una Firma (P3 o P2/P3), se hereda como P2**, salvo que sustituya a la Firma de la forma actual. Así ninguna ficha tiene dos P3. *(El Pepper Breath de Agumon, usado por WarGreymon: 2d12 como P2; Terra Force sigue siendo su Firma.)*
- **Técnica perfeccionada** (avance): una técnica gana una palabra clave del vocabulario (aprobada por el DJ; máximo 2 en total) o sube de P1 a P2.
- **Técnica nueva** (avance): aprende una técnica genérica de la lista siguiente.
- **Tarjeta Digimon** (programa 22, 13.2): permite usar una técnica oficial de otro Digimon, como mucho como P2. Con el avance *Técnica nueva*, una técnica de una Tarjeta que el Tamer posea puede aprenderse de forma permanente (con su potencia, máximo P2).
- **Maestros:** un PNJ mentor (Leomon, Gennai, Jijimon…) puede enseñar una técnica genérica o perfeccionar una técnica a cambio de una misión: cuenta como un avance sin gastar el del nivel, una vez por arco.

**Técnicas genéricas (12):**

| Técnica | Ficha | Requisito |
|---|---|---|
| Embestida | P1 · Toque · Individual · Neutro · *Derribar* | — |
| Grito de guerra | Apoyo · Personal · *Mejora* (P1) | — |
| Aullido | sin daño · Distancia · Zona · Oscuridad · *Asustar* (una tirada contra la Def de cada enemigo de la zona; Asustado con 10+, o 7–9 si el rol es Místico) | — |
| Barrera de datos | Apoyo P2 (Agotadora) · Distancia · *Escudo* | — |
| Ráfaga de datos | P2 · Distancia · Ráfaga · afinidad de la familia (2 dados contra uno; 1 contra cada uno de dos) | — |
| Golpe certero | P2 · Toque · Individual · Neutro · *Certero* | — |
| Placaje protector | P1 · Toque · Individual · Neutro · *Provocar* | — |
| Reparación de datos | Apoyo P2 (Agotadora) · Distancia · *Curar* | rol Apoyo o Místico |
| Pulso purificador | Apoyo P1 · Distancia · *Purificar* | rol Apoyo o Místico, o familia Sagrado |
| Paso fantasma | P1 · Toque · Individual · Neutro · *Rápido, Ocultar* | Ágil o Acechador |
| Disparo cargado | P2 · Larga · Individual · afinidad · *Cargado* | Tirador |
| Contragolpe | P2 · Toque · Individual · Neutro · *Contraataque* | Tanque, Bruto o Versátil |

---

## 13. Programas (Tarjetas de modificación) [N]

### 13.1 Cómo funcionan
El Digivice ejecuta programas gastando **Carga**. Se usan con la acción de Tamer *Usar un programa* sobre el compañero (como mucho a 1 zona), salvo que se indique otra cosa. Al crear el personaje se conocen **3 programas de Nivel 1**; se aprenden más al subir de nivel (17.2), comprándolos (Nv1: 100 Bits, Nv2: 300, Nv3: 800) o encontrándolos como tarjetas. Los de **Nivel 2** se pueden usar desde el nivel 3 de Tamer y los de **Nivel 3**, desde el nivel 6: por eso los programas de Nivel 2 y 3 son material **[A]** (no se enseñan en la primera sesión). Un mismo programa solo se puede usar **una vez por asalto**. «Dados del compañero» = su dado de poder actual.

### 13.2 Lista de programas (35)
| # | Programa | Nv. | Carga | Efecto |
|---|---|---|---|---|
| 1 | **Potencia** | 1 | 1 | +1 dado de daño en la próxima técnica del compañero en este asalto (no es un estado: no deja al compañero Potenciado). |
| 2 | **Guardia** | 1 | 1 | El compañero gana Escudo = 2 × VF. |
| 3 | **Velocidad** | 1 | 1 | La próxima técnica del compañero gana *Rápido* y tiene +1 Def hasta tu próximo turno. |
| 4 | **Escáner** | 1 | 1 | *Analizar* con un 7–9 automático (puedes tirar para intentar el 10+). |
| 5 | **Antídoto** | 1 | 1 | Elimina un estado del compañero. |
| 6 | **Señuelo** | 1 | 1 | Un holograma distrae a un enemigo de la zona del compañero: el próximo ataque de ese enemigo da +2 a la Defensa del objetivo. |
| 7 | **Utilidad** | 1 | 1 | Linterna, mapa de la zona o traductor: +1 a una tirada de exploración de la escena. |
| 8 | **Puntería** | 1 | 1 | La próxima técnica del compañero gana *Certero*. |
| 9 | **Enfoque** | 1 | 1 | La Firma del compañero queda lista aunque la usara en su turno anterior. |
| 10 | **Bengala** | 1 | 1 | Revela a los Ocultos de una zona a la vista; tira AST + Tecnología: 10+ todos los enemigos de esa zona quedan Cegados; 7–9, uno. |
| 11 | **Ancla de suelo** | 1 | 1 | Hasta tu próximo turno, el compañero no puede ser Empujado ni Derribado. |
| 12 | **Cortafuegos** | 2 | 2 | Todos los aliados de la zona del compañero ganan Escudo = VF. |
| 13 | **Restaurar** | 2 | 2 | El compañero recupera 2 dados de poder de PV. |
| 14 | **Transferencia** | 2 | 2 | Mueve al compañero (y, si quieres, a ti) a cualquier zona a la vista, sin ataques de retirada. |
| 15 | **Candado** | 2 | 2 | Tira AST + Tecnología − rango de un enemigo a la vista: 10+ queda Sellado 2 turnos; 7–9, 1 turno. |
| 16 | **Copia** | 2 | 2 | En este asalto, el compañero puede usar una técnica P1 o P2 de un Digimon analizado en este combate (con su propio dado). |
| 17 | **Hackeo** | 2 | 2 | Abre o cierra una puerta digital, desactiva una trampa o controla una máquina simple durante una escena (AST + Tecnología si hay oposición). |
| 18 | **Ancla de datos** | 2 | 2 | Hasta el final de la escena, la primera vez que la forma temporal del compañero caiga a 0, se queda a 1 PV. |
| 19 | **Hiperpotencia** | 2 | 2 | La próxima técnica P3 del compañero tiene +1 a la tirada y gana *Certero*. |
| 20 | **Convertidor** | 2 | 2 | Hasta el final del asalto, el compañero cuenta como Vacuna, Datos o Virus (a elegir) para el triángulo. |
| 21 | **Cambio elemental** | 2 | 2 | La próxima técnica del compañero cambia su elemento por el que elijas (no cambia sus palabras clave). |
| 22 | **Tarjeta Digimon [X]** | 2 | 2 | Requiere poseer la Tarjeta de X. Lo ejecuta **cualquier Digivice**. En este asalto, el compañero usa una técnica oficial de X con **su propio** dado y Atq, con la potencia de X pero **como máximo P2** (así nunca tiene dos P3). No vale con Legendarios. *El D-Arc puede usar Tarjetas sin conocer este programa y con 1 Carga menos (15).* |
| 23 | **Radar** | 2 | 2 | Durante la escena el grupo no puede ser sorprendido y detecta Digimon Ocultos a 2 zonas. |
| 24 | **Overclock** | 3 | 3 | El compañero obtiene una acción adicional en este asalto (no puede ser una técnica Agotadora); después, −1 Def hasta su próximo turno. |
| 25 | **Purgado** | 3 | 3 | Elimina todos los estados negativos de los aliados de una zona, y todos los Escudos y los estados Potenciado y Potenciado+ de los enemigos de esa zona. |
| 26 | **Catalizador** | 3 | 3 | La próxima digievolución del compañero en esta escena cuesta 1 Chispa menos (mínimo 1). |
| 27 | **Fortaleza** | 3 | 3 | El compañero gana +2 Arm (máximo 3) hasta el final del siguiente asalto. |
| 28 | **Exploit** | 3 | 3 | El siguiente ataque aliado contra un enemigo analizado ignora su Resistencia y gana *Perforante*. |
| 29 | **Reinicio de zona** | 3 | 3 | Elimina invocaciones, terrenos alterados y efectos de zona de una zona. |
| 30 | **Velocidad de la luz** | 3 | 3 | 1 vez por sesión. El compañero hace un turno completo extra al final del asalto; después queda Hambriento. |
| 31 | **Restauración total** | 3 | 3 | 1 vez por combate. El compañero recupera la mitad de sus PV máximos. |
| 32 | **Muralla** | 3 | 3 | Todos los aliados del combate ganan Escudo = VF del compañero. |
| 33 | **Tarjeta Azul** | ★ | — | Objeto de trama, un uso: el compañero digievoluciona un nivel sin Chispa e ignorando el límite de Vínculo durante una escena. |
| 34 | **Tarjeta Dorada** | ★ | — | Objeto de trama, un uso: Modo Supremo [O] durante una escena. |
| 35 | **Programa X** | ★ | — | Objeto de trama: concede el Anticuerpo X al compañero (20.5). |

**Card Slash (D-Arc):** 1 vez por escena, un programa de Nivel 1 cuesta 0 Carga. Además, el D-Arc usa Tarjetas Digimon sin conocer el programa 22 y con 1 Carga menos.

---

## 14. Objetos, equipo y Bits [N]

### 14.1 Consumibles y objetos para el compañero
| Objeto | Efecto | Precio (Bits) |
|---|---|---|
| Disco de recuperación S | Recupera 2 dados de PV | 50 |
| Disco de recuperación M | Recupera 4 dados de PV | 150 |
| Disco de recuperación L | Recupera todos los PV | 400 |
| Disco antiestado | Elimina todos los estados (salvo Hambriento) | 80 |
| Disco de ánimo | Elimina Agotado | 120 |
| Disco de reinicio *(raro)* | Un compañero Derrotado vuelve a su forma estable con la mitad de PV | 1.000 |
| Chip de ataque | +1 Atq durante la escena (no acumulable) | 200 |
| Chip de defensa | +1 Def durante la escena (no acumulable) | 200 |
| Chip de velocidad | +2 Ini y *Rápido* en la próxima técnica | 150 |
| Chip de blindaje | +1 Arm durante la escena (máximo 3) | 250 |
| Chip elemental [elemento] | Resistencia a ese elemento durante la escena | 180 |
| Carne digital | Fuera de combate: recupera 2 × VF PV, elimina Hambriento y cuenta como comida del día | 20 |
| Carne gigante | Fuera de combate: todos los PV; comida para todo el grupo | 120 |
| Fruta de datos | Elimina Hambriento y el Tamer recupera 1 Aguante | 15 |
| Ración de viaje | Comida de un día para un Tamer o un compañero | 10 |
| Recarga de Digivice | +2 Carga (no supera el máximo) | 100 |
| Bomba de humo digital | Una zona gana Cobertura este asalto y los aliados de ella pueden Retirarse gratis | 60 |
| Cebo de datos | Atrae a Digimon salvajes; +1 a Empatía con ellos durante la escena | 30 |
| Tarjeta Digimon [X] | Se usa con el programa 22 (cualquier Digivice) o directamente con un D-Arc; precio según el nivel de X | Novato 100 · Campeón 300 · Perfecto 800 · Definitivo 2.000 |

### 14.2 Objetos de trama
| Objeto | Efecto |
|---|---|
| Digi-Huevo | Armadura (20.1) |
| Espíritu | Híbrido (20.2) |
| Chip X / Programa X | Anticuerpo X (20.5) |
| Emblema (Crest) físico | Despierta el Emblema del Tamer. En campañas «clásicas» es el requisito del primer Perfecto: el detonante de 5.6 exige, además, llevar el Emblema físico; lo activa (lo «desbloquea») el Digivice clásico o cualquier otro, si la campaña lo permite |
| Tarjeta Azul / Dorada | Programas 33 y 34 |
| Engranaje Negro, Espiral del Mal, Anillo Maligno, Aguja de Control | Corrupción (20.8) |

### 14.3 Equipo del Tamer
Los **2 objetos de equipo** de la creación (3.1, paso 9) salen de esta tabla.

| Objeto | Efecto | Precio |
|---|---|---|
| Mochila | Lleva hasta 10 objetos | 20 |
| Linterna | Anula el penalizador por oscuridad para el Tamer | 15 |
| Cuerda | +1 a Atletismo para escalar o rescatar | 10 |
| Botiquín | +1 a Medicina; 3 usos: recupera 2 Aguante | 40 |
| Portátil o tableta | +1 a Tecnología; necesario para hackear a distancia | 300 |
| Prismáticos | +1 a Observación a distancia | 60 |
| Silbato | Puedes dar Órdenes a 2 zonas de tu compañero | 5 |
| Navaja multiusos | +1 a Supervivencia, o a Tecnología para reparar | 25 |
| Brújula | +1 a Supervivencia para orientarse (en zonas glitch gira loca) | 20 |
| Tienda de campaña | Permite el descanso largo en terreno hostil | 80 |
| Bici o monopatín | El Tamer se mueve 2 zonas por turno en terreno llano | 120 |
| Cámara o móvil | Analizar desde 2 zonas de distancia (sin cobertura en el Mundo Digital) | 150 |
| Gafas protectoras | +1 a la Defensa del Tamer contra técnicas de Luz, arena o humo; inmune a Cegar | 30 |
| Walkie-talkies (pareja) | Comunicación entre Tamers separados hasta 1 región | 80 |
| Capa impermeable | Ignora el penalizador de clima para el Tamer | 25 |
| Cuaderno de campo | +1 a Saber Digital sobre Digimon ya Analizados | 15 |

### 14.4 Bits
La moneda del Mundo Digital. Se ganan con encargos (50–300), cofres de datos (d20 × 10) y vendiendo objetos (a la mitad de su precio). Un día de posada en una ciudad Digimon cuesta 10 y la comida para el grupo, unos 20.

---

## 15. Digivices [N]

**Funciones comunes de todos:** canal del Dado de Vínculo, Carga para programas, digievolución, escaneo básico (permite Analizar), ejecutar cualquier programa (incluida la Tarjeta Digimon, programa 22) y brújula hacia la Puerta Digital más cercana. Cada Tamer elige un modelo al crear el personaje, o lo fija la campaña. **Todos tienen una función de núcleo útil sin módulos**; lo marcado [O] solo existe si el módulo está activo.

| Modelo | Serie de referencia | Carga | Especial |
|---|---|---|---|
| **Digivice clásico** | Adventure | +1 | *Luz del Digivice:* 1 vez por escena, como acción de Tamer, un Digimon de la familia Oscuro o en Modo Oscuro, Novato o Campeón, queda Asustado de ti (sin tirada). Libera de Engranajes Negros (AST + Tecnología 7+). Activa el Emblema físico (14.2). |
| **D-3** | Adventure 02 | +1 | *Radar D-3:* mientras el Tamer esté consciente, el grupo no puede ser sorprendido por Digimon a 2 zonas o menos; abre Puertas Digitales desde ordenadores. [O] Permite la Armadura (20.1) y funciona dentro del alcance de una Aguja de Control (20.8). |
| **D-Arc / D-Power** | Tamers | +1 | *Card Slash:* 1 vez por escena, un programa de Nivel 1 cuesta 0 Carga. Usa Tarjetas Digimon sin conocer el programa 22 y con 1 Carga menos. |
| **D-Tector** | Frontier | +1 | Detecta datos ocultos: +1 a Observación en el Mundo Digital y revela a los Ocultos de su zona. [O] Guarda Espíritus (20.2). |
| **Digivice iC / Burst** | Savers | +0 | *DigiSoul:* 1 vez por combate, si tu Tamer está en la zona de su compañero, +1 dado a un ataque de Toque de este. Ganas 1 Chispa la primera vez en cada sesión que tu Tamer se enfrenta cara a cara a un Digimon hostil. |
| **Xros Loader** | Xros Wars | +0 | Guarda hasta 3 Digimon aliados de rango inferior al de tu compañero. *Digixros* (acción de Tamer): fusiona uno con tu compañero, que gana +1 dado de daño durante la escena; ese aliado no puede volver a usarse hasta un descanso largo. |
| **Digivice de campaña** | Original | +1 | Lo diseñan el DJ y la mesa: una función de escena (como las de arriba) y nada más. |

---

## 16. Emblemas (Crests) [N]

El Emblema es la virtud del Tamer. Le da Chispa (5.1), es el detonante de su primer Perfecto (5.6) y, desde el **nivel 5 de Tamer y Vínculo 3** (hacen falta las dos cosas), permite la **Resonancia del Emblema** (2 Chispa, 1 vez por sesión; material [A]). Cerrar el **arco del Emblema** (una historia en la que el Tamer supera su mayor dificultad con esa virtud) es el requisito del Vínculo ★.

| Emblema | Ganas Chispa cuando… | Resonancia (Vínculo 3+) |
|---|---|---|
| **Valor** | te enfrentas de cara a un peligro para proteger a otros | El compañero ignora Asustado y gana +1 dado en sus ataques contra enemigos de rango superior durante la escena. |
| **Amistad** | arriesgas algo tuyo por un amigo | Transfiere hasta 3 de tu Chispa a otros Tamers, o da +2 a la tirada de un aliado. |
| **Amor** | proteges o consuelas a alguien vulnerable | Todos los aliados de una zona recuperan 2 × VF PV. |
| **Sabiduría** | resuelves un problema con conocimiento | *Analizar* con 10+ automático a todos los enemigos a la vista; los aliados tienen +1 en su primer ataque contra cada uno. |
| **Pureza** | actúas con inocencia aunque te cueste | Purificar P3 sobre todos los aliados del combate. |
| **Sinceridad** | dices una verdad incómoda | Anula una ilusión, un engaño, un Encantado o un Confundido; el enemigo responsable queda Marcado. |
| **Fiabilidad** | cumples una promesa que te cuesta | Convierte el 6– de un aliado en un 7–9. |
| **Esperanza** | te niegas a rendirte en una situación desesperada | Un compañero Derrotado vuelve a su forma estable con la mitad de PV. |
| **Luz** | revelas la verdad o iluminas a alguien perdido | Las técnicas de Luz del grupo tienen +1 dado durante la escena; los enemigos de la familia Oscuro o en Modo Oscuro quedan Asustados (1 turno). |
| **Bondad** | muestras piedad a un enemigo | Un enemigo que no sea Jefe, con la mitad de PV o menos, deja de luchar (o huye). |
| **Milagros** *(dorado, de trama; no se elige al crear el personaje)* | haces lo que nadie cree posible | Repite cualquier tirada del grupo, o convierte un 6– en un 10+. |
| **Destino** *(dorado, de trama; no se elige al crear el personaje)* | aceptas una carga que nadie más puede llevar | El compañero alcanza un nivel por encima de su máximo durante 3 asaltos sin tirar por forzar (5.10), pagando el coste normal de Chispa de ese nivel. |

---

## 17. Progresión [N]

### 17.1 Experiencia (XP)
Al final de cada sesión, cada jugador gana **1 XP por cada «sí»**:
1. ¿Has venido y has jugado? (siempre sí)
2. ¿Superó el grupo un desafío importante (un combate difícil, un misterio, un viaje peligroso)?
3. ¿Descubrió el grupo algo nuevo sobre el Mundo Digital o sobre el villano?
4. ¿Actuó tu Tamer según su Emblema asumiendo un coste?
5. ¿Vivió tu pareja un Momento de Vínculo?
6. ¿Hizo el grupo un nuevo aliado o amigo?

Lo habitual son 3–5 XP por sesión. **Subes de nivel con 10 XP** (se gastan). Una campaña completa (nivel 1 a 10) dura unas 20–25 sesiones.

### 17.2 Niveles del Tamer (1–10)

| Nivel | Vínculo (máx.) | Ganas |
|---|---|---|
| 1 | 1 | Creación: Senda y talento inicial; 3 programas de Nivel 1 |
| 2 | 1 | Talento · +1 programa |
| 3 | 2 | +1 atributo · Avance del compañero · acceso a programas de Nivel 2 |
| 4 | 2 | Talento · +1 programa · +1 Carga |
| 5 | 3 | Avance del compañero · +1 habilidad (entrenar una nueva o hacer experta una entrenada) · Resonancia del Emblema (si ya tienes Vínculo 3) |
| 6 | 3 | +1 atributo · +1 programa · acceso a programas de Nivel 3 · puedes tomar talentos de otra Senda |
| 7 | 4 | Talento · Avance del compañero |
| 8 | 4 | +1 atributo · +1 programa · +1 Carga |
| 9 | 5 | Talento · Avance del compañero |
| 10 | 5 (★ con el arco del Emblema) | +1 atributo · Avance del compañero · +1 habilidad |

Máximo de atributo +3. Al subir Valor sube el Aguante; al subir Astucia, la Carga. **El Vínculo solo sube con el Momento de Vínculo** (5.2): la tabla indica el máximo posible a cada nivel. Al subir el Vínculo, el nivel estable y el máximo cambian según la tabla 5.2.

### 17.3 Talentos de Tamer (por Senda)
Se ganan en los niveles 2, 4, 7 y 9, de la propia Senda o de los generales (desde el nivel 6, uno de otra Senda).

| Senda | Talento | Efecto |
|---|---|---|
| Estratega | *Mando a distancia* | Tus Órdenes pueden dirigirse a cualquier compañero aliado a 1 zona de ti. |
| Estratega | *¡Combo!* | Nueva Orden: designa un enemigo; el siguiente impacto de un aliado contra él antes del final del asalto lo deja Expuesto. |
| Estratega | *Lectura del campo* | +2 a la iniciativa de tu pareja; antes del primer turno del combate puedes mover a tu compañero 1 zona. |
| Estratega | *Plan maestro* (nv. 6+) | 1 vez por combate, al inicio de un asalto, decides en qué fase actúa cada pareja aliada este asalto. |
| Estratega | *Doble orden* (nv. 7+) | 1 vez por asalto, das una segunda Orden (distinta) como acción gratuita. |
| Técnico | *Programa favorito* | Elige un programa: el primer uso en cada combate cuesta 0 Carga. |
| Técnico | *Hackeo de entorno* | Acción de Tamer: AST + Tecnología para crear o quitar Cobertura, desactivar una zona de Peligro o abrir o cerrar un paso. |
| Técnico | *Mecánico* | 1 vez por escena, un programa cuesta 1 Carga menos (mínimo 0). |
| Técnico | *Cortafuegos personal* | Reacción, 1 vez por asalto: gasta 1 Carga para anular un estado que vaya a sufrir tu compañero. |
| Técnico | *Codificador maestro* (nv. 7+) | Puedes usar dos programas distintos en el mismo turno con una sola acción (pagas ambos). |
| Protector | *¡Resiste!* | Nueva Orden: tu compañero gana Escudo = 2 × VF. |
| Protector | *Primeros auxilios digitales* | Acción: un Digimon aliado de tu zona recupera 1 dado de su poder + tu COR (1 vez por objetivo y combate). |
| Protector | *Inquebrantables* | Tú y tu compañero sois inmunes a Asustar mientras estéis en la misma zona; tu Tamer tiene +1 a su Defensa. |
| Protector | *Último bastión* (nv. 6+) | 1 vez por combate, cuando un compañero aliado a 1 zona de ti caería a 0 PV, se queda a 1 PV. |
| Protector | *Fortaleza del vínculo* (nv. 7+) | Tu compañero no sufre la regresión a Bebé II tras saltos de 2 niveles (sí tras DNA y digievolución forzada). |
| Batidor | *¡Por aquí!* | Nueva Orden: todos los compañeros aliados de tu zona se mueven 1 zona gratis sin provocar ataques de retirada. |
| Batidor | *Emboscador* | Si tu grupo sorprende al enemigo, todos los ataques aliados del primer asalto tienen +1. |
| Batidor | *Jinete* | Puedes montar a tu compañero si es Campeón o superior: os movéis juntos, tu Tamer tiene +2 a su Defensa y no queda Expuesto por terminar su turno en una zona con enemigos (6.11). |
| Batidor | *Superviviente* | +1 Aguante; Herido no te penaliza. Ventaja en tu papel de viaje (18.3). |
| Batidor | *Rastreador de datos* (nv. 6+) | 1 vez por combate, Analizar con 10+ automático; tu grupo no puede ser sorprendido mientras estés consciente. |
| Inspirador | *¡A por ellos!* | Nueva Orden: todos los compañeros aliados de tu zona tienen +1 a su próximo ataque este asalto. |
| Inspirador | *Corazón ardiente* | +1 Chispa máxima. |
| Inspirador | *Digievolución inspirada* | 1 vez por combate, una digievolución de tu compañero cuesta 1 Chispa menos (mínimo 1). |
| Inspirador | *Discurso* | +1 a Persuasión y Empatía; como acción de Tamer puedes intentar calmar a un Digimon salvaje en combate (COR + Empatía, 10+: no ataca durante 1 asalto; no vale con Jefes). |
| Inspirador | *Eco del Emblema* (nv. 6+) | Puedes usar la Resonancia del Emblema 2 veces por sesión. |
| General | *Duro de pelar* | +2 Aguante. |
| General | *Reflejos felinos* | +1 a la Defensa del Tamer. |
| General | *Domador/a* | Ventaja en Empatía con Digimon salvajes; empiezan un paso más amistosos. |
| General | *Políglota digital* | Entiendes y te haces entender por cualquier Digimon; +1 a Saber Digital. |
| General | *Coleccionista* | Al empezar cada aventura, +1 Disco de recuperación S y +1 objeto de 150 Bits o menos. |
| General | *Cocinero/a* | En un descanso corto con tu comida, todos los compañeros recuperan VF PV extra y se elimina Hambriento sin gastar comida (1 vez por sesión). |

### 17.4 Avances del compañero
Se aplican a **todas** sus formas. *(En la versión 1.0 se llamaban «Mejoras»; se renombran para no confundirlas con la palabra clave Mejora.)*

| Avance | Efecto | Límite |
|---|---|---|
| Entrenamiento ofensivo | +1 Atq | 1 vez |
| Entrenamiento defensivo | +1 Def | 1 vez |
| Robustez | +VF PV (el VF de la forma actual) | 2 veces |
| Reflejos | +1 Ini | 1 vez |
| Técnica heredada | Una técnica de una forma inferior se usa en todas las superiores con el dado actual y su potencia original; si era una Firma, como P2 (12.4) | Sin límite |
| Técnica perfeccionada | Una técnica gana una palabra clave del vocabulario (máximo 2) o sube de P1 a P2 | Una vez por técnica |
| Técnica nueva | Aprende una técnica genérica (12.4) o la de una Tarjeta Digimon que poseas (máximo P2) | Sin límite |
| Afinidad | Elimina una debilidad de familia de una forma, o gana Resistencia a un elemento en todas sus formas | 1 vez |
| Rama alternativa | Desbloquea otra forma de un nivel ya alcanzado (de su lista *next*) sin detonante | Sin límite |

---

## 18. Exploración, relaciones y Mundo Digital [N]

### 18.1 Escenas fuera de combate
Se juega por escenas. El DJ describe, los jugadores dicen qué hacen y **solo se tira cuando hay riesgo e incertidumbre**. Los compañeros también actúan (2.13). Los fallos dan Chispa (1 por escena) y siempre cambian algo (2.10). Para retos largos, relojes (2.11); para el grupo entero, pruebas de grupo (2.12).

### 18.2 Relaciones con Digimon (actitud)
Todo PNJ tiene una **actitud** hacia el grupo:

| Hostil | Recelosa | Neutral | Amistosa | Leal |
|---|---|---|---|---|
| −2 | −1 | 0 | +1 | +2 |

**Tirada social:** 2d6 + COR (o AST o VAL, según el enfoque) + Persuasión, Engaño o Empatía + **actitud**; −1 si el PNJ es de rango superior al compañero del Tamer («no se toma en serio a los críos»).
- **10+:** la actitud sube 1 paso y consigues lo que pides, si es razonable.
- **7–9:** elige: sube 1 paso **o** consigues lo que pides a cambio de algo (un favor, Bits, una prueba).
- **6–:** la actitud baja 1 paso o surge una complicación (y Chispa por fallo dramático si había tensión).
Un Digimon con Engranaje Negro, Espiral del Mal o Anillo Maligno no puede pasar de Hostil hasta que se le libere (20.8).

### 18.3 Viajes
Por cada jornada de viaje, cada jugador asume un **papel** y tira:

| Papel | Tirada | 10+ |
|---|---|---|
| Guía | AST o VAL + Supervivencia | Llegáis antes: un día menos, o un atajo. |
| Vigía | AST + Observación | Ningún encuentro os sorprende; vosotros sorprendéis. |
| Intendente | AST + Supervivencia o COR + Arte | Comida de sobra: nadie empieza Hambriento y todos tienen +1 en su primera tirada del día. |
| Ojeador | DES + Atletismo o AST + Saber Digital | Encontráis algo: un cofre de datos (d20 × 10 Bits), una pista o un aliado. |

Con 7–9 no pasa nada especial. **Con 6–, el DJ tira (o elige) en la tabla de eventos.** Si nadie falla, el DJ puede tirar una vez al día con un resultado suave. Con más de 4 jugadores, se repiten papeles (el segundo Vigía da Ayuda +1).

**Eventos de viaje (d12)**

| d12 | Evento |
|---|---|
| 1 | Tormenta de datos: refugio (Supervivencia 7+) o −1 Aguante a cada Tamer. |
| 2 | Glitch: la zona se reescribe y os perdéis (+1 día) salvo AST + Tecnología 7+. |
| 3 | Digimon salvajes territoriales (encuentro, actitud Recelosa). |
| 4 | Un Digimon herido pide ayuda (Medicina; posible aliado). |
| 5 | Mercader ambulante (objetos con un 20 % de recargo). |
| 6 | Ruinas con un terminal antiguo (Saber Digital: pista sobre la trama). |
| 7 | Comida escasa: los compañeros empiezan mañana Hambrientos salvo Supervivencia 7+. |
| 8 | Emboscada: un pelotón de esbirros del nivel de la región. |
| 9 | Puerta digital inestable: con Tecnología 10+ es un atajo. |
| 10 | Aldea Digimon en fiesta: descanso largo gratis y un rumor. |
| 11 | Rastro de Engranajes Negros o de una Torre Oscura: si se ignora, el reloj del villano avanza 1. |
| 12 | Presagio: un Legendario os observa desde lejos… y se va. |

**Clima digital (d6):** 1 lluvia de datos (−1 a Observación; zonas abiertas cuentan como Agua para los combos) · 2 niebla binaria (todas las zonas tienen Cobertura) · 3 tormenta eléctrica (técnicas de Eléctrico +1 dado; los que vuelan −1 Def) · 4 despejado · 5 calor de servidor (Fuego +1 dado; Hielo −1 dado) · 6 aurora de código (al acampar, cada Tamer gana 1 Chispa).

### 18.4 Persecuciones
Medidor de **Distancia de 0 a 6**; empieza en 3 (2 si están muy cerca, 4 si hay ventaja).
Cada asalto, el **líder** del grupo (o cada pareja, si van separadas) tira **2d6 + Ini de su compañero − Ini del rival más rápido** (o DES + Atletismo − rango del rival más rápido, a pie). Los demás pueden ayudar (+1) o crear un obstáculo con una tirada propia (con 10+, +1 Distancia extra).
- **10+:** +1 Distancia y una ventaja (atajo, esconderse, trampa).
- **7–9:** +1 Distancia con un coste (alguien recibe un ataque P1, se pierde algo, os separáis), o 0 sin coste.
- **6–:** −1 Distancia y una complicación.
**6 = escapáis** (o alcanzáis, si perseguís). **0 = os alcanzan:** combate, y el perseguido empieza en la fase lenta. Quien vuela, en terreno abierto, tira con Ventaja.

### 18.5 El Mundo Digital
**Regiones de ejemplo (d8)**

| d8 | Región | Nivel típico | Familias frecuentes |
|---|---|---|---|
| 1 | Ciudad del Comienzo (zona segura, cuna de Digi-Huevos) | Bebés | — |
| 2 | Bosque Nativo | Novato–Campeón | Naturaleza, Bestia |
| 3 | Desierto de Datos | Campeón | Saurio, Máquina, Anomalía |
| 4 | Costa del Mar de Código | Novato–Perfecto | Acuático |
| 5 | Ciudad Juguete y Fábrica de Metal | Campeón–Perfecto | Juguete, Máquina |
| 6 | Montaña Infinita | Perfecto | Dragón, Ave |
| 7 | Ruinas del Cortafuegos | Perfecto–Definitivo | Caballero, Sagrado, Arcano |
| 8 | Zona Oscura | Definitivo | Oscuro, Anomalía, Legendarios |

**Encuentros del Bosque Nativo (d20)**

| d20 | Encuentro | Actitud |
|---|---|---|
| 1–2 | Pelotón de 4 Goblimon (esbirros Novato) | Hostil |
| 3 | Kuwagamon (Campeón) | Hostil |
| 4 | 2 Gotsumon | Recelosa |
| 5 | Palmon y Floramon, perdidas | Amistosa |
| 6 | 3 Numemon (esbirros Campeón) | Recelosa |
| 7 | Elecmon, guardián de Digi-Huevos | Recelosa |
| 8 | Tentomon curioso | Neutral |
| 9 | Ogremon, rival bravucón | Hostil |
| 10 | Leomon, mentor | Neutral |
| 11 | 2 Kokuwamon | Neutral |
| 12 | Snimon | Hostil |
| 13 | Woodmon | Hostil |
| 14 | 3 Mushroomon bromistas | Recelosa |
| 15 | Unimon con Engranaje Negro | Hostil (liberable) |
| 16 | Monochromon territorial | Recelosa |
| 17 | Biyomon | Amistosa |
| 18 | Drimogemon excavando | Neutral |
| 19 | Devimon (presagio; huye tras 2 asaltos) | Hostil |
| 20 | Andromon, Perfecto perdido y sin memoria | Neutral |

**Encuentros de Ciudad Juguete y Fábrica de Metal (d12):** 1–2 pelotón de 4 PawnChessmon · 3 Guardromon de patrulla (Recelosa) · 4 Tankmon averiado (Neutral; Tecnología para repararlo) · 5 Monzaemon triste (Amistosa) · 6 Hagurumon con Engranaje Negro (liberable) · 7 Mekanorimon pilotado por nadie (Hostil) · 8 Andromon guardián (Neutral) · 9 3 Numemon en las tuberías · 10 Clockmon con un mensaje del futuro · 11 Puppetmon jugando a ser rey (Jefe, Hostil) · 12 Machinedramon en el horizonte (presagio).

### 18.6 Peligros ambientales
| Peligro | Tirada para evitarlo | Fallo |
|---|---|---|
| Caída, desprendimiento | DES o VAL + Atletismo | Leve 1 / Serio 2 / Grave 3 Aguante |
| Río de datos, corriente | VAL + Atletismo (−1 a −2) | Arrastrado a otra zona y Serio 2 |
| Zona glitch | AST + Tecnología o Saber Digital | Perdidos: +1 día o separados del grupo |
| Frío, calor o tormenta | VAL + Supervivencia | −1 Aguante por jornada y compañeros Hambrientos |
| Datos corruptos | COR + Empatía (el compañero tiembla) | El compañero queda Confundido en el siguiente combate de la jornada |

### 18.7 Comida, descanso y Bits
- Cada día, cada Tamer y cada compañero necesitan una comida (4.5); una comida para el grupo en una aldea cuesta unos 20 Bits. Un **Tamer que no ha comido** en el día tiene −1 a sus tiradas físicas hasta que coma.
- El descanso largo exige un lugar seguro: una posada (10 Bits), una tienda de campaña o una aldea Amistosa.

---

## 19. Amenazas: esbirros, élites, jefes, legendarios y hordas [N]

### 19.1 Niveles de amenaza
Todas las fichas del bestiario son **Estándar**. El DJ aplica una **plantilla de amenaza** al usarlas como enemigo (el bestiario solo sugiere una en `amenaza_sugerida`). **N** = número de parejas Tamer-Digimon del grupo.

| Amenaza | PV | Atq | Def | Arm | Ini | Acciones | Dados | PA | Reglas |
|---|---|---|---|---|---|---|---|---|---|
| **Esbirro** | ceil(PV / 4) | −1 | −1 | 0 | 0 | 1 | — | 0.25 | No usa P3: su Firma se usa como P2. Daño fijo: VF por dado (VF + 1 por dado si el PJ saca 6– al defenderse). Huye si cae su líder. Se pueden agrupar en Pelotones de 3 a 6: un solo perfil, PV = suma; cada vez que pierde los PV de un esbirro, cae uno; ataca una vez por asalto con +1 dado por cada miembro por encima del primero (máximo +2); las técnicas de área le hacen daño doble. |
| **Estándar** | PV | 0 | 0 | 0 | 0 | 1 | — | 1 | — |
| **Élite** | floor(PV * 1.5) | +1 | +1 | 0 | +1 | 1 | — | 2 | 1 reacción por asalto: Contraataque con su técnica básica cuando un PJ saca 6– atacándole, o Proteger a un aliado. |
| **Jefe** | floor(PV * (N + 2) / 2); con refuerzo, floor(PV * (N + 3) / 2) | +1 | +1 | +1 | +2 | ceil(N / 2); con refuerzo, más (19.4) | — (Refuerzo II: +1) | N (reforzado: cuenta un nivel más) | Ver 19.4. |
| **Legendario** | floor(PV * (N + 3) / 2) | +1 | +1 | +1 | +2 | ceil(N / 2) | +1 | 2 * N | Ver 19.5. Nunca lleva refuerzo. |

**Índice de amenaza:** cada ficha del bestiario imprime «Amenaza: baja / media / alta», calculada por el generador a partir de su daño esperado, su Arm, sus resistencias y lo fácil que es impactarla, comparada con las demás fichas de su fila. Los PA de esa ficha se multiplican por **×¾ (baja), ×1 (media) o ×1½ (alta)**. Así, dos Jefes del mismo nivel no cuentan igual: Myotismon es «alta» y Etemon, «baja».

### 19.2 Presupuesto de encuentro
**Nivel de referencia (nivel de combate del grupo):** el nivel que **la mayoría de los compañeros puede alcanzar en el asalto 1** con la Chispa que tiene su Tamer al empezar el combate: **nivel estable + 1 por cada 2 Chispa**, contando solo formas desbloqueadas y sin pasar del máximo del Vínculo. Al empezar una sesión (Chispa = Vínculo):

| Vínculo | 1 | 2 | 3 | 4 | 5 y ★ |
|---|---|---|---|---|---|
| Nivel de referencia | Novato | Campeón | Perfecto | Definitivo si está desbloqueado (si no, Perfecto) | Definitivo |

Si el grupo llega a un combate con más o menos Chispa (la gastó, la acumuló), recalcula el nivel de referencia con la que tenga.

**PA de un enemigo = PA de su amenaza × factor por diferencia de rango con el nivel de referencia × modificador de su índice de amenaza** (×¾ / ×1 / ×1½, 19.1):

| Diferencia | −3 o menos | −2 | −1 | 0 | +1 | +2 | +3 o más |
|---|---|---|---|---|---|---|---|
| Factor | ×⅛ | ×¼ | ×½ | ×1 | ×2 | ×5 | ×15 (Mortal) |

*Más de 2 pelotones de esbirros contra compañeros 3 o más rangos por encima no se tiran: se narran (19.3).*

| Dificultad | PA totales | Qué esperar (simulación de la versión 1.1, 4 parejas a Vínculo 1, sin programas ni objetos) |
|---|---|---|
| Fácil | N ÷ 2 | 2,1–2,6 asaltos; sin riesgo. |
| Normal | N | 2,7–3,0 asaltos; una o dos digievoluciones (de media en el asalto 1,5–1,8, tras una Crisis). |
| Difícil | 1,5 × N | 3,4–3,7 asaltos; alguna forma temporal cae, pero el grupo no pierde. |
| Épico | 2 × N | El Jefe de la aventura (tabla siguiente): de 3 a 5 asaltos y de 0 a 28 % de derrota según el Vínculo y el Jefe. |
| Mortal | más de 2 × N | Ofrece siempre la huida o un objetivo de escena. |

*Ejemplo:* 4 Tamers de Vínculo 1 (nivel de referencia Novato). Normal = 4 PA: Kuwagamon (Campeón, +1, amenaza media: 1 × 2 × 1 = 2 PA) + Gizamon (Novato, media: 1 PA) + un pelotón de 4 Mushroomon esbirros (4 × ¼ × 1 = 1 PA). Es la receta del **episodio de digievolución** (solo a Vínculo 1): un encuentro Normal al nivel de referencia con un enemigo de un nivel más.

**El Jefe de la aventura** vale **2N PA (Épico)** y se elige según el Vínculo de la mayoría del grupo. Desde Vínculo 2 el Jefe es **del nivel de referencia** con un **refuerzo** (19.4), porque un Jefe un nivel por encima de lo que el grupo puede alcanzar es Mortal (75 % de derrota a Vínculo 2 contra un Jefe Perfecto sin el Perfecto desbloqueado). Un Jefe reforzado cuenta, para el presupuesto, como un nivel por encima del de referencia.

| Vínculo del grupo | Jefe de la aventura | Plantilla | Medido (asaltos; derrota) |
|---|---|---|---|
| 1 | Campeón (referencia + 1) | Jefe | 5,0–5,3; 1–3 % (hasta 14 % con el Jefe más duro) |
| 2 | Campeón | Jefe con Refuerzo I | 3,6–3,8; 2–10 % |
| 3 | Perfecto | Jefe con Refuerzo I | 4,3–4,7; 16–28 % |
| 4 sin Definitivo desbloqueado | Perfecto | Jefe con Refuerzo I | 4,3–4,8; 13–27 % |
| 4 con Definitivo desbloqueado | Definitivo | Jefe con Refuerzo II | 3,0–4,3; 3–26 % |
| 5 | Definitivo | Jefe con Refuerzo II | 2,9–4,1; 0–10 % |
| ★ | Definitivo | Legendario (sin refuerzo) | 3,8–4,4; 7–22 % |

*Las horquillas son las medias de las líneas Adventure, Tamers y Savers; entre Jefes del mismo nivel hay mucha más diferencia (por ejemplo, a Vínculo 3, Myotismon 60–97 % y Etemon 0 %): aplica siempre el modificador del índice de amenaza y, con un Jefe de amenaza alta, ofrece un objetivo de escena.*

### 19.3 Esbirros y pelotones (hordas)
- **Esbirro:** ¼ de los PV (redondeo hacia arriba), −1 Atq y −1 Def, **daño fijo**, no usa P3 (su Firma va como P2) y huye si cae su líder.
- **Pelotón (horda) de 3 a 6 esbirros iguales:** un solo perfil. PV = la suma de los PV de esbirro; cada vez que pierde el equivalente a un esbirro, cae uno (el daño sobrante pasa al siguiente). Ataca **una vez por asalto** con **+1 dado por cada miembro por encima del primero (máximo +2)**. Las técnicas de área le hacen **daño doble**. Cuenta como un enemigo a efectos de iniciativa y de los estados (un estado afecta a todo el pelotón).
- **Hordas inferiores:** contra un esbirro o un pelotón **2 o más rangos por debajo** del atacante, **cualquier técnica cuenta como de área** a efectos del daño doble, y **cada impacto elimina como mínimo tantos miembros como rangos de diferencia**. Así un Definitivo sin técnica de área no tarda nueve asaltos en limpiar a 24 Goblimon.
- **Hordas que no se tiran:** más de 2 pelotones contra compañeros 3 o más rangos por encima se **narran**: el grupo los barre (con un coste del menú de 2.9 si el DJ quiere) y la escena sigue.
- **Manada grande** (más de 6): divide en varios pelotones.

### 19.4 Anatomía de un Jefe [N; las partes marcadas, A]
1. **Turno = asalto:** el turno de un Jefe es el **asalto completo**. Sus estados avanzan una vez por asalto (al inicio de su 1.ª acción), su daño por turno (Quemar, Veneno, invocaciones) se le aplica **una vez por asalto** y todas sus duraciones («1 turno», «hasta su próximo turno») se cuentan en asaltos.
2. **Acciones:** ⌈N/2⌉ acciones por asalto (más con refuerzo, punto 3). La 1.ª en la fase enemiga; la 2.ª al final del asalto (tras la fase lenta); la 3.ª y siguientes, al principio del asalto siguiente. **Agotadora:** no usa su Firma (ni otra técnica Agotadora) dos veces en el mismo asalto ni en dos asaltos seguidos.
3. **Refuerzo según el Vínculo** (para el Jefe de la aventura, 19.2): el refuerzo no se suma a la plantilla Legendario.

| Vínculo de la mayoría | Refuerzo | PV | Acciones por asalto | Dados |
|---|---|---|---|---|
| 1 | ninguno (Jefe un nivel por encima) | floor(PV × (N + 2) / 2) | ⌈N/2⌉ | — |
| 2–3 (y 4 sin Definitivo desbloqueado) | **Refuerzo I** | floor(PV × (N + 3) / 2) | ⌈N/2⌉ + 1 | — |
| 4 con Definitivo desbloqueado, y 5 | **Refuerzo II** | floor(PV × (N + 3) / 2) | N | +1 en todas sus técnicas |

4. **Inmunidades:** Aturdir y Dormir le quitan **una sola** acción del asalto (si solo le queda una, queda Ralentizado). Congelado y Atrapado le duran como máximo 1 asalto. Inmune a Ejecutar (en su lugar, +1 dado).
5. **Fases con escudo de fase:** 2 fases, con el umbral en la mitad de sus PV. El daño que sobrepasa el umbral **se pierde** (no se puede saltar una fase de un golpe).
6. **Furia (al cruzar el umbral):** elimina sus estados, su Firma queda lista, sus técnicas ganan **+1 dado** el resto del combate y **cada Tamer gana 1 Chispa** («¡no podemos rendirnos ahora!»). Si tiene Modos, **cambia de Modo** (Jupitermon → Jupitermon: Wrath Mode; Belphemon: Sleep Mode → Rage Mode): usa la nueva ficha conservando el daño.
7. **Firma telegrafiada** [A]: su Firma P3 tiene siempre *Cargado*. **Carga con una acción** (el DJ anuncia qué hará y a qué zona) y **la lanza con la 1.ª acción del asalto siguiente**, así que todo el grupo tiene un turno para responder. **Guardia de carga** = PV base de su nivel ÷ 2 (Novato 10, Campeón 14, Perfecto 17, Definitivo 21): si antes de que la lance el grupo le inflige ese daño, o le aplica Aturdir o Sellar con 10+, la carga se rompe, queda **Expuesto** (7.3: +1 a los ataques de los PJ contra él hasta el final del asalto siguiente) y no puede volver a cargarla en esta fase.
8. **Punto débil** [A]: todo Jefe tiene uno que se descubre con Analizar 10+ o investigando antes del combate: un elemento extra al que es débil, una parte destructible (cuernos, cañón, alas: 2 × VF de daño la rompen y anulan una técnica) o una ventana (tras lanzar su Firma queda Expuesto).
9. **Objetivos de escena** [A]: el combate puede ganarse de otra forma (desactivar la Torre, liberar a los rehenes, purificar el Engranaje): reloj de 4–6 segmentos que los Tamers avanzan con *Actuar en el entorno*.

### 19.5 Legendarios
Plantilla **Legendario** = todas las reglas de Jefe (sin refuerzo), más: PV × (N + 3) / 2, **+1 dado** en todas sus técnicas, **3 fases** (umbrales a 2/3 y 1/3 de sus PV, cada una con escudo de fase y Furia) y el **Dominio** de su grupo. Vale 2N PA al nivel de referencia: es el clímax de Vínculo ★ (3,8–4,4 asaltos y 7–22 % de derrota medidos; contra Vínculo 5, 3,7–4,4 asaltos y 0–6 %). Solo se aplica a PNJ: un compañero que llega a Gallantmon o a Beelzemon usa la ficha base.

| Grupo | Dominio | Regla |
|---|---|---|
| **Caballeros Reales** | Código caballeresco | Inmunes a Asustar, Encantar, Confundir y Dormir. Una vez por asalto, cuando un PJ falla (6–) un ataque contra ellos, contraatacan con su técnica básica sin tirada. |
| **Señores Demonio** | Pecado capital | Según el demonio: Orgullo (Lucemon) — los PJ no pueden darse Ayuda; Ira (Creepymon) — todas las técnicas de la escena, las suyas incluidas, +1 dado; Envidia (Leviamon) — cada vez que un compañero digievoluciona, recupera 2 × VF PV; Lujuria (Lilithmon) — al empezar cada asalto, un compañero a su elección queda Encantado; Pereza (Belphemon) — todos los PJ empiezan el combate en la fase lenta; Avaricia (Barbamon) — cada vez que un Tamer gasta Chispa, el DJ gana 1 punto de Codicia que puede gastar para dar +1 dado a una técnica; Gula (Beelzemon, Ogudomon) — todas sus técnicas tienen Drenar. |
| **Olimpo XII** | Dominio divino | En la zona que ocupa, +1 a todas sus tiradas y Resistencia al elemento de su Firma; cada fase cambia el terreno según su dios. |
| **Bestias Sagradas** | Guardián cardinal | Regenera VF PV al empezar cada asalto e ignora la debilidad de su familia. |
| **Grandes Ángeles** | Coro celestial | Sus aliados tienen +1 Def; todas sus técnicas tienen además Purificar. |
| **Guerreros Antiguos** | Legado ancestral | Al empezar cada asalto elige un elemento: es inmune a él hasta el siguiente asalto. Sus técnicas ignoran Resistencias. |
| **Amenazas finales** | Catástrofe | Al empezar cada asalto, los PJ de una zona a su elección reciben VF de daño sin tirada (menos Arm) o sufren el estado por defecto de su elemento (sin control duro). |

**Lista curada de Legendarios** (126 fichas; el bestiario las marca como `amenaza_sugerida: legendario`). Como los nombres de Digimon se repiten en los datos, `spec_fichas.json` guarda esta lista **por id**; aquí se dan los nombres. **Cada variante X y cada Modo figura uno a uno**: no se deduce ninguno. Todas son de nivel Definitivo salvo las marcadas.

- **Caballeros Reales (34):** Alphamon, Alphamon: Ouryuken, Craniamon, Craniamon (X Antibody), Dynasmon, Dynasmon (X Antibody), Examon, Examon (X Antibody), Gallantmon, Gallantmon (X Antibody), Gallantmon: Crimson Mode, Gankoomon, Gankoomon (X Antibody), Jesmon, Jesmon (X Antibody), Jesmon GX, Kentaurosmon, Kentaurosmon (X Antibody), Leopardmon, Leopardmon (X Antibody), Leopardmon: Leopard Mode, LordKnightmon, LordKnightmon (X Antibody), Magnamon (X Antibody), Magnamon (nivel Armadura, fila de Definitivo; un compañero que lo alcanza usa la ficha base), Omnimon, Omnimon (X Antibody), Omnimon Alter-B, Omnimon Alter-S, Omnimon Zwart, Omnimon Zwart Defeat, Omnimon: Merciful Mode, UlforceVeedramon, UlforceVeedramon (X Antibody).
- **Señores Demonio (21):** Lucemon: Chaos Mode (Perfecto), Lucemon: Satan Mode, Lucemon: Larva, Lucemon (X Antibody), Leviamon, Leviamon (X Antibody), Creepymon, Creepymon (X Antibody), Lilithmon, Lilithmon (X Antibody), Belphemon: Sleep Mode, Belphemon: Rage Mode, Belphemon (X Antibody), Barbamon, Barbamon (X Antibody), Beelzemon, Beelzemon (2010 Anime Version), Beelzemon: Blast Mode, Beelzemon (X Antibody), Ogudomon, Ogudomon (X Antibody).
- **Olimpo XII (19):** Jupitermon, Jupitermon: Wrath Mode, Junomon, Junomon: Hysteric Mode, Neptunemon, Apollomon, Apollomon:Whispered, Dianamon, Marsmon, Minervamon, Minervamon (X Antibody), Venusmon, Vulcanusmon, Ceresmon, Bacchusmon, Plutomon, ZombiePlutomon, Merukimon, Mervamon.
- **Bestias Sagradas (6):** Azulongmon, Zhuqiaomon, Baihumon, Ebonwumon, Fanglongmon, Fanglongmon: Ruin Mode.
- **Grandes Ángeles (9):** Seraphimon, Ophanimon, Ophanimon (X Antibody), Ophanimon: Falldown Mode, Ophanimon: Falldown Mode (X Antibody), Cherubimon (Good), Cherubimon (Good) (X Antibody), Cherubimon (Black), Cherubimon (Black) (X Antibody).
- **Guerreros Antiguos (10):** AncientGreymon, AncientGarurumon, AncientKazemon, AncientBeetlemon, AncientMegatheriummon, AncientTroymon, AncientSphinxmon, AncientMermaimon, AncientVolcanomon, AncientWisemon.
- **Amenazas finales (27):** Apocalymon, Armageddemon, Diaboromon, Diaboromon (X Antibody), Millenniummon, ZeedMillenniummon, MoonMillenniummon, Quartzmon, King Drasil_7D6, Chaosmon, Chaosmon: Valdur Arm, UltimateChaosmon, MaloMyotismon, NEO (nivel Indeterminado, fila de Definitivo), DeathXmon, Susanomon, GraceNovamon, Imperialdramon: Paladin Mode, Bagramon, DarknessBagramon, Abbadomon, Abbadomon Core, Ordinemon, Galacticmon, Mastemon, Raguelmon, Eosmon (solo la ficha Definitivo; las de Campeón y Perfecto son estándar).

Un **Legendario de nivel Perfecto** (Lucemon: Chaos Mode) o un Jefe de cualquier nivel puede usar su Firma de Zona como **Total** (plantilla, 11.3), aunque el bestiario solo imprima Total en Firmas de rango 4.

**Jefes sugeridos** (27 fichas, `amenaza_sugerida: jefe`): Amos Oscuros (Definitivo): MetalSeadramon, Puppetmon, Machinedramon, Piedmon; Doce Devas (Perfecto): Kumbhiramon, Vajramon, Mihiramon, Antylamon (Deva), Majiramon, Sandiramon, Indramon, Pajiramon, Makuramon, Sinduramon, Caturamon, Vikaralamon; villanos clásicos: Devimon (Campeón), Etemon, Myotismon, Kimeramon, Arukenimon, Mummymon (Perfecto), KingEtemon, VenomMyotismon, Diaboromon, BlackWarGreymon, Parasimon, Ghoulmon, Beelzemon (Definitivo). *(Diaboromon y Beelzemon figuran también entre los Legendarios, y esa marca manda: por eso son 27 fichas y no 29. Daemon no existe con ese nombre en los datos: es Creepymon, que ya figura entre los Señores Demonio.)*
**Esbirros naturales** (20 fichas, `amenaza_sugerida: esbirro`): Goblimon, Gizamon, PawnChessmon (Black), PawnChessmon (White), Gotsumon, Otamamon, Kokuwamon, Commandramon, Mushroomon, Floramon, Syakomon, Hagurumon (Novato); Bakemon, Numemon, Tankmon, Troopmon, Snimon, Flymon, DarkLizardmon, Sukamon (Campeón).

### 19.6 Tamers rivales
Un Tamer rival actúa en la fase enemiga junto a su Digimon: da +1 (Orden) a su compañero y tiene 1 o 2 programas (con el mismo efecto que los de los PJ). Su compañero digievoluciona cuando la historia lo pide, sin contar Chispa (el DJ lo anuncia: «¡su Digivice brilla!»). Un rival tiene Aguante 6 y se rinde o huye al quedar a 0.

---

## 20. Reglas opcionales avanzadas [O]

Cada módulo es independiente. Ninguno es necesario para la aventura de inicio. Recomendación: activar **un módulo por arco** de campaña.

### 20.1 Armadura (Digi-Huevos)
*Requisito:* poseer el Digi-Huevo y un **D-3** (o un permiso de la historia).
- Solo desde **Novato**. Cuesta **2 Chispa** (como subir un nivel), **no depende del Vínculo** (es un poder prestado: la forma Armadura es de rango 2, el de Campeón, aunque el máximo del Vínculo sea Campeón) y **no da hambre**.
- **No se puede activar en el asalto 1** de un combate, salvo como digievolución de emergencia (5.8, +1 Chispa). Cuenta como digievolución para el límite de una por asalto.
- El compañero adopta la ficha de la forma Armadura del bestiario (**nivel Armadura = fila de Campeón**). Su ficha ya incluye Resistencia al elemento de su Firma; además, mientras dure, resiste el elemento de su Digi-Huevo.
- Dura la escena. A 0 PV vuelve a Novato con sus PV guardados y **queda Agotado**, como cualquier forma temporal, y además el huevo queda descargado hasta un descanso corto.
- Desde una forma Armadura **no se puede digievolucionar** a otro nivel.
- **Funciona aunque la digievolución normal esté bloqueada** (Agujas de Control, Sellado): es la gran baza de las campañas «02».
- **Huevos dorados** (Milagros, Destino): **respetan el máximo del Vínculo** y cuestan **2 Chispa por cada nivel por encima de Novato** de la fila que usan: Rapidmon (Armadura) y GoldVeedramon usan la fila de **Perfecto** (4 Chispa, desde Vínculo 2); Magnamon, la de **Definitivo** (6 Chispa, desde Vínculo 4). Al terminar la escena provocan la regresión a Bebé II (5.7), como cualquier salto de 2 o más niveles.
- *Medido (equipo «02» a Vínculo 1 contra Jefe Campeón):* con Armadura, 3,2–5,2 asaltos y 0–5 % de derrota, primera Armadura de media en el asalto 2,1–2,4; con digievolución normal, 5,0 asaltos y 2 %.

| Digi-Huevo | Elemento | Forma de referencia |
|---|---|---|
| Valor | Fuego | Flamedramon |
| Amistad | Eléctrico | Lighdramon |
| Amor | Viento | Halsemon |
| Sabiduría | Tierra | Digmon |
| Pureza | Planta | Shurimon |
| Sinceridad | Agua | Submarimon |
| Fiabilidad | Agua | Submarimon |
| Esperanza | Luz | Pegasusmon |
| Luz | Luz | Nefertimon |
| Bondad | Mental | a elección del DJ |
| Milagros (dorado) | Luz | Magnamon |
| Destino (dorado) | Acero | Rapidmon (Armadura), GoldVeedramon |

Qué forma sale con cada huevo: una forma Armadura cuya lista *prev* incluya al Novato, a elección del jugador y del DJ. Las demás formas Armadura del bestiario (Allomon, Pteramon, Kabukimon, Sheepmon…) se asignan al huevo cuyo elemento encaje con su Firma.

### 20.2 Espíritus (Híbridos)
Variante de campaña («Guerreros Legendarios») o recurso de trama: **el propio Tamer** se transforma usando un Espíritu guardado en un D-Tector.
- **Campaña de Espíritus:** los Tamers no tienen compañero; su Espíritu hace de compañero. Se usan las mismas reglas de Chispa, Vínculo (sintonía con el Espíritu) y Dado de Vínculo. Mientras está transformado, el Tamer **es** la criatura: usa la ficha del Híbrido, tiene **una acción de Digimon** por turno y solo las acciones gratuitas de Tamer. El Aguante del Tamer queda protegido bajo los PV del Híbrido.
- **Campaña mixta:** un Tamer con compañero que obtiene un Espíritu puede transformarse; mientras tanto su compañero se retira de la escena (o se funde con él, si el DJ quiere).
- **Atributo:** Variable mientras dure la transformación (rasgo *Espíritu legendario*).
- **A 0 PV:** el Tamer recupera su forma humana, pierde 2 Aguante y queda Agotado.

| Espíritu | Coste | Requisito | Fila | Formas del bestiario |
|---|---|---|---|---|
| Forma base | 0 | — | Novato | Flamemon, Strabimon |
| Humano | 2 | Vínculo 1 | Campeón | Agunimon, Arbormon, Beetlemon, Duskmon, Grumblemon, Kazemon, Kumamon, Lanamon, Lobomon, Loweemon, Mercurymon |
| Bestia | 3 | Vínculo 2 | Perfecto | BurningGreymon, Calmaramon, Gigasmon, JagerLoweemon, KendoGarurumon, Korikakumon, MetalKabuterimon, Petaldramon, Sephirothmon, Velgrmon, Zephyrmon |
| Fusión (Humano + Bestia) | 4 | Vínculo 3 | Perfecto, con la plantilla Fusión (+1 Atq, +1 Def) | Aldamon, Beowolfmon, DaiPenmon, JetSilphymon, Rhihimon, RhinoKabuterimon |
| Unificado | 6 | Vínculo 5 o trama | Definitivo | EmperorGreymon, MagnaGarurumon |

**Espíritu salvaje:** las tres primeras veces que se usa un Espíritu de Bestia, al empezar cada turno se tira 2d6 + COR: con 6– el Híbrido ataca a la criatura más cercana (la elige el DJ). *(En los datos, varios Híbridos aparecen marcados como «modo»: no son Modos y no usan las plantillas de Modo.)*

### 20.3 DNA / Jogress (fusión de dos compañeros)
- **Requisitos:** dos compañeros en la misma zona y del mismo nivel; ambos Tamers con Vínculo 2+ (resultado Perfecto) o 4+ (resultado Definitivo); una forma DNA aprobada (en su lista *prev* figuran ambas formas, o el DJ lo permite). La **primera vez** hace falta que la pareja de Tamers haya hecho antes un Ataque conjunto con éxito o que vivan un Momento de Vínculo compartido.
- **Coste:** cada Tamer paga **2 Chispa** (resultado Perfecto) o **3 Chispa** (resultado Definitivo). Es una acción gratuita de ambos Tamers al comienzo del turno de cualquiera de ellos.
- **Resultado:** la forma DNA (un nivel por encima de los componentes) con **PV × 1,5**. **Actúa en el turno de cada uno de los dos Tamers** (dos acciones por asalto; solo una técnica P3 por asalto). Ambos Tamers conservan sus acciones y cada uno puede usar su Dado de Vínculo en las tiradas de la forma DNA.
- **Fin:** al final de la escena o a 0 PV, se separa en los dos compañeros con sus PV guardados; si fue por 0 PV, ambos quedan Agotados. Al terminar la escena, ambos sufren la regresión a Bebé II (5.7).
- La primera fusión DNA cuenta como Momento de Vínculo para los dos Tamers.

### 20.4 Modos
Los Digimon marcados como *modo* en los datos (salvo los Híbridos) son formas alternativas de la misma especie. El bestiario les aplica una de tres plantillas (cap. 21):
- **Modo alterno** (Imperialdramon: Dragon Mode ↔ Fighter Mode, Leopardmon ↔ Leopard Mode…): cambiar de modo **gasta el movimiento** y conserva el daño recibido (PV = PV máximos de la nueva ficha − daño acumulado). Para un compañero, cambiar a un modo alterno de su forma actual es gratis si ya lo tiene desbloqueado.
- **Modo Supremo** (*Burst Mode, Crimson Mode, Paladin Mode, Merciful Mode, Superior Mode, Blast Mode, Itto Mode, Awakened, Promote, GX, Takemikazuchi, Holy Mode, Alter-S*): plantilla Supremo (+1 Atq, +1 Def, +VF PV). Para un compañero: requiere Vínculo ★ o una Tarjeta Dorada, cuesta **4 Chispa**, dura hasta el final de la escena y al terminar deja al compañero Agotado y en regresión a Bebé II.
- **Modo Oscuro** (*Ruin, Rage, Wrath, Hysteric, Fury, Satan, Destroy, Chaos, Falldown, Vicious Mode, Zwart Defeat, Alter-B, Whispered*): plantilla Oscuro (+1 Atq, +1 Def, +VF PV, +1 dado y −1 Def contra Luz). Un compañero solo llega a él por digievolución oscura (5.10) y entonces lo controla el DJ.
- **Jefes con Modos:** cambian de Modo al entrar en Furia (19.4).

### 20.5 X-Antibody
- **En el bestiario:** las 120 fichas X llevan la plantilla X (+1 Atq, +VF PV) y el rasgo **Anticuerpo X:** inmune a Sellar y a Ejecutar; una vez por combate, si es un PJ, repite una tirada de Defensa; si es un PNJ, obliga a un PJ a repetir un 10+ obtenido contra él.
- **Para un compañero («Evolución X»):** tras un hito de la historia (exposición al Programa X), el compañero obtiene el Anticuerpo X: a partir de entonces usa la versión X de cada forma si existe en el bestiario o, si no, aplica la plantilla X a la ficha normal. Recomendado como recompensa de mitad de campaña (nivel 5+).

### 20.6 Digimon salvajes como compañeros
- **Aliado temporal:** un Digimon con actitud **Leal** puede acompañar al grupo durante una aventura. Lo manejan los jugadores por turnos (actúa en la fase lenta), sin Chispa ni Dado de Vínculo y sin digievolucionar (salvo por la historia). Para el presupuesto, suma sus PA a N.
- **Nuevo compañero:** si un compañero se pierde (Borrado, 20.12), si llega un jugador nuevo o si la historia lo pide, un Digimon salvaje con actitud Leal puede convertirse en compañero tras un **Momento de Vínculo** y la activación de un Digivice. Empieza con **Vínculo 1** (o el Vínculo anterior −2, mínimo 1, si es un reemplazo); el Tamer conserva su nivel.
- **Reclutamiento con Xros Loader:** los Digimon Leales de rango inferior al compañero pueden guardarse (cap. 15).
- **Variante «Solo Digimon»:** cada jugador lleva un Digimon salvaje, sin Tamer. El Digimon usa además los atributos y habilidades de un Tamer (Valor, Astucia, Corazón, Destreza) para las escenas fuera de combate, tiene Chispa (su determinación), un Vínculo con el grupo (sube con Momentos de Vínculo del grupo) y el Dado de Vínculo se lo puede dar **otro jugador** a su Digimon (un DV por jugador y asalto, nunca a sí mismo). Las reglas de digievolución no cambian.

### 20.7 Fatiga acumulada (alternativa a la regresión)
Para campañas largas que prefieran una contabilidad fina: al terminar un combate en el que el compañero estuvo por encima de su nivel estable, gana **Fatiga** igual a los niveles que subió (DNA +2, Supremo +2, forzada +2). Con 1–2: −1 a sus tiradas por punto. Con 3–4: regresión a Bebé II hasta un descanso largo. Con 5+: no puede digievolucionar. Un descanso corto quita 1; uno largo, toda.

### 20.8 Corrupción y bloqueos
- **Engranajes Negros, Espirales del Mal y Anillos Malignos:** un Digimon que lleva uno es **Hostil**, tiene +1 Atq y no se puede razonar con él. Se libera destruyendo el objeto: *Purificar* con 10+, *Luz del Digivice* (Digivice clásico, AST + Tecnología 7+), o una Maniobra 10+ apuntando al objeto. Liberado, su actitud pasa a Neutral (o Amistosa si el grupo lo trató con cuidado).
- **Agujas de Control y Torres Oscuras:** en su región (o en un radio que fije el DJ), **la digievolución normal es imposible**; la Armadura y los Espíritus sí funcionan. Para derribar una: un reloj de 6 segmentos (Tecnología, Hackeo, Luz del Digivice) o destruirla (PV 30, Arm 2, Def 2; solo la dañan técnicas P2 o superiores).
- **Sellado temporal:** el estado Sellar (11.4) impide digievolucionar durante su duración.
- **Corrupción del Tamer (0–3):** el Tamer gana 1 punto cuando su compañero sufre una digievolución oscura, cuando actúa movido por el odio contra un enemigo indefenso o al usar objetos del enemigo (un Engranaje, una Espiral). Con 1: −1 a Animar. Con 2: la Chispa por fallo dramático solo puede gastarse en digievolución forzada. Con 3: la próxima digievolución temporal es automáticamente oscura. Se limpia 1 punto con un Momento de Vínculo, con la Resonancia del Emblema de Pureza o de Luz, o con una escena de reparación.

### 20.9 Combos elementales
Cuando una técnica impacta a un objetivo que ya está en cierto estado, se desencadena un efecto extra (sin gastar palabras clave; como mucho un combo por técnica):

| Estado previo | Técnica que impacta | Combo | Efecto |
|---|---|---|---|
| Empapado | Eléctrico | Electrocución | +1 dado y Paralizar (aunque saque 7–9) |
| Empapado | Hielo | Ultracongelación | Congelar (aunque saque 7–9) |
| Empapado | Tierra | Lodazal | Ralentizar |
| Congelado | Toque Neutro, Tierra o Acero | Quebrar | +1 dado; termina Congelado |
| Quemado | Viento | Incendio | Quemar a todos los enemigos de la zona del objetivo |
| Envenenado | Planta | Floración tóxica | Atrapar |
| Atrapado | Fuego | Pira | +1 dado; termina Atrapado |
| Cegado | Oscuridad | Eclipse | Asustar |
| Asustado, Confundido o Sellado | Luz | Purga | +1 dado; termina ese estado |
| Ralentizado | Cósmico | Colapso | Derribar |

Los combos que aplican control duro o «aunque saque 7–9» no funcionan contra Jefes (que solo sufren su efecto de daño).

### 20.10 Casillas, tamaño y flanqueo
Para mesas con tablero: **1 zona ≈ un área de 4 × 4 casillas**. Movimiento 6 casillas (Correr, 12). **Toque** = adyacente; **Distancia** = 8 casillas; **Larga** = 16. **Ráfaga** = 2 objetivos a 2 casillas o menos uno del otro; **Zona** = explosión de radio 2; **Total** = todo lo que esté a la vista. **Tamaño:** Bebé y Novato ocupan 1 casilla; Campeón y Perfecto, 1 o 2 × 2 si son grandes; Definitivo, 2 × 2 o 3 × 3. **Flanqueo:** +1 a las técnicas de Toque si un aliado está en el lado opuesto del objetivo (situacional).

### 20.11 Iniciativa individual
Cada pareja y cada PNJ tiran (los PNJ, 2d6 + Ini); se actúa de mayor a menor. Es más lenta que las fases y no se recomienda con más de 6 enemigos.

### 20.12 Borrado (muerte permanente)
Con este módulo, un compañero Derrotado que vuelve a recibir daño en el mismo combate de una técnica P3 **es borrado**: se convierte en un Digi-Huevo que renacerá en la Ciudad del Comienzo. Con Vínculo 3 o más, el nuevo Bebé recuerda a su Tamer; si no, hay que reconstruir el vínculo (Vínculo 1). Los PNJ no apuntan nunca a un Derrotado salvo por una jugada telegrafiada con un turno de antelación.

### 20.13 Fricción del Vínculo
Si el Tamer traiciona gravemente la confianza de su compañero, el Vínculo baja 1 de forma **temporal** hasta una escena de reconciliación (COR + Empatía, 7+).

### 20.14 Herramientas de mesa
- **Dados:** cada jugador necesita 3d6 (dos de un color y el Dado de Vínculo de otro) y un dado de poder de cada tipo (d4–d12). El DJ, d20, d12, d8 y d6 para las tablas. *No hacen falta reservas grandes de dados.*
- **Daño fijo para todos:** si la mesa prefiere no tirar daño nunca, todos usan el daño fijo (6.8).
- **App de dados:** la web del manual incluirá un lanzador con el Dado de Vínculo y la lectura de franjas.

---

## 21. Especificación de fichas (resumen de `spec_fichas.json`)

Las 1.317 fichas del bestiario se **generan por fórmula** a partir de cinco datos de cada entrada de `src/all.json`: **nivel + rol + atributo + familia + lista de técnicas oficiales**. El JSON es la especificación exacta y programable; este capítulo la resume para los redactores. Un generador de referencia (`work_final/gen.py`) la implementa leyendo el propio JSON, genera las 1.317 fichas y comprueba todas las reglas de validación (21.8): **0 errores**, incluidas las formas Armadura, Híbrido e Indeterminado. Si una validación falla, el generador se detiene.

### 21.1 Orden de cálculo
1. Fila de nivel: niveles[level] (o niveles[level].por_id[id] → fila de ese nivel) → rango, dado, vf, pv_base, atq, def, ini.
2. Familia: la familia cuya lista 'tipos' contiene type. Bebés: solo para afinidad, sin rasgo ni mods.
3. Técnicas, primera pasada (clasificador): firma, potencias, apoyo, alcance, elemento, área, palabras clave encontradas por raíz.
4. Rol (rol_algoritmo) — salvo Bebés; override por id si existe.
5. Técnicas, segunda pasada: estado por defecto del elemento, palabra de Firma del rol, Larga del Tirador, Ejecutar en área → Brutal.
6. Plantillas (x_antibody, supremo, modo_oscuro, modo_alterno, fusion, hibrido, armadura, bebe).
7. Estadísticas (formulas).
8. Elemento principal, debilidades y resistencias; vuelo y nado.
9. Rasgos (rol, familia, atributo, plantillas), técnica básica y maniobra de rol.
10. amenaza_sugerida por id (legendario, jefe, esbirro; resto estandar) e índice de amenaza con su modificador de PA.
11. Overrides (overrides_iniciales + overrides.json) y validación (21.8). Si una validación falla, el generador se detiene.

**Ids, no nombres:** los nombres de Digimon se repiten en los datos (Argomon ×6, Eosmon ×3, Rapidmon, Burgamon y Cyberdramon ×2), así que **todas** las listas de Digimon de la especificación usan el id: overrides de Digimon, filas `por_id` de niveles, clases de Híbrido, Legendarios, Jefes y esbirros sugeridos y vuelo. Los overrides de técnicas usan el nombre oficial exacto tal como aparece en `moves`. En los nombres de técnica que se imprimen, el carácter de media anchura «ｰ» se cambia por un guion («CoronaｰKnuckles» → «Corona-Knuckles»); el nombre original se guarda en `nombre_dato`.

### 21.2 Tabla base por nivel
| Nivel (datos) | Fila | Rango | Dado | VF | PV base | Atq | Def | Ini | Arm | Potencia máx. | Peligro Tamer | Umbral Ejecutar | Guardia de carga | Rol y familia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `In-Training 1` | **Bebé I** | 0 | d4 | 2 | 6 | 0 | 0 | 0 | 0 | P1 | 1 | 4 | — | no |
| `In-Training 2` | **Bebé II** | 0 | d4 | 2 | 10 | 0 | 0 | 0 | 0 | P2 | 1 | 4 | — | no |
| `Rookie` | **Novato** | 1 | d6 | 3 | 21 (VF × 7) | +1 | +1 | +1 | 0 | P3 | 1 | 6 | 10 | sí |
| `Champion` | **Campeón** | 2 | d8 | 4 | 28 (VF × 7) | +2 | +2 | +2 | 0 | P3 | 2 | 8 | 14 | sí |
| `Ultimate` | **Perfecto** | 3 | d10 | 5 | 35 (VF × 7) | +3 | +3 | +3 | 0 | P3 | 3 | 10 | 17 | sí |
| `Mega` | **Definitivo** | 4 | d12 | 6 | 42 (VF × 7) | +4 | +4 | +4 | 0 | P3 | 4 | 12 | 21 | sí |
| `Armor` | **Armadura** | 2 | d8 | 4 | 28 (VF × 7) | +2 | +2 | +2 | 0 | P3 | 2 | 8 | 14 | sí |
| `Hybrid` | **Híbrido** | 2 | d8 | 4 | 28 (VF × 7) | +2 | +2 | +2 | 0 | P3 | 2 | 8 | 14 | sí |
| `Unknown` | **Indeterminado** | 1 | d6 | 3 | 21 (VF × 7) | +1 | +1 | +1 | 0 | P3 | 1 | 6 | 10 | sí |

*Armadura* usa la fila de Campeón (Rapidmon (Armadura) y GoldVeedramon, la de Perfecto; Magnamon, la de Definitivo). *Híbrido* usa la fila de su clase de Espíritu (20.2). *Indeterminado* (nivel `Unknown`; se llama así para no confundirlo con el atributo Desconocido) usa la de Novato (Calumon y Burpmon) y NEO, la de Definitivo. Todas estas fichas usan el **rango** de la fila que toman para la escala de daño, el presupuesto y las tiradas, y se validan con los rangos de esa fila. La ficha imprime el rango.

### 21.3 Fórmulas
- **rango:** niveles[level].rango (o niveles[level].por_id[id] → fila de ese nivel)
- **dado:** d4 si rango 0; si no d(4 + 2*rango)
- **vf:** dado_caras / 2
- **pv:** Bebé I: 6; Bebé II: 10; resto: vf * (7 + rol.pv_mult + familia.pv_mult + atributo.pv_mult + Σ plantillas.pv_mult)
- **atq:** rango + rol.atq + atributo.atq + Σ plantillas.atq
- **def:** rango + rol.def + atributo.def + Σ plantillas.def
- **arm:** min(2, rol.arm + familia.arm + Σ plantillas.arm)  (Bebés: 0)
- **ini:** rango + rol.ini + atributo.ini + familia.ini + Σ plantillas.ini
- **peligro_tamer:** max(1, rango); +1 si la técnica es P3
- **umbral_ejecutar:** 2 * vf
- **dados_tecnica:** potencia (P1 = 1, P2 = 2, P3 = 3; P2/P3: 2 o 3). Una técnica de área que alcanza de verdad a 2 o más objetivos tira potencia − 1 (mínimo 1); contra un solo objetivo cuenta como Individual. La ficha guarda los dos valores: `dados` (contra un objetivo) y `dados_area` (contra 2+; null si es Individual).
- **dano_tecnica_impreso:** 'Nd(dado)' con N = dados contra un objetivo; si la técnica es de área se imprime además 'contra 2+: Md(dado)'. La ficha guarda también las medias (`dano_medio` = N × (dado_caras + 1) / 2 y `dano_medio_area`).
- **escala:** se compara el **rango** de la fila que usa cada ficha (Armadura = Campeón; Rapidmon (Armadura) y GoldVeedramon = Perfecto; Magnamon y NEO = Definitivo; Híbrido = la fila de su clase), no la etiqueta de nivel. Atacante de rango inferior al objetivo: el daño se divide a la mitad por cada rango de diferencia (redondeo abajo, mínimo 1). Atacante de rango superior: +1 dado de daño (no acumulable por más rangos).
- **triangulo:** +1 a las tiradas del PJ (ataque y Defensa) contra un PNJ si el atributo del PJ vence al del PNJ; −1 si el atributo del PNJ vence al del PJ; 0 si alguno de los dos es neutral (Libre, Desconocido, SIN DATOS, Ninguno). Variable usa el atributo elegido en la escena. Es un modificador situacional (cuenta para el límite de ±3).
- **tirada_pj_ataque:** 2d6 + atq_propio − def_objetivo + situacionales (máx. ±3)
- **tirada_pj_defensa:** 2d6 + def_propia − atq_atacante + situacionales (máx. ±3)
- **tirada_fuera_de_combate_digimon:** 2d6 + rango (+1 si es su especialidad de familia o rol)
- **guardia_de_carga:** pv_base del nivel / 2 (redondeo abajo)
- **jefe_pv:** floor(pv * (N + 2) / 2); con Refuerzo I o II (19.4): floor(pv * (N + 3) / 2)
- **legendario_pv:** floor(pv * (N + 3) / 2)
- **esbirro_pv:** ceil(pv / 4)
- **elite_pv:** floor(pv * 1.5)
- **debilidades:** Bebés: ninguna. Resto: familia.debilidad (Elemental: la de su tipo; excepciones_tipo de la familia si existen) ∪ {primer elemento de orden_debilidad (agua, fuego, planta, eléctrico, veneno, viento, tierra, hielo, acero, mental, luz, oscuridad, cósmico) cuyo 'vence_a' contiene el elemento principal y que no esté ya entre las debilidades ni las resistencias de la familia}; resistencias: familia.resistencia ∪ {elemento principal si no es neutro ni cosmico}; se quita de ambas listas lo que aparezca en las dos; máximo 2 de cada (primero las de familia). Plantilla Armadura: se añade a resistencias el elemento de la Firma (si no es neutro), manteniendo el máximo de 2, y se quita de debilidades.
- **elemento_principal:** el elemento más repetido entre sus técnicas oficiales sin contar neutro; empate → el de la técnica que va antes (la Firma primero); Elemental: el de su tipo; sin técnicas con elemento: ninguno

### 21.4 Asignación del rol
Cada rol recibe puntos: **+3** al rol primario de la familia y **+1** al secundario; **+4** si el tipo está en la lista de excepciones de un rol (p. ej., *Cyborg* → Tirador, *Holy Knight* → Versátil, *Pixie* → Apoyo); y evidencia de sus técnicas (×2 la Firma): técnica de apoyo → Apoyo +3; Toque detectado por palabra → Bruto; Distancia o Larga detectada por palabra → Tirador; palabras clave encontradas por raíz → el rol afín (estados de control —Dormir, Encantar, Confundir, Sellar, Regresión, Atrapar, Ralentizar, Debilitar, Asustar, Cegar— → Místico; Perforante, Certero, Ejecutar, Ocultar → Acechador; Rápido → Ágil; Provocar, Contraataque, Escudo en daño → Tanque; Brutal, Romper, Derribar, Aturdir → Bruto; Invocar, Drenar, Mejora o Curar en daño → Místico). Extras: Definitivo con técnicas de Toque y de Distancia → Versátil +2; más de la mitad de sus técnicas de apoyo → Apoyo +4. Gana la puntuación más alta; en caso de empate, el rol primario de la familia, luego la excepción de tipo y luego el orden fijo. Los Bebés no tienen rol. Hay *overrides* por id para Digimon icónicos.

**Distribución resultante en el bestiario (versión 1.1):** Bruto 298, Místico 223, Versátil 182, Ágil 159, Tirador 118, Tanque 110, sin rol (Bebés) 108, Acechador 80, Apoyo 39. Apoyo y Tanque son escasos entre los Digimon salvajes: por eso **el jugador puede fijar el rol de su compañero** (4.1).

### 21.5 Plantillas
| Plantilla | Se aplica si | Modificadores | Rasgo |
|---|---|---|---|
| **X-Antibody** | x_antibody == true | Atq +1, PV +VF | *Anticuerpo X:* Inmune a Sellar y a Ejecutar. Una vez por combate: si es PJ, repite una tirada de Defensa; si es PNJ, obliga a un PJ a repetir un 10+ obtenido contra él. |
| **Modo Supremo** | is_mode == true, nivel != Hybrid y el nombre contiene una marca de modo supremo (marcas: Burst Mode, Crimson Mode, Paladin Mode, Merciful Mode, Superior Mode, Blast Mode, Itto Mode, Awakened, Promote, GX, Takemikazuchi, Holy Mode, Alter-S) | Atq +1, Def +1, PV +VF | *Poder desatado:* Al entrar en este modo su Firma queda lista aunque la hubiera usado el turno anterior. |
| **Modo Oscuro** | is_mode == true, nivel != Hybrid y el nombre contiene una marca de modo oscuro (marcas: Ruin Mode, Rage Mode, Wrath Mode, Hysteric Mode, Fury Mode, Satan Mode, Destroy Mode, Chaos Mode, Falldown Mode, Vicious Mode, Zwart Defeat, Alter-B, Whispered) | Atq +1, Def +1, PV +VF | *Descontrol:* +1 dado de daño en todas sus técnicas y −1 Def contra técnicas de Luz. Un compañero en esta forma actúa como en la digievolución oscura (lo controla el DJ). |
| **Modo alterno** | is_mode == true, nivel != Hybrid, sin marca de supremo ni oscuro | — | *Cambio de modo:* Cambiar a otro modo de la misma especie gasta el movimiento; conserva el daño recibido (PV = PV máximos de la nueva ficha − daño acumulado). |
| **Fusión de Espíritus** | Híbrido de clase fusion | Atq +1, Def +1 | *Fusión de Espíritus:* Combina los Espíritus Humano y Bestia (incluido). |
| **Híbrido** | nivel == Hybrid | — | *Espíritu legendario:* Es la transformación de un Tamer (módulo de Espíritus). Atributo Variable. |
| **Armadura** | nivel == Armor | — | *Poder del Digi-Huevo:* Resistencia al elemento de su Firma (incluida). Funciona aunque la digievolución normal esté bloqueada. No puede digievolucionar a otro nivel desde esta forma. Como compañero: 2 Chispa (20.1). |
| **Bebé** | nivel In-Training 1 o In-Training 2 | — | *Bebé:* Sin rol ni rasgo de familia; no puede usar P3; +2 a las tiradas para esconderse o huir. Sus técnicas no aplican control duro ni Ejecutar. |

### 21.6 Clasificador de técnicas (del nombre oficial a la mecánica)
1. **Normalización** (la misma para nombres, contexto y raíces): Unicode NFKD sin diacríticos (*Mjölnir* → *mjolnir*; «ｰ» cuenta como guion), minúsculas, sin paréntesis, y todo lo que no sea letra a–z o dígito → espacio (guiones, apóstrofos, barras, signos). Las raíces de la especificación ya están escritas normalizadas (*self destruct\**, *all out*, *can t be dodged*) y la validación comprueba que ninguna contiene caracteres que la normalización elimina.
2. **Raíces:** cada elemento, palabra clave, alcance y área tiene una lista cerrada de raíces en inglés. `burn*` coincide como prefijo; una raíz sin asterisco de 6 letras o más, también; una raíz corta solo coincide como palabra completa, admitiendo solo los sufijos -s, -es, -ed, -ing, de modo que *sin* no salta en *single*, *light* en *lightning*, *show* en *shower*, *arm* en *army* ni *rock* en *rocker*.
3. **Dos fuentes:** primero el **nombre** de la técnica (manda siempre) y, si no basta, la **cláusula de contexto** extraída del perfil inglés (`background_EN_reference_only`): en cada frase que nombra la técnica, el tramo que **empieza justo después de su nombre** y termina donde se nombra la siguiente técnica de la lista o al final de la frase (lo dicho antes del nombre suele describir la técnica anterior y se descarta); se añade la frase siguiente si empieza por «This…», «The attack…» y similares y no nombra otra técnica. El contexto solo sirve para clasificar; **nunca** se copia ni se traduce.
4. **Firma:** la primera técnica de la lista, salvo que otra lleve una palabra de potencia máxima (*giga, final, ultimate, supreme, nova, omega, genesis, judgment…*) o que la primera sea de apoyo.
5. **Potencia** según el número de técnicas y el nivel (11.2).
6. **Apoyo** si (a) el nombre tiene una raíz de Curar, Escudo, Mejora o Purificar y ninguna palabra de daño; (b) el nombre no tiene ninguna raíz de efecto, de elemento ni de daño y el contexto solo contiene raíces de apoyo; o (c) aunque el nombre tenga raíces de elemento, el contexto describe ayuda a aliados («heals its allies», «protects nearby comrades»: verbo de ayuda seguido, a 4 palabras o menos, de un aliado) y no hay palabras de daño. Una técnica de apoyo lleva solo palabras de apoyo.
7. **Alcance:** Larga > Distancia fuerte (*breath, blast, beam, cannon, missile…*) > Toque (*punch, claw, sword, tackle…*) > verbos del contexto > Distancia débil (*wave, storm, ball, flame…*) > por defecto (la Firma, Distancia; las demás, según el rol primario de la familia).
8. **Elemento:** primero las **frases** (raíces de varias palabras) de todos los elementos en el nombre y después las palabras sueltas, en el orden de prioridad Veneno, Hielo, Eléctrico, Fuego, Agua, Planta, **Oscuridad, Luz**, Cósmico, Mental, Viento, Tierra, Acero (así *gold rush* es Tierra y *Seven Hells*, *Ruin Laser* o *Chaos Lights* son Oscuridad); si no, lo mismo en el contexto con las **raíces de contexto** de cada elemento (10); si no, la afinidad de la familia (si no es de Toque) o Neutro.
9. **Área:** Total (solo Firma de Definitivo con raíz de Total) > Zona > Ráfaga > Individual. Una técnica de daño P1 es siempre Individual.
10. **Palabras clave (máx. 2):** primero el nombre y luego el contexto, por categorías (apoyo, daño, estado, táctica); en una segunda pasada, si falta un estado, el estado por defecto del elemento y, si es la Firma, la palabra de Firma del rol. **Ejecutar solo en técnicas Individuales** (en una de área pasa a Brutal). Total no admite control duro. Los Bebés no llevan Ejecutar, Aturdir, Dormir ni Regresión.
11. **Overrides:** `overrides_iniciales` (**74 técnicas** y 24 Digimon icónicos) y `overrides.json` corrigen a mano lo que el algoritmo clasifique mal. **Siempre ganan.** Cada clave de técnica debe existir tal cual en algún `moves` (Ice Wolf Claw, Lightning Joust, Heaven's Gate, Luna Claw, Night Raid…) y cada clave de Digimon debe ser un id existente: si no, el generador falla. Si un override fija las palabras clave, se omite toda la segunda pasada (también la Larga del Tirador): por eso Terrier Tornado y River of Power fijan además el alcance Larga. Antes de publicar, hay que revisar a mano todos los Digimon de las aventuras de inicio y de las series principales (≈150 fichas).

### 21.7 Amenaza sugerida
Legendario si el **id** está en la lista curada (19.5; 126 fichas); Jefe si está en la lista de jefes sugeridos (27); Esbirro si está en la de esbirros naturales (20); Estándar en los demás casos (1.144). **La plantilla de amenaza no se aplica en el bestiario**: la aplica el DJ al usar la ficha.

**Índice de amenaza** (`amenaza.indice_amenaza`): el generador calcula para cada ficha con rol `ofensiva² × PV efectivos` frente a una pareja media de su rango (Def y Atq = rango + 1): la ofensiva sale del dado, de los dados de su Firma y de su mejor otra técnica, de la probabilidad de que la Defensa del PJ saque 6– o 7–9 y del área de su Firma (Ráfaga ×1,4, Zona ×1,6, Total ×2); los PV efectivos, de sus PV, su Arm, sus resistencias (+15 % cada una), Drenar o familia Oscuro (×1,2) y la probabilidad de impactarla. Las fichas de cada fila se ordenan y se cortan en terciles: **baja** (PA ×¾), **media** (×1) y **alta** (×1½). Los Bebés son siempre «media».

### 21.8 Validación automática
| Fila | PV | Atq | Def | Arm |
|---|---|---|---|---|
| bebe_1 | 6–6 | +0 a +2 | +0 a +2 | 0–0 |
| bebe_2 | 10–10 | +0 a +2 | +0 a +2 | 0–0 |
| novato | 15–36 | +0 a +5 | +0 a +4 | 0–2 |
| campeon | 20–48 | +1 a +6 | +1 a +5 | 0–2 |
| perfecto | 25–60 | +2 a +7 | +2 a +6 | 0–2 |
| definitivo | 30–72 | +3 a +8 | +3 a +7 | 0–2 |

Las filas Armadura, Híbrido e Indeterminado se validan con el rango de la fila que usan.

- Como mucho una técnica P3 (o P2/P3) por ficha.
- Máximo 2 palabras clave por técnica.
- Ningún Bebé con P3, Ejecutar ni control duro (Aturdir, Dormir, Regresión).
- Área Total solo en la Firma de rango 4.
- Ejecutar solo en técnicas Individuales.
- Una técnica de daño P1 es siempre Individual.
- Las técnicas de apoyo no hacen daño ni llevan palabras de daño ni de estado; tácticas, solo por override.
- Toda ficha tiene técnica básica y maniobra de rol (salvo Bebés: solo básica).
- Cada uno de los 140 tipos pertenece a exactamente una familia.
- Toda clave de override de técnica existe en algún `moves`; todo id de las listas (overrides de Digimon, `por_id`, clases de Híbrido, Legendarios, Jefes, esbirros, vuelo) existe en los datos.
- Ninguna raíz contiene caracteres que la normalización elimina.

**Objetivos de diseño medidos por simulación** (versión 1.1; `work_final/r3_sim.py` con las fichas de `gen.py` y los guiones de `work_final/cal_biblia/`; Orden y Dado de Vínculo en cada asalto, sin programas ni objetos, sin Firma telegrafiada):
- **Duelos 1 contra 1 al mismo nivel** (PJ contra PNJ estándar): 3,1–3,2 asaltos de media en Novato, Campeón y Perfecto. Los emparejamientos más largos son Apoyo contra Apoyo (4,3–5,9 asaltos; hasta un 36 % pasa de 6) y Tanque contra Tanque (4,3–4,8; 12–18 % pasa de 6). Ninguna media de emparejamiento de roles pasa de 6 asaltos.
- **Enemigos de rango superior** (mediana de ataques que necesita un Novato que no puede caer): mismo rango 3; +1: 9; +2: 29; +3: 77 (imposible en la práctica). La media es mucho mayor por la Arm y las Resistencias.
- **Encuentros a Vínculo 1** (4 parejas): Fácil 2,1–2,6 asaltos, Normal 2,7–3,0, Difícil 3,4–3,7, sin derrotas; quien digievoluciona lo hace de media en los asaltos 1,5–1,8, tras una Crisis.
- **Jefe de la aventura y Legendario:** tabla de 19.2.
- **Armadura** (equipo «02» a Vínculo 1 contra Jefe Campeón): 3,2–5,2 asaltos, 0–5 % de derrota.

### 21.9 Formato de la ficha
Cada ficha se publica como JSON (para la web y la ficha editable) y como bloque de texto:
```
NOMBRE — Nivel [etiqueta] · Familia (Tipo) · Rol · Atributo [· plantillas] [· Amenaza sugerida]
Rango _ · PV __ · Atq +_ · Def +_ · Arm _ · Ini +_ · Dado d_ (VF _) [· Vuela] [· Nada]
Debilidad: __ · Resistencia: __ · Triángulo: vence a __
Especialidades: <familia>; <rol> · Amenaza: baja (PA ×¾) | media | alta (PA ×1½)
Rasgos: <rol>; <familia>; <atributo>; <plantillas>
Técnicas:
· <Básica> — P1 · Toque · Individual · <elemento>  [1d_]
· <Maniobra de rol> — …
· <Firma> — P3 (Agotadora) · <alcance> · <área> · <elemento> · <claves>  [3d_; contra 2+: 2d_ si es de área]
Evoluciona de: … · Evoluciona a: … · Modos: …
[Notas: …]
```
El JSON añade, además, `fila_validacion`, `especialidades`, `indice_amenaza`, `amenaza_nivel`, `mod_pa` y `notas`, y en cada técnica `nombre_dato`, `dados_area` y `dano_medio_area` (`spec_fichas.json`, `salida`).

### 21.10 Ejemplos calculados (Agumon → WarGreymon)
#### Agumon (`agumon`)
Entrada: nivel Rookie · tipo Reptile · atributo Vaccine · técnicas Pepper Breath.

1. Nivel Rookie → fila Novato: rango 1, dado d6, VF 3, Atq/Def/Ini base 1.
2. Tipo Reptile → familia Saurio (afinidad neutro; rasgo Piel gruesa; mods pv_mult +1, arm +0, ini +0).
3. Técnica Pepper Breath [Firma]: P2/P3 (Agotadora) · distancia · individual · fuego · claves quemar, brutal. (override)
4. Puntuación de rol {"bruto": 3, "tanque": 1, "tirador": 2} → bruto → override por id: bruto.
5. Plantillas: ninguna.
6. PV = VF 3 × (7 +1 rol +1 familia +0 atributo +0 plantillas) = 27.
7. Atq = 1 +1 rol +0 atributo +0 plantillas = 2; Def = 1 +0 rol +1 atributo +0 plantillas = 2.
8. Arm = min(2, 0 rol +0 familia +0 plantillas) = 0; Ini = 1 +0 rol +0 atributo +0 familia +0 plantillas = 1.
9. Elemento principal Fuego → debilidades: Hielo, Agua; resistencias: Tierra, Fuego.

```
Agumon — Novato · Saurio (Reptil) · Bruto · Vacuna
Rango 1 · PV 27 · Atq +2 · Def +2 · Arm 0 · Ini +1 · Dado d6 (VF 3)
Debilidad: Hielo, Agua · Resistencia: Tierra, Fuego · Triángulo: vence a Virus
Especialidades: aguante, fuerza, morder; fuerza y romper cosas · Amenaza: media
Rasgos: Arrollador (rol); Piel gruesa (familia); Antivirus (atributo)
Técnicas:
· Mordisco — P1 · Toque · Individual · Neutro
· Arremetida — P1 · Toque · Individual · Neutro · Derribar
· Pepper Breath — P2/P3 (Agotadora) · Distancia · Individual · Fuego · Quemar, Brutal  [2d6 / 3d6]
Evoluciona de: Koromon · Evoluciona a: Greymon (2010 Anime Version), Greymon, GeoGreymon, Coredramon (Green), Raptordramon, Numemon
```

#### Greymon (`greymon-first`)
Entrada: nivel Champion · tipo Dinosaur · atributo Vaccine · técnicas Mega Flame.

1. Nivel Champion → fila Campeón: rango 2, dado d8, VF 4, Atq/Def/Ini base 2.
2. Tipo Dinosaur → familia Saurio (afinidad neutro; rasgo Piel gruesa; mods pv_mult +1, arm +0, ini +0).
3. Técnica Mega Flame [Firma]: P2/P3 (Agotadora) · distancia · individual · fuego · claves brutal, quemar. (override)
4. Puntuación de rol {"bruto": 9, "tanque": 1, "tirador": 2} → bruto.
5. Plantillas: ninguna.
6. PV = VF 4 × (7 +1 rol +1 familia +0 atributo +0 plantillas) = 36.
7. Atq = 2 +1 rol +0 atributo +0 plantillas = 3; Def = 2 +0 rol +1 atributo +0 plantillas = 3.
8. Arm = min(2, 0 rol +0 familia +0 plantillas) = 0; Ini = 2 +0 rol +0 atributo +0 familia +0 plantillas = 2.
9. Elemento principal Fuego → debilidades: Hielo, Agua; resistencias: Tierra, Fuego.

```
Greymon — Campeón · Saurio (Dinosaurio) · Bruto · Vacuna
Rango 2 · PV 36 · Atq +3 · Def +3 · Arm 0 · Ini +2 · Dado d8 (VF 4)
Debilidad: Hielo, Agua · Resistencia: Tierra, Fuego · Triángulo: vence a Virus
Especialidades: aguante, fuerza, morder; fuerza y romper cosas · Amenaza: media
Rasgos: Arrollador (rol); Piel gruesa (familia); Antivirus (atributo)
Técnicas:
· Mordisco — P1 · Toque · Individual · Neutro
· Arremetida — P1 · Toque · Individual · Neutro · Derribar
· Mega Flame — P2/P3 (Agotadora) · Distancia · Individual · Fuego · Brutal, Quemar  [2d8 / 3d8]
Evoluciona de: Agumon, SnowAgumon, Huckmon, Shoutmon, Agumon (2006 Anime Version), Ryudamon · Evoluciona a: MetalGreymon (Vaccine), SkullGreymon, Megadramon, Kimeramon, WarGrowlmon (Orange), MetalGreymon (Virus)
```

#### MetalGreymon (`metalgreymon-v`)
Entrada: nivel Ultimate · tipo Cyborg · atributo Vaccine · técnicas Trident Arm, Giga Destroyer, Giga Storm.

1. Nivel Ultimate → fila Perfecto: rango 3, dado d10, VF 5, Atq/Def/Ini base 3.
2. Tipo Cyborg → familia Máquina (afinidad acero; rasgo Blindaje; mods pv_mult +0, arm +1, ini -1).
3. Técnica Giga Destroyer [Firma]: P3 (Agotadora) · larga · individual · acero · claves brutal, certero. (override)
3. Técnica Trident Arm: P2 · toque · individual · acero · claves perforante. (override)
3. Técnica Giga Storm: P2 · distancia · zona · acero · claves brutal. (override; 2d10 contra un objetivo, 1d10 contra cada uno si alcanza a 2 o más)
4. Puntuación de rol {"tanque": 3, "tirador": 8, "bruto": 4, "acechador": 1} → tirador.
5. Plantillas: ninguna.
6. PV = VF 5 × (7 +0 rol +0 familia +0 atributo +0 plantillas) = 35.
7. Atq = 3 +1 rol +0 atributo +0 plantillas = 4; Def = 3 -1 rol +1 atributo +0 plantillas = 3.
8. Arm = min(2, 0 rol +1 familia +0 plantillas) = 1; Ini = 3 +1 rol +0 atributo -1 familia +0 plantillas = 3.
9. Elemento principal Acero → debilidades: Eléctrico, Fuego; resistencias: Veneno, Acero.

```
MetalGreymon (Vaccine) — Perfecto · Máquina (Cíborg) · Tirador · Vacuna
Rango 3 · PV 35 · Atq +4 · Def +3 · Arm 1 · Ini +3 · Dado d10 (VF 5) · Vuela
Debilidad: Eléctrico, Fuego · Resistencia: Veneno, Acero · Triángulo: vence a Virus
Especialidades: fuerza, cálculo, sensores, interfaz; puntería y vigilancia · Amenaza: media
Rasgos: Francotirador (rol); Blindaje (familia); Antivirus (atributo)
Técnicas:
· Disparo — P1 · Distancia · Individual · Acero
· Disparo certero — P1 · Larga · Individual · Acero · Certero
· Giga Destroyer — P3 (Agotadora) · Larga · Individual · Acero · Brutal, Certero  [3d10]
· Trident Arm — P2 · Toque · Individual · Acero · Perforante  [2d10]
· Giga Storm — P2 · Distancia · Zona · Acero · Brutal  [2d10; contra 2+: 1d10]
Evoluciona de: Growlmon, DarkTyrannomon, Leomon, Airdramon, Tyrannomon, GoldVeedramon · Evoluciona a: WarGreymon, BlitzGreymon, VictoryGreymon, Gaiomon, ShineGreymon, Alphamon
```

#### WarGreymon (`wargreymon`)
Entrada: nivel Mega · tipo Dragon Man · atributo Vaccine · técnicas Terra Force, Great Tornado.

1. Nivel Mega → fila Definitivo: rango 4, dado d12, VF 6, Atq/Def/Ini base 4.
2. Tipo Dragon Man → familia Dragón (afinidad fuego; rasgo Corazón de dragón; mods pv_mult +0, arm +0, ini +0).
3. Técnica Terra Force [Firma]: P3 (Agotadora) · distancia · individual · fuego · claves cargado, quemar. (override)
3. Técnica Great Tornado: P2 · toque · individual · viento · claves perforante, rapido. (override)
4. Puntuación de rol {"bruto": 4, "versatil": 7, "tirador": 2, "acechador": 1, "agil": 1} → versatil → override por id: versatil.
5. Plantillas: ninguna.
6. PV = VF 6 × (7 +0 rol +0 familia +0 atributo +0 plantillas) = 42.
7. Atq = 4 +0 rol +0 atributo +0 plantillas = 4; Def = 4 +0 rol +1 atributo +0 plantillas = 5.
8. Arm = min(2, 0 rol +0 familia +0 plantillas) = 0; Ini = 4 +1 rol +0 atributo +0 familia +0 plantillas = 5.
9. Elemento principal Fuego → debilidades: Hielo, Agua; resistencias: Fuego.

```
WarGreymon — Definitivo · Dragón (Hombre Dragón) · Versátil · Vacuna
Rango 4 · PV 42 · Atq +4 · Def +5 · Arm 0 · Ini +5 · Dado d12 (VF 6) · Vuela
Debilidad: Hielo, Agua · Resistencia: Fuego · Triángulo: vence a Virus
Especialidades: fuerza, intimidar, volar si tiene alas; una a elección del jugador · Amenaza: baja (PA ×¾)
Rasgos: Adaptable (rol); Corazón de dragón (familia); Antivirus (atributo)
Técnicas:
· Garra de dragón — P1 · Toque · Individual · Neutro
· Cambio de guardia — P1 · Toque · Individual · Neutro
· Terra Force — P3 (Agotadora) · Distancia · Individual · Fuego · Cargado, Quemar  [3d12]
· Great Tornado — P2 · Toque · Individual · Viento · Perforante, Rápido  [2d12]
Evoluciona de: Megadramon, Mamemon, WarGrowlmon (Orange), RizeGreymon (X Antibody), MetalGreymon: Alterous Mode, Scorpiomon · Evoluciona a: Omnimon, Omnimon (X Antibody), WarGreymon (X Antibody)
```

#### La misma línea como compañero con rol fijado (Bruto)
El jugador fijó el rol Bruto para su Agumon: todas sus formas usan los modificadores de Bruto en lugar del rol del bestiario (familia, atributo y técnicas no cambian; el rasgo y la maniobra pasan a ser los de Bruto). Con un rol fijo los PV crecen siempre al subir de nivel.

| Forma | Dado | PV | Atq | Def | Arm |
|---|---|---|---|---|---|
| Koromon | d4 | 10 | 0 | 0 | 0 |
| Agumon | d6 | 27 | +2 | +2 | 0 |
| Greymon | d8 | 36 | +3 | +3 | 0 |
| MetalGreymon (Vaccine) | d10 | 40 | +4 | +4 | 1 |
| WarGreymon | d12 | 48 | +5 | +5 | 0 |

---

## 22. Hoja de referencia rápida y notas para redactores

### 22.1 Hoja de referencia (una cara)
- **Tirada:** 2d6 + mod · **10+** total · **7–9** con coste · **6–** fallo y +1 Chispa (máx. 1 por asalto en combate, 1 por escena fuera) · ⚅⚅ crítico · ⚀⚀ pifia · situacionales ±3 como mucho.
- **Espejo:** el DJ no tira para impactar: un modificador a la tirada de un PNJ se aplica con el signo cambiado a la del PJ (−2 a sus ataques = +2 a tu Defensa).
- **Atacar:** el DJ anuncia el modificador neto · 2d6 + Atq − Def. 10+ daño y efectos · 7–9 daño sin estados · 6– fallo (Expuesto).
- **Defender:** 2d6 + Def − Atq. 10+ nada · 7–9 mitad · 6– todo y efectos · contra un área, cada PJ tira su Defensa.
- **Daño:** dados de poder = potencia (+1 debilidad, Brutal con 10+, crítico, Potenciado+, rango superior; −1 si es de área **y alcanza a 2+ objetivos**) − Arm; mitad por 7–9, por Resistencia y por cada rango que el objetivo te supere; mínimo 1 · **golpe aguantado:** un impacto de PNJ quita como mucho la mitad de los PV máximos de un compañero.
- **Dados de poder:** Bebé d4 · Novato d6 · Campeón d8 · Perfecto d10 · Definitivo d12 · VF = mitad de las caras.
- **Turno:** Tamer (1 acción + mover) y Digimon (1 acción + mover) · gratis: digievolucionar y Dado de Vínculo, una vez por asalto cada uno · 1 reacción por asalto · **Agotadora:** tras una P3 (o apoyo con Curar/Escudo), el turno siguiente ninguna Agotadora.
- **Dado de Vínculo:** Ventaja en una tirada del compañero; un 6 da 1 Chispa (Vínculo 4+: 5–6).
- **Chispa:** empieza en 1 (cada sesión, sube hasta el Vínculo) · máximo 3 + Vínculo · +1 por fallo, Resonancia, Crisis, Emblema · digievolucionar = 2 por nivel sobre el estable (+1 Hambriento) · Esfuerzo 1 = +1.
- **Digievolución:** PV llenos y estados limpios hasta el final de la escena (solo si se paga con Chispa, una vez por forma y escena) · a 0 PV vuelve a la forma de partida y queda Agotado · si cae la forma estable, Derrotado · al terminar: Hambriento; si subió 2 o más niveles, regresión a Bebé II.
- **Escena:** tramo continuo con un lugar y un objetivo; termina cuando el DJ corta (cambio de lugar, paso de tiempo, descanso). Dos combates seguidos sin pausa son la misma escena.
- **Triángulo:** Vacuna > Virus > Datos > Vacuna: ±1.
- **Iniciativa:** 2d6 + Ini − Ini del enemigo más rápido: 7+ fase rápida.
- **Expuesto:** −1 Def hasta el final de su próximo turno (PNJ: +1 a los ataques de los PJ).
- **Tamer atacado:** solo si se telegrafió, está Expuesto en la zona del atacante o lo alcanza un área · Defensa 2d6 + DES + Atletismo − Atq · Peligro = max(1, rango del atacante) (+1 si es P3).

### 22.2 Glosario fijo (usar siempre estos términos)
Bebé I, Bebé II, Novato, Campeón, Perfecto, Definitivo, Armadura, Híbrido, Indeterminado · rango (0–4) · Vacuna, Datos, Virus, Libre, Variable, Desconocido, SIN DATOS, Ninguno · Tamer, compañero, pareja, DJ · Chispa, Vínculo, Dado de Vínculo (DV), Resonancia, Resonancia del Emblema, Carga, Aguante · PV, Atq, Def, Arm, Ini, VF, dado de poder · P1, P2, P3, Firma, Agotadora · Toque, Distancia, Larga, Personal · Individual, Ráfaga, Zona, Total · fase rápida, fase enemiga, fase lenta · reacción · escena, combate · forma estable, forma temporal, forma de partida · Expuesto, Agotado, Hambriento, Derrotado, Potenciado, Potenciado+ · golpe aguantado, regla de espejo · Esbirro, Estándar, Élite, Jefe, Legendario, Pelotón, Refuerzo I y II · PA (puntos de amenaza), nivel de referencia, índice de amenaza · avances del compañero · cualidad (rasgo personal) y virtud (del Emblema).

**Términos que se parecen y no hay que mezclar:**

| Término | Qué es | No confundir con |
|---|---|---|
| **Nivel** (Novato…Definitivo; Armadura, Híbrido, Indeterminado) | La etapa del Digimon; para comparar se usa siempre el **rango** (0–4) de la fila que usa | **nivel de Tamer** (1–10), **nivel de programa** (1–3), **nivel estable** y **nivel máximo** del Vínculo |
| **Arm** | La estadística de armadura plana | **Armadura**, el nivel de los Digi-Huevos (20.1) y la plantilla; *Armor*, un tipo de la familia Máquina |
| **Indeterminado** | El nivel `Unknown` de los datos | **Desconocido**, el atributo `Unknown` |
| **Agotado** | Estado tras caer una forma temporal (7.3) | **Agotadora**, propiedad de las técnicas P3 y de apoyo con Curar o Escudo |
| **Mejora** | Palabra clave de apoyo (11.4) | **Avances del compañero** (17.4) |
| **Místico** | Un **rol** (12.1) | **Arcano**, la familia de magos y hadas (9.1) |
| **familia Oscuro** | Demonios, no muertos, fantasmas (9.1) | **Modo Oscuro** (plantilla, 20.4) y **digievolución oscura** (5.10) |
| **Grito de guerra** | Técnica genérica (12.4) | **¡A por ellos!**, la Orden del Inspirador (17.3) |
| **Escurridizo** | Rasgo del rol Ágil | **Huidizo**, rasgo del trasfondo Pícaro |
| **Explorador/a** | Trasfondo (3.4) | **Batidor**, la Senda (3.5); **Ojeador**, el papel de viaje (18.3) |
| **Protector** | Senda (3.5) | *Protector*, el rasgo del trasfondo Hermano/a mayor |
| **Purga** | Combo de Luz (20.9) | **Purgado**, el programa 25 |
| **Sobrecarga controlada** | Resultado 10+ de la digievolución forzada (5.10) | **Overclock**, el programa 24 |
| **Bloqueos** | Agujas de Control, Torres Oscuras, Sellado (20.8) | **Candado**, el programa 15 |
| **Resonancia** | Un 6 en el Dado de Vínculo da Chispa (5.3) | **Resonancia del Emblema** (cap. 16) y **Catalizador**, el programa 26 |
| **Carga** | Los puntos del Digivice para programas | **Cargar** (acción), **Cargado** (palabra clave) y **Guardia de carga** (Jefe) |
| **Valor** | Atributo del Tamer (VAL) | Emblema del Valor |
| **Cualidad** | Rasgo personal positivo (3.6) | **Virtud**, la del Emblema (cap. 16) |

### 22.3 Reglas de redacción
1. **Originalidad:** ningún texto se copia ni se traduce de los perfiles oficiales ni de otros juegos. Las descripciones del bestiario se escriben desde cero (una o dos frases de tono propio: aspecto, costumbre, gancho de aventura). Los nombres de Digimon y de técnicas se usan en su forma oficial inglesa.
2. **Capas:** el capítulo de inicio rápido solo usa el **Núcleo de primera sesión** (1.1). El resto del núcleo [N] se presenta en las sesiones siguientes; todo [A] y [O] va en recuadros o capítulos aparte.
3. **Cifras:** cualquier número del bestiario sale del generador; si un capítulo necesita un ejemplo, que use las fichas de 21.10.
4. **Aventuras de inicio:** deben respetar el presupuesto con el nivel de referencia y el índice de amenaza (19.2), usar el Jefe de la aventura de la tabla de 19.2, ofrecer siempre una huida o un objetivo de escena, telegrafiar los ataques a Tamers y no usar enemigos dos niveles por encima del nivel de referencia salvo como presagio que huye.
5. **Tono:** aventura juvenil, amistad, valentía y misterio. Los Tamers no mueren; los Digimon renacen salvo con el módulo de Borrado.
6. **Parejas pregeneradas:** el manual y la aventura de inicio deben incluir **de 4 a 6 parejas pregeneradas**: Tamer completo (con su Senda como paquete cerrado de 3.1), compañero Novato con su ficha impresa, **su ficha de Campeón ya impresa**, Bebé II, personalidad y **3 programas ya elegidos**. Al menos una pareja debe tener un compañero robusto (Agumon, Gabumon, Gomamon) y como mucho una, un compañero frágil (4.2).

### 22.4 Riesgos vigilados y cómo quedan resueltos
| Riesgo señalado | Solución en esta versión |
|---|---|
| Digievolución en el asalto 1 | A Vínculo 1: Chispa inicial 1, coste 2 y Crisis la primera vez (medido: quien digievoluciona lo hace en el asalto 1,5–1,8, tras una Crisis). Desde Vínculo 2 la Chispa inicial ya paga un nivel: el **nivel de referencia** (19.2) cuenta el nivel que el grupo alcanza en el asalto 1 y el Jefe se **refuerza** según el Vínculo. |
| PV comprimidos y solapados entre niveles | PV = VF × (7 + m): los modificadores escalan con el nivel; validación por rangos. |
| Armadura que se acumula (Tanque + Máquina) | Arm máximo 2 en la ficha y 3 con programas; nunca crece con el nivel. Tanque con Atq 0 y PV +1 VF (no +2): los duelos Tanque contra Tanque bajan a 4,3–4,8 asaltos. |
| Segunda barra de vida demasiado dura | Como mucho dos barras: la forma temporal y la de partida; si cae la estable, Derrotado (sin cascada); volver a una forma caída cura solo la mitad; las formas iguales o inferiores a la estable conservan el daño. El presupuesto se calibró con estas reglas. |
| Novatos derrotados de un golpe | **Golpe aguantado:** un impacto de PNJ no quita más de la mitad de los PV máximos de un compañero; la Chispa del mismo impacto paga la emergencia. |
| Tamers frágiles | Ataques a Tamers solo telegrafiados, Expuestos o por área, uno por asalto; Instinto protector; estados en Tamers acotados (6.11); el jugador sigue jugando con su compañero si su Tamer cae. |
| Jefe demasiado corto o demasiado letal | Jefe de la aventura por tramo de Vínculo (19.2) con Refuerzo I o II, turno de Jefe = asalto, Firma cargada que se lanza al asalto siguiente, índice de amenaza por ficha. Medido: de 2,9 a 5,3 asaltos y de 0 a 28 % de derrota según el tramo. |
| Estados que no hacían nada contra PNJ | Regla de espejo (2.1) y tabla de traducción (11.4). |
| Áreas que debilitaban a su usuario | −1 dado solo si la técnica alcanza a 2 o más objetivos; la ficha imprime ambos dados. |
| Curación a voluntad | Las técnicas de apoyo con Curar o Escudo son Agotadoras; Sanador da +VF solo al objetivo principal. |
| Clasificador por nombre con errores | Dos pasadas (nombre y contexto que empieza tras el nombre de la técnica), raíces de contexto propias por elemento, frases antes que palabras, reglas de palabra completa sin sufijos -er/-y, overrides validados contra los datos y revisión manual obligatoria de ≈150 fichas. |
| Legendarios asignados por tipo | Lista curada **por id** (los nombres se repiten); la plantilla solo se aplica a PNJ. |
| Roles sesgados | Toque y Distancia solo puntúan si los detecta una palabra; Anomalía con rol primario Versátil; rol fijado por el jugador. |
| Muchos dados y cálculo | 3d6 como mucho por tirada; daño fijo por defecto para esbirros y pelotones; Energía eliminada; el DJ anuncia el modificador neto. |
| Engordar el núcleo con injertos | Todo lo que viene de B y C, salvo el Dado de Vínculo y Hambriento, va en [A] o [O]; Núcleo de primera sesión explícito (1.1) y parejas pregeneradas (22.3). |
