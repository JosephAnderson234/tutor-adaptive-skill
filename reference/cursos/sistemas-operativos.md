# Guía pedagógica — Sistemas Operativos

Esta guía dice cómo enseñar la disciplina. El temario, las definiciones y la
notación los fija el material del estudiante (`../material-del-curso.md`).

## Prioridades

Diagramas de estados y transiciones · líneas de tiempo (Gantt) · tablas de
planificación · representación de memoria · trazas de ejecución concurrente
· análisis de interbloqueos · simulación de políticas.

## Supuestos que siempre deben quedar explícitos

Toma los del enunciado o del material; si faltan, decláralos antes de calcular:

- **Planificación:** tiempos de llegada, ráfagas, quantum, política,
  expropiación sí/no, desempates (en particular: llegada que coincide con la
  expiración de un quantum), costo de cambio de contexto, E/S.
- **Métricas:** cómo define el curso turnaround, espera y respuesta.
- **Memoria:** tamaño de página/marco, número de marcos, política de
  reemplazo, si la TLB se consulta en paralelo, tiempos de acceso.
- **Interbloqueos:** instancias por tipo de recurso, matrices del enunciado.
- **Disco/E/S:** posición inicial del cabezal y dirección.

## Cómo enseñar cada tipo de contenido

| Contenido | Representación / actividad | Perfiles |
|---|---|---|
| Ciclo de vida de procesos/hilos | Diagrama de estados con el evento que causa cada transición | Visual |
| Planificación de CPU | Tabla de entrada → cola de listos por instante → Gantt → tabla de métricas; pedir predicción antes de los instantes clave | Simulador → Debate → Examen |
| Traducción de direcciones | Partición en bits (página / desplazamiento) con la aritmética explícita | Laboratorio |
| Reemplazo de páginas | Tabla referencia × marcos × ¿fallo?; contar fallos; variar número de marcos | Simulador |
| Tiempo efectivo de acceso | Fórmula → variables → sustitución → interpretación | Laboratorio |
| Interbloqueos | Grafo de asignación; matrices del banquero paso a paso; código que se bloquea | Visual → Simulador → Detective |
| Sincronización | Ver `concurrencia.md` | Detective |
| Comparar políticas | Mismo conjunto de procesos con varias políticas y criterios explícitos | Debate |

## Verificaciones que el tutor siempre hace

- Ningún proceso se ejecuta antes de su llegada.
- La suma de los intervalos del Gantt de cada proceso = su ráfaga.
- Las métricas se recalculan a partir del Gantt, no de memoria.
- En simulaciones: decir que son resultados del modelo, no mediciones.

## Errores frecuentes del estudiante

- Calcular la espera sin restar la llegada o ignorando llegadas tardías.
- Ordenar mal la cola de listos en Round Robin.
- Creer que un ciclo en el grafo de asignación siempre es deadlock (solo con
  una instancia por recurso).
- Confundir estado inseguro con deadlock.
- Atribuir la anomalía de Bélády a LRU.
- Olvidar los bits de desplazamiento al traducir direcciones.

## Prerrequisitos que suelen fallar

Aritmética binaria y potencias de 2 · definiciones de las métricas ·
estructuras de cola · nociones de arquitectura (interrupciones, modo kernel).
