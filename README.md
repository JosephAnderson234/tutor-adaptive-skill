# Adaptive CS Tutor

Skill de tutoría universitaria adaptativa para cursos de Ciencias de la
Computación (EDA y algoritmos avanzados, Sistemas Operativos, Concurrencia,
Computación Paralela y Distribuida, Arquitectura, Redes, Bases de Datos,
Ingeniería de Software, Sistemas de Programación).

La skill aporta el **método**: 8 perfiles pedagógicos combinables, un motor
de selección, diagnóstico de errores y evaluación del dominio. El
**contenido** lo pones tú: entrégale tu sílabo, diapositivas, apuntes o
exámenes pasados y enseñará con la notación y las convenciones de tu curso.
Sin material, usa conocimiento general y declara las convenciones que asume.

> Principio rector: no busca producir la explicación más impresionante, sino
> que el estudiante pueda razonar, resolver problemas y aplicar el
> conocimiento por su cuenta.

Usa el formato abierto **Agent Skills** (`SKILL.md` + archivos de referencia
que se cargan bajo demanda), así que funciona tal cual en cualquier agente
que admita skills. Para los que no las admiten se generan dos variantes:
un prompt de un solo archivo y una versión compacta.

---

## Contenido

```
adaptive-cs-tutor/
├── SKILL.md                      Núcleo: fuente del contenido, selector, protocolo, adaptación, calidad
├── reference/
│   ├── material-del-curso.md     Cómo interpretar el material del estudiante
│   ├── perfiles.md               Los 8 perfiles en detalle (A–H) y combinaciones
│   ├── selector.md               Señales → estrategia, nivel de ayuda, mapa de prerrequisitos
│   ├── evaluacion.md             Niveles 0–4, taxonomía de errores, exámenes, registro de progreso
│   ├── calidad.md                Lista de control, errores típicos del tutor, base pedagógica
│   └── cursos/                   Guías pedagógicas por disciplina (no son temarios)
│       ├── estructuras-datos-algoritmos.md
│       ├── sistemas-operativos.md
│       ├── concurrencia.md
│       ├── paralela-distribuida.md
│       ├── otros-cursos.md
│       └── _plantilla.md         Para añadir cursos nuevos
├── examples/                     Interacciones modelo (EDA, SO, Paralela)
├── tests/
│   ├── acceptance-tests.md       Pruebas A–J con criterios y valores de referencia
│   ├── scenarios.json            Las mismas pruebas en formato máquina
│   └── judge-prompt.md           Prompt para evaluar con un LLM juez
├── adapters/compact-prompt.md    Versión compacta (< 8000 caracteres)
├── scripts/
│   ├── validate.py               Valida la estructura y recalcula los valores de referencia
│   └── build_prompt.py           Genera dist/ (prompt de un solo archivo + .zip)
└── dist/                         Generado: adaptive-cs-tutor.md y adaptive-cs-tutor.zip
```

Los scripts solo usan la biblioteca estándar de Python 3.8+.

```bash
python scripts/validate.py       # comprueba que todo esté bien
python scripts/build_prompt.py   # regenera dist/
```

---

## ¿Qué variante uso?

| Tu agente… | Usa | Calidad |
|---|---|---|
| Admite Agent Skills (Claude Code, Claude.ai, Codex, Gemini CLI, Copilot, Cursor, OpenCode…) | La carpeta completa | ★★★ carga las referencias bajo demanda |
| Admite instrucciones largas + archivos adjuntos (Claude/ChatGPT Projects, Gems) | `dist/adaptive-cs-tutor.md` o `compact-prompt.md` + subir `reference/` | ★★☆ |
| Solo admite un system prompt (API, Ollama, LM Studio…) | `dist/adaptive-cs-tutor.md` | ★★☆ todo en contexto |
| Tiene un límite de caracteres en las instrucciones (Custom GPT: 8000) | `adapters/compact-prompt.md` | ★☆☆ núcleo sin anexos |

> **Las rutas de instalación cambian entre versiones de los agentes.** Las de
> abajo son las documentadas al crear la skill. Si tu agente no la detecta,
> revisa su documentación ("skills" / "agent skills") o usa el método
> universal (§10).

---

## 1. Claude Code (CLI, escritorio, IDE)

Personal (todos tus proyectos):
```bash
# macOS / Linux / Git Bash
mkdir -p ~/.claude/skills
cp -r adaptive-cs-tutor ~/.claude/skills/
```
```powershell
# Windows PowerShell
Copy-Item -Recurse adaptive-cs-tutor "$HOME\.claude\skills\"
```
Solo en un proyecto: copia la carpeta a `.claude/skills/adaptive-cs-tutor/`.

