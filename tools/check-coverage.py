#!/usr/bin/env python3
"""Memory coverage report: finds code areas with no module counterpart in memory.
Advisory only (exit code is always 0) — the module/directory mapping may not be 1:1.

Usage: python3 tools/check-coverage.py [project-root]
"""
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd()
MEM = ROOT / "docs" / "memory"

IGNORE = {
    ".git", ".github", ".obsidian", "docs", "tools", "node_modules",
    "dist", "build", "out", "target", "vendor", ".venv", "venv",
    "__pycache__", ".idea", ".vscode", "coverage",
}

# Modules in memory: folders under docs/memory that contain an index.md
modules = set()
if MEM.exists():
    for d in MEM.iterdir():
        if d.is_dir() and not d.name.startswith("_") and (d / "index.md").exists():
            modules.add(d.name.lower())

# Code areas: directories at the root (and under src/ if present)
def code_areas():
    areas = []
    for d in sorted(ROOT.iterdir()):
        if d.is_dir() and d.name not in IGNORE and not d.name.startswith("."):
            areas.append(d)
    src = ROOT / "src"
    if src.exists():
        for d in sorted(src.iterdir()):
            if d.is_dir() and d.name not in IGNORE and not d.name.startswith("."):
                areas.append(d)
    return areas

uncovered = []
for area in code_areas():
    name = area.name.lower()
    # does the area name match a module (exact or containment)?
    if not any(name == m or name in m or m in name for m in modules):
        uncovered.append(area.relative_to(ROOT).as_posix())

print(f"Modules in memory: {', '.join(sorted(modules)) if modules else '(none)'}")
if uncovered:
    print("\nWARNING — code areas with no module counterpart in memory:")
    for u in uncovered:
        print(f"  {u}/")
    print("\nThese areas should either be tied to a module or deliberately ignored.")
else:
    print("OK — every code area has a counterpart in memory.")
sys.exit(0)
