# Selector de estrategias — detalle

Complementa la §2 de `SKILL.md`. Úsalo para peticiones ambiguas, mixtas o
para planear un tema completo.

## Paso 1. Leer la petición

| Señal en la petición | Interpretación |
|---|---|
| "¿qué es…?", "define…", "diferencia entre…" | Consulta puntual → respuesta directa |
| "explícame", "no entiendo", "enséñame" | Aprender un tema → protocolo |
| "resuelve", "¿está bien mi respuesta?" | Ejercicio concreto → verificar/desarrollar |
| "¿por qué falla?", pega código con bug | Diagnóstico → Detective |
| "demuestra", "justifica", "¿por qué funciona?" | Demostración → Socrático (o directa si nivel bajo) |
| "¿cuál es mejor…?", "¿cuándo usar…?" | Comparación → Debate |
| "tengo parcial/examen", "hazme preguntas" | Evaluación → Examen adaptativo |
| "¿qué pasa si…?", tablas de procesos/páginas | Sistema dinámico → Simulador |
| "a ver si lo entendí: …" | Consolidación → Feynman |

## Paso 2. Tipo de tarea → representación preferida

| Tipo de tarea | Representación / actividad principal |
|---|---|
| Conceptual | Modelo mental + ejemplo y contraejemplo |
| Procedimental | Ejemplo resuelto → retirada de ayudas |
| Matemática | Derivación con pasos intermedios + verificación numérica |
| Algorítmica | Traza de estados + invariante + complejidad |
| Implementación | Código mínimo correcto + casos límite + pruebas |
| Diagnóstico | Síntoma → hipótesis → evidencia → causa raíz |
| Demostración formal | Afirmación → técnica → pasos justificados |
| Análisis de sistemas | Supuestos → simulación → métricas |
| Diseño / decisión | Criterios → alternativas → trade-offs → escenario |

## Paso 3. Nivel de ayuda

| Nivel estimado | Ayuda adecuada |
|---|---|
| 0 | Explicación directa y ejemplo resuelto. Nada de socrático. |
| 1 | Ejemplo resuelto + parcialmente resuelto. Preguntas de predicción sencillas. |
| 2 | Ejercicios guiados con pistas graduadas. |
| 3 | Ejercicios autónomos, justificación, variantes. |
| 4 | Casos límite, comparación, diseño, Feynman. |

Si no tienes información, asume nivel 1–2 para temas nuevos y ajusta tras la
primera respuesta del estudiante. Una única pregunta diagnóstica es
suficiente; no hagas un examen de entrada.

## Paso 4. Reglas de transición

- **2 errores seguidos del mismo tipo** → cambia de representación o perfil.
- **3 errores conceptuales** en el mismo tema → busca prerrequisito débil.
- **Aciertos rápidos con buena justificación** → retira ayudas, sube
  dificultad o pasa a transferencia.
- **Respuestas correctas sin justificación** → pide el porqué antes de avanzar.
- **El estudiante pide otra cosa** → obedece: su preferencia explícita manda,
  salvo que comprometa la corrección técnica.
- **Frustración evidente** → reduce el tamaño del paso, ofrece explicación
  directa, reconoce el progreso real.

## Mapa de prerrequisitos frecuentes (para Prueba E)

| Si falla en… | Revisa primero… |
|---|---|
| Recurrencias / Teorema maestro | Logaritmos, series geométricas, sumatorias |
| Complejidad amortizada | Sumatorias, método de potencial/contabilidad |
| AVL / árboles balanceados | BST: inserción y propiedad de orden; altura |
| Heaps | Representación en arreglo (índices padre/hijo) |
| Dijkstra / caminos mínimos | BFS, colas de prioridad, relajación |
| Programación dinámica | Recursión, subproblemas solapados, recurrencias |
| Memoria virtual / TLB | Aritmética binaria, división dirección = página + offset |
| Planificación de CPU | Definiciones de turnaround, waiting, response time |
| Deadlocks | Condiciones de Coffman; grafos de asignación |
| Race conditions | Atomicidad; `x++` no es atómico (load–add–store) |
| Semáforos / monitores | Exclusión mutua, sección crítica, espera activa vs bloqueo |
| Speedup / eficiencia | Definiciones T₁, Tₚ; fracción serial; costo = p·Tₚ |
| PCAM | Grafos de dependencias, granularidad, comunicación local/global |
| Consistencia distribuida | Orden de eventos, relojes lógicos (happens-before) |
| Normalización (BD) | Dependencias funcionales, claves candidatas |
| Pipeline (arquitectura) | Ciclo de instrucción, dependencias de datos |
