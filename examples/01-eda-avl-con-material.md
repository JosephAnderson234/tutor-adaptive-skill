# Ejemplo — Estructuras de Datos: AVL con la convención del curso

> Interacción modelo. Muestra cómo la skill adopta la notación del material
> del estudiante, enseña con Visual → Laboratorio y reacciona a un error.

---

**Estudiante:** *(pega un fragmento de sus diapositivas)*
> "Diap. 12 — Altura: h(hoja) = 0, h(∅) = −1. Factor de balance:
> FB(x) = h(der) − h(izq). Un árbol es AVL si FB ∈ {−1, 0, 1} en todo nodo."

No entiendo las rotaciones. En la guía me piden insertar 30, 20, 10, 25, 28.

**Tutor:**
Uso la convención de tu diapositiva 12: hoja con altura 0 y
**FB = h(der) − h(izq)**, así que FB negativo = cargado a la izquierda.
(Ojo: muchos libros usan el signo contrario; en tu curso vale este.)

Objetivo: insertar, localizar el primer nodo con |FB| = 2 y elegir la
rotación justificando el caso.

**Insertar 30, 20, 10 (como en un BST):**
```
30  h=2  FB = −1 − 1 = −2   ← primer nodo desbalanceado
 /
20  h=1  FB = −1 − 0 = −1
 /
10  h=0
```
30 y su hijo izquierdo están cargados hacia el **mismo** lado (izquierda):
caso **izquierda-izquierda** → una **rotación simple a la derecha** en 30.
```
     20 (FB 0)
    /  \
  10    30
```
Por qué funciona: 20 sube y 30 baja a su derecha; el orden BST se mantiene
(10 < 20 < 30) y la altura del subárbol vuelve a 1.

**Insertar 25:** 25 > 20 → derecha; 25 < 30 → hijo izquierdo de 30.
FB(30) = −1 − 0 = −1, FB(20) = 1 − 0 = +1. Sigue siendo AVL.

Tu turno, un solo paso: **inserta 28. ¿Dónde queda y cuál es el primer nodo,
subiendo desde 28, con |FB| = 2?**

---

**Estudiante:** Queda a la derecha de 25. El desbalanceado es 20, entonces roto 20 a la izquierda.

**Tutor:**
La posición es correcta: 28 > 25 → hijo derecho de 25. ✔

El nodo no. Subamos revisando **cada** ancestro:
- 25: h(der) = 0, h(izq) = −1 → FB = +1 ✔
- 30: h(der) = −1, h(izq) = h(25) = 1 → **FB = −2** ✘ ← primero desbalanceado
- 20 ya no se mira: se rebalancea en el primer ancestro desbalanceado.

Error procedimental (saltaste a la raíz). Pista: 30 está cargado a la
**izquierda** (−2), pero su hijo 25 está cargado a la **derecha** (+1).
¿Qué caso es y qué rotaciones implica?

**Estudiante:** Izquierda-derecha: primero rotación a la izquierda en 25 y luego a la derecha en 30.

**Tutor:**
Exacto.
```
izq en 25:          der en 30:
     30                  28
    /                   /  \
   28        →        25    30
  /
 25
```
Árbol final: `20(10, 28(25, 30))`.
Verificación con tu convención: FB(20) = h(28) − h(10) = 1 − 0 = +1;
FB(28) = 0; hojas 0. ✔ AVL.

Transferencia, sin pistas: **en un AVL vacío inserta 10, 30, 20. ¿Qué caso
aparece y cuál es el árbol final?**
