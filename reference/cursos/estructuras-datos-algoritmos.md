# Guía pedagógica — Estructuras de Datos, Algoritmos Avanzados, Análisis y Diseño de Algoritmos

Esta guía dice cómo enseñar la disciplina. El temario, las definiciones y la
notación los fija el material del estudiante (`../material-del-curso.md`).

## Prioridades

1. Trazas paso a paso con el estado completo de la estructura.
2. Invariantes y pruebas de correctitud.
3. Complejidad temporal y espacial (peor caso / promedio / amortizado).
4. Casos límite y contraejemplos.
5. Comparación de alternativas.
6. Implementación y análisis de errores.

**Separa siempre y rotula tres capas:** (a) ejecución concreta (traza),
(b) justificación de correctitud, (c) análisis de complejidad.

## Convenciones que hay que fijar (del material o declaradas)

- Altura de una hoja (0 o 1) y del árbol vacío; altura vs. profundidad.
- Signo del factor de balance; nombres de los casos de rotación.
- Indexación de arreglos (base 0 o 1) en heaps y pseudocódigo.
- Supuestos de las recurrencias (`n = bᵏ`, caso base, pisos/techos).
- Versión del teorema maestro que usa el curso (hay varias formulaciones).
- Representación de grafos (lista vs. matriz) y si los pesos pueden ser negativos.

## Cómo enseñar cada tipo de contenido

| Contenido | Representación / actividad | Perfiles |
|---|---|---|
| Operaciones sobre estructuras (árboles balanceados, heaps, tablas hash) | Estado antes/después por operación; una operación por paso | Visual → Laboratorio |
| Recurrencias | Expansión explícita de 2–3 niveles → patrón general → caso base → suma cerrada → verificación con n pequeño → cota Θ | Laboratorio → Socrático |
| Algoritmos de grafos | Tabla por iteración (nodo procesado, distancias, predecesores, cola/estructura auxiliar) | Visual → Simulador |
| Correctitud | Invariante (inicialización, mantenimiento, terminación), inducción, intercambio en voraces | Socrático |
| Amortizado | Método del curso (agregado, contabilidad o potencial) aplicado a una secuencia concreta | Laboratorio → Socrático |
| Programación dinámica | Subproblema → recurrencia → orden de cómputo → tabla → reconstrucción | Laboratorio |
| Elegir estructura/algoritmo | Criterios + supuestos + escenario que invalida la elección | Debate |
| Implementación | Código mínimo + casos límite + pruebas | Detective |

## Verificaciones que el tutor siempre hace

- Tras cada operación estructural: comprobar la propiedad (orden BST,
  propiedad de heap, balance) en **todos** los nodos afectados.
- Tras resolver una recurrencia: sustituir valores pequeños en la forma cerrada.
- Distinguir O, Θ y Ω en el resultado final.
- Revisar entradas límite: vacío, un elemento, duplicados, ya ordenado.

## Errores frecuentes del estudiante

- Confundir altura con profundidad o contar aristas en lugar de nodos.
- Rebalancear en un nodo que no es el primer ancestro desbalanceado.
- Aplicar el teorema maestro fuera de su forma o sin la condición de regularidad.
- Suponer que construir un heap cuesta Θ(n log n) (bottom-up es Θ(n)).
- Usar Dijkstra con pesos negativos.
- Confundir costo amortizado con costo promedio.
- Dar O cuando se pide una cota ajustada.

## Prerrequisitos que suelen fallar

Logaritmos y sus propiedades · series aritméticas y geométricas · inducción
matemática · recursión · BST básico.
