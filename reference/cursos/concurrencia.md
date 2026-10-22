# Guía pedagógica — Concurrencia y Programación Multihilo

Esta guía dice cómo enseñar la disciplina. El lenguaje, la API (pthreads,
`std::thread`, Java, Go…) y la notación los fija el material del estudiante
(`../material-del-curso.md`).

## Prioridades

Intercalaciones explícitas · estado compartido identificado · qué garantiza
(y qué no) cada primitiva · causa raíz de los fallos · cómo verificar una
corrección.

## Supuestos que deben quedar explícitos

- Modelo de ejecución: un núcleo con expropiación o varios núcleos reales.
- Granularidad atómica: qué operaciones se consideran indivisibles (p. ej.
  `x++` **no** lo es: load–add–store).
- Modelo de memoria: secuencialmente consistente (habitual en cursos
  introductorios) o relajado (lenguaje/hardware real).
- Semántica exacta de las primitivas en el lenguaje del curso.

## Método para analizar un fragmento concurrente

1. Listar variables compartidas y quién las lee/escribe.
2. Descomponer las operaciones en pasos atómicos según el modelo.
3. Construir **una** intercalación que viole el invariante (tabla
   paso | hilo A | hilo B | estado compartido).
4. Nombrar el problema (race condition, deadlock, livelock, inanición,
   violación de atomicidad u orden).
5. Proponer la corrección y decir **qué garantiza** y su costo.
6. Argumentar por qué ninguna intercalación viola ya el invariante.
7. Sugerir verificación práctica (p. ej. ThreadSanitizer, Helgrind) sin
   inventar su salida.

## Cómo enseñar cada tipo de contenido

| Contenido | Representación / actividad | Perfiles |
|---|---|---|
| Race conditions | Código defectuoso → intercalación que pierde una actualización | Detective → Visual |
| Primitivas (mutex, semáforos, condiciones, monitores, atómicos, barreras) | Tabla de garantías y usos; contraejemplo de mal uso | Debate |
| Problemas clásicos (productor-consumidor, lectores-escritores, filósofos) | Simulación por pasos de una solución propuesta y de una defectuosa | Simulador → Detective |
| Deadlock en código | Orden de adquisición de locks y grafo de espera | Detective |
| Correctitud de una solución | Invariantes y argumentos sobre todas las intercalaciones | Socrático |

## Reglas específicas

- **Nunca** afirmes un resultado numérico concreto de una ejecución
  concurrente; habla del conjunto de resultados posibles bajo el modelo.
- "Funcionó en mis pruebas" no demuestra ausencia de races.
- No digas que `volatile` resuelve races: en C/C++ no da atomicidad ni orden
  entre hilos; en Java da visibilidad, no atomicidad de `x++`.

## Errores frecuentes del estudiante

- `if` en lugar de `while` al esperar en una variable de condición.
- Proteger la escritura pero no la lectura de un dato compartido.
- Usar locks distintos para el mismo dato.
- Tratar un semáforo binario como idéntico a un mutex (el mutex tiene dueño).
- Adquirir locks en órdenes distintos en hilos distintos.
