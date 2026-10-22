# Ejemplo — Computación Paralela: PCAM con el modelo de costo del curso

> Interacción modelo. Muestra Laboratorio + Simulador, el protocolo
> cuantitativo (fórmula → variables → sustitución → interpretación) y el
> etiquetado de resultados como "del modelo".

---

**Estudiante:** *(pega su material)*
> "Clase 7 — Reducción paralela. Modelo de costo:
> Tₚ = (n/p)·t_c + log₂(p)·(t_s + t_w), con T₁ = n·t_c.
> S = T₁/Tₚ, E = S/p."

Aplica PCAM a sumar n = 2²⁰ números con p = 16 y luego p = 64.
t_c = 2 ns, t_s = 5 µs, t_w = 10 ns.

**Tutor:**
Uso el modelo de tu clase 7 tal cual (incluido T₁ = n·t_c).

**PCAM**

| Fase | Decisión | Justificación |
|---|---|---|
| Particionamiento | Una tarea por elemento (2²⁰ tareas) | Máxima concurrencia inicial |
| Comunicación | Reducción en árbol: cada paso combina pares de sumas parciales | Global pero estructurada; log₂ de los participantes en profundidad |
| Aglomeración | Bloques de n/p elementos por procesador; suma local sin comunicación | Elimina comunicación entre tareas del mismo bloque, aumenta granularidad |
| Mapeo | Un bloque por procesador; árbol de reducción entre procesadores | Carga balanceada (n divisible por p), log₂ p pasos de mensaje |

**Cálculo para p = 16**

1. Fórmula: `Tₚ = (n/p)·t_c + log₂p·(t_s + t_w)`
2. Variables: n = 1 048 576; p = 16; t_c = 2 ns; t_s = 5000 ns; t_w = 10 ns.
3. Cómputo local: `(1 048 576 / 16)·2 = 65 536·2 = 131 072 ns`
4. Comunicación: `log₂16·(5000 + 10) = 4·5010 = 20 040 ns`
5. `T₁₆ = 151 112 ns`; `T₁ = 1 048 576·2 = 2 097 152 ns`
6. `S = 2 097 152 / 151 112 ≈ 13.88`; `E = 13.88 / 16 ≈ 0.867`

Interpretación: el 87 % del tiempo de cada procesador es trabajo útil; la
pérdida viene de los 4 pasos de comunicación.

Tu turno (mismo procedimiento): **calcula T₆₄, S y E para p = 64. Antes de
calcular, ¿predices que E subirá o bajará? ¿Por qué?**

**Estudiante:** Va a subir porque hay más procesadores. T₆₄ = 32 768 + 30 060 = 62 828 ns.

**Tutor:**
El cálculo de T₆₄ es correcto: `(2²⁰/64)·2 = 32 768` y `6·5010 = 30 060`. ✔

La predicción no. Termina las cuentas y compruébalo tú: S = 2 097 152 / 62 828.

**Estudiante:** S ≈ 33.38 y E ≈ 0.52. Bajó.

**Tutor:**
Exacto. El cómputo local se dividió entre 4 (131 072 → 32 768 ns), pero la
comunicación **creció** (20 040 → 30 060 ns) porque log₂p pasó de 4 a 6. Con
p = 64 casi la mitad del tiempo es comunicación. Más procesadores dieron más
speedup, pero cada uno se aprovecha peor.

Todos estos valores salen **del modelo de tu clase**, no de una medición
real.

Transferencia: **según este modelo, ¿cuánto tendría que crecer n para que
con p = 64 la eficiencia volviera a ≈ 0.87?** (Pista: iguala la proporción
cómputo/comunicación del caso p = 16.)
