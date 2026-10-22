# Efectos de Firma: reglas y guía de redacción

Este documento tiene dos partes:
- **Parte A:** las reglas, que se copian a la biblia (11.6) y al capítulo 8.
- **Parte B:** la guía para redactar los 1.316 efectos.

---

## Parte A. Reglas (biblia 11.6)

La Firma es la técnica que hace único a cada Digimon. Además de sus dados y sus palabras clave, cada Firma del bestiario tiene un **efecto de Firma** propio, con un nombre y tres partes.

**Sello.** Es el rasgo especial de la técnica. Funciona siempre que el Digimon usa su Firma como Firma, ya sea P3 o P2/P3 usada como P3. En los Bebés, que no tienen P3, funciona cada vez que la usan. Lo que diga el Sello se suma a las palabras clave de la técnica.

**Desatado.** Es el momento en que Tamer y compañero dan todo. Cuando el compañero declara su Firma como P3, el Tamer puede gastar **1 Chispa** para desatarla, como mucho **una vez por combate**. Un PNJ Élite, Jefe o Legendario desata su Firma gratis una vez por combate: el Jefe, en la primera Firma que lance tras entrar en Furia, y los demás, cuando el DJ quiera. Los Bebés no tienen Desatado.

**Eco.** Es lo que la técnica puede hacer fuera de combate. Se usa **una vez por escena**: concede un permiso narrativo (hacer algo que sin ella no se podría) y, si hay tirada, da **Ventaja** a una tirada en la que la técnica encaje. El Eco nunca resuelve por sí solo un obstáculo central de la aventura: abre una vía, no la recorre.

**Límites:**
- **Firma heredada** como P2 (12.4): conserva solo el Eco.
- **Tarjeta Digimon** (13.2): no copia ni el Sello ni el Desatado.
- **Esbirros:** no usan ni el Sello ni el Desatado.
- **Estados:** un efecto de Firma que aplica un estado sigue las reglas generales (7.1). Los de control duro (Aturdir, Dormir, Regresión) nunca se aplican con 7–9, y los Jefes los sufren de forma limitada.
- **Dados:** el Sello y el Desatado no suman entre los dos más de **+1 dado** de daño en una misma tirada.
- **Valores:** se calculan con el VF del usuario, igual que las palabras clave.

---

## Parte B. Guía para los redactores

### Formato de salida
Un JSON `{ id: { "nombre", "sello", "desatado", "eco" } }`. En Bebé I y Bebé II, `"desatado": null`.

### Extensión
| Campo | Qué es | Extensión |
|---|---|---|
| `nombre` | Nombre evocador del efecto, en español, propio; no traduce la técnica. Por ejemplo, para Pepper Breath: «Chispa de valor». | 2–4 palabras |
| `sello` | Regla de juego | Hasta 40 palabras |
| `desatado` | Regla de juego. Empieza siempre igual: «La técnica…», «Su objetivo…», etc. No repitas «gasta 1 Chispa». | Hasta 40 palabras |
| `eco` | Uso fuera de combate | Hasta 35 palabras |

### Presupuesto del Sello
Ventaja pequeña, condicionada y temática. Elige **uno** de estos patrones, o una combinación pequeña:
1. **Añadido con 10+** del atacante (o 6– del defensor si la usa un PNJ). Puede ser:
   - un estado extra de la lista;
   - Empujar o atraer 1 zona;
   - Marcar;
   - el usuario gana Escudo VF;
   - un aliado queda Potenciado;
   - el objetivo pierde su Escudo o su Potenciado;
   - el usuario se mueve 1 zona gratis;
   - crear o quitar un terreno de la zona (Cobertura, Terreno difícil, Peligro, Altura).
2. **+1 dado bajo una condición estrecha y temática.** Por ejemplo:
   - contra un objetivo Quemado, que vuela o Derribado;
   - contra los de un atributo o familia concretos;
   - si el usuario recibió daño este asalto;
   - si el objetivo está trabado con un aliado;
   - en terreno de agua;
   - si el Tamer está en la misma zona.
   Nunca dés +1 dado sin condición.
3. **Táctico al usarla:**
   - ignorar Cobertura u Oculto;
   - excluir aliados de un área;
   - moverse 1 zona antes o después;
   - no quedar trabado;
   - alcance +1 zona si la técnica es de Distancia;
   - la técnica no cuenta como Agotadora si falla.
4. **Efecto persistente leve:** hasta el final del siguiente asalto, en la zona del objetivo. Por ejemplo:
   - la zona queda en Llamas (Peligro: VF al entrar o empezar el turno);
   - neblina (Oculto para quien entre);
   - charcos (Empapado).

**Prohibido en el Sello:**
- acciones o turnos extra;
- curar más de VF;
- inmunidades permanentes;
- matar al instante;
- control duro con 7–9;
- efectos que duren toda la escena (salvo Romper, que ya lo hace);
- efectos que cambien las reglas de la Chispa.

### Presupuesto del Desatado
El gran momento, más o menos **+1 dado** o un efecto equivalente. Elige **uno**:
- +1 dado y un añadido temático pequeño;
- el estado de la técnica entra también con 7–9 (salvo control duro, que sigue siendo solo con 10+);
- ampliar el área:
  - Individual → Ráfaga;
  - Ráfaga → Zona;
  - Zona → Total, solo en Perfecto o Definitivo;
  - sin el −1 dado por área en esa tirada;
