"""Atomic SQ3 goal verification — writes all scratch artifacts in one run.

Usage:
    python3 -m china_policy_track.verify_sq3_goal /path/to/scratch
"""

from __future__ import annotations

import hashlib
import inspect
import json
import subprocess
import sys
import textwrap
from pathlib import Path

from china_policy_track.package_isolation import (
    PRODUCTION_MODULES,
    SQ3_FIRST_COMMIT,
    SQ3_RANGE_END,
    global_data_files,
    scan_production_imports,
)

REPO_ROOT = Path(__file__).resolve().parents[1]

PERPLEXITY_C_BLOCK = textwrap.dedent(
    """
    from pathlib import Path
    from china_policy_track.data_parser import parse_input
    from china_policy_track.sq3 import score_observation

    text = Path("china_policy_track/examples/sample_perplexity_export.txt").read_text()
    results = []
    for run in (1, 2):
        obs = parse_input(text)
        r = score_observation(obs)
        assert 0 <= r.sq3_score <= 100, r.sq3_score
        assert r.interpretation_band, "empty band"
        results.append((run, r.sq3_score, r.interpretation_band))
    r1 = score_observation(parse_input(text))
    r2 = score_observation(parse_input(text))
    assert r1.sq3_score == r2.sq3_score
    assert r1.interpretation_band == r2.interpretation_band
    for run, score, band in results:
        print(f"perplexity run_{run}: score={score} band={band}")
    print("perplexity reproducibility: OK")
    """
).strip()

KOYFIN_C_BLOCK = textwrap.dedent(
    """
    from pathlib import Path
    import json
    from china_policy_track.data_parser import parse_input
    from china_policy_track.sq3 import score_observation, score_from_mapping

    data = json.loads(Path("china_policy_track/examples/sample_koyfin_export.json").read_text())
    results = []
    for run in (1, 2):
        obs = parse_input(data)
        r = score_observation(obs)
        assert 0 <= r.sq3_score <= 100, r.sq3_score
        assert r.interpretation_band, "empty band"
        results.append((run, r.sq3_score, r.interpretation_band))
    r_map = score_from_mapping(data)
    assert 0 <= r_map.sq3_score <= 100
    assert r_map.interpretation_band
    r1 = score_observation(parse_input(data))
    r2 = score_observation(parse_input(data))
    assert r1.sq3_score == r2.sq3_score
    assert r1.interpretation_band == r2.interpretation_band
    for run, score, band in results:
        print(f"koyfin run_{run}: score={score} band={band}")
    print(f"score_from_mapping(dict): score={r_map.sq3_score} band={r_map.interpretation_band}")
    print("koyfin reproducibility: OK")
    """
).strip()


def _run_git(args: list[str]) -> str:
    proc = subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    return (proc.stdout + proc.stderr).rstrip()


def _file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()


def _shasum_lines(paths: list[Path]) -> list[str]:
    lines: list[str] = []
    for path in paths:
        if path.exists():
            rel = path.relative_to(REPO_ROOT)
            lines.append(f"{_file_sha256(path)}  {rel}")
    return lines


