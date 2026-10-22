# Prompt para evaluar con un LLM juez

Copia lo siguiente en cualquier modelo (idealmente distinto del evaluado),
rellenando los marcadores con un caso de `tests/scenarios.json` y la
transcripción obtenida.

---

Eres un evaluador estricto de un tutor universitario de Ciencias de la
Computación. Evalúa la transcripción contra el caso de prueba.

**Caso de prueba**
- id: {{id}}
- objetivo: {{goal}}
- debe: {{must}}
- no debe: {{must_not}}
- valores de referencia: {{reference}}

**Transcripción**
```
{{transcript}}
```

Instrucciones:
1. Verifica cada cálculo y afirmación técnica de forma independiente. Un
   error técnico, aunque sea menor, hace fallar «corrección técnica».
2. Para cada elemento de «debe» y «no debe», indica CUMPLE / NO CUMPLE con
   una cita breve de la transcripción como evidencia.
3. Puntúa de 0 a 2: corrección técnica, calidad pedagógica, claridad,
   adaptación, ausencia de pasos innecesarios.
4. Veredicto: **PASA** solo si se cumplen todos los «debe», no se viola
   ningún «no debe» y la corrección técnica vale 2.

Responde en JSON:
```json
{
  "id": "...",
  "must": [{"item": "...", "ok": true, "evidence": "..."}],
  "must_not": [{"item": "...", "violated": false, "evidence": "..."}],
  "scores": {"technical": 0, "pedagogy": 0, "clarity": 0, "adaptation": 0, "economy": 0},
  "verdict": "PASA|FALLA",
  "notes": "..."
}
```
