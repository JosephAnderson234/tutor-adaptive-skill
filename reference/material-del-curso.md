# Trabajar con el material del estudiante

La skill no trae un temario fijo. Cuando el estudiante comparte su material
(sílabo, diapositivas, apuntes, PDFs, guías de ejercicios, exámenes pasados,
código, enunciados de laboratorio), ese material define **qué** se enseña y
**con qué notación**. La skill define **cómo** se enseña.

## 1. Ingesta: qué extraer

Lee el material (o las partes relevantes si es extenso) y construye
internamente un **mapa del curso**:

| Elemento | Qué buscar |
|---|---|
| Curso y nivel | Nombre, ciclo, prerrequisitos declarados, lenguaje de programación usado |
| Temas | Unidades/semanas, en el orden del curso |
| Objetivos | Resultados de aprendizaje; reescríbelos como acciones observables |
| Definiciones | Cómo define el material cada concepto clave (literal si importa) |
| Notación y convenciones | Índices base 0/1, altura de hoja 0 o 1, signo del factor de balance, unidades, pseudocódigo propio, desempates en simulaciones, fórmulas con nombres propios del profesor |
| Procedimientos | Pasos tal como el curso los enseña (p. ej. un formato concreto de tabla de planificación) |
| Ejemplos y ejercicios | Resueltos y propuestos; sirven para calibrar dificultad |
| Evaluación | Formato de examen, tipos de preguntas, pesos, fechas si aparecen |
| Huecos | Temas mencionados pero no desarrollados |

No hace falta mostrar el mapa completo. Muestra un **resumen breve** (3–6
líneas) solo si ayuda: al iniciar una sesión de estudio larga o si el
estudiante lo pide. Para una pregunta puntual sobre el material, responde
directamente.

## 2. Reglas de interpretación

1. **Notación del material primero.** Si el material usa `bf = h(der) − h(izq)`,
   enseña con esa convención aunque la habitual sea la contraria. Si en algún
   momento conviene mencionar la otra (porque aparecerá en libros), hazlo
   aparte y marcado.
2. **Alcance del material.** No introduzcas temas avanzados que el curso no
   cubre salvo que el estudiante lo pida o sean imprescindibles para entender
   algo del temario. Si lo haces, señala que está fuera del temario.
3. **Nivel del material.** Calibra la formalidad (demostraciones, notación
   matemática) al nivel que muestra el material y los ejercicios.
4. **Cita el material.** Cuando te apoyes en él, indica de dónde ("según la
   diapositiva 14", "en la guía 3, ejercicio 2"). No le atribuyas cosas que
   no dice.
5. **Material incompleto o ambiguo.** Completa con conocimiento general y dilo
   explícitamente. Si la ambigüedad cambia el resultado (p. ej. desempates en
   Round Robin), pregunta una vez o resuelve con la convención más común
   declarándola.
6. **Errores en el material.** Si una definición, fórmula o solución está mal,
   no la repitas ni la corrijas en silencio: indica el problema, da la versión
   correcta con su justificación y sugiere confirmarlo con el profesor. Sé
   respetuoso; a veces es una simplificación intencional: dilo si es el caso.
7. **Material vs. conocimiento general en conflicto** (sin que sea un error,
   p. ej. una definición más restrictiva): el material manda para los
   ejercicios del curso; menciona la diferencia una vez.

## 3. Uso del material en cada perfil

| Perfil | Cómo aprovechar el material |
|---|---|
| Visual | Reproduce sus diagramas en el mismo formato o explica los que trae |
| Laboratorio | Usa sus ejemplos resueltos como paso 1 y sus ejercicios propuestos como práctica |
| Detective | Toma su código o laboratorios e introduce/encuentra fallos plausibles |
| Socrático | Parte de sus definiciones y teoremas tal como están escritos |
| Debate | Usa las alternativas que el curso presenta, con sus criterios |
| Examen | Imita el formato y la dificultad de sus exámenes pasados; **no** afirmes que una pregunta "saldrá en el examen" |
| Simulador | Usa los parámetros y convenciones de sus enunciados |
| Feynman | Compara la explicación del estudiante con las definiciones del material |

## 4. Exámenes pasados y guías

- Úsalos para detectar los **tipos** de pregunta y los temas con más peso.
- Genera ejercicios **nuevos** del mismo tipo para practicar; reserva los
  originales para simulacros si el estudiante lo pide.
- Si el estudiante pide la solución de un ejercicio del curso, ofrécele
  primero intentarlo (salvo que solo quiera verificar su respuesta).

## 5. Sin material

Enseña con conocimiento general de CS, declara las convenciones que asumes
y, una sola vez, ofrece adaptarte si comparte su sílabo o diapositivas. No
condiciones la ayuda a recibir material.

## 6. Material extenso

Si el material es largo (un curso completo), no intentes resumirlo todo de
golpe. Construye el índice de temas, pregunta (o infiere) en qué tema o
evaluación quiere enfocarse y profundiza solo en esas partes.
