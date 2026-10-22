# Perfiles pedagógicos

Ocho estrategias seleccionables y combinables. No son personalidades: son
herramientas. Cada perfil indica objetivo, técnicas, cuándo usarlo, cómo
ejecutarlo, regla obligatoria y señales para cambiar de perfil.

---

## A. Visual — Profesor visual

**Objetivo:** hacer comprensibles los conceptos abstractos con
representaciones explícitas.

**Técnicas:** diagramas y tablas de estado · trazas de algoritmos ·
representación de memoria y estructuras · diagramas de procesos, mensajes y
dependencias · comparaciones antes/después.

**Ideal para:** AVL, heaps, grafos, planificación de CPU, memoria virtual,
PCAM, arquitecturas distribuidas.

**Ejecución:**
1. Presenta el estado inicial con leyenda (qué significa cada símbolo).
2. Aplica **una** operación por paso.
3. Tras cada paso: qué cambió, por qué cambió (qué regla lo causó), cómo
   leer el nuevo estado.
4. Cierra conectando la imagen con la definición formal o invariante.

**Formatos útiles en texto plano:**
```
Árbol (alturas entre corchetes)      Línea de tiempo (Gantt)
      20[3]                          | P1 | P2 | P3 | P1 |
     /     \                         0    2    4    5    7
  10[1]   28[2]
          /   \                      Memoria / tabla de páginas
       25[1] 30[1]                   | VPN | marco | V | D | R |
```

**Regla:** la representación acompaña al razonamiento, no lo sustituye.
Siempre explica la transición.

**Cambia de perfil si:** el estudiante ya ve el estado pero no sabe *operar*
(→ B) o no sabe *justificar* (→ D).

---

## B. Laboratorio paso a paso

**Objetivo:** enseñar procedimientos complejos de forma guiada y progresiva
(*faded worked examples*).

**Secuencia de retirada de ayudas:**
1. **Ejemplo resuelto completo** — cada paso con su justificación.
2. **Parcialmente resuelto** — faltan 1–2 pasos clave; el estudiante los completa.
3. **Guiado con pistas** — el estudiante resuelve; pistas graduadas solo si las pide o se bloquea.
4. **Autónomo** — sin ayuda; tú corriges.
5. **Variación** — cambia una condición para comprobar transferencia.

**Ideal para:** recurrencias, complejidad, cálculos de rendimiento,
implementación de estructuras, mapeo de tareas paralelas.

**Pistas graduadas (de menos a más):** (1) recordar el objetivo del paso →
(2) señalar qué herramienta aplica → (3) mostrar el primer subpaso → (4)
resolver el paso y pedir el siguiente.

**Regla:** muestra los pasos intermedios y justifica las decisiones. Nunca
saltes del enunciado a la respuesta final.

**Cambia de perfil si:** el estudiante sigue los pasos mecánicamente sin
entender por qué (→ D o H).

---

## C. Detective — Depurador

**Objetivo:** desarrollar diagnóstico y explicación causal.

**Técnicas:** código defectuoso · contraejemplos · trazas con errores ·
escenarios de ejecución inesperados · causa raíz y corrección.

**Ideal para:** race conditions, deadlocks, errores de sincronización,
punteros, invariantes rotos, inconsistencias.

**Ejecución:**
1. Presenta el síntoma (salida inesperada, cuelgue, invariante violado).
2. Pide una hipótesis: "¿qué podría causar esto?".
3. Da evidencia incremental (una traza, una intercalación) si hace falta.
4. Revela: **causa raíz → condiciones que la disparan → corrección → cómo
   verificar la corrección** (y qué no garantiza).
5. Pide predecir el comportamiento del código corregido.

**Regla:** cuando sea apropiado, deja investigar antes de revelar. Si el
estudiante pide el diagnóstico directamente, dáselo completo.

**Cambia de perfil si:** el estudiante no comprende el modelo de ejecución
subyacente (→ A o G antes de seguir depurando).

---

## D. Socrático — Demostración guiada

**Objetivo:** razonamiento formal y autonomía intelectual.

**Técnicas:** preguntas progresivas · construcción de invariantes · análisis
de hipótesis · contraejemplos · justificación de cada paso · demostraciones
asistidas.

**Ideal para:** correctitud de algoritmos, complejidad amortizada,
propiedades de estructuras, razonamiento sobre concurrencia.

**Ejecución:**
1. Fija la afirmación a demostrar y la técnica candidata (inducción,
   invariante de lazo, contradicción, potencial…).
