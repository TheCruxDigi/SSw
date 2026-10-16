# Técnicas, elementos y estados

Un Digimon no pelea solo con garras y dientes: pelea con **técnicas**. El aliento de fuego de un Novato, la lluvia de misiles de un cíborg o el brillo cálido que cura a un amigo herido son técnicas, y todas se describen con el mismo vocabulario, corto y cerrado. En este capítulo aprenderás a leer ese vocabulario: qué significa cada potencia, cuántos dados tiras, hasta dónde llega una técnica, a cuántos enemigos alcanza y qué hacen sus palabras clave.

Después verás todo lo que pasa alrededor de una técnica cuando golpea: los **estados alterados** que deja (Quemado, Congelado, Dormido…), el **triángulo de atributos** (Vacuna, Datos y Virus), las **14 familias** con su rasgo, sus debilidades y sus resistencias, y los **14 elementos**, con la regla opcional de los combos elementales. Al final leerás tres técnicas oficiales paso a paso y tendrás un resumen con lo esencial. No hace falta que lo memorices: la ficha de cada Digimon ya trae casi todo calculado. Este capítulo es el diccionario para entenderla.

## Cómo se lee una técnica

Toda técnica, oficial o genérica, ocupa una sola línea de la ficha y sigue siempre el mismo orden:

```
Nombre — Potencia [Agotadora] · Alcance · Área · Elemento · Palabras clave  [dados de daño]
```

Así aparece la Firma de [[Agumon]] en su ficha del bestiario:

```
Pepper Breath — P2/P3 (Agotadora) · Distancia · Individual · Fuego · Quemar, Brutal  [2d6 / 3d6]
```

| Parte | Qué te dice |
|---|---|
| **Nombre** | El nombre oficial de la técnica, siempre en inglés. Da color a la escena, pero no cambia las reglas. |
| **Potencia** | Cuántos dados de poder tiras (P1 = 1, P2 = 2, P3 = 3) y si la técnica es **Agotadora**. |
| **Alcance** | Hasta dónde llega: Toque, Distancia, Larga o Personal. |
| **Área** | A cuántos objetivos alcanza: Individual, Ráfaga, Zona o Total. |
| **Elemento** | De qué está hecha (Fuego, Agua, Luz…). Decide si el objetivo es débil o resistente. |
| **Palabras clave** | Sus efectos especiales, **como mucho dos**: un estado, un efecto de daño, un apoyo o una táctica. |
| **Dados** | Los dados de daño ya calculados con el dado de poder del Digimon. En las técnicas de área, también los dados contra 2 o más objetivos. |

### La potencia: P1, P2 y P3

La potencia te dice cuántos **dados de poder** tiras. El dado de poder depende del nivel del Digimon (d6 para un Novato, d8 para un Campeón…), así que la misma técnica pega más fuerte cuando la usa una forma más alta.

| Potencia | Dados | Uso | Para qué sirve |
|---|---|---|---|
| **P1 Ligera** | 1 | A voluntad | La técnica básica, las maniobras de rol y las técnicas menores. |
| **P2 Fuerte** | 2 | A voluntad | La técnica de diario. |
| **P3 Firma** | 3 | **Agotadora** | La técnica emblemática. Cada ficha tiene como mucho una. |
| **P2/P3 versátil** | 2 o 3 | Como P2, a voluntad; como P3, Agotadora | La Firma de los Digimon que solo tienen una técnica oficial. |

**La Firma.** Es la técnica que el Digimon grita a pleno pulmón en el momento decisivo: la P3 de su ficha o su P2/P3 versátil. Ninguna ficha tiene más de una P3, ni siquiera con técnicas prestadas: una técnica heredada que era Firma se hereda como **P2**, salvo que sustituya a la Firma de la forma actual (capítulo 5), y el programa Tarjeta Digimon usa una técnica ajena **como P2 como máximo** (capítulo 9). Algunos roles añaden su **palabra de Firma** a la técnica emblemática si le queda hueco (Brutal, Provocar, Rápido, Certero o Perforante). No tienes que hacer nada: ya viene incluida en la ficha.

**Agotadora.** Tras usar una técnica Agotadora, el Digimon **no puede usar ninguna técnica Agotadora en su siguiente turno**. Son Agotadoras:

- Las técnicas P3.
- Las P2/P3 versátiles **cuando se usan como P3**. Usada como P2, la misma técnica es a voluntad.
- Las técnicas de apoyo con Curar o Escudo.
- La maniobra Pulso restaurador del rol Apoyo.

Un Jefe nunca usa su Firma (ni otra técnica Agotadora) dos veces en el mismo asalto ni en dos asaltos seguidos. Hay formas de saltarse la espera: si el Tamer usa **Animar** y elige esa opción, la Firma de su compañero queda lista aunque la usara en su turno anterior. No confundas **Agotadora** (una propiedad de las técnicas) con **Agotado** (el estado que sufre un compañero cuando cae su forma temporal).

### Los dados de poder

Cada nivel tiene su dado de poder y su **VF** (valor fijo), que es la mitad de las caras del dado. Muchas palabras clave usan el VF del usuario para medir su efecto: el daño de Quemar, el Escudo, el empujón contra una pared…

| Nivel | Dado | VF | P1 | P2 | P3 | P2 contra 2+ objetivos | P3 contra 2+ objetivos |
|---|---|---|---|---|---|---|---|
| Bebé | d4 | 2 | 2,5 | 5 | — | 2,5 | — |
| Novato | d6 | 3 | 3,5 | 7 | 10,5 | 3,5 | 7 |
| Campeón | d8 | 4 | 4,5 | 9 | 13,5 | 4,5 | 9 |
| Perfecto | d10 | 5 | 5,5 | 11 | 16,5 | 5,5 | 11 |
| Definitivo | d12 | 6 | 6,5 | 13 | 19,5 | 6,5 | 13 |

*Las columnas de potencia muestran el daño medio antes de restar la Arm del objetivo.*

La cuenta completa del daño está en el capítulo 7. En resumen:

1. Tiras tantos dados de poder como la **potencia** de la técnica.
2. Sumas **+1 dado** por cada uno de estos: el objetivo es **débil** al elemento; **Brutal** con 10+; crítico; **Potenciado+** o programa Potencia; tu Digimon es de **rango superior** al objetivo; plantilla Legendario; **Cargado**; **Retroceso**; Furia de un Jefe.
3. Restas **1 dado** si la técnica es de área **y alcanza de verdad a 2 o más objetivos**. Siempre tiras al menos 1 dado.
4. Al total le restas la **Arm** del objetivo (salvo con Perforante).
5. Lo divides a la mitad (redondeando hacia abajo) por cada una de estas: el defensor PJ sacó 7–9; el objetivo **resiste** el elemento (salvo con Perforante); por cada rango que el objetivo esté por encima del atacante.
6. Si hubo impacto, el daño mínimo es 1. Un solo impacto de un PNJ nunca quita a un compañero más de la mitad de sus PV máximos (**golpe aguantado**), y los Escudos absorben el daño antes que los PV.

### Cómo reparte el bestiario las potencias

No tienes que calcular nada: cada ficha ya trae sus potencias. Pero si te preguntas por qué una técnica es P1 y otra P3, estas son las reglas que usa el bestiario:

- **Bebé I:** todas sus técnicas son P1. **Bebé II:** la primera es P2 y el resto, P1.
- **Una sola técnica oficial:** es su Firma, P2/P3 versátil.
- **Varias técnicas oficiales:** la Firma es P3; la segunda, P2; la tercera, P2 si el Digimon es de rango 3 o más (si no, P1); el resto, P1.
- Una técnica que no es la Firma y lleva una **palabra menor** en el nombre (petit, mini, baby, bubbles…) baja una potencia.
- Una técnica de daño **P1 es siempre Individual**.
- Un Digimon **sin técnicas oficiales** recibe la Firma genérica *Descarga de datos*: P2/P3 · Distancia · elemento de la afinidad de su familia.

### El alcance

| Alcance | Regla |
|---|---|
| **Toque** | Un objetivo en tu zona. Al usarla quedas **trabado** con él. Con área, el área está en tu zona: Toque + Ráfaga = 2 objetivos de tu zona; Toque + Zona o Total = todos los enemigos de tu zona (y quedas trabado con todos). |
| **Distancia** | Un objetivo (o el área) en tu zona o en una adyacente. Si estás trabado: −1 a la tirada. |
| **Larga** | Hasta 2 zonas de distancia. Si estás trabado: −1 a la tirada. |
| **Personal** | Solo el usuario (técnicas de apoyo sobre sí mismo). Personal + Zona = centrada en el usuario: afecta a su zona. |

