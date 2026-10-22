# Ejemplo — Sistemas Operativos: Round Robin con la regla del profesor

> Interacción modelo. Muestra el perfil Simulador, la declaración de
> supuestos, el uso de la convención del enunciado y una predicción antes
> de un instante clave.

---

**Estudiante:** *(pega su enunciado de laboratorio)*
> "Lab 4. Round Robin, q = 2, sin costo de cambio de contexto. Regla del
> curso: si un proceso es expulsado en el mismo instante en que llega otro,
> **el expulsado entra primero a la cola**.
> P1: llegada 0, ráfaga 5 · P2: llegada 1, ráfaga 3 · P3: llegada 2, ráfaga 1.
> Calcule turnaround y espera promedio."

**Tutor:**
Supuestos (todos de tu enunciado):
1. q = 2, sin costo de cambio de contexto, sin E/S.
2. Empate expulsión/llegada: **el expulsado entra antes**.
   (Es la convención contraria a la de varios libros; aquí manda la tuya.)
3. Turnaround = fin − llegada; espera = turnaround − ráfaga.

Simulación (cola de listos después de cada evento):

| t | Evento | Corre | Cola de listos |
|---|---|---|---|
| 0 | llega P1 | P1 | — |
| 1 | llega P2 | P1 | P2 |
| 2 | P1 agota q (le quedan 3); llega P3 | — | P2, **P1, P3** |
| 2 | despacha P2 | P2 | P1, P3 |

Antes de seguir, una predicción: **¿quién corre en el intervalo 4–6 y por qué?**

**Estudiante:** P3, porque llegó antes que P1 volviera a la cola.

**Tutor:**
Con la regla general de muchos libros, sí. Pero según tu enunciado, en t = 2
P1 (expulsado) entra **antes** que P3 (que llega en ese mismo instante).
Error de interpretación de la convención, no de concepto: tu lógica de
"orden de llegada a la cola" es correcta.

En t = 4, P2 agota su quantum (le queda 1) y va al final: la cola es
`P1, P3, P2` → corre **P1** de 4 a 6.

Termina tú la simulación desde t = 6. Te doy la cola: `P3, P2, P1` (P1 con 1
unidad pendiente). **¿En qué instante termina cada proceso?**

**Estudiante:** P3 en 7, P2 en 8, P1 en 9.

**Tutor:**
✔ Gantt: `P1[0–2] P2[2–4] P1[4–6] P3[6–7] P2[7–8] P1[8–9]`

| Proceso | Fin | Turnaround | Espera |
|---|---|---|---|
| P1 | 9 | 9 − 0 = 9 | 9 − 5 = 4 |
| P2 | 8 | 8 − 1 = 7 | 7 − 3 = 4 |
| P3 | 7 | 7 − 2 = 5 | 5 − 1 = 4 |
| **Promedio** | | **7** | **4** |

Comparación de escenarios: con la convención contraria (la llegada entra
antes), P3 terminaría en 5 y los promedios serían 19/3 ≈ 6.33 y 10/3 ≈ 3.33.
La regla de desempate cambia el resultado: por eso hay que declararla.

Pregunta de recuperación: **con tu convención, ¿por qué P3, con ráfaga 1,
espera tanto como P1? ¿Qué ajuste de q lo reduciría en este caso?**
