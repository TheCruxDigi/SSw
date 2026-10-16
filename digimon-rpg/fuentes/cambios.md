# Biblia de reglas 1.0 → 1.1: cambios aplicados

Fuentes: `design/issues.json` (61 problemas; aquí se citan por su posición, de #0 a #60), la comparación entre `backup_r2/spec_fichas.json` (1.0) y `design/spec_fichas.json` (1.1) y nuevas simulaciones con `work_final/r3_sim.py` sobre las fichas reales (guiones en `work_final/cal_biblia/`).

Resultado: se han aplicado los 2 problemas críticos y los 10 altos, y todos los medios y bajos que afectan al texto de reglas, algunos de forma parcial (ver el final). La biblia ya no contradice la especificación 1.1. Copia de la versión anterior: `backup_r3/biblia_reglas.md`.

## Cambios en `spec_fichas.json` (parte 2 de la ronda 3)

La especificación 1.1 había quedado a medias: `r3_spec.py` termina con «parte 1 OK» y dice «se completa en la parte 2», pero `formulas`, `validacion`, `amenaza.jefe` y `ejemplos` seguían como en la 1.0. Eso dejaba **contradicciones internas graves**, así que se han corregido con `work_final/r3_spec_parte2.py`. El guion parte de `backup_r3/spec_fichas_1.1_parte1.json`, que es una copia de la especificación tal como estaba. Después `gen.py` se volvió a ejecutar y dio **«errores de validación: 0»**. `gen.py` no se ha tocado.

- `formulas.triangulo`: las dos cláusulas tenían el signo contrario (#8). Ahora dice: «+1 si el atributo del PJ vence; −1 si el del PNJ vence».
- `formulas.dados_tecnica` y `dano_tecnica_impreso` aún restaban 1 dado a toda técnica de área y contradecían `formula_dano` y `areas`. Ahora restan 1 dado solo con 2 o más objetivos, y la ficha imprime `dados` y `dados_area` (#21).
- `formulas.rango` pasa a usar `por_id`, y `formulas.escala` compara rangos (#55).
- `formulas.debilidades` ahora describe lo que hace `gen.py`: la debilidad derivada no puede estar ya en las listas de la familia.
- `formulas.jefe_pv` incluye el refuerzo.
- `amenaza.jefe` (y su copia `jefe`):
  - el turno es el asalto, y el daño por turno se aplica una vez por asalto;
  - la Firma cargada se lanza en el asalto siguiente y no puede usar P3 en asaltos seguidos;
  - Expuesto queda unificado;
  - nuevo bloque `refuerzos` (Vínculo 1 / Refuerzo I / Refuerzo II / ★) (#19, #24, #52);
  - el PA cuenta un nivel más si el Jefe va reforzado.
- `amenaza.nivel_de_referencia` pasa a ser el nivel de combate en el asalto 1. `presupuesto.nota` cambia y se añade `presupuesto.mortal`. `pa_por_diferencia_de_nivel` admite «−3 o menos: ⅛» y «3 o más: 15», con su nota (#9.2, #19, #23).
- `amenaza.esbirro` (y su copia `esbirro`): se añade la regla de hordas inferiores (#23). `amenaza.legendario` aclara «sin refuerzos».
- `validacion.reglas` incluye las reglas que `gen.py` ya comprobaba: Ejecutar solo Individual, P1 de daño sin área, apoyo sin estados, overrides e ids existentes, raíces normalizadas y validación de Armadura, Híbrido e Indeterminado (#2, #7, #12, #18).
- `validacion.objetivos_de_diseño` recoge las cifras medidas (#22, #27).
- `overrides_iniciales.tecnicas`: Terrier Tornado y River of Power pasan a alcance `larga`, porque un override que fija las claves se salta toda la segunda pasada y con ella la Larga del Tirador (#9.5). La nota de Terrier Tornado prometía Larga y no se cumplía. `clasificador.palabras_clave_orden[8]` lo explica. Cambian 6 fichas (Terriermon, Terriermon (X Antibody), Terriermon Assistant, Lopmon, Lopmon (X Antibody) y MetalSeadramon). `work_final/fichas_r3.json` se ha regenerado.
- `salida`: `json_ficha` añade los campos que ya genera `gen.py`, y `bloque_texto` añade el rango, las especialidades y la amenaza (#56). En `ejemplos`, Giga Storm queda «Brutal · 2d10; contra 2+: 1d10», y los bloques de texto llevan las nuevas líneas.

## Cambios en la biblia, por sección

**Cabecera.** Versión 1.1. Remite a `cambios.md`. Nueva definición de [N], que remite al Núcleo de primera sesión (#31).

**§0 Decisiones de diseño.**
- Agotadora redefinida.
- La regla «nunca en el asalto 1» queda limitada a Vínculo 1, y desde Vínculo 2 remite al nivel de referencia (#19).
- Nueva fila: golpe aguantado, regla de espejo, Jefe reforzado e índice de amenaza.
- Calibración reescrita con las cifras medidas por Vínculo, y se retiran las promesas que no se cumplían: «Legendario 4–6 asaltos» y «15–20 %» (#19, #27).

**§1 El sistema en una página.**
- Aviso de la regla de espejo (#29) y límite de Chispa por 6– (#36).
- Agotadora redefinida; forma de partida.
- Nuevo **1.1 Núcleo de primera sesión** (#31).

**§2 Resolución.**
- 2.1: el Tamer resta siempre el rango del Digimon (#60.3); nuevo desempate de la tirada enfrentada (#54); **regla de espejo** (#29).
- 2.5: la Ayuda en combate es la Orden y no se suma a ella (#57).
- 2.10: duración de Expuesto (#39).
- 2.13: el rango y las especialidades aparecen en la ficha (#56).
- Nuevo **2.14 Escena y combate** (#32).

**§3 El Tamer.**
- 3.1:
  - el paso 8 se desdobla: Bebé II, Campeón probable, personalidad, rol y especialidad del Versátil (#43);
  - Chispa 1 y Carga llena al empezar; Milagros y Destino no se pueden elegir;
  - los objetos iniciales salen de 14.3;
  - **creación rápida** con la Senda como paquete cerrado (#31).
- 3.2: se define el «defecto marcado» (#43).
- 3.4: efectos de los objetos de trasfondo (#43). El rasgo del Pícaro pasa de *Escurridizo* a *Huidizo* (#42).
- 3.5: la Senda Explorador pasa a **Batidor** (#42). ¡Flanqueo! sustituye al +1 de la Orden (#57).
- 3.6: «virtud» pasa a «cualidad» (#42).
- 3.7: Chispa 1 al crear el personaje.

**§4 El compañero.**
- 4.1: la remisión va a 21.10 (#60.2); «Mejoras» pasa a **Avances** (#42).
- 4.2:
  - regla para los 27 Novatos sin Bebé II (#44);
  - tabla recalculada con `gen.py`: Gomamon 24/+1/+3/+0; Betamon 24/+2/+2; Coronamon separado de Lunamon (Bruto, Vacuna, 24, «Corona-Knuckles»); Terriermon con Firma Larga; Gotsumon resiste Tierra; Renamon con 3d6/2d6; Lalamon duerme con Sing a Song (#5, #9.4, #9.5, #20c, #21, #26, #60.6);
  - se marcan como **frágiles** los Novatos de 21 PV o menos y Def +1 (#20c).
- 4.3: el cambio lateral conserva el daño (#30).
- 4.6: Avances.

**§5 Chispa y digievolución.**
- 5.1: Crisis única, que incluye el ataque telegrafiado (#37). La Resonancia del Emblema exige nivel 5 y Vínculo 3 (#60.5).
- 5.2: ir a una forma igual o inferior a la estable no restaura PV; excepción de Derrotado y regresión (#30, #33).
- 5.4: **forma de partida**. La digievolución pagada llena los PV como mucho una vez por forma y escena, y las formas estables conservan el daño (#30, #34).
- 5.5: vuelta a la forma de partida; la forma estable a 0 queda Derrotada **sin cascada** (#34).
- 5.6: Crisis según 5.1 y nota sobre Vínculo 2 (#19, #37).
- 5.8: la Chispa del mismo impacto paga la emergencia y ese impacto cuenta como Crisis; el daño sobrante pasa a la forma de partida (#20a, #28).
- 5.10: como mucho un nivel por encima del máximo, se paga al menos la mitad y la tirada la declara el DJ (#53).

**§6 Combate.**
- 6.1: zonas adyacentes (#59).
- 6.3: **reacciones** (#58).
- 6.4: Agotadora afecta al Digimon (#48).
- 6.5:
  - la Orden especial sustituye al +1 (#57);
  - Animar solo quita Descontrolado con 10+ (#35).
- 6.6:
  - el DJ anuncia el modificador neto (#40);
  - Regresión es control duro;
  - Chispa como mucho 1 por asalto (#36).
- 6.7:
  - el rol Místico (#41);
  - en un área de un PNJ, cada PJ tira su Defensa (#50).
- 6.8:
  - −1 dado solo con 2 o más objetivos (#21);
  - Potenciado+ (#47) y Furia;
  - se compara el rango (#55);
  - **golpe aguantado** (#20).
- 6.9: «Arm» (#42).
- 6.11:
  - un Zona alcanza a cualquier Tamer (#38);
  - cómo queda Expuesto un Tamer (#39);
  - Peligro = max(1, rango);
  - el Instinto protector es una reacción;
  - tabla de **estados en Tamers** (#51).
- 6.12: no hay cascada (#34).
- 6.13: la huida a pie resta el rango (#60.3).
- 6.15: el Jefe usa la Firma en asaltos alternos (#24).

**§7 Estados.**
- 7.1:
  - el rol Místico;
  - el turno de un Jefe es el asalto (#24, #52);
  - una sola invocación activa (#16);
  - Regresión es control duro (#17);
  - el daño por turno se reduce por rango (#24);
  - remisiones a la regla de espejo y a los estados en Tamers.
- 7.2: 20 estados.
- 7.3: Expuesto unificado (#39); nota sobre Agotado y Agotadora (#42); Potenciado y Potenciado+, y el programa Potencia no es un estado (#47).

**§9 Familias.**
- La familia Místico pasa a **Arcano** (#41).
- Sagrado no se aplica contra el Modo Oscuro (#41).
- Elemental resiste en lugar de ser inmune (#26).
- La lista de voladores usa ids (Lilamon y MegaKabuterimon (Red/Blue)) (#7).

**§10 Elementos.**
- Cósmico vence a Tierra y Acero; Mental vence a Veneno y Cósmico.
- Columna «deriva debilidades».
- Nuevo orden de debilidades y regla de «no repetir la de la familia».
- Raíces de contexto propias (#1, #6).

**§11 Vocabulario.**
- 11.2:
  - Agotadora;
  - P1 de daño siempre Individual (#14);
  - técnicas heredadas y Tarjetas como P2 (#48);
  - tabla «contra 2+ objetivos»;
  - fórmula de la 1.1 con golpe aguantado (#20, #21).
- 11.3:
  - alcances con área (Toque + Zona, Personal + Zona) (#14, #49);
  - áreas con −1 dado solo contra 2 o más (#21);
  - Zona alcanza a cualquier Tamer (#38);
  - Total en Jefes y Legendarios (#9.1);
  - áreas de un PNJ (#50).
- 11.4:
  - 35 palabras clave;
  - columna «Se activa»: Certero, Retroceso, Rápido y Ocultar se activan «al usarla», e Invocar «al impactar (7+)» (#15);
  - Ejecutar solo Individual (#13);
  - Quemar y Veneno: una vez por asalto en un Jefe y reducción por rango (#24);
  - nueva palabra **Regresión** (#17);
  - Curar y Escudo de apoyo son Agotadoras (#3);
  - Mejora P1 y P2 (#47);
  - Invocar: una por usuario (#16);
  - Ocultar en técnicas de apoyo (#49);
  - las técnicas de apoyo no llevan estados ni tácticas (#5);
  - **tabla de traducción de estados para PNJ** (#29).
- 11.5: la familia es Arcano.

**§12 Roles y técnicas.**
- 12.1:
  - Tanque: Atq 0 y PV +1 VF (#22);
  - Sanador: +VF solo al objetivo principal (#3);
  - Maestro de estados es un rasgo del rol (#41).
- 12.2: Desafío pasa a Toque · Zona (#14, #49); Pulso restaurador es Agotadora.
- 12.4:
  - una Firma heredada se usa como P2 (#48);
  - Barrera de datos y Reparación de datos son Agotadoras (#3);
  - requisitos «rol / familia» (#41);
  - Aullido pasa a «sin daño» y Ráfaga de datos a P2, para cumplir «P1 de daño siempre Individual» (#14).

**§13 Programas.**
- Los programas de Nivel 2 y 3 se marcan [A] (#31).
- Potencia no es un estado (#47).
- Bloqueo pasa a **Candado** y resta el rango (#42, #60.3).
- Tarjeta Digimon: cualquier Digivice, como máximo P2; el D-Arc la usa sin el programa y con 1 Carga menos (#46, #48).
- Sobrecarga pasa a **Overclock**, Purga a **Purgado** y Resonancia evolutiva a **Catalizador** (#42).

**§14 Objetos.**
- La Tarjeta funciona con cualquier Digivice (#46).
- Se define el Emblema físico (#45).
- Los 2 objetos iniciales salen de 14.3 (#43).

**§15 Digivices.**
- Todos tienen una función de núcleo.
- D-3: Carga +1 y *Radar D-3*.
- D-Tector: Carga +1 y revela a los Ocultos.
- Las funciones de módulo se marcan [O].
- Luz del Digivice: familia Oscuro o Modo Oscuro (#41, #45, #46).

**§16 Emblemas.**
- La Resonancia exige nivel 5 y Vínculo 3 (#60.5).
- Luz: familia Oscuro o Modo Oscuro (#41).
- Milagros y Destino no se pueden elegir al crear el personaje; Destino paga el coste normal (#43, #53).

**§17 Progresión.**
- Avances del compañero (#42).
- La Resonancia del Emblema exige Vínculo 3.
- Talentos de Batidor; Jinete según la nueva regla de Expuesto (#39).
- El talento Grito de guerra pasa a **¡A por ellos!** (#42).
- La técnica heredada se usa como P2.

**§18 Exploración.**
- La tirada social compara rangos (#55).
- Persecución a pie: resta el rango (#60.3).
- Familia Arcano en la tabla de regiones.
- El papel de viaje Explorador pasa a **Ojeador** (#42).
- Tamer sin comer (#60.4).

**§19 Amenazas.**
- 19.1: Jefe con refuerzo; el Legendario nunca lleva refuerzo; **índice de amenaza** (×¾ / ×1 / ×1½) (#26).
- 19.2 se reescribe:
  - **nivel de referencia** = nivel alcanzable en el asalto 1;
  - factor de diferencia de −3 o menos a +3 o más;
  - PA × índice de amenaza;
  - cifras medidas;
  - ejemplo recalculado (Gizamon y pelotón de Mushroomon, porque Goblimon es de amenaza alta);
  - tabla del **Jefe de la aventura por Vínculo**, con resultados medidos (#19, #23, #26, #27).
- 19.3: hordas inferiores y hordas narradas (#23).
- 19.4:
  - el turno es el asalto;
  - Agotadora para el Jefe;
  - **tabla de refuerzos**;
  - Firma telegrafiada: carga y se lanza en el asalto siguiente;
  - Expuesto unificado (#19, #24, #39, #52).
- 19.5:
  - Legendario sin refuerzo y con cifras medidas;
  - las listas se rehacen a partir de los ids: 126 Legendarios, con Eosmon solo Definitivo, Cherubimon (Black), Chaosmon: Valdur Arm y Magnamon (Armadura); 27 Jefes, sin Daemon; 20 esbirros, con su nivel (#7);
  - nota sobre Total en Jefes y Legendarios (#9.1).

**§20 Opcionales.** 20.1 Armadura:
- 2 Chispa, y nunca en el asalto 1 salvo como emergencia;
- a 0 PV queda Agotado;
- los huevos dorados respetan el Vínculo, cuestan 2 por nivel y provocan regresión;
- cifras medidas (#25).

**§21 Especificación.**
- Introducción: 0 errores de validación.
- 21.1: orden de cálculo de la 1.1 e **ids en lugar de nombres**; normalización de «ｰ» (#7, #9.4).
- 21.2: el nivel Unknown pasa a **Indeterminado**; uso del rango (#18, #42, #55).
- 21.3: fórmulas corregidas (#8, #21, #55).
- 21.4: Regresión pasa a Místico; nueva distribución de roles.
- 21.5: Modo Oscuro excluye a los Híbridos (#9.6); Armadura cuesta 2 Chispa.
- 21.6: clasificador de la 1.1 (#0, #1, #2, #4, #5, #10, #11, #12, #13):
  - normalización;
  - sufijos;
  - contexto que empieza tras el nombre;
  - apoyo (c);
  - frases antes que palabras y Oscuridad antes que Luz;
  - P1 Individual;
  - Ejecutar;
  - Regresión;
  - **74 overrides validados**.
- 21.7: amenaza por id con los recuentos y fórmula del índice (#26).
- 21.8: nuevas reglas de validación y objetivos **medidos** (#18, #22, #27).
- 21.9: formato con rango, especialidades y amenaza, y dados contra 2+ (#21, #56).
- 21.10: ejemplos recalculados con `gen.py` (Giga Storm y las líneas nuevas).

**§22 Referencia y redacción.**
- 22.1: hoja de referencia actualizada (#20, #21, #29, #32, #36, #39, #60.1):
  - Chispa como mucho 1 por asalto;
  - regla de espejo;
  - modificador anunciado;
  - área;
  - golpe aguantado;
  - Agotadora;
  - escena;
  - Expuesto;
  - Peligro = max(1, rango).
- 22.2: glosario ampliado y tabla de términos que se confunden (#42).
- 22.3:
  - núcleo de primera sesión;
  - presupuesto con nivel de referencia;
  - **4–6 parejas pregeneradas** (#31).
- 22.4: tabla de riesgos actualizada.

## Problemas no aplicados, o aplicados de otra forma, y motivo

- **#19, opción 3** (prohibir gastar en el asalto 1 la Chispa que se trae de la sesión anterior): no se aplica. En la simulación del verificador no devolvía el riesgo (V5: 0 %). Se usan en su lugar el nivel de referencia y el Jefe reforzado. **Objetivo 10–20 %:** no se alcanza en todos los tramos (V2: 2–10 %; V5: 0–10 %). Se publican las horquillas medidas en lugar de una promesa, y el índice de amenaza cubre la diferencia entre Jefes, que pesa más que la diferencia entre tramos.
- **#20 b** (que el Jefe no sume su +1 Atq contra compañeros de nivel inferior): no se aplica. Con el golpe aguantado ya no hay derrotas de un golpe, y la calibración de Vínculo 1 con +1 Atq da 1–3 % de derrota. La excepción solo añadiría contabilidad.
- **#22, opcional** (la Arm no se resta con 10+): no se aplica. El cambio del Tanque basta: el peor emparejamiento queda en 4,3–4,8 asaltos. Tampoco se añade a `gen.py` una simulación de duelos, porque `gen.py` no se toca; los duelos se miden con `work_final/cal_biblia/b7.py`.
- **#23, alternativa** (resolver las hordas con un reloj): no se aplica. Se elige la regla de daño de área y de miembros eliminados por rango, más la de hordas narradas.
- **#25:** se combinan las dos opciones propuestas para los huevos dorados (respetan el Vínculo y además cuestan 2 por nivel y provocan regresión), en lugar de elegir una.
- **#26:** la regla «si más de la mitad del grupo depende del elemento inmune, el Jefe cuenta un nivel más» ya no hace falta, porque Elemental resiste en lugar de ser inmune.
- **#27:** se probó el Legendario con ⌈N/2⌉+1 acciones y se rechazó: 32–58 % de derrota a Vínculo ★, y 44–66 % con además PV (N+4)/2. La plantilla Legendario no cambia.
- **#31:** no se reetiquetan como [A] capítulos enteros (familias, elementos, Sendas…). [N] sigue siendo el núcleo de campaña y se añade un **Núcleo de primera sesión** explícito; solo pasan a [A] los programas de Nivel 2 y 3 y la Resonancia del Emblema. Reetiquetar todo habría roto remisiones sin aportar nada a la primera sesión.
- **#34:** en lugar de «una sola cascada», se elige **ninguna cascada**: la forma estable a 0 queda Derrotada. Así hay como mucho dos barras de PV, y es la regla con la que el motor 1.1 (`NO_CASCADE = True`) midió todas las cifras.
- **#39:** la duración de Expuesto se unifica como «hasta el final de su próximo turno», y no como «lo que llegue antes», para que sirva igual a PJ, PNJ y Jefes.
- **#42:** no se renombran Agotado/Agotadora, Carga/Cargar/Cargado/Guardia de carga, Valor (atributo y Emblema), Resonancia y Resonancia del Emblema, ni Protector (Senda y rasgo). Se distinguen en la nueva tabla del glosario (22.2). Renombrar mecánicas del núcleo tan usadas costaría más de lo que aclara.
- **#3, comprobación del Monte Carlo con un Apoyo en el grupo:** pendiente. `r3_sim.py` no modela las técnicas de apoyo. La corrección (Agotadora y +VF solo al objetivo principal) reduce la curación por asalto a la mitad o menos.
- **#4 y #12:** se resolvieron en la especificación 1.1 (raíces de contexto). En la biblia solo se resume en 21.6.
- **#55:** «rango» se usa en todas las comparaciones entre Digimon (escala, tirada social, presupuesto, Xros Loader, Emblema del Valor). La palabra «nivel» se mantiene en el texto narrativo y en «nivel estable», «nivel máximo», «nivel de Tamer» y «nivel de programa», que el glosario distingue.
- **#9.2:** las claves de PA no se separan una a una (−3, −4, +4); se usan «−3 o menos» y «3 o más». Tampoco se añade una clave «mortal» al factor: «Mortal» queda como dificultad del presupuesto (`presupuesto.mortal`) y como nota del +3.
- **Firma telegrafiada:** se mantiene como [A]. Las cifras publicadas se midieron sin ella, que es el núcleo.