- Perforante y además Certero;
- Escudo 2 × VF a todos los aliados de la zona;
- curar 1 dado a todos los aliados de la zona;
- Purificar los estados de los aliados de la zona;
- Drenar todo el daño en lugar de la mitad;
- el objetivo queda Expuesto y Marcado;
- la técnica impacta aunque el atacante saque 6–, con la mitad del daño y sin efectos.

En **Definitivo** puede ser algo más espectacular, siempre que no se convierta en «cae a 0». Por ejemplo:
- el área pasa a Total y la técnica deja una zona de Peligro;
- +1 dado y Romper garantizado al impactar.

**Prohibido en el Desatado:**
- matar al instante;
- más de +1 dado;
- turnos extra para el usuario;
- quitar la Agotadora de forma permanente.

### Eco (fuera de combate)
Concreto, físico y útil en exploración o en relaciones. Por ejemplo:
- Pepper Breath: encender una hoguera o fundir una cerradura de hielo; Ventaja para intimidar a una criatura pequeña.
- Una técnica de agua: apagar un incendio o crear un puente de hielo, si es de hielo.
- Una técnica sagrada: señalar si algo está corrompido por datos oscuros.
- Una técnica de veneno o burbujas: disolver una cerradura o un obstáculo blando.
- Una técnica musical: calmar a una multitud.

Evita repetir «Ventaja en X» como única idea: el Eco debe dar un **permiso** que se pueda narrar.

### Unicidad
- Inspírate en lo que hace la técnica según la franquicia (forma, origen, mitología del Digimon) y en la descripción de su ficha. Escribe con palabras propias y sin copiar perfiles oficiales.
- Si varios Digimon comparten técnica (Acid Bubbles, Mega Flame, Giga Destroyer, las versiones X-Antibody o Anime Version…), dale a cada uno un efecto **distinto**, que refleje sus diferencias:
  - el X-Antibody, más salvaje o con un giro de «anticuerpo»;
  - el Blue, más frío o técnico;
  - el Virus, más cruel;
  - la versión de un Tamer concreto, ligada a su historia.
- **Coherencia con el rol:**
  - Bruto: golpes que derriban o rompen.
  - Tirador: precisión y alcance.
  - Místico: estados.
  - Tanque: proteger y provocar.
  - Ágil: movimiento.
  - Acechador: Oculto, Marcar y Ejecutar.
  - Apoyo: curar, Escudo y Potenciado.
  - Versátil: cambiar de modo.
- **Coherencia con la ficha:** no repitas lo que ya hacen sus palabras clave; complétalas. Si la Firma ya lleva Quemar, el Sello no debe ser «Quemar con 10+». Mejor: «contra un objetivo ya Quemado, +1 dado» o «la zona queda en Llamas».

### Estilo
- Español de España, segunda persona solo si hace falta. Frases cortas y reglas exactas.
- Usa los términos del juego con su mayúscula: Quemado, Marcado, Escudo, Ventaja, VF, zona, Toque, Distancia, Larga, Ráfaga, Zona, Total, Tamer, Chispa, PNJ y PJ.
- Nada de «puede que» ni de reglas ambiguas. Di siempre:
  - **quién** (el usuario, el objetivo, un aliado, todos los enemigos de la zona);
  - **cuándo** (al usarla, al impactar, con 10+);
  - **cuánto dura** (hasta el final del siguiente asalto, 1 turno…).
- Los nombres de las técnicas y de los Digimon van en su forma oficial. El resto, en español.

### Ejemplos
**Agumon · Pepper Breath** (Novato, Bruto, Fuego, Quemar y Brutal):
```json
{"nombre":"Chispa de valor","sello":"Si el objetivo es de un nivel superior al de Agumon, la técnica gana +1 a la tirada: cuanto más grande el rival, más fuerte sopla.","desatado":"La técnica alcanza a todos los enemigos de una zona sin perder dados, y esa zona queda en Llamas hasta el final del siguiente asalto (Peligro: VF de daño al entrar o al empezar el turno en ella).","eco":"Enciende hogueras, funde hielo o cera y ahuyenta a criaturas pequeñas: Ventaja para intimidarlas. Si tiene hambre, la llama sale débil y solo da para cocinar."}
```

**Gabumon · Blue Blaster** (Novato, Fuego azul):
```json
{"nombre":"Llama fría","sello":"Con 10+, además de su efecto, el objetivo queda Ralentizado 1 turno: el fuego azul quema y entumece a la vez.","desatado":"La técnica es Perforante y Certero: el chorro azul atraviesa cualquier escudo o coraza.","eco":"Su fuego azul ilumina sin quemar ni delatar: alumbra una zona oscura sin revelar al grupo, o calienta a alguien congelado. Ventaja para orientarse en cuevas."}
```

**WarGreymon · Gaia Force** (Definitivo, Total o Zona):
```json
{"nombre":"Esfera del mundo","sello":"Si WarGreymon no se movió este turno antes de lanzarla, la técnica gana Romper: reúne la energía del entorno antes de soltarla.","desatado":"La técnica pasa a Total, no pierde dados por área, y todos los aliados de las zonas alcanzadas ganan Escudo VF por la onda de calor.","eco":"Abre un túnel a través de roca, metal o datos corruptos en un solo golpe. Una vez abierto el camino, todos en la escena saben que el compañero está aquí."}
```
