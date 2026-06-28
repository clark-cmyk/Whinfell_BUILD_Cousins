"""Shared helpers to prove China Policy track isolation from Global score logic."""

from __future__ import annotations

import ast
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
PKG_ROOT = Path(__file__).resolve().parent

# Production modules scanned for forbidden Global-score dependencies.
PRODUCTION_MODULES: tuple[str, ...] = (
    "__init__.py",
    "version.py",
    "models.py",
    "schema.py",
    "data_parser.py",
    "storage.py",
    "ingest.py",
    "sq3.py",
)

FORBIDDEN_GLOBAL_MARKERS: tuple[str, ...] = (
    "04_Score_Calculation",
    "Credit_Confirmation",
    "Whinfell_Credit_Confirmation",
)

SQ3_FIRST_COMMIT = "9f7ae5b"
SQ3_RANGE_END = "HEAD"


def production_py_paths() -> list[Path]:
    return [PKG_ROOT / name for name in PRODUCTION_MODULES if (PKG_ROOT / name).exists()]


def scan_production_imports() -> list[tuple[str, int, str]]:
    """AST import scan across all production china_policy_track modules."""
    hits: list[tuple[str, int, str]] = []
    for py_file in production_py_paths():
        source = py_file.read_text(encoding="utf-8")
        tree = ast.parse(source, filename=str(py_file))
        rel = str(py_file.relative_to(REPO_ROOT))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    for marker in FORBIDDEN_GLOBAL_MARKERS:
                        if marker in alias.name:
                            hits.append((rel, node.lineno, alias.name))
            elif isinstance(node, ast.ImportFrom):
                module = node.module or ""
                for marker in FORBIDDEN_GLOBAL_MARKERS:
                    if marker in module:
                        hits.append((rel, node.lineno, module))
    return hits


def global_data_files() -> list[Path]:
    root = REPO_ROOT / "data" / "global"
    if not root.exists():
        return []
    return sorted(p for p in root.rglob("*") if p.is_file())