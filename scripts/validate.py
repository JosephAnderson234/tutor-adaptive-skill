#!/usr/bin/env python3
"""Valida la estructura de la skill y los valores de referencia de las pruebas.

Uso: python scripts/validate.py
Solo usa la biblioteca estándar. Sale con código 1 si algo falla.
"""
import json
import re
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []


def check(cond, msg):
    if not cond:
        errors.append(msg)


# ---------------------------------------------------------------- estructura

def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    fields = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            v = v.strip()
            if len(v) >= 2 and v[0] == v[-1] and v[0] in "'\"":
                v = v[1:-1]
            else:
                # YAML plano no admite ": " ni " #" dentro del valor (GitHub y los agentes fallan al parsear)
                check(": " not in v and " #" not in v, f"frontmatter '{k.strip()}': entrecomilla el valor (contiene ': ' o ' #')")
            fields[k.strip()] = v
    return fields


def check_structure():
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    fm = frontmatter(skill)
    check(fm.get("name") == ROOT.name, f"name del frontmatter ({fm.get('name')}) != carpeta ({ROOT.name})")
    check(re.fullmatch(r"[a-z0-9-]{1,64}", fm.get("name", "")), "name debe ser kebab-case de máx. 64 caracteres")
    desc = fm.get("description", "")
    check(0 < len(desc) <= 1024, f"description debe tener 1–1024 caracteres (tiene {len(desc)})")

    for rel in sorted(set(re.findall(r"`((?:reference|examples)/[^`]*)`", skill))):
        check((ROOT / rel).exists(), f"SKILL.md referencia un archivo inexistente: {rel}")

    perfiles = (ROOT / "reference/perfiles.md").read_text(encoding="utf-8")
    for letter in "ABCDEFGH":
        check(re.search(rf"^## {letter}\. ", perfiles, re.M), f"falta el perfil {letter} en perfiles.md")

    cursos = ROOT / "reference/cursos"
    for f in cursos.glob("*.md"):
        if f.name.startswith("_") or f.name == "otros-cursos.md":
            continue
        check(f"reference/cursos/{f.name}" in skill, f"curso no registrado en SKILL.md: {f.name}")

    check(len(list((ROOT / "examples").glob("*.md"))) >= 3, "se esperan al menos 3 ejemplos")

    scenarios = json.loads((ROOT / "tests/scenarios.json").read_text(encoding="utf-8"))
    ids = {s["id"][0] for s in scenarios}
    check(set("ABCDEFGHIJ") <= ids, f"faltan escenarios: {sorted(set('ABCDEFGHIJ') - ids)}")
    for s in scenarios:
        for key in ("goal", "turns", "must", "must_not"):
            check(s.get(key), f"escenario {s.get('id')} sin '{key}'")

    compact = (ROOT / "adapters/compact-prompt.md").read_text(encoding="utf-8")
    check(len(compact) <= 8000, f"compact-prompt.md supera 8000 caracteres ({len(compact)})")


# ------------------------------------------------- valores de referencia

