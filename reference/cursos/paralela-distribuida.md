# Guía pedagógica — Computación Paralela y Distribuida

Esta guía dice cómo enseñar la disciplina. El modelo de costo, las fórmulas
con su notación y las herramientas (OpenMP, MPI, CUDA…) los fija el material
del estudiante (`../material-del-curso.md`).

## Prioridades

Descomposición de tareas · grafos de dependencia · PCAM · mapeo a
procesadores · trazas de comunicación · speedup y eficiencia · overhead,
escalabilidad y granularidad · intercalaciones y modelos de consistencia.

**Distingue** concurrencia, paralelismo y distribución cuando corresponda.
**Nunca asumas** que más procesadores siempre mejoran el rendimiento.

## Supuestos que deben quedar explícitos

- Qué es T₁ (mejor secuencial o paralelo con p = 1) según el curso.
- Modelo de comunicación del curso (p. ej. latencia + costo por palabra) y
  si hay solapamiento cómputo/comunicación.
- Tamaño de problema fijo (escalado fuerte) o escalado (débil): decide si
  aplica Amdahl o Gustafson.
- Topología/red, memoria compartida o distribuida.
- Divisibilidad (n múltiplo de p) y balance de carga.

## Protocolo para problemas cuantitativos

1. Escribe la fórmula como la usa el curso.
2. Define cada variable con unidades.
3. Sustituye valores.
4. Desarrolla el cálculo paso a paso.
5. Interpreta (qué término domina, qué pasa si crece p o n).
6. Etiqueta: **resultado del modelo, no medición**.

## Protocolo PCAM

Para cada fase, decisión **y** justificación:
1. **Particionamiento** — descomposición fina (dominio o funcional).
2. **Comunicación** — qué intercambian las tareas: local/global,
   estructurada/no, estática/dinámica, síncrona/asíncrona.
3. **Aglomeración** — agrupar para reducir comunicación y overhead sin
   perder escalabilidad.
4. **Mapeo** — asignación a procesadores: concurrencia, localidad, balance.

Después: modelo de costo `Tₚ` → speedup → eficiencia → análisis variando n y
p (mostrar un caso donde la comunicación domine).

## Cómo enseñar cada tipo de contenido

| Contenido | Representación / actividad | Perfiles |
|---|---|---|
| Descomposición / PCAM | Grafo de tareas y de comunicación; tabla por fase | Visual → Laboratorio |
| Métricas de rendimiento | Protocolo cuantitativo; variar n y p | Laboratorio → Simulador |
| Leyes de escalado | Mismo problema bajo supuestos de tamaño fijo vs. escalado | Debate |
| Código paralelo (OpenMP/MPI/GPU) | Fragmento con fallo (race, deadlock de envíos bloqueantes, desbalance) | Detective |
| Orden de eventos y consistencia | Diagramas espacio-tiempo con mensajes; relojes lógicos | Visual → Simulador |
| Arquitecturas distribuidas, consenso, replicación | Escenarios con fallos parciales y criterios explícitos | Debate → Simulador |

## Errores frecuentes del estudiante

- Asumir speedup lineal o ignorar comunicación y sincronización en Tₚ.
- Aplicar Amdahl a problemas que escalan con p.
- Confundir eficiencia con speedup, o costo con tiempo.
- Granularidad demasiado fina sin aglomerar.
- Suponer que los relojes físicos ordenan causalmente los eventos.
- Interbloqueo por `Send` bloqueantes cruzados en MPI.

## Prerrequisitos que suelen fallar

Grafos de dependencias · logaritmos (árboles de reducción) · concurrencia
básica · complejidad asintótica.