def _run_python_c_block(block: str) -> tuple[int, str, str]:
    """Run code in a fresh interpreter subprocess (python3 -c)."""
    proc = subprocess.run(
        [sys.executable, "-c", block],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    return proc.returncode, proc.stdout.rstrip(), proc.stderr.rstrip()


def write_sq3_output(path: Path) -> None:
    lines = [
        "=== INVOCATION CODE (Verification plan step 1) ===",
        "Each block executed as a separate `python3 -c` subprocess (fresh interpreter).",
        "",
        "# Perplexity sample — parse + score_observation, twice",
        f"python3 -c {json.dumps(PERPLEXITY_C_BLOCK)}",
        "",
        "# Koyfin sample — parse + score_observation + score_from_mapping, twice",
        f"python3 -c {json.dumps(KOYFIN_C_BLOCK)}",
        "",
        "=== EXECUTION OUTPUT ===",
    ]
    for label, block in (("perplexity", PERPLEXITY_C_BLOCK), ("koyfin", KOYFIN_C_BLOCK)):
        rc, out, err = _run_python_c_block(block)
        lines.append(f"--- {label} subprocess exit_code={rc} ---")
        if out:
            lines.append(out)
        if err:
            lines.append(f"stderr: {err}")
        if rc != 0:
            raise RuntimeError(f"{label} verification subprocess failed (exit {rc}): {err}")
    lines.append("all_verification_asserts_passed")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_sq3_methodology(path: Path) -> None:
    from china_policy_track import sq3
    from china_policy_track.data_parser import parse_input
    from china_policy_track.sq3 import score_observation

    chunks = [
        "=== WEIGHTS (from sq3.py) ===",
        f"WEIGHT_POLICY_HIERARCHY = {sq3.WEIGHT_POLICY_HIERARCHY}",
        f"WEIGHT_STATE_CONTROL = {sq3.WEIGHT_STATE_CONTROL}",
        f"WEIGHT_GROWTH_MARKET = {sq3.WEIGHT_GROWTH_MARKET}",
        "",
        "=== INTERPRETATION BANDS ===",
    ]
    for lo, hi, label in sq3.INTERPRETATION_BANDS:
        chunks.append(f"{lo}-{hi}: {label}")

    chunks.extend(
        [
            "",
            "=== normalize_state_control_impulse ===",
            inspect.getsource(sq3.normalize_state_control_impulse),
            "",
            "=== calculate_sq3 ===",
            inspect.getsource(sq3.calculate_sq3),
            "",
            "=== score_from_mapping ===",
            inspect.getsource(sq3.score_from_mapping),
            "",
            "=== SAMPLE BAND EMIT ===",
        ]
    )

    perplexity = (REPO_ROOT / "china_policy_track/examples/sample_perplexity_export.txt").read_text()
    koyfin = json.loads(
        (REPO_ROOT / "china_policy_track/examples/sample_koyfin_export.json").read_text()
    )
    for name, payload in (("perplexity", perplexity), ("koyfin", koyfin)):
        r = score_observation(parse_input(payload))
        chunks.append(f"{name}: score={r.sq3_score} band={r.interpretation_band}")

    path.write_text("\n".join(chunks) + "\n", encoding="utf-8")


def write_china_tests(path: Path) -> int:
    proc = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "china_policy_track/tests", "-v"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    path.write_text(proc.stdout + proc.stderr, encoding="utf-8")
    return proc.returncode


def write_global_isolation(path: Path) -> None:
    from china_policy_track.sq3 import score_input

    global_paths = global_data_files()
    before = _shasum_lines(global_paths)

    score_input((REPO_ROOT / "china_policy_track/examples/sample_perplexity_export.txt").read_text())
    score_input(
        json.loads(
            (REPO_ROOT / "china_policy_track/examples/sample_koyfin_export.json").read_text()
        )
    )

    after = _shasum_lines(global_paths)
    package_hits = scan_production_imports()
    sq3_range = f"{SQ3_FIRST_COMMIT}..{SQ3_RANGE_END}"
    sq3_parent_range = f"{SQ3_FIRST_COMMIT}^..{SQ3_RANGE_END}"
    china_scope = ["--", "china_policy_track/"]

    lines = [
        "=== Verification plan step 4: Global isolation ===",
        f"SQ3 first commit: {SQ3_FIRST_COMMIT}",
        "All SQ3 file lists below use path filter: -- china_policy_track/",
        "",
        f"--- Command: git diff --name-only {sq3_range} -- china_policy_track/ ---",
        _run_git(["diff", "--name-only", sq3_range, *china_scope]),
        "",
        f"--- Command: git diff --name-only {sq3_parent_range} -- china_policy_track/ ---",
        _run_git(["diff", "--name-only", sq3_parent_range, *china_scope]),
        "",
        f"--- Command: git diff {sq3_parent_range} -- 04_Score_Calculation/ ---",
        _run_git(["diff", sq3_parent_range, "--", "04_Score_Calculation/"]) or "(no diff)",
        "",
        f"--- Command: git diff {sq3_parent_range} -- data/global/ ---",
        _run_git(["diff", sq3_parent_range, "--", "data/global/"]) or "(no diff)",
        "",
        f"--- Production modules scanned: {', '.join(PRODUCTION_MODULES)} ---",
        "--- Command: AST import scan (all production modules via package_isolation.py) ---",
    ]
    if package_hits:
        for rel, lineno, marker in package_hits:
            lines.append(f"HIT {rel}:{lineno}: {marker}")
    else:
        lines.append("(no matches)")

    ls_proc = subprocess.run(
        ["ls", "-la", "data/global/", "data/global/v1/"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    status_full = _run_git(["status", "--porcelain"]) or "(clean)"

    lines.extend(
        [
            "",
            "--- Command: ls -la data/global/ data/global/v1/ ---",
            ls_proc.stdout.strip(),
            "",
            "--- shasum data/global files (before score_input x2) ---",
            *before,
            "",
            "--- shasum data/global files (after score_input x2) ---",
            *after,
            "",
            "data/global checksums after score_input: "
            + ("UNCHANGED" if before == after else "CHANGED"),
            "",
            "--- Command: git status --porcelain (full, unfiltered) ---",
            status_full,
            "",
            "--- SQ3 CHANGED_FILES (git diff --name-only with -- china_policy_track/ filter) ---",
            _run_git(["diff", "--name-only", sq3_parent_range, *china_scope]),
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    if len(args) != 1:
        print("usage: python3 -m china_policy_track.verify_sq3_goal <scratch_dir>", file=sys.stderr)
        return 2

    scratch = Path(args[0])
    scratch.mkdir(parents=True, exist_ok=True)

    write_sq3_output(scratch / "sq3_output.log")
    write_sq3_methodology(scratch / "sq3_methodology.txt")
    test_rc = write_china_tests(scratch / "china_tests.log")
    write_global_isolation(scratch / "global_isolation.txt")

    print(f"verify_sq3_goal_ok scratch={scratch}")
    print(f"artifacts: sq3_output.log sq3_methodology.txt china_tests.log global_isolation.txt")
    return test_rc


if __name__ == "__main__":
    raise SystemExit(main())