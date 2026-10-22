#!/usr/bin/env python3
"""Genera los artefactos de distribución en dist/.

- dist/adaptive-cs-tutor.md   Prompt de un solo archivo (SKILL.md + referencias),
                              para agentes sin soporte de skills.
- dist/adaptive-cs-tutor.zip  Carpeta de la skill lista para subir (Claude.ai, etc.).

Uso: python scripts/build_prompt.py
"""
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
REFERENCE_ORDER = [
    "reference/material-del-curso.md",
    "reference/perfiles.md",
    "reference/selector.md",
    "reference/evaluacion.md",
    "reference/calidad.md",
    "reference/cursos/estructuras-datos-algoritmos.md",
    "reference/cursos/sistemas-operativos.md",
    "reference/cursos/concurrencia.md",
    "reference/cursos/paralela-distribuida.md",
    "reference/cursos/otros-cursos.md",
]
PACKAGE = ["SKILL.md", "README.md", "reference", "examples"]


def build_single_file():
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    body = re.sub(r"^---\n.*?\n---\n", "", skill, flags=re.S)
    parts = [
        "<!-- Generado por scripts/build_prompt.py. No editar: edita SKILL.md y reference/. -->",
        body.strip(),
        "\n---\n\n# Anexos\n\nLos archivos `reference/...` mencionados arriba están "
        "incluidos a continuación como anexos. Consulta solo el que necesites.",
    ]
    for rel in REFERENCE_ORDER:
        text = (ROOT / rel).read_text(encoding="utf-8").strip()
        text = re.sub(r"^(#+)", r"#\1", text, flags=re.M)  # bajar un nivel los títulos
        parts.append(f"\n---\n\n## Anexo `{rel}`\n\n{text}")
    out = DIST / "adaptive-cs-tutor.md"
    out.write_text("\n\n".join(parts) + "\n", encoding="utf-8")
    return out


def build_zip():
    out = DIST / "adaptive-cs-tutor.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for item in PACKAGE:
            path = ROOT / item
            files = [path] if path.is_file() else sorted(p for p in path.rglob("*") if p.is_file())
            for f in files:
                z.write(f, Path(ROOT.name) / f.relative_to(ROOT))
    return out


if __name__ == "__main__":
    DIST.mkdir(exist_ok=True)
    for out in (build_single_file(), build_zip()):
        print(f"{out.relative_to(ROOT)}  ({out.stat().st_size:,} bytes)")