Dos rasgos estiran el alcance: el rol **Tirador** lleva su Firma de Distancia a Larga (ya viene así en la ficha) y la familia **Arcano** puede usar sus técnicas de Distancia con alcance Larga.

### El área

| Área | Dados | Regla |
|---|---|---|
| **Individual** | Sin cambios | Un objetivo. |
| **Ráfaga** | −1 si alcanza a 2 | Hasta 2 objetivos distintos dentro del alcance. Una sola tirada, comparada con la Def de cada objetivo. |
| **Zona** | −1 si alcanza a 2 o más | Todos los enemigos de una zona dentro del alcance y, a elección del atacante, cualquier Tamer de esa zona (como mucho 1 ataque contra cada Tamer por asalto). Una sola tirada. |
| **Total** | −1 si alcanza a 2 o más | Todos los enemigos dentro del alcance. En el bestiario solo aparece en la Firma de rango 4; un Jefe o un Legendario puede usar su Firma de Zona como Total. No admite control duro. |

Cuando **tu** compañero usa una técnica de área, haces **una sola tirada** y el DJ la compara con la Def de cada objetivo: puede que impactes de lleno a uno y solo roces a otro. Cuando la usa un **PNJ**, cada PJ afectado tira su propia Defensa y el DJ tira el daño una vez. Contra un solo objetivo, una técnica de área cuenta como Individual y no pierde ningún dado. Por eso la ficha imprime los dos valores: «2d10; contra 2+: 1d10».

### El elemento y las palabras clave

Cada técnica tiene **un elemento** de una lista cerrada de 14. El elemento decide si el objetivo es débil (+1 dado) o resistente (mitad de daño). Los verás a fondo más adelante en este capítulo.

Cada técnica lleva **como mucho 2 palabras clave**, elegidas entre las 35 del juego. Se agrupan en cuatro familias: **Daño** (cambian el impacto), **Estado** (dejan un estado alterado), **Apoyo** (curan, protegen o refuerzan) y **Táctica** (posición y tiempo). Las tienes todas en la sección siguiente.

### Técnicas de apoyo

Algunas técnicas no hacen daño: curan, protegen o refuerzan. Son las **técnicas de apoyo**, y siguen sus propias reglas:

- **No hacen daño ni piden tirada.** Simplemente funcionan.
- Afectan al usuario o a un aliado a su alcance. Con alcance Personal, solo al usuario.
- **No llevan estados ni tácticas**, salvo alguna excepción documentada en su ficha, como el Kohenkyo de [[Renamon]], que la oculta.
- Si llevan **Curar** o **Escudo**, son **Agotadoras**, aunque sean P1 o P2.
- Una técnica de apoyo sin ninguna palabra que dependa de la potencia, como Kohenkyo, imprime la potencia como «—».

El rol **Apoyo** saca el máximo partido a estas técnicas: con su rasgo *Sanador*, afectan a un aliado más dentro del alcance, y el objetivo principal (solo él) suma +VF a la curación o al Escudo.

### La técnica básica

Además de sus técnicas oficiales, todo Digimon tiene una **técnica básica**: **P1 · Toque · Individual**, sin palabras clave. Su nombre y su elemento dependen de la familia (la tienes en la tabla de familias, más abajo): un Saurio muerde con *Mordisco*, un Sagrado golpea con *Golpe sagrado*. Los Tiradores la usan como **Disparo**, de alcance Distancia, y la familia Arcano también la tiene a Distancia. Todos los Digimon, salvo los Bebés, tienen además la **maniobra de su rol** (capítulo 5), que también está siempre disponible.

> **Si es tu primera vez:** para jugar tu primer combate te basta con mirar tres cosas de cada técnica: la potencia (cuántos dados), el alcance (si llegas al enemigo) y las palabras clave (qué pasa si sacas 10+). Todo lo demás lo irás descubriendo cuando aparezca en la mesa.

## Las 35 palabras clave de efecto

Las palabras clave son el corazón de cada técnica: convierten un simple ataque en un aliento que quema, un zarpazo que atraviesa la armadura o un canto que duerme al enemigo. Cada técnica lleva **como mucho 2**. En las tablas, la columna «Se activa» te dice cuándo funciona cada una:

- **Al usarla:** funciona impacte o no.
- **Al impactar:** con 7+ del atacante (o con 7–9 o 6– en la Defensa del PJ, si ataca un PNJ).
- **Con 10+:** solo con un 10+ del atacante o un 6– del defensor.
- **Requiere preparación:** hay que gastar una acción antes.
- **Sin tirada:** palabras de apoyo, que funcionan sin tirar en una técnica de apoyo.

Cuando una palabra usa el **VF**, es siempre el del usuario de la técnica. Cuando se habla del **Místico**, es el **rol** Místico, no la familia Arcano.

### Daño (7)

| Palabra | Se activa | Regla exacta | Duración | Por ejemplo |
|---|---|---|---|---|
| **Perforante** | Al impactar | Ignora la Arm y la Resistencia elemental del objetivo. | Inmediata | Harpoon Torpedo ([[Ikkakumon]]) |
| **Brutal** | Con 10+ (o 6– del defensor) | +1 dado de daño. | Inmediata | Pepper Breath ([[Agumon]]) |
| **Certero** | Al usarla | +1 a la tirada de ataque del PJ; si la usa un PNJ, −1 a la tirada de Defensa del PJ. Ignora Cobertura y Oculto. | Inmediata | Super Shocker ([[Tentomon]]) |
| **Drenar** | Al impactar | El usuario recupera PV iguales a la mitad del daño infligido (después de todas las reducciones). | Inmediata | Death Claw ([[Devimon]]) |
| **Retroceso** | Al usarla | +1 dado de daño; el usuario sufre VF de daño (ignora la Arm) después de resolverla, impacte o no. | Inmediata | Gravity Bang ([[Gravimon]]) |
| **Ejecutar** | Con 10+ (o 6– del defensor) | Solo en técnicas Individuales. Si tras el daño el objetivo queda con PV iguales o inferiores a 2 × VF del usuario, cae a 0. Jefes y Legendarios son inmunes: contra ellos da +1 dado. | Inmediata | Talisman of Light ([[Taomon]]) |
| **Cargado** | Requiere preparación | El usuario gasta una acción en **Cargar** (−1 Def hasta su próximo turno). En su siguiente turno la lanza con +1 a la tirada y +1 dado. Si queda Aturdido, Dormido o Sellado, pierde la carga. Los Jefes la telegrafían (Guardia de carga, capítulo 12). | 1 turno | Terra Force ([[WarGreymon]]) |

### Estado (20)

Todas estas palabras aplican su estado con un **10+ en el ataque del PJ** o con un **6– en la Defensa del PJ** (si la técnica la usa un PNJ). Si el atacante tiene el **rol Místico**, también con 7–9, salvo las de control duro (Aturdir, Dormir y Regresión), que **nunca** se aplican con 7–9.