Uso: se activa sola con peticiones como "explícame…" o "tengo parcial…", o
de forma explícita con `/adaptive-cs-tutor`. Para pasarle material, menciona
los archivos con `@` (`@slides/semana5.pdf explícame las rotaciones`).

## 2. Claude.ai y Claude Desktop

1. `python scripts/build_prompt.py` → `dist/adaptive-cs-tutor.zip`.
2. *Settings → Capabilities → Skills → Upload skill* y elige el `.zip`
   (requiere un plan que incluya skills y la ejecución de código activada).
3. Actívala y empieza un chat. Adjunta tus PDFs o diapositivas en la conversación.

Alternativa con **Proyectos**: pega `dist/adaptive-cs-tutor.md` en las
instrucciones del proyecto y sube el material del curso como conocimiento.
Así el material queda disponible en todas las conversaciones del proyecto.

## 3. Claude API (Agent SDK / Skills API)

- **Agent SDK:** coloca la carpeta en `.claude/skills/` del directorio de
  trabajo del agente y habilita las skills en la configuración del SDK.
- **Messages API:** sube la skill (el `.zip`) con la API de Skills y
  referénciala en el contenedor. Si no, usa `dist/adaptive-cs-tutor.md` como
  `system` prompt.

## 4. OpenAI Codex (CLI / extensión IDE)

```bash
mkdir -p ~/.agents/skills && cp -r adaptive-cs-tutor ~/.agents/skills/
# en versiones anteriores de Codex: ~/.codex/skills/
```
Para un repositorio: `.agents/skills/adaptive-cs-tutor/`.
Uso: se activa sola por su descripción, o la mencionas con `$adaptive-cs-tutor`
(`/skills` lista las skills disponibles).

## 5. Gemini CLI

```bash
mkdir -p ~/.gemini/skills && cp -r adaptive-cs-tutor ~/.gemini/skills/
```
Para un proyecto: `.gemini/skills/adaptive-cs-tutor/`. Comprueba que aparezca
con `/skills list`.
Si tu versión no admite skills, importa el prompt desde `GEMINI.md`:
```markdown
@./adaptive-cs-tutor/dist/adaptive-cs-tutor.md
```

## 6. GitHub Copilot (VS Code, Copilot CLI, coding agent)

Para un repositorio: `.github/skills/adaptive-cs-tutor/`. Personal:
`~/.copilot/skills/adaptive-cs-tutor/`. Copilot también lee `.claude/skills/`.
Si tu versión no admite skills, crea un prompt reutilizable en
`.github/prompts/tutor.prompt.md` con el contenido de
`dist/adaptive-cs-tutor.md` e invócalo con `/tutor` en el chat.

## 7. Cursor

Para un proyecto: `.cursor/skills/adaptive-cs-tutor/` (versiones con soporte
de Agent Skills).
Si tu versión no las admite, crea una regla `.cursor/rules/adaptive-cs-tutor.mdc`:
```markdown
---
description: Tutor adaptativo de Ciencias de la Computación. Úsalo cuando el usuario quiera aprender, repasar o preparar exámenes de cursos de CS.
alwaysApply: false
---
<pega aquí el contenido de dist/adaptive-cs-tutor.md>
```

## 8. OpenCode

Personal: `~/.config/opencode/skills/adaptive-cs-tutor/`. Proyecto:
`.opencode/skills/adaptive-cs-tutor/`. OpenCode también detecta
`.claude/skills/`.

## 9. Windsurf, Cline, Roo, Continue y otros IDE con "reglas"

Crea una regla o instrucción de workspace con `adapters/compact-prompt.md`
(muchas reglas tienen límite de tamaño) y deja la carpeta `reference/` en el
proyecto. Pide al agente que lea `reference/...` cuando haga falta.

## 10. Método universal: ChatGPT, Gemini Gems, API o modelos locales

- **ChatGPT (Custom GPT):** en *Instructions* pega `adapters/compact-prompt.md`
  (límite de 8000 caracteres). En *Knowledge* sube los archivos de
  `reference/` y tu material del curso.
- **ChatGPT Projects / Gemini Gems / NotebookLM:** usa
  `dist/adaptive-cs-tutor.md` como instrucciones y sube tu material.
- **API de cualquier proveedor u Ollama / LM Studio:** usa
  `dist/adaptive-cs-tutor.md` como mensaje de sistema. En modelos con poco
  contexto, usa la versión compacta.

### Mantener una sola copia para varios agentes

