#!/usr/bin/env python3
"""Memory link checker: finds broken [[wiki-links]] and memory files
unreachable from the index chain (orphans). See constitution rule 4.

Usage: python3 tools/check-links.py [project-root]
Exit code: 0 = clean, 1 = broken links or orphans found
"""
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd()
SKIP_DIRS = {".git", ".obsidian", "node_modules", ".github"}

def skipped(p: Path) -> bool:
    return any(part in SKIP_DIRS for part in p.parts)

def is_template(p: Path) -> bool:
    # Files/folders starting with _ are templates; their placeholder links are not checked
    return any(part.startswith("_") for part in p.relative_to(ROOT).parts)

md_files = [p for p in ROOT.rglob("*.md") if not skipped(p)]

by_base = {}
by_rel = {}
for p in md_files:
    by_base.setdefault(p.stem.lower(), []).append(p)
    by_rel[p.relative_to(ROOT).as_posix()[:-3].lower()] = p

LINK = re.compile(r"\[\[([^\]|#]+)")

def resolve(target: str):
    # Escaped pipes in Markdown tables ([[target\|alias]]) leave a trailing backslash
    t = target.strip().rstrip("\\").strip().lower()
    if t.endswith(".md"):
        t = t[:-3]
    for rel, f in by_rel.items():
        if rel == t or rel.endswith("/" + t):
            return f
    cands = by_base.get(t.split("/")[-1])
    return cands[0] if cands else None

inbound = {p: 0 for p in md_files}
broken = []

for p in md_files:
    if is_template(p):
        continue
    text = p.read_text(encoding="utf-8", errors="ignore")
    text = re.sub(r"```.*?```", "", text, flags=re.S)   # fenced code blocks
    text = re.sub(r"`[^`\n]*`", "", text)                # inline code
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)   # comments
    for m in LINK.finditer(text):
        hit = resolve(m.group(1))
        if hit is not None:
            inbound[hit] += 1
        else:
            broken.append((p.relative_to(ROOT).as_posix(), m.group(1).strip()))

orphans = []
for p in md_files:
    rel = p.relative_to(ROOT).as_posix()
    if not rel.startswith("docs/memory/") or is_template(p):
        continue
    if rel == "docs/memory/index.md":  # root entry point
        continue
    # activeContext/ holds dynamic per-contributor files created at runtime;
    # they are ephemeral coordination state, not part of the durable graph.
    if rel.startswith("docs/memory/activeContext/"):
        continue
    if inbound[p] == 0:
        orphans.append(rel)

ok = True
if broken:
    ok = False
    print("BROKEN LINKS:")
    for src, tgt in broken:
        print(f"  {src}  →  [[{tgt}]]")
if orphans:
    ok = False
    print("ORPHAN FILES (no inbound links):")
    for rel in orphans:
        print(f"  {rel}")

if ok:
    print(f"OK — {len(md_files)} files scanned, no broken links or orphans.")
sys.exit(0 if ok else 1)