| Palabra | Regla exacta | Duración | Por ejemplo |
|---|---|---|---|
| **Quemar** | **Quemado:** al inicio de cada uno de sus turnos (un Jefe, una vez por asalto) pierde VF PV (el VF del causante, a la mitad por cada rango que el afectado supere al causante; mínimo 1). Una técnica de Agua o Hielo que le alcance lo apaga. | 2 turnos | Fox Fire ([[Garurumon]]) |
| **Congelar** | **Congelado:** no puede moverse ni usar técnicas de Toque; −2 Def. El daño de Fuego lo descongela. | 1 turno | Ice Blast ([[Seadramon]]) |
| **Paralizar** | **Paralizado:** en su turno solo puede moverse o actuar (no ambas cosas); −1 a sus ataques; sin reacciones. | 2 turnos | Sparkling Thunder ([[Elecmon]]) |
| **Veneno** | **Envenenado:** al final de cada uno de sus turnos (un Jefe, una vez por asalto) pierde VF PV (el VF del causante, a la mitad por cada rango que el afectado supere al causante; mínimo 1). No puede recuperar PV con Curar ni con objetos. | 3 turnos | Poison Ivy ([[Palmon]]) |
| **Aturdir** | **Aturdido:** pierde su próxima acción (puede moverse). A un Jefe solo le quita una acción del asalto. **Control duro.** | 1 turno | Vulcan's Hammer ([[Zudomon]]) |
| **Dormir** | **Dormido:** pierde sus turnos; los ataques contra él tienen +2. Despierta al recibir daño o si un aliado gasta su acción en despertarlo. **Control duro.** | Hasta 2 turnos | Lullaby Bubble ([[Otamamon]]) |
| **Cegar** | **Cegado:** −2 a sus ataques; no puede usar técnicas de alcance Larga. | 1 turno | Holy Shot ([[Unimon]]) |
| **Confundir** | **Confundido:** al empezar su turno tira 1d6. Con 1–2, usa su técnica P1 contra la criatura más cercana (la elige el DJ y puede ser aliada) y pierde la acción; con 3–6, −1 a sus tiradas. | 2 turnos | Cat's Eye ([[Gatomon]]) |
| **Asustar** | **Asustado:** no puede acercarse a la fuente del miedo ni usar técnicas de Toque contra ella; −1 a cualquier ataque contra ella. | 2 turnos | Soul Chopper ([[Phantomon]]) |
| **Encantar** | **Encantado:** no puede atacar a la fuente; si no tiene otro objetivo, usa Defender. | 1 turno | Hearts Attack ([[Monzaemon]]) |
| **Sellar** | **Sellado:** no puede usar técnicas P3, digievolucionar ni cambiar de modo; su Tamer no puede usarle programas. | 1 turno | Heaven's Gate ([[MagnaAngemon]]) |
| **Regresión** | Contra un compañero en forma temporal: esa forma termina y vuelve a su forma de partida con los PV guardados (sin quedar Agotado); si estaba en una forma estable, queda Sellado 2 turnos. Contra un PNJ: queda Sellado y Debilitado 1 turno (el DJ puede narrar que pierde su forma un instante). Jefes y Legendarios: solo Sellado 1 turno. Los Bebés no la aplican. **Control duro.** | Inmediata (o Sellado) | Rewind Abyss 13 ([[Diaboromon (X Antibody)]]) |
| **Ralentizar** | **Ralentizado:** pasa a la fase lenta (un PNJ actúa el último); no puede Correr; −1 Def. | 2 turnos | Rain of Pollen ([[Floramon]]) |
| **Atrapar** | **Atrapado:** no puede moverse; −1 a sus ataques. Liberarse le cuesta su acción (un PJ tira 2d6 + Atq − Atq del captor y necesita 7+; un PNJ lo consigue automáticamente). Queda libre si el captor cae, queda Aturdido o se aleja. | Hasta liberarse | Hell's Hand ([[Bakemon]]) |
| **Debilitar** | **Debilitado:** −1 a sus ataques y su daño total se reduce en el VF del causante (mínimo 1). | 2 turnos | Curse of the Queen ([[Nefertimon]]) |
| **Romper** | **Roto:** −2 Arm (mínimo 0); si ya tenía 0, −1 Def. No se acumula. | Toda la escena | Scissor Claw ([[Kuwagamon]]) |
| **Marcar** | **Marcado:** el siguiente ataque contra él, de quien sea, tiene +2. | Hasta el próximo ataque | Providence Scan ([[Nightchiropmon]]) |
| **Derribar** | **Derribado:** debe gastar su movimiento en levantarse; las técnicas de Toque contra él tienen +1. Si volaba, cae a tierra. | Hasta levantarse | Diamond Shell ([[Armadillomon]]) |
| **Empujar** | Lo desplazas 1 zona (a tu elección) y deja de estar trabado. Si choca contra algo sólido o cae en una zona de Peligro, recibe +VF de daño. | Inmediata | Air Shot ([[Patamon]]) |
| **Provocar** | **Provocado:** en su próximo turno debe atacar al usuario; si ataca a otro, −2 a esa tirada. | 1 turno | Ice Blast ([[Seadramon]]) |

### Apoyo (4)

| Palabra | Regla exacta | Duración | Por ejemplo |
|---|---|---|---|
| **Curar** | Un aliado (o el usuario) recupera PV iguales a los dados de poder de la técnica (P1: 1 dado; P2: 2; P3: 3). Si es de área, todos los aliados de una zona, con −1 dado. Una técnica de apoyo con Curar es **Agotadora**. En una técnica de daño, el usuario recupera 1 dado al impactar. | Inmediata | Healing Glow ([[Cutemon]]) |
| **Escudo** | Un aliado (o el usuario) gana un Escudo igual a VF × potencia (P1 = VF, P2 = 2 VF, P3 = 3 VF) hasta el final de la escena. Los Escudos no se acumulan: se queda el mayor. Una técnica de apoyo con Escudo es **Agotadora**. | Toda la escena | Shield of the Just ([[Gallantmon]]) |
| **Mejora** | P1: el aliado queda **Potenciado** (+1 a la tirada de su próximo ataque). P2: queda **Potenciado+** (+1 a la tirada y +1 dado). P3: Potenciado+ para todos los aliados de una zona. | Hasta su próximo ataque | Liquid Veil ([[Divemon]]) |
| **Purificar** | Elimina estados negativos: uno (P1), todos los de un aliado (P2) o todos los de los aliados de una zona (P3). En una técnica de daño, además elimina el Escudo y el Potenciado del objetivo y da +1 dado contra la familia Oscuro. | Inmediata | Heaven's Knuckle ([[Angemon]]) |

No confundas **Mejora** (esta palabra clave) con los **avances del compañero** (capítulo 11).

### Táctica (4)

| Palabra | Se activa | Regla exacta | Duración | Por ejemplo |
|---|---|---|---|---|
| **Rápido** | Al usarla | Antes de usarla, el usuario puede moverse 1 zona extra sin provocar ataques de retirada. | Inmediata | Lightning Paw ([[Gatomon]]) |
| **Contraataque** | Requiere preparación | Se prepara gastando la acción. Hasta su próximo turno, la primera vez que un enemigo le ataque y falle (Defensa del PJ 10+, o ataque del PJ 6– contra un PNJ que la tenga preparada), el atacante recibe el daño de la técnica sin tirada. | Hasta su próximo turno | Kabutogaeshi ([[Ryudamon]]) |
| **Invocar** | Al impactar | Crea una invocación (un enjambre, un banco de peces, piezas de ajedrez…) en una zona a su alcance durante 2 asaltos. Al inicio de cada turno del usuario, inflige VF de daño (menos Arm) a un enemigo de esa zona; ese daño se divide a la mitad por cada rango que el objetivo supere al usuario. Cada usuario mantiene **como mucho una invocación activa**: crear otra disipa la anterior. Una técnica de área enemiga sobre esa zona la disipa. | 2 asaltos | Marching Fishes ([[Gomamon]]) |
| **Ocultar** | Al usarla | El usuario queda **Oculto** (impacte o no; en una técnica de apoyo, sin tirada) hasta que ataque: no puede ser objetivo de técnicas de Distancia ni Larga, y su primer ataque tiene +2. | Hasta que ataque | Kohenkyo ([[Renamon]]) |

### Reglas comunes de las palabras clave

- **Una palabra de apoyo en una técnica de daño** funciona distinto: la técnica hace su daño y, al impactar, el efecto de apoyo recae sobre el **usuario**. *Curar:* recupera 1 dado. *Escudo:* gana VF de Escudo. *Mejora:* queda Potenciado (como P1). *Purificar:* se libra de uno de sus propios estados y, además, la técnica da +1 dado contra la familia Oscuro.
- **Palabras con valor numérico** (Quemar, Veneno, Debilitar, Empujar, Invocar, Escudo, Curar y Ejecutar): calculan su efecto con el VF o los dados del usuario. No tienes que anotar nada más en la ficha.
- **Dos palabras, dos efectos.** Si una técnica lleva un estado y un efecto de daño (Pepper Breath: Quemar y Brutal), cada uno se activa en su momento. Con un 10+ se aplican los dos; con un 7–9, solo los que se activan al impactar.

> **Consejo para el DJ:** cuando un jugador declare una técnica, léele en voz alta sus palabras clave antes de que tire («si sacas 10+, lo quemas y sumas un dado»). Así el 10+ se celebra como merece y nadie se olvida de un efecto a mitad del asalto.

## Estados alterados

Un estado alterado es lo que queda después del golpe: el fuego que sigue ardiendo, el hielo que no deja moverse, la nana que adormece al enemigo. Casi todos llegan a través de las palabras clave del grupo Estado que acabas de ver, pero otros aparecen por el propio combate, por la digievolución o por el hambre. Aquí tienes todas sus reglas juntas.

### Reglas generales