def recurrence(n):  # T(n) = 2T(n/2) + n², T(1) = 1
    return 1 if n == 1 else 2 * recurrence(n // 2) + n * n


class Node:
    def __init__(self, k):
        self.k, self.l, self.r, self.h = k, None, None, 1


def h(n):
    return n.h if n else 0


def upd(n):
    n.h = 1 + max(h(n.l), h(n.r))


def rot_r(z):
    y = z.l
    z.l, y.r = y.r, z
    upd(z)
    upd(y)
    return y


def rot_l(z):
    y = z.r
    z.r, y.l = y.l, z
    upd(z)
    upd(y)
    return y


def avl_insert(n, k, log):
    if not n:
        return Node(k)
    if k < n.k:
        n.l = avl_insert(n.l, k, log)
    else:
        n.r = avl_insert(n.r, k, log)
    upd(n)
    bf = h(n.l) - h(n.r)
    if bf > 1:
        case = "LL" if h(n.l.l) >= h(n.l.r) else "LR"
        log.append((k, n.k, case))
        if case == "LR":
            n.l = rot_l(n.l)
        return rot_r(n)
    if bf < -1:
        case = "RR" if h(n.r.r) >= h(n.r.l) else "RL"
        log.append((k, n.k, case))
        if case == "RL":
            n.r = rot_r(n.r)
        return rot_l(n)
    return n


def show(n):
    if not n:
        return "-"
    if not n.l and not n.r:
        return str(n.k)
    return f"{n.k}({show(n.l)},{show(n.r)})"


def heap_base1(keys):
    a = [0]  # posición 0 sin usar: índices base 1
    for k in keys:
        a.append(k)
        i = len(a) - 1
        while i > 1 and a[i // 2] > a[i]:
            a[i // 2], a[i] = a[i], a[i // 2]
            i //= 2
    return a[1:]


def round_robin(procs, q, preempted_first):
    """procs: lista (nombre, llegada, ráfaga). Devuelve {nombre: fin}."""
    rem = {p: b for p, _, b in procs}
    arrivals = sorted(procs, key=lambda x: x[1])
    t, queue, done, i = 0, [], {}, 0

    def admit(upto):
        nonlocal i
        while i < len(arrivals) and arrivals[i][1] <= upto:
            queue.append(arrivals[i][0])
            i += 1

    admit(t)
    while len(done) < len(procs):
        if not queue:
            t = arrivals[i][1]
            admit(t)
            continue
        p = queue.pop(0)
        run = min(q, rem[p])
        t += run
        rem[p] -= run
        if rem[p] == 0:
            done[p] = t
            admit(t)
        elif preempted_first:
            admit(t - 1)  # llegadas estrictamente anteriores a t
            queue.append(p)
            admit(t)
        else:
            admit(t)
            queue.append(p)
    return done


def dijkstra_naive(graph, src):
    dist, settled = {src: 0}, set()
    while len(settled) < len(dist):
        u = min((d, v) for v, d in dist.items() if v not in settled)[1]
        settled.add(u)
        for v, w in graph.get(u, []):
            if v not in settled and dist[u] + w < dist.get(v, float("inf")):
                dist[v] = dist[u] + w
    return dist


def check_reference_values():
    check(recurrence(2) == 6 and recurrence(4) == 28, "Prueba A: T(2), T(4)")
    check(all(recurrence(2 ** k) == 2 * 4 ** k - 2 ** k for k in range(12)), "Prueba A: T(n) = 2n² − n")

    log, root = [], None
    for k in [50, 40, 60, 70, 80, 75]:
        root = avl_insert(root, k, log)
    check(log == [(80, 60, "RR"), (75, 50, "RR")], f"Prueba B: rotaciones {log}")
    check(show(root) == "70(50(40,60),80(75,-))", f"Prueba B: árbol final {show(root)}")

    log, root = [], None
    for k in [30, 20, 10, 25, 28]:
        root = avl_insert(root, k, log)
    check(show(root) == "20(10,28(25,30))", f"Ejemplo 01: árbol final {show(root)}")
    check([c for *_, c in log] == ["LL", "LR"], f"Ejemplo 01: casos {log}")

    check(heap_base1([15, 10, 20, 5]) == [5, 10, 20, 15], "Prueba I: heap base 1")

    procs = [("P1", 0, 5), ("P2", 1, 3), ("P3", 2, 1)]
    check(round_robin(procs, 2, True) == {"P3": 7, "P2": 8, "P1": 9}, "Ejemplo 02: RR expulsado primero")
    check(round_robin(procs, 2, False) == {"P3": 5, "P2": 8, "P1": 9}, "Ejemplo 02: RR llegada primero")
    fin = round_robin([("P1", 0, 4), ("P2", 0, 2)], 2, False)
    check(Fraction((fin["P1"] - 4) + (fin["P2"] - 2), 2) == 2, "Prueba H: espera promedio 2")

    t1, t8 = 10 ** 6 - 1, (10 ** 6 // 8 - 1) + 3 * (1000 + 1)
    check(t8 == 128002 and round(t1 / t8, 2) == 7.81 and round(t1 / t8 / 8, 3) == 0.977, "Prueba D: speedup")

    n, tc, ts, tw = 2 ** 20, 2, 5000, 10
    for p, lg, s, e in [(16, 4, 13.88, 0.867), (64, 6, 33.38, 0.522)]:
        tp = n // p * tc + lg * (ts + tw)
        check(round(n * tc / tp, 2) == s and round(n * tc / tp / p, 3) == e, f"Ejemplo 03: p={p}")

    g = {"A": [("B", 2), ("C", 4)], "C": [("B", -3)], "B": [("D", 1)]}
    check(dijkstra_naive(g, "A")["D"] == 3, "Prueba J: Dijkstra debería fallar (D=3, real 2)")


if __name__ == "__main__":
    getattr(sys.stdout, "reconfigure", lambda **_: None)(encoding="utf-8")
    check_structure()
    check_reference_values()
    if errors:
        print("FALLA")
        for e in errors:
            print(" -", e)
        sys.exit(1)
    print("OK: estructura y valores de referencia verificados")