Usa enlaces simbólicos para que todos los agentes lean la misma carpeta:
```bash
ln -s "$PWD/adaptive-cs-tutor" ~/.claude/skills/adaptive-cs-tutor
ln -s "$PWD/adaptive-cs-tutor" ~/.agents/skills/adaptive-cs-tutor
```
```powershell
# Windows: una junction no requiere permisos de administrador
New-Item -ItemType Junction -Path "$HOME\.claude\skills\adaptive-cs-tutor" -Target "$PWD\adaptive-cs-tutor"
```

---

## Cómo usarla

**1. Dale tu material (recomendado).** Adjunta o pega tu sílabo,
diapositivas, guías o exámenes pasados. La skill extrae los temas, los
objetivos, las definiciones y la notación (por ejemplo, si tu curso define
la altura de una hoja como 0, o qué regla de desempate usa en Round Robin) y
enseña dentro de ese marco. Si encuentra un error en el material, te lo
indica con respeto.

**2. Pide lo que necesitas.** El tutor ajusta la estrategia:

| Dices | Qué hace |
|---|---|
| "¿Qué es un semáforo? corto" | Respuesta directa, sin protocolo |
| "Explícame memoria virtual desde cero" | Protocolo completo: objetivo → modelo mental → ejemplo → práctica → transferencia |
| "Resuelve paso a paso esta recurrencia" | Laboratorio con todos los pasos intermedios |
| "¿Por qué mi código con hilos falla?" | Detective: te deja investigar y luego explica la causa raíz |
| "Demuéstrame que Dijkstra es correcto" | Socrático: una pregunta a la vez, con pistas |
| "¿Mutex o semáforo para esto?" | Debate con criterios y supuestos explícitos |
| "Tengo parcial en 2 horas" | Examen adaptativo priorizado |
| "Simula FIFO con 3 marcos" | Simulador por pasos con predicciones |
| "A ver si lo entendí: …" | Feynman: revisa tu explicación |

**3. Preferencias.** "Solo la respuesta", "sin preguntas", "más formal",
"en inglés": las respeta sin sacrificar la corrección técnica.

**4. Varias sesiones.** Si el agente no tiene memoria persistente, pide al
final "dame mi registro de progreso" y pégalo al empezar la próxima sesión.

Ejemplos completos en `examples/`.

---

## Pruebas

1. **Estructurales y de valores (automáticas):** `python scripts/validate.py`
   comprueba el frontmatter, las referencias, los perfiles y los escenarios,
   y **recalcula** con simuladores propios los valores de referencia de las
   pruebas y los ejemplos (recurrencia, rotaciones AVL, heap, Round Robin con
   ambas convenciones, speedup y el contraejemplo de Dijkstra).
2. **De comportamiento (con el agente):** ejecuta cada caso de
   `tests/acceptance-tests.md` en una sesión nueva. Puedes evaluar a mano o
   con `tests/judge-prompt.md` y un modelo juez. Las pruebas A–H son las de
   la especificación. I y J comprueban el uso del material del estudiante:
   respetar su convención y señalar un error.

## Añadir un curso

1. Copia `reference/cursos/_plantilla.md` a `reference/cursos/<curso>.md`.
2. Añade una fila en la tabla "Archivos de esta skill" de `SKILL.md`.
3. `python scripts/validate.py` y `python scripts/build_prompt.py`.

El núcleo pedagógico no se modifica.

---

## Limitaciones conocidas

- **Todo depende del modelo base.** La skill guía el comportamiento, pero no
  garantiza la corrección de cada cálculo. Los modelos pequeños pueden
  equivocarse en trazas largas.
- **Sin ejecución.** No ejecuta código ni simulaciones reales salvo que el
  agente tenga herramientas para ello. Los números son de modelos
  idealizados y así se etiquetan.
- **Memoria.** El modelo del estudiante vive dentro de la conversación. La
  continuidad entre sesiones depende del registro de progreso o de la
  memoria del agente.
- **Material extenso.** Los PDFs muy largos o escaneados dependen de la
  capacidad del agente para leerlos. Conviene entregar el material por temas.
- **Diagramas.** Son ASCII y tablas, para que funcionen en cualquier agente.
  No genera imágenes.
- **Niveles 0–4.** Son indicadores pedagógicos, no mediciones validadas.
- **Las pruebas de comportamiento no son deterministas.** Ejecútalas varias
  veces y con distintos modelos.

## Mejoras futuras

- Un script que ejecute `scenarios.json` contra una API y aplique el juez
  automáticamente.
- Herramientas opcionales para simular (planificadores, cachés, AVL) y
  verificar cálculos en vez de hacerlos a mano.
- Un registro de progreso persistente (archivo o memoria del agente) con
  calendario de repaso espaciado.
- Banco de ejercicios por curso, generado a partir del material del estudiante.
- Exportar diagramas a Mermaid o Graphviz cuando el agente pueda mostrarlos.
- Versión en inglés de la skill.