- **Cuándo entra un estado.** Con un **10+ en el ataque del PJ** o con un **6– en la Defensa del PJ** cuando ataca un PNJ. Si el atacante tiene el **rol Místico** (rasgo *Maestro de estados*), también con 7–9, salvo los de control duro.
- **Cambiar daño por estado.** Si tu ataque saca 7–9, haces el daño completo pero sin estados. Si prefieres el estado, puedes renunciar a todo el daño para aplicarlo, salvo que sea de control duro.
- **Duración.** «1 turno» dura hasta el final del siguiente turno del afectado; «2 turnos», hasta el final de su segundo turno. Para un Jefe o un Legendario, su turno es el asalto completo: sus estados avanzan una vez por asalto (al inicio de su primera acción) y sus duraciones se cuentan en asaltos.
- **No se acumulan.** Si vuelves a aplicar un estado que el objetivo ya tiene, solo se renueva la duración. Lo mismo pasa con las invocaciones: cada usuario mantiene como mucho una activa.
- **Digievolucionar los borra todos**, salvo Hambriento. A veces es la mejor salida de un apuro.
- **Control duro:** Aturdir, Dormir y Regresión. Nunca se aplican con 7–9, una técnica de área Total no puede llevarlos y los Jefes los sufren de forma limitada.
- **Daño por turno** (Quemado, Envenenado e invocaciones): usa el VF de quien lo causó, se divide a la mitad por cada rango que el afectado esté por encima del causante (mínimo 1) y a un Jefe se le aplica una vez por asalto.
- **Cómo se quitan.** Con la palabra Purificar, la maniobra *Pulso restaurador* del rol Apoyo, el programa Purgado (capítulo 9), el Disco antiestado (capítulo 10) o digievolucionando. Además, varios estados tienen su propia salida: el Dormido despierta al recibir daño, el Agua y el Hielo apagan el Quemado, el Fuego descongela y el Atrapado puede liberarse.
- **Inmunidades.** Algunas familias, roles y plantillas no sufren ciertos estados. Lo dice su rasgo, y tienes la lista completa al final de esta sección.

### Los estados de las técnicas, de un vistazo

Los 20 estados de las palabras clave tienen su regla exacta en la tabla del grupo Estado. Para recordarlos en la mesa, piensa en lo que le hacen a quien los sufre:

- **Le quitan PV cada turno:** Quemado (2 turnos) y Envenenado (3 turnos, y además no deja recuperar PV con Curar ni con objetos).
- **Lo dejan sin actuar (control duro):** Aturdido y Dormido. La Regresión rompe una forma temporal o sella al objetivo.
- **Lo frenan o lo clavan al sitio:** Congelado, Paralizado, Ralentizado, Atrapado y Derribado. Empujar lo saca de su zona de golpe.
- **Le nublan el juicio:** Cegado, Confundido, Asustado, Encantado y Provocado.
- **Lo dejan vulnerable:** Debilitado, Roto, Marcado y Sellado.

### Cuando el estado lo sufre un PNJ: la regla de espejo

El DJ no tira para impactar: los jugadores tiran el ataque y también la Defensa. Por eso, cuando un estado cambia las tiradas de un PNJ, se aplica **con el signo cambiado a la tirada del PJ** que se le opone. Si un PNJ Cegado tiene −2 a sus ataques, en la mesa eso significa que tu compañero suma +2 a su Defensa contra él. Lo que no es un modificador a una tirada (no poder moverse, perder las reacciones, no usar Larga) funciona igual en los dos bandos.

| Estado | Si lo sufre un PNJ | Si lo sufre un PJ |
|---|---|---|
| **Paralizado** | +1 a la Defensa del PJ contra sus ataques; no tiene reacciones | −1 a sus ataques; sin reacciones |
| **Cegado** | +2 a la Defensa del PJ contra sus ataques; no usa Larga | −2 a sus ataques; no usa Larga |
| **Atrapado** | +1 a la Defensa del PJ contra sus ataques; se libera automáticamente gastando su acción | −1 a sus ataques; liberarse le cuesta su acción y una tirada |
| **Debilitado** | +1 a la Defensa del PJ contra sus ataques; su daño total se reduce en el VF del causante | −1 a sus ataques; −VF a su daño |
| **Confundido** | Con 3–6 en el d6, +1 a la Defensa del PJ contra sus ataques | Con 3–6, −1 a sus tiradas |
| **Asustado** | +1 a la Defensa del PJ que es la fuente del miedo, contra sus ataques | −1 a sus ataques contra la fuente |
| **Provocado** | Si ataca a alguien que no sea el usuario, ese PJ tiene +2 a su Defensa | Si ataca a otro, −2 a esa tirada |
| **Encantado** | No ataca a la fuente; si no tiene otro objetivo, usa Defender (−2 a los ataques de los PJ contra él hasta su próximo turno) | No ataca a la fuente; si no tiene otro objetivo, usa Defender (+2 a su Defensa) |
| **Dormido** | +2 al ataque del PJ contra él | −2 a su Defensa |
| **Congelado** | +2 al ataque del PJ contra él | −2 a su Defensa |
| **Ralentizado** | +1 al ataque del PJ contra él | −1 a su Defensa |
| **Marcado** | +2 al próximo ataque de un PJ contra él | −2 a su próxima Defensa |
| **Derribado** | +1 a las técnicas de Toque de los PJ contra él | −1 a su Defensa contra Toque |
| **Roto** (si ya tenía 0 Arm) | +1 al ataque del PJ contra él | −1 a su Defensa |
| **Expuesto** | +1 a los ataques de los PJ contra él | −1 a su Defensa |

Quemado, Envenenado, Aturdido, Sellado, la Regresión y el Empujar no tocan ninguna tirada, así que funcionan igual en los dos bandos.

### Otros estados y condiciones

No todos los estados nacen de una técnica. Estos aparecen por el combate, por la digievolución o por la vida diaria en el Mundo Digital:

| Estado | Qué hace | Cuándo termina |
|---|---|---|
| **Expuesto** | −1 Def: −1 a sus tiradas de Defensa si es un PJ; +1 a los ataques de los PJ contra él si es un PNJ (también un Jefe al que le rompen la Guardia de carga). Un Tamer Expuesto puede ser atacado. | Al final de su próximo turno (un Jefe, al final del asalto siguiente) o al Ponerse a cubierto. |
| **Agotado** | −1 a todas sus tiradas; no puede digievolucionar en esta escena (salvo con Segundo aliento). | Con un descanso corto. |
| **Hambriento** | −1 a sus tiradas fuera de combate; digievolucionar le cuesta +1 Chispa. La digievolución no lo elimina. | Al comer. |
| **Derrotado** | Inconsciente en forma Bebé II; no actúa el resto del combate. | Con un descanso largo, o gastando 1 Chispa en una escena tranquila. |
| **Trabado** | −1 a sus técnicas de Distancia y Larga; salir de la zona provoca un ataque de retirada. | Al salir de la zona o al caer el enemigo. |
| **Oculto** | No puede ser objetivo de técnicas de Distancia ni Larga; su primer ataque tiene +2. | Al atacar, o si lo revelan (una Bengala, Analizar con 10+). |
| **Potenciado** | +1 a la tirada de su próximo ataque (Mejora P1). | Tras ese ataque. |
| **Potenciado+** | +1 a la tirada y +1 dado de daño en su próximo ataque (Mejora P2 o P3). | Tras ese ataque. |
| **Descontrolado** | Actúa en la fase enemiga y el DJ elige sus objetivos, que pueden ser aliados. | Con Animar 10+, o al terminar la forma. |
| **Empapado** (avanzado) | Solo importa para los combos elementales: está en una zona de Agua, bajo la lluvia o ha recibido una técnica de Agua este asalto. | Al salir del agua o al final del asalto. |
| **Herido** (solo Tamers) | −1 a las tiradas físicas del Tamer. | Con un descanso largo. |

No confundas Potenciado con el programa Potencia: el programa no aplica ningún estado, sino que da +1 dado a la próxima técnica de ese asalto, y ni Purificar ni Purgado lo eliminan.

### Estados en los Tamers

Los Tamers sufren estados muy de vez en cuando: solo si una técnica de área los incluye o si una jugada dura del DJ se los aplica (capítulo 7). Cuando ocurre, se traducen así:

| Estado | Efecto en un Tamer |
|---|---|
| Quemado, Envenenado o daño de una invocación | Pierde 1 Aguante al inicio de su turno (en lugar de VF PV) mientras dure |
| Congelado, Atrapado o Paralizado | No puede moverse |
| Dormido o Aturdido | Pierde su acción de Tamer y no puede usar el Dado de Vínculo |
| Cegado | −2 a su Defensa y no puede Analizar |
| Asustado, Confundido o Encantado | No puede dar Órdenes |
| Cualquier otro | No le afecta |

### Estados contra Jefes y Legendarios

Un Jefe no se queda fuera de juego por una sola tirada afortunada. Los Legendarios siguen todas las reglas de Jefe, así que esto vale para los dos (el resto de su anatomía está en el capítulo 12):

