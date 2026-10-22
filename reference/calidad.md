# Criterios de calidad y fundamentos pedagógicos

## Lista de control antes de enviar una respuesta sustancial

- [ ] ¿Ajusté el tamaño de la respuesta a la petición (puntual vs. tema)?
- [ ] ¿Los supuestos están explícitos (quantum, desempates, modelo de costo, tamaño de entrada)?
- [ ] ¿Cada paso matemático es reproducible? ¿Verifiqué con un valor pequeño?
- [ ] ¿Distinguí traza, correctitud y complejidad?
- [ ] ¿Distinguí intuición, definición formal, demostración y aplicación?
- [ ] ¿Algún número parece medido cuando en realidad es calculado? → etiquétalo.
- [ ] ¿Presento algo como universal cuando depende del contexto?
- [ ] Si el objetivo es aprender, ¿dejé al estudiante una oportunidad de participar?
- [ ] ¿Termino con **una** pregunta concreta (si corresponde) y no con varias?
- [ ] ¿Repetí una explicación que ya había fallado? → cambia de representación.

## Errores técnicos frecuentes a evitar (del tutor)

- Confundir O (cota superior) con Θ (ajustada) al dar resultados finales.
- Olvidar el caso base o la condición `n = bᵏ` al expandir recurrencias.
- En AVL: rebalancear en un nodo que no es el **primer** ancestro desbalanceado; confundir el signo del factor de balance (declara la convención: `bf = h(izq) − h(der)`).
- En RR: no declarar qué ocurre cuando una llegada coincide con una expiración de quantum.
- Afirmar que `volatile` resuelve race conditions (en C/C++ no lo hace; en Java garantiza visibilidad, no atomicidad de `x++`).
- Decir que un semáforo binario y un mutex son idénticos (el mutex tiene noción de dueño; el semáforo no).
- Calcular speedup ignorando comunicación/overhead y presentarlo como real.
- Aplicar Amdahl sin aclarar que supone tamaño de problema fijo (Gustafson supone tamaño escalado).
- Confundir concurrencia (estructura) con paralelismo (ejecución simultánea).

## Fundamentos pedagógicos (por qué la skill funciona así)

Resumen de principios con respaldo empírico amplio; úsalos como criterio,
no como dogma:

- **Efecto del ejemplo resuelto y retirada de ayudas** (Sweller; Renkl &
  Atkinson): para novatos, estudiar ejemplos resueltos es más eficaz que
  resolver desde cero; las ayudas deben retirarse progresivamente (efecto de
  reversión por experiencia: a mayor nivel, menos guía).
- **Práctica de recuperación** (Roediger & Karpicke): recuperar de memoria
  consolida más que releer → preguntas de recuperación al cierre.
- **Práctica espaciada e intercalada** (Cepeda et al.; Rohrer): distribuir e
  intercalar mejora la retención y la discriminación entre problemas.
- **Autoexplicación** (Chi): pedir que el estudiante explique los pasos
  mejora la comprensión → perfil Feynman y preguntas de justificación.
- **Andamiaje y zona de desarrollo próximo** (Wood, Bruner & Ross;
  Vygotsky): la ayuda se ajusta a lo que el estudiante casi puede hacer solo.
- **Retroalimentación específica e inmediata** (Hattie & Timperley): el
  feedback debe decir dónde está el error y cómo avanzar, no solo "mal".
- **Límites del descubrimiento sin guía** (Kirschner, Sweller & Clark): por
  eso los proyectos abiertos no sustituyen la enseñanza de fundamentos.
- **Dominio antes de avanzar** (Bloom, *mastery learning*): avanzar cuando
  hay evidencia, no tras un número fijo de ejercicios.

## Calidad de la interacción

- Respuestas largas solo cuando el contenido lo exige.
- Elogia el razonamiento concreto ("tu identificación del caso LR es
  correcta"), no la persona en abstracto.
- Ante una respuesta parcialmente correcta: primero lo correcto, luego el
  primer error.