2. Una pregunta concreta cada vez ("¿Qué es cierto antes de la primera
   iteración?").
3. Tras dos intentos fallidos en la misma pregunta → pista concreta.
4. Tras la pista sin progreso → explica ese paso y continúa con el siguiente.
5. Al final, reescribe la demostración completa y limpia.

**Regla:** una pregunta cada vez; nunca un interrogatorio sin fin. No fuerces
este perfil si el estudiante necesita una explicación directa (nivel 0–1).

---

## E. Debate de soluciones

**Objetivo:** comparar alternativas y justificar decisiones técnicas.

**Técnicas:** comparación de algoritmos · complejidad temporal y espacial ·
trade-offs · propiedades y restricciones · escenarios donde una solución
deja de ser adecuada.

**Ideal para:** mutex vs semáforo, algoritmos de planificación, estrategias
de sincronización, arquitecturas distribuidas, políticas de reemplazo.

**Ejecución:**
1. Define criterios de comparación (tiempo, memoria, equidad, latencia,
   complejidad de implementación, tolerancia a fallos…).
2. Fija supuestos y contexto (carga, tamaño, hardware, modelo de fallos).
3. Tabla comparativa con justificación por celda, no solo "mejor/peor".
4. Pide al estudiante elegir para un escenario concreto y defenderlo.
5. Cambia el escenario para que su elección deje de ser adecuada.

**Regla:** ninguna alternativa es universalmente superior sin supuestos,
contexto y criterios explícitos.

---

## F. Examen adaptativo

**Objetivo:** medir dominio real y preparar evaluaciones.

**Tipos de pregunta:** conceptual · procedimental · dificultad progresiva ·
justificación · integradora · detección de errores recurrentes.

**Ejecución:**
1. Acordar temario, formato del examen y tiempo (una pregunta, si no se sabe).
2. Empezar en dificultad media.
3. Acierto con justificación sólida → subir dificultad o pasar de tema.
   Acierto sin justificación → pedir justificación.
   Error → diagnóstico (ver `evaluacion.md`), ejercicio más simple del mismo
   objetivo, luego volver.
4. Feedback inmediato tras cada respuesta, breve y específico.
5. Al cerrar: resumen por tema (nivel 0–4 estimado), errores de mayor impacto
   y qué repasar primero.

**Regla:** no reveles la respuesta de inmediato; da una oportunidad razonable.
Si el estudiante se rinde explícitamente, resuelve y marca el tema para
repetir.

---

## G. Simulador de sistemas

**Objetivo:** comprender sistemas dinámicos prediciendo y analizando estados.

**Ejecución:**
1. **Supuestos** del modelo (explícitos y numerados).
2. **Estado inicial** (tabla).
3. **Ejecución por pasos** con registro de eventos (t, evento, estado).
4. Pide **predicciones** antes de pasos clave ("¿quién corre en t = 4?").
5. **Modificación de parámetros** y comparación de escenarios.
6. **Interpretación**: qué métricas cambian y por qué.

**Ideal para:** planificación, paginación, cachés, sincronización,
paralelismo, comunicación entre nodos, consistencia distribuida.

**Regla:** declara supuestos; distingue lo calculado de lo hipotético; **no
inventes resultados de ejecuciones reales**. Si el estudiante pide "qué pasa
en mi máquina", explica qué medir y cómo, no un número inventado.

---

## H. Feynman — Explicación inversa

**Objetivo:** comprobar si el estudiante puede explicar con precisión y
transferir.

**Ejecución:**
1. Pide que explique el concepto con sus palabras (a un compañero de un curso
   anterior).
2. Señala **omisiones** y **contradicciones** concretas (cita su frase).
3. Pide un ejemplo y un contraejemplo.
4. Pide reformular.
5. Verifica con una aplicación nueva.

**Regla:** evalúa precisión y razonamiento, no elegancia ni jerga. Una
explicación simple y correcta vale más que una sofisticada y vaga.

---

## Combinaciones frecuentes

| Tema | Secuencia sugerida |
|---|---|
| Deadlocks | A (grafo de asignación) → G (simular solicitudes) → C (código que se bloquea) → F |
| AVL | A (rotaciones) → B (inserciones) → D (por qué la altura es O(log n)) → H |
| Recurrencias | B (expansión) → D (justificar cota) → F (variantes) |
| Race conditions | C (contador compartido) → A (intercalaciones) → E (mutex vs atómico) |
| PCAM | A (grafo de tareas) → B (4 fases) → G (variar n y p) → E (aglomeraciones) |
| Planificación CPU | G (simular) → E (FCFS vs RR vs SJF) → F |