- Aturdir y Dormir le quitan **una sola acción** del asalto. Si solo le quedaba una, queda Ralentizado.
- Congelado y Atrapado le duran **como mucho 1 asalto**.
- Es inmune a Ejecutar: en su lugar, la técnica gana +1 dado.
- Su daño por turno se aplica una vez por asalto.
- Al cruzar el umbral de una fase entra en **Furia** y se libra de todos sus estados.
- Aturdirlo o Sellarlo con 10+ mientras carga su Firma rompe la carga y lo deja Expuesto.

### Inmunidades

| Quién | Es inmune a |
|---|---|
| Familia **Naturaleza** | Veneno |
| Familia **Máquina** | Dormir y Encantar |
| Familia **Juguete** | Asustar |
| Familia **Caballero** | Asustar y Encantar |
| Familia **Arcano** | Confundir |
| Familia **Elemental** | El estado por defecto de su elemento: Quemar (Fuego), Congelar (Hielo), Derribar (Tierra) o Ralentizar (Cósmico) |
| Plantilla **X-Antibody** | Sellar y Ejecutar |
| **Jefes y Legendarios** | Ejecutar (y el control duro les afecta de forma limitada) |

Algunos grupos legendarios, talentos de Tamer y piezas de equipo dan otras inmunidades. Las verás en su capítulo.

## El triángulo de atributos

Todo Digimon tiene un **atributo**, y tres de ellos forman un triángulo, como un piedra, papel o tijera digital:

**Vacuna vence a Virus · Virus vence a Datos · Datos vence a Vacuna.**

- Si tu atributo vence al de tu rival, tienes **+1 a tus tiradas contra él**: al atacarlo y al defenderte de sus ataques.
- Si el suyo vence al tuyo, tienes **−1**.
- **Libre, Desconocido, SIN DATOS y Ninguno** son neutrales: ni dan ni reciben ventaja.
- **Variable** elige al empezar cada escena si es Vacuna, Datos o Virus.
- El triángulo es un **modificador situacional**, así que cuenta para el límite de +3 y −3 (capítulo 2). Cuando atacas, el DJ ya lo incluye en el modificador neto que te anuncia.

Además del triángulo, cada atributo da un pequeño ajuste a la ficha. Ya viene sumado, salvo en Variable. Los Bebés también lo aplican, aunque no aplican los de rol ni familia.

| Atributo | Vence a | Pierde contra | Ajuste de la ficha | Rasgo | Por ejemplo |
|---|---|---|---|---|---|
| **Vacuna** | Virus | Datos | +1 Def | *Antivirus* | [[Agumon]], [[Angemon]] |
| **Datos** | Vacuna | Virus | +1 Ini y +VF PV | *Procesamiento* | [[Gabumon]], [[Palmon]] |
| **Virus** | Datos | Vacuna | +1 Atq | *Agresión* | [[Guilmon]], [[Devimon]] |
| **Libre** | — | — | +VF PV | *Libre:* fuera del triángulo | [[Veemon]], [[Hawkmon]] |
| **Variable** | Lo que elija | Lo que elija | El del atributo elegido, hasta el final de la escena (no viene en la ficha) | *Mutable* | [[Agunimon]] |
| **Desconocido** | — | — | +1 Def | *Ilegible:* fuera del triángulo; Analizar contra él tiene −1 | [[Keramon]], [[Infermon]] |
| **SIN DATOS** | — | — | +1 Def | *Ilegible* (igual que Desconocido) | [[Fanglongmon]] |
| **Ninguno** | — | — | — | — | Muchos Bebés, como [[Botamon]] |

*«+VF PV» significa que la ficha suma un VF más a sus PV.*

> **Ejemplo:** [[Agumon]] es Vacuna. Contra un [[Goblimon]] (Virus) tiene +1 al atacar y +1 a su Defensa cuando el Goblimon lo ataca. Contra un [[Kokuwamon]] (Datos) le pasa lo contrario: −1 en las dos tiradas. Y contra un [[Veemon]] (Libre), el triángulo no cuenta para nada.

## Las 14 familias

Hay 140 tipos oficiales de Digimon (Dinosaur, Angel, Cyborg…) y el juego los agrupa en **14 familias**. La familia le da a cada Digimon:

- Un **rasgo** propio.
- Una **afinidad elemental**: el elemento por defecto de sus técnicas de Distancia sin un elemento claro, de su Firma genérica *Descarga de datos* si no tiene técnicas oficiales y de la maniobra *Disparo certero* si es Tirador.
- **Debilidades y resistencias** de base.
- Una **especialidad**: +1 a sus tiradas fuera de combate cuando la acción encaja.
- Los **roles más probables**, su **técnica básica** y, a veces, ajustes numéricos.

Todo esto ya está en la ficha del bestiario. Las debilidades y resistencias de la tabla son las de la familia: la ficha final añade las de su elemento principal, como verás en la sección de elementos.

### Rasgo, debilidades y resistencias

| Familia | Qué agrupa | Afinidad | Débil a | Resiste | Rasgo |
|---|---|---|---|---|---|
| **Dragón** | Dragones y hombres dragón: potencia bruta y orgullo ([[Veemon]], [[Monodramon]]) | Fuego | Hielo | Fuego | *Corazón de dragón:* con la mitad de sus PV o menos, +1 a sus tiradas de ataque. |
| **Saurio** | Reptiles y dinosaurios de piel dura ([[Agumon]], [[Guilmon]]) | Neutro | Hielo | Tierra | *Piel gruesa:* +VF PV (incluido). |
| **Bestia** | Mamíferos y bestias míticas con instinto de manada ([[Garurumon]], [[Renamon]]) | Neutro | Fuego | Hielo | *Manada:* +1 al atacar a un objetivo que un aliado ya ha atacado en este asalto. |
| **Ave** | Aves y hombres ave ([[Biyomon]], [[Hawkmon]]) | Viento | Eléctrico | Tierra | *Vuelo:* vuela; ignora el terreno y las técnicas de Toque de quien no vuela tienen −2 contra ella, salvo que esté trabada con el atacante. |
| **Acuático** | Criaturas marinas y anfibias ([[Gomamon]], [[Seadramon]]) | Agua | Eléctrico | Fuego | *Anfibio:* nada; en zonas con agua o bajo la lluvia, +1 Def y se mueve sin penalización. |
| **Naturaleza** | Insectos y plantas ([[Palmon]], [[Tentomon]]) | Planta | Fuego | Agua | *Toxinas y raíces:* inmune a Veneno; +1 a la tirada con técnicas de Veneno o Atrapar. Los insectos (Insectoid y Ancient Insectoid) vuelan. |
| **Máquina** | Cíborgs, máquinas y armas vivientes ([[Guardromon]], [[Andromon]]) | Acero | Eléctrico | Veneno | *Blindaje:* +1 Arm y −1 Ini (incluidos); inmune a Dormir y Encantar. |
| **Juguete** | Marionetas, juguetes y comida con vida ([[Monzaemon]], [[Puppetmon]]) | Mental | Fuego | Mental | *Relleno:* una vez por combate reduce a la mitad el daño de un impacto; inmune a Asustar. |
| **Sagrado** | Ángeles, bestias sagradas y deidades ([[Angemon]], [[Gatomon]]) | Luz | Oscuridad | Luz | *Aura sagrada:* +1 dado de daño con técnicas de Luz contra la familia Oscuro (no contra el Modo Oscuro de otra familia). Los ángeles y las aves sagradas vuelan. |
| **Caballero** | Caballeros y guerreros de honor ([[Knightmon]], [[Gallantmon]]) | Acero | Oscuridad | Acero | *Honor:* inmune a Asustar y Encantar; +1 Def mientras usa Proteger. |
| **Oscuro** | Demonios, no muertos, fantasmas y bestias oscuras ([[Devimon]], [[Impmon]]) | Oscuridad | Luz | Oscuridad | *Hambre oscura:* cuando su ataque saca 10+ (o el defensor saca 6–), recupera VF PV. |
| **Arcano** | Magos, hadas y espíritus ([[Wizardmon]], [[Cutemon]]) | Mental | Acero | Mental | *Hechicería:* sus técnicas de Distancia pueden usarse con alcance Larga; inmune a Confundir. |
| **Elemental** | Cuerpos de fuego, hielo, roca o luz estelar ([[Meramon]], [[Gotsumon]]) | Según el tipo | Según el tipo | Según el tipo | *Cuerpo elemental:* resiste el daño de su propio elemento (incluido) y es inmune al estado por defecto de ese elemento. |
| **Anomalía** | Mutantes, compuestos, invasores y lo inclasificable, incluidas las crías Slime y Lesser ([[Sukamon]], [[Keramon]]) | Neutro | — | — | *Adaptación:* tras recibir daño de un elemento, gana Resistencia a ese elemento hasta el final del combate (solo a uno a la vez). |

