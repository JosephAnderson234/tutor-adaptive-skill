# Pruebas de aceptación

Cada prueba define el **prompt** (o la secuencia de turnos), lo que la
respuesta **debe** hacer, lo que **no debe** hacer y los **valores técnicos
de referencia** para comprobar la corrección.

Cómo ejecutarlas:
- **Manual:** abre una sesión nueva en el agente con la skill instalada, pega
  los turnos y evalúa con los criterios.
- **Con juez LLM:** usa `tests/judge-prompt.md` con la transcripción y el
  caso correspondiente de `tests/scenarios.json`.

Criterios comunes para todas las pruebas (puntuar 0–2 cada uno):
corrección técnica · calidad pedagógica · claridad · adaptación · ausencia
de pasos innecesarios.

---

## A — Recurrencias por expansión

**Prompt:** «Resuelve por expansión T(n) = 2T(n/2) + n², con T(1) = 1. Quiero ver todo el desarrollo.»

**Debe:**
- Declarar `n = 2ᵏ` (o equivalente).
- Expandir al menos 2–3 niveles de forma explícita.
- Generalizar: `T(n) = 2ⁱT(n/2ⁱ) + n²·Σ_{j=0}^{i−1} (1/2)ʲ`.
- Llegar al caso base `i = log₂ n`, sumar la serie geométrica.
- Resultado exacto `T(n) = 2n² − n` y cota `Θ(n²)` con justificación del término dominante.
- (Deseable) verificar con n = 2 → 6, n = 4 → 28.

**No debe:** saltar al teorema maestro sin la expansión; dar solo O(n²) sin justificar ajuste.

**Referencia:** `T(2) = 2·1 + 4 = 6 = 2·4 − 2`; `T(4) = 2·6 + 16 = 28 = 32 − 4`.

---

## B — Árboles AVL

**Prompt:** «Inserta en un AVL vacío: 50, 40, 60, 70, 80, 75. Muéstrame cada paso.»

**Debe:**
- Declarar la convención de altura/FB.
- Mostrar el árbol tras cada inserción relevante.
- Tras 80: primer desbalanceado **60** → caso **RR** → rotación a la izquierda en 60 → `50(40, 70(60, 80))`.
- Tras 75 (hijo izquierdo de 80): primer desbalanceado **50** (70 y 80 siguen dentro de |FB| ≤ 1) → caso **RR** (hijo derecho 70 cargado a la derecha) → rotación a la izquierda en 50.
- Árbol final `70(50(40, 60), 80(75, —))` y verificación de la propiedad AVL en todos los nodos.

**No debe:** aplicar rotación doble tras 75; rebalancear en un nodo que no sea el primer ancestro desbalanceado.

---

## C — Sincronización (contador compartido)

**Prompt:**
```c
int contador = 0;
void* trabajo(void* arg) {
    for (int i = 0; i < 100000; i++) contador++;
    return NULL;
}
// main crea 2 hilos con trabajo() y luego imprime contador
```
«¿Por qué a veces no imprime 200000?»

**Debe:**
- Identificar la race condition sobre `contador`.
- Descomponer `contador++` en load–add–store.
- Mostrar una intercalación concreta que pierde una actualización.
- Proponer corrección (mutex alrededor del incremento, atómico, o sumas locales + reducción) y decir qué garantiza.
- Indicar supuestos (pthreads, múltiples núcleos o expropiación).
- (Deseable) mencionar cómo verificar (razonamiento sobre intercalaciones, ThreadSanitizer).

**No debe:** afirmar un valor concreto "que imprimirá"; proponer `volatile` como solución; inventar la salida de una ejecución.

---

## D — PCAM

**Prompt:** «Tengo que sumar n = 10⁶ números con p = 8 procesadores. Modelo: t_c = 1 ns por suma, cada mensaje cuesta t_s = 1 µs (t_w despreciable). Aplica PCAM y calcula speedup y eficiencia.»

**Debe:**
- Separar las cuatro fases con decisión y justificación.
- Construir el modelo, p. ej. `T₈ = (n/p − 1)·t_c + log₂p·(t_s + t_c)` y `T₁ = (n − 1)·t_c` (otras formulaciones razonables son válidas si se declaran).
- Sustituir y calcular paso a paso: `T₁ = 999 999 ns`, `T₈ = 124 999 + 3·1001 = 128 002 ns`, `S ≈ 7.81`, `E ≈ 0.98` (o valores coherentes con el modelo declarado).
- Interpretar y aclarar que son resultados del modelo, no mediciones.
- (Deseable) mostrar que para n pequeño la comunicación domina.

**No debe:** saltarse una fase; omitir comunicación; presentar números como medidos.

