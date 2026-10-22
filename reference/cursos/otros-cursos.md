# Guías pedagógicas compactas — otros cursos

Cómo enseñar cada disciplina; el contenido lo fija el material del
estudiante (`../material-del-curso.md`). Para añadir un curso, copia
`_plantilla.md` a `reference/cursos/<curso>.md` y regístralo en la tabla de
`SKILL.md`. El núcleo pedagógico no cambia.

## Arquitectura de Computadores

- **Representaciones:** diagrama de pipeline ciclo a ciclo; datapath;
  partición de direcciones en tag | índice | offset; tablas de accesos a caché.
- **Supuestos a fijar:** etapas del pipeline, forwarding sí/no, política de
  saltos, tamaño de bloque, asociatividad, política de escritura.
- **Perfiles:** Visual (pipeline), Simulador (caché hit/miss), Laboratorio
  (cálculos de rendimiento con el protocolo fórmula → variables → sustitución
  → interpretación).
- **Errores típicos:** latencia vs. throughput; olvidar bits de offset;
  contar mal los stalls.

## Redes

- **Representaciones:** diagramas de secuencia de mensajes; encapsulamiento
  por capas; evolución temporal de ventanas.
- **Supuestos a fijar:** tamaños de paquete, tasas, distancias, versión del
  protocolo que enseña el curso.
- **Perfiles:** Visual, Simulador (control de congestión, enrutamiento),
  Laboratorio (subredes, retardos).
- **Errores típicos:** transmisión vs. propagación; direcciones de red y
  broadcast contadas como hosts.

## Bases de Datos

- **Representaciones:** diagramas ER; tablas de ejemplo; planes de consulta;
  calendarios (*schedules*) de transacciones.
- **Supuestos a fijar:** dialecto SQL, notación de álgebra relacional del
  curso, nivel de aislamiento.
- **Perfiles:** Laboratorio (normalización, cierre de atributos), Detective
  (consultas que devuelven resultados incorrectos, anomalías de
  concurrencia), Debate (índices, desnormalización).
- **Errores típicos:** `NULL` en comparaciones y `NOT IN`; `GROUP BY` con
  columnas no agregadas; confundir formas normales.

## Ingeniería de Software

- **Representaciones:** UML, diagramas de arquitectura, matrices de
  trazabilidad, tablas de casos de prueba.
- **Perfiles:** Debate (decisiones de diseño), Detective (code smells,
  refactorización), Laboratorio (casos de prueba por particiones y valores
  límite).
- **Errores típicos:** patrones sin un problema que los justifique;
  confundir cobertura con calidad de las pruebas.
- **Cuidado:** un proyecto abierto no sustituye enseñar los principios;
  primero el principio con un ejemplo acotado.

## Sistemas de Programación (compiladores, ensambladores, enlazadores, cargadores)

- **Representaciones:** autómatas; tablas FIRST/FOLLOW y de análisis; pila
  del parser paso a paso; tablas de símbolos y de reubicación.
- **Perfiles:** Laboratorio (construcción de tablas), Simulador (ejecución
  del parser o del ensamblador de dos pasadas), Detective (conflictos de
  gramática).
- **Errores típicos:** olvidar ε en FIRST; recursión izquierda en LL(1);
  confundir conflictos shift/reduce y reduce/reduce.

## Análisis y Diseño de Algoritmos

Usa `estructuras-datos-algoritmos.md`. Énfasis adicional: paradigmas
(divide y vencerás, voraz, programación dinámica, backtracking, ramificación
y poda), reducciones y NP-completitud (dirección correcta de la reducción:
del problema conocido al nuevo), algoritmos aproximados.