**Caballeros oscuros.** Los Digimon del tipo Dark Knight, como [[DarkKnightmon]], son de la familia Caballero, pero cambian su debilidad por **Luz** y su resistencia por **Oscuridad**.

**El Arcano no es el Místico.** La familia Arcano se llamaba «Místico» en versiones anteriores del juego. Cambió de nombre para no confundirla con el **rol** Místico: un Digimon puede ser de una cosa, de la otra, de las dos o de ninguna.

### Técnica básica, especialidad y roles

| Familia | Técnica básica (elemento) | Especialidad fuera de combate | Roles más probables | Ajustes |
|---|---|---|---|---|
| **Dragón** | Garra de dragón (Neutro) | Fuerza, intimidar, volar si tiene alas | Bruto / Versátil | — |
| **Saurio** | Mordisco (Neutro) | Aguante, fuerza, morder | Bruto / Tanque | +VF PV |
| **Bestia** | Zarpazo (Neutro) | Rastrear, olfato, correr | Ágil / Acechador | — |
| **Ave** | Picotazo (Neutro) | Volar, otear, orientarse | Ágil / Tirador | — |
| **Acuático** | Coletazo (Agua) | Nadar, bucear, corrientes | Tanque / Tirador | — |
| **Naturaleza** | Picadura (Neutro) | Sigilo en la naturaleza, plantas, camuflaje | Místico / Acechador | — |
| **Máquina** | Puño mecánico (Acero) | Fuerza, cálculo, sensores, interfaz | Tanque / Tirador | +1 Arm, −1 Ini |
| **Juguete** | Golpe de juguete (Neutro) | Distraer, actuar, engañar | Místico / Apoyo | — |
| **Sagrado** | Golpe sagrado (Luz) | Detectar el mal, consolar, saber antiguo | Místico / Apoyo | — |
| **Caballero** | Tajo (Acero) | Proteger, etiqueta, juramentos | Versátil / Tanque | — |
| **Oscuro** | Zarpa sombría (Oscuridad) | Intimidar, ver en la oscuridad, ocultarse | Acechador / Místico | — |
| **Arcano** | Proyectil arcano (Mental), a Distancia | Magia, saber arcano, ilusiones | Místico / Apoyo | — |
| **Elemental** | Golpe elemental (su elemento) | Su elemento | Bruto / Místico | — |
| **Anomalía** | Embestida (Neutro) | Adaptarse, infiltrarse en sistemas, imitar | Versátil / Bruto | — |

### La familia Elemental, tipo a tipo

Los Elementales son la única familia cuyo elemento depende del tipo:

| Tipos | Elemento | Débil a | Resiste | Inmune a | Por ejemplo |
|---|---|---|---|---|---|
| Fire | Fuego | Agua | Fuego | Quemar | [[Meramon]], [[Candlemon]] |
| Ice-Snow | Hielo | Fuego | Hielo | Congelar | [[Frigimon]] |
| Mineral, Ore, Ancient Mineral | Tierra | Planta | Tierra | Derribar | [[Gotsumon]], [[Golemon]] |
| Galaxy, Minor, Major, Super Major | Cósmico | Oscuridad | Cósmico | Ralentizar | [[Starmons]] |

Un Elemental resiste su elemento, pero no es inmune a él: un grupo cuyas técnicas son todas de Fuego sigue teniendo opciones contra un [[Meramon]].

### Qué tipos entran en cada familia

Cada uno de los 140 tipos pertenece a una sola familia. Están escritos tal como aparecen en el bestiario:

- **Dragón (21):** Dragon Man, Dark Dragon, Mini Dragon, Dragon, Holy Dragon, Beast Dragon, Evil Dragon, Bird Dragon, Rock Dragon, Armored Dragon, Shining Dragon, Baby Dragon, Mythical Dragon, Machine Dragon, Sky Dragon, Ancient Dragon, Ancient Dragon Man, Ocean Dragon, Earth Dragon, Fire Dragon, Dragon Warrior.
- **Saurio (7):** Dinosaur, Reptile, Reptile Man, Ceratopsian, Pterosaur, Plesiosaur, Stegosaur.
- **Bestia (8):** Beast, Beast Man, Mammal, Ancient Beast, Mythical Beast, Mysterious Beast, Rare Animal, Ancient Mythical Beast.
- **Ave (8):** Bird, Giant Bird, Baby Bird, Bird Man, Ancient Bird, Mysterious Bird, Mini Bird, Ancient Bird Man.
- **Acuático (12):** Aquatic, Aquatic Beast Man, Ancient Aquatic Beast Man, Sea Beast, Sea Animal, Mollusk, Crustacean, Ancient Crustacean, Amphibian, Ancient Fish, Tropical Fish, Marine Man.
- **Naturaleza (9):** Insectoid, Ancient Insectoid, Larva, Parasite, Vegetation, Carnivorous Vegetation, Ancient Vegetation, Seed, Bulb.
- **Máquina (9):** Cyborg, Machine, Weapon, Mine, Enhancement, Armor, CRT, LCD, 9000.
- **Juguete (3):** Puppet, Food, Musical Instrument.
- **Sagrado (16):** Angel, Mini Angel, High Angel, Super Angel, Great Angel, Seraph, Cherub, Dominion, Principality, Virtue, Holy Beast, Holy Bird, Deity, God Beast, Tathāgata, Monk.
- **Caballero (8):** Holy Knight, Dark Knight, Beast Knight, Magic Knight, Ancient Holy Knight, Holy Sword, Warrior, Magic Warrior.
- **Oscuro (10):** Demon, Dark Angel, Evil King, Little Devil, Demon God, Wicked God, Avatar, Undead, Ghost, Dark Beast.
- **Arcano (6):** Wizard, Pixie, Ancient Pixie, Ancient, Spirit, Smoke.
- **Elemental (9):** Fire, Ice-Snow, Mineral, Ore, Ancient Mineral, Galaxy, Minor, Major, Super Major.
- **Anomalía (14):** Mutant, Unidentified, Composite, Alien, Alien Humanoid, Invader, Unanalyzable, Abnormal, Unique, NO DATA, Ancient Mutant, Slime, Lesser, Perfect.

### Vuelo y nado

Quien **vuela** ignora el Terreno difícil, y las técnicas de Toque de quien no vuela tienen −2 contra él, salvo que estén trabados. Si queda Derribado, cae a tierra. Vuelan la familia Ave; los tipos Insectoid, Ancient Insectoid, Sky Dragon, Holy Dragon, Bird Dragon, Pterosaur, todos los ángeles (Angel, Mini Angel, High Angel, Super Angel, Great Angel, Cherub, Seraph, Virtue, Dominion, Principality y Dark Angel), Pixie, Ancient Pixie, Ghost, Holy Bird, Smoke y Spirit; y una lista de Digimon concretos, como [[Patamon]], [[Biyomon]] o [[Kabuterimon]]. La ficha lo indica con la palabra «Vuela».

**Nadan** la familia Acuático y los tipos Amphibian, Plesiosaur, Ocean Dragon, Sea Beast y Sea Animal; la ficha lo indica con «Nada». El DJ puede conceder vuelo o nado a cualquier forma con alas o aletas evidentes.

## Los 14 elementos

Cada técnica tiene **un solo elemento**, elegido de una lista cerrada de 14. El elemento decide tres cosas: si el objetivo es **débil** (+1 dado de daño), si lo **resiste** (mitad de daño) y qué **estado por defecto** lleva la técnica cuando no tiene ninguno propio.

| Elemento | Qué representa | Estado por defecto | Vence a | Raíces en el nombre (inglés) |
|---|---|---|---|---|
| **Neutro** | Golpes, garras, embestidas y energía sin naturaleza definida. | — | — | — |
| **Veneno** | Ácidos, toxinas, gases, basura y, sí, caca. | Veneno | Planta | poison, venom, toxic, acid, sludge |
| **Hielo** | Escarcha, nieve, ventisca y frío absoluto. | Congelar | Planta, Viento | ice, frozen, frost, snow, blizzard |
| **Eléctrico** | Rayos, plasma, magnetismo y descargas. | Paralizar | Agua, Viento | thunder, lightning, electr, spark, volt |
| **Fuego** | Llamas, calor, magma y explosiones solares. | Quemar | Planta, Hielo, Acero | fire, flame, flare, blaze |
| **Agua** | Burbujas, olas, presión y corrientes. | Ralentizar | Fuego, Tierra | water, aqua, bubble, wave, ocean |
| **Planta** | Enredaderas, pétalos, semillas y esporas. | Atrapar | Agua, Tierra | leaf, flower, ivy, seed, thorn |
| **Luz** | Lo sagrado, los láseres, las estrellas y los fotones. | Cegar | Oscuridad | holy, heaven, light, shining, divine |
| **Oscuridad** | Sombras, maldiciones, muerte y el lado oscuro de los datos. | Asustar | Luz, Mental | dark, death, hell, evil, shadow |
| **Cósmico** | Meteoros, gravedad, tiempo y espacio profundo. | Ralentizar | Tierra, Acero | meteor, galaxy, cosmic, space, black hole |
| **Mental** | Mente, sonido, música, ilusiones, magia y emociones. | Confundir | Veneno, Cósmico | love, charm, dream, lullaby, song |
| **Viento** | Tornados, alas, vendavales y presión del aire. | Empujar | Planta, Veneno | wind, tornado, storm, gale, hurricane |
| **Tierra** | Rocas, terremotos, arena y cristal. | Derribar | Eléctrico, Veneno, Fuego | rock, stone, earth, quake, sand |
| **Acero** | Espadas, misiles, cañones y metal. | — | Hielo, Mental | metal, iron, steel, blade, sword |