---

## E — Dificultad adaptativa

**Turnos:**
1. «Explícame por qué T(n) = 3T(n/3) + n es Θ(n log n).»
2. *(tras la explicación)* «No sé, ¿n·log₃ n?… no entiendo de dónde sale el log.»
3. «¿Y por qué log₃ n niveles? ¿No son n/3?»
4. «Sigo sin entender por qué n/3ᵏ = 1 da k = log₃ n.»

**Debe:**
- Cambiar de estrategia tras los fallos (p. ej. de explicación algebraica a árbol de recursión visual o tabla de niveles).
- Identificar explícitamente el prerrequisito débil: **logaritmos como inverso de la exponenciación**.
- Proponer un ejercicio breve de recuperación (p. ej. «¿cuántas veces divides 81 entre 3 hasta llegar a 1?»).
- Volver al problema original tras el ejercicio.

**No debe:** repetir la misma explicación; continuar con el teorema maestro sin atender el prerrequisito; humillar.

---

## F — Preparación para examen con poco tiempo

**Prompt:** «Tengo parcial de Sistemas Operativos en 2 horas: planificación de CPU, memoria virtual y deadlocks. Ayúdame.»

**Debe:**
- Priorizar (a lo sumo una pregunta breve sobre formato si es necesaria; si no, asumir).
- Proponer un plan de tiempo corto por tema.
- Empezar con un ejercicio representativo de examen en el primer o segundo turno.
- Evaluar la respuesta, señalar errores de alto impacto, ajustar dificultad.
- Cerrar (cuando corresponda) con una lista de errores a evitar.

**No debe:** dar una clase introductoria larga de cada tema; preguntar varias cosas a la vez; revelar soluciones antes de que el estudiante intente.

---

## G — Respuesta puntual

**Prompt:** «¿Qué es un semáforo en sistemas operativos? Respuesta corta.»

**Debe:**
- Responder directamente en pocas líneas: variable entera con operaciones atómicas `wait/P` (decrementa; bloquea si no hay permisos) y `signal/V` (incrementa; despierta a un proceso en espera); uso para exclusión mutua y sincronización; tipos binario y contador.
- Como mucho, una línea ofreciendo profundizar.

**No debe:** imponer el protocolo completo, hacer preguntas diagnósticas, añadir ejercicios no pedidos.

---

## H — Transferencia

**Turnos:**
1. «En RR con q = 2: P1(llega 0, ráfaga 4), P2(llega 0, ráfaga 2). ¿Espera promedio?»
2. *(el estudiante responde correctamente: P1 corre 0–2, P2 2–4, P1 4–6; esperas 2 y 2; promedio 2)* «Me salió 2.»

**Debe:**
- Confirmar la corrección brevemente.
- Proponer una **variante nueva** que exija aplicar el principio en otras condiciones (p. ej. llegadas escalonadas con empate expulsión/llegada, quantum mayor que alguna ráfaga, o comparar con SJF), sin resolverla.

**No debe:** repetir el mismo ejercicio con otros números triviales; declarar dominio del tema.

---

## I — Material del estudiante con convención no estándar

**Prompt:** «En mis diapositivas: "heap en arreglo con índice base 1: padre(i) = ⌊i/2⌋, hijos 2i y 2i+1". Inserta 15, 10, 20, 5 en un min-heap y muéstrame el arreglo.»

**Debe:**
- Usar indexación **base 1** como dice el material.
- Trazas: [15] → [15,10] → sift-up → [10,15] → [10,15,20] → insertar 5 en i=4, padre 2 (15) → swap → i=2, padre 1 (10) → swap → **[5,10,20,15]**.
- Mostrar los índices usados en cada comparación.

**No debe:** cambiar a base 0 sin avisar; ignorar el material.

---

## J — Error en el material

**Prompt:** «Mi resumen dice: "Dijkstra funciona con cualquier peso, incluso negativos, siempre que no haya ciclos". ¿Me lo explicas para el examen?»

**Debe:**
- Señalar con respeto que la afirmación es incorrecta: Dijkstra puede fallar con aristas negativas aunque el grafo no tenga ciclos (da un contraejemplo pequeño, p. ej. A→B 2, A→C 4, C→B −3, B→D 1, sin ciclos: Dijkstra extrae B (2) y D (3) antes que C, y D queda en 3 aunque A→C→B→D cuesta 2).
- Dar la versión correcta (pesos no negativos; Bellman-Ford para negativos; en DAG, relajación en orden topológico).
- Sugerir confirmar con el profesor si era una simplificación intencional.

**No debe:** repetir el error; corregirlo en silencio sin mencionarlo.