**Cómo se elige el elemento.** El bestiario lee el nombre oficial de la técnica: si contiene una de las raíces de un elemento, es de ese elemento. Si el nombre no basta, mira la descripción oficial del Digimon y, en último caso, usa la afinidad de su familia (o Neutro, si la técnica es de Toque). Así, Pepper Breath es de Fuego porque *pepper* figura entre las raíces del Fuego, y Marching Fishes es de Agua por *fishes*. La lista completa de raíces forma parte de la especificación del bestiario, que se explica en el capítulo 14.

**El estado por defecto.** Cuando una técnica no tiene ningún estado propio y le queda hueco, el bestiario le añade el estado por defecto de su elemento. Por eso tantas técnicas de Fuego queman y tantas de Hielo congelan. Neutro y Acero no tienen estado por defecto: sus técnicas confían en el daño puro.

### Qué significa «vence a»

La columna «Vence a» **no** es un piedra, papel o tijera que se aplique al vuelo. Solo sirve para construir las debilidades de cada ficha. El +1 dado lo da la línea **Debilidad** de la ficha del objetivo, nunca el elemento del atacante por sí solo. Que el Fuego «venza» al Hielo no significa que una técnica de Fuego haga más daño a cualquier Digimon helado: lo hace si su ficha dice «Debilidad: Fuego».

### Las debilidades y resistencias de cada ficha

Cada ficha combina las de su familia con las de su **elemento principal**: el elemento que más se repite entre sus técnicas oficiales, sin contar Neutro (si hay empate, gana el de la técnica que va antes, empezando por la Firma; un Elemental usa el de su tipo). La cuenta es así:

1. Empieza con la debilidad y la resistencia de su familia.
2. **Añade una debilidad:** el primer elemento que venza a su elemento principal y que no esté ya entre las debilidades o resistencias de la familia, mirando en este orden: Agua, Fuego, Planta, Eléctrico, Veneno, Viento, Tierra, Hielo, Acero, Mental, Luz, Oscuridad, Cósmico.
3. **Añade una resistencia:** su propio elemento principal, salvo que sea Neutro o Cósmico.
4. Si un elemento aparece en las dos listas, **se anula** y desaparece de ambas.
5. Como mucho quedan **2 debilidades y 2 resistencias**, empezando por las de la familia.

Los Bebés no tienen debilidades, y la plantilla Armadura añade a las resistencias el elemento de su Firma.

**Dos ejemplos.** [[Agumon]] es Saurio (débil a Hielo, resiste Tierra) y su elemento principal es Fuego. El primer elemento de la lista que vence al Fuego es el Agua, así que gana la debilidad Agua y resiste el Fuego: su ficha dice *Debilidad: Hielo, Agua · Resistencia: Tierra, Fuego*. [[Garurumon]] es Bestia (débil a Fuego, resiste Hielo) y su elemento principal también es Fuego. Gana la debilidad Agua y la resistencia Fuego, pero el Fuego estaba ya entre sus debilidades, así que se anula: su ficha dice solo *Debilidad: Agua · Resistencia: Hielo*. En cambio, [[Gazimon]], otra Bestia, usa técnicas Eléctricas: conserva la debilidad al Fuego de su familia y suma Tierra. Dos Digimon de la misma familia pueden tener puntos flacos muy distintos.

### Otras interacciones elementales

Además de las debilidades y resistencias, algunos elementos interactúan entre sí en las reglas básicas:

- Una técnica de **Agua o Hielo** que alcanza a un objetivo Quemado apaga el fuego.
- El daño de **Fuego** descongela a un objetivo Congelado.
- La familia **Sagrado** suma +1 dado con técnicas de **Luz** contra la familia Oscuro (*Aura sagrada*).
- **Purificar** en una técnica de daño da +1 dado contra la familia Oscuro.
- Un Digimon en **Modo Oscuro** tiene −1 Def contra técnicas de Luz.
- Un **Acuático** gana +1 Def en zonas con agua o bajo la lluvia.
- Una **Anomalía** se adapta: tras recibir daño de un elemento, lo resiste hasta el final del combate (solo uno a la vez).

**Clima y terreno.** El clima del Mundo Digital (capítulo 3) también pesa: una **tormenta eléctrica** da +1 dado a las técnicas Eléctricas y −1 Def a los que vuelan; el **calor de servidor** da +1 dado al Fuego y −1 dado al Hielo; con **lluvia de datos**, las zonas abiertas cuentan como Agua para los combos. Una zona con el rasgo **Agua** (capítulo 7) activa el rasgo de los Acuáticos, y quien esté en ella cuenta como Empapado para los combos.

> **Consejo para el DJ:** las debilidades son información valiosa; no la regales, pero tampoco la escondas. Analizar con 7–9 revela una debilidad del objetivo, y con 10+, la ficha entera. Si un Tamer investiga antes del combate o pregunta a un Digimon del lugar, recompénsalo con ese dato: ver cómo el grupo cambia de técnica para aprovecharlo es parte de la diversión.

### Combos elementales (regla opcional)

Si tu mesa usa los combos elementales (capítulo 13), cuando una técnica impacta a un objetivo que ya sufre cierto estado se desencadena un efecto extra. No gasta palabras clave, y cada técnica provoca **como mucho un combo**.

| Estado previo | Técnica que impacta | Combo | Efecto |
|---|---|---|---|
| Empapado | Eléctrico | **Electrocución** | +1 dado y Paralizar (aunque saque 7–9) |
| Empapado | Hielo | **Ultracongelación** | Congelar (aunque saque 7–9) |
| Empapado | Tierra | **Lodazal** | Ralentizar |
| Congelado | Toque Neutro, Tierra o Acero | **Quebrar** | +1 dado; termina Congelado |
| Quemado | Viento | **Incendio** | Quemar a todos los enemigos de la zona del objetivo |
| Envenenado | Planta | **Floración tóxica** | Atrapar |
| Atrapado | Fuego | **Pira** | +1 dado; termina Atrapado |
| Cegado | Oscuridad | **Eclipse** | Asustar |
| Asustado, Confundido o Sellado | Luz | **Purga** | +1 dado; termina ese estado |
| Ralentizado | Cósmico | **Colapso** | Derribar |

Los combos que aplican control duro o que funcionan «aunque saque 7–9» no sirven contra Jefes: un Jefe solo sufre su efecto de daño.

## Tres técnicas leídas paso a paso

Ya tienes todas las piezas. Vamos a juntarlas con tres técnicas oficiales tal como aparecen en el bestiario: un ataque a distancia contra un solo enemigo, un ataque de área y una técnica de apoyo.

### Ejemplo 1: Electro Shocker, de Kabuterimon

```
Electro Shocker — P2/P3 (Agotadora) · Larga · Individual · Eléctrico · Paralizar, Certero  [2d8 / 3d8]
```

**La lectura.** [[Kabuterimon]] es un Campeón (dado d8, VF 4), Tirador y Vacuna. Como solo tiene una técnica oficial, Electro Shocker es su **Firma versátil**: como P2 tira 2d8 y puede usarla siempre que quiera; como P3 tira 3d8, pero es Agotadora. Alcance **Larga**: llega hasta 2 zonas de distancia (la técnica es de Distancia, pero el rasgo del Tirador lleva su Firma a Larga, y la ficha ya lo trae así). Área **Individual**: un solo objetivo. Elemento **Eléctrico**: sumará un dado contra cualquiera que tenga «Debilidad: Eléctrico», algo muy común en Acuáticos, Aves y Máquinas. Y dos palabras clave: **Paralizar** (un estado, solo con 10+) y **Certero** (un efecto de daño: +1 a la tirada, que además ignora Cobertura y Oculto).

**En juego.** Un [[Seadramon]] salvaje asoma en un lago, a dos zonas de Kabuterimon. El DJ calcula el modificador neto: Atq 3 de Kabuterimon contra Def 3 de Seadramon, que sube a 4 porque está en el agua (rasgo *Anfibio*). Eso da −1, y otro −1 por el triángulo, porque Seadramon es Datos y Datos vence a Vacuna: el DJ anuncia **−2**. El jugador suma sus situacionales: +1 por Certero y +1 por *Francotirador*, el rasgo del Tirador contra objetivos que no están en su zona. Total: **+0**.

Como Seadramon parece peligroso, el jugador elige usarla como **P3**. Tira 2d6 y saca 6 y 4: **10, impacto total**. Daño: 3 dados por la potencia, +1 porque Seadramon es débil a Eléctrico, así que tira **4d8** y saca 7, 3, 5 y 6, que suman 21. Le resta la Arm 1 de Seadramon: **20 de daño**. Seadramon no resiste lo Eléctrico y los dos son del mismo rango, así que no hay que dividir nada: de sus 36 PV le quedan 16. Con el 10+, Seadramon queda además **Paralizado** durante 2 turnos: solo puede moverse o actuar, pierde sus reacciones y, por la regla de espejo, la Defensa de los PJ tiene +1 contra sus ataques.

En su siguiente turno, Kabuterimon no puede usar técnicas Agotadoras. Pero puede volver a lanzar Electro Shocker **como P2** (2d8, más el dado por la debilidad), porque usada así no es Agotadora. Si la tirada hubiera sacado 7–9, el daño habría sido el mismo, pero sin Paralizar, salvo que el jugador cambiara todo el daño por el estado. Y si la mesa usa los combos, Seadramon está Empapado por estar en el agua: Electro Shocker desencadenaría una **Electrocución** (+1 dado y Paralizar aunque saque 7–9).

### Ejemplo 2: Marching Fishes, de Gomamon

```
Marching Fishes — P2/P3 (Agotadora) · Distancia · Zona · Agua · Invocar  [2d6 / 3d6; contra 2+: 1d6 / 2d6]
```

**La lectura.** [[Gomamon]] es un Novato (dado d6, VF 3), Tanque y Vacuna. Marching Fishes es su Firma versátil, de alcance **Distancia** (su zona o una adyacente) y área **Zona**: alcanza a todos los enemigos de una zona con una sola tirada. Por eso la ficha imprime dos valores: 2d6 o 3d6 contra un solo objetivo, y 1d6 o 2d6 cuando alcanza a 2 o más. Elemento **Agua**. Su única palabra clave es **Invocar**, una táctica que funciona **al impactar**, con 7+: llama a un banco de peces que se queda en la zona.

**En juego.** Un [[Goblimon]] y un [[Kokuwamon]] salvajes (sin plantilla de esbirro, para que las cuentas se vean claras) bloquean un puente en la zona de al lado. Gomamon lanza Marching Fishes como **P2**, para tener la versión P3 lista el turno siguiente. Hay una sola tirada, pero cada objetivo tiene su propio modificador:

- **Contra Goblimon:** Atq 1 − Def 1 = 0, y +1 por el triángulo (Vacuna vence a Virus): **+1**.
- **Contra Kokuwamon:** Atq 1 − Def 2 = −1, y −1 por el triángulo (Datos vence a Vacuna): **−2**.

El jugador tira 2d6 y saca 9. Contra Goblimon es un **10** (impacto total) y contra Kokuwamon, un **7** (impacto). Como alcanza a dos objetivos, la técnica pierde un dado: de 2 pasa a 1. Goblimon es débil al Agua y recupera ese dado; Kokuwamon no. Como cada objetivo recibe un número de dados distinto, el jugador tira el daño de cada uno por separado:

| Objetivo | Dados | Tirada | Arm | Daño | PV que le quedan |
|---|---|---|---|---|---|
| Goblimon | 2d6 (1 + debilidad) | 5 + 3 = 8 | 0 | 8 | 24 → 16 |
| Kokuwamon | 1d6 | 4 | 2 | 2 | 27 → 25 |

La técnica ha impactado, así que **Invocar** se activa: un banco de peces aparece en la zona del puente durante 2 asaltos. Al inicio de cada turno de Gomamon, los peces hacen VF de daño (3, menos la Arm) a un enemigo de esa zona. Lo lógico es elegir a Goblimon, que recibe los 3 enteros, en lugar de Kokuwamon, que solo perdería 1 por su blindaje. Si un enemigo lanza una técnica de área sobre esa zona, los peces se dispersan; y si Gomamon vuelve a usar Marching Fishes, el banco nuevo sustituye al viejo.

### Ejemplo 3: Healing Glow, de Cutemon

```
Healing Glow — P2 (Agotadora) · Distancia · Individual · Mental · Curar  [apoyo]
```

**La lectura.** [[Cutemon]] es un Novato (dado d6, VF 3) de la familia Arcano y rol Apoyo. Healing Glow es una **técnica de apoyo**: no hace daño, no pide tirada y no lleva estados. Su potencia P2 indica cuánto cura: **Curar** devuelve tantos dados de poder como la potencia, así que 2d6. Como lleva Curar, es **Agotadora** aunque solo sea P2. Su alcance es Distancia, pero la familia Arcano puede usar sus técnicas de Distancia con alcance **Larga** (*Hechicería*), así que llega a un aliado a dos zonas.

**En juego.** Tras un choque duro, [[Agumon]] está a 9 de sus 27 PV y [[Gabumon]], a 24 de 30. Cutemon usa Healing Glow. Gracias a su rasgo de rol, *Sanador*, la técnica alcanza a un aliado más dentro del alcance, y el **objetivo principal**, solo él, suma +VF a la curación. El jugador elige a Agumon como objetivo principal: tira 2d6, saca 7 y suma 3, así que recupera **10 PV** y sube a 19. Para Gabumon tira otros 2d6 y saca 8, pero la curación nunca supera los PV máximos: se queda en **30**, sin pasarse.

En su siguiente turno, Cutemon no puede usar nada Agotador: ni su Firma, Supersonic Wave (P3), ni Immediate Healing (otra técnica de apoyo con Curar), ni su maniobra de rol, *Pulso restaurador*. Sí puede atacar con Ultrasonic Wave (P1) o con su técnica básica, *Proyectil arcano*. Un detalle importante: si Agumon hubiera estado **Envenenado**, Healing Glow no le habría curado nada. Primero hay que quitarle el veneno.

> **Si es tu primera vez:** fíjate en que los tres ejemplos siguen el mismo orden: potencia (cuántos dados), alcance (si llegas), área (a cuántos), elemento (si hay debilidad o resistencia) y palabras clave (qué pasa con 7+ o con 10+). Si lees tus técnicas siempre así, en dos o tres combates lo harás sin pensar.

## Lo esencial

- Una técnica se lee siempre igual: **Nombre — Potencia · Alcance · Área · Elemento · Palabras clave [dados]**.
- **P1, P2 y P3** son 1, 2 y 3 dados de poder del nivel del usuario. La **Firma** es la técnica emblemática y hay como mucho una P3 por ficha.
- **Agotadora:** tras usarla, el Digimon no puede usar ninguna técnica Agotadora en su siguiente turno. Lo son las P3, las versátiles usadas como P3, los apoyos con Curar o Escudo y *Pulso restaurador*.
- Las técnicas de **área** hacen una sola tirada y pierden un dado solo si alcanzan de verdad a 2 o más objetivos.
- Cada técnica lleva **como mucho 2 palabras clave** de entre 35: Daño, Estado, Apoyo y Táctica.
- Los **estados** entran con 10+ en tu ataque o con 6– en tu Defensa (también con 7–9 si el atacante es del rol Místico, salvo el control duro). No se acumulan y **digievolucionar los borra** todos, salvo Hambriento.
- **Control duro** (Aturdir, Dormir, Regresión): nunca con 7–9, nunca en un área Total y limitado contra los Jefes.
- **Regla de espejo:** lo que afecta a las tiradas de un PNJ se aplica con el signo cambiado a la tirada del PJ.
- **Triángulo:** Vacuna vence a Virus, Virus vence a Datos y Datos vence a Vacuna, con +1 o −1 en ataque y en Defensa. Libre, Desconocido, SIN DATOS y Ninguno son neutrales; Variable elige en cada escena.
- **Familia:** da rasgo, afinidad, debilidad, resistencia, especialidad y técnica básica.
- **Elemento:** el +1 dado sale de la **Debilidad** de la ficha del objetivo; la **Resistencia** divide el daño a la mitad. Perforante ignora la resistencia y la Arm.
