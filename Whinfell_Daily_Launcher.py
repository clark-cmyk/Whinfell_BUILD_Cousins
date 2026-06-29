#!/usr/bin/env python3
"""Whinfell Daily Launcher — one-click morning desk tool (Tkinter, stdlib only)."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
import threading
import tkinter as tk
from tkinter import font as tkfont
from tkinter import scrolledtext

PROJECT_DIR = "/Users/clarksonwthornburgh/Desktop/Whinfell_BUILD_Cousins"
HYDRATION_DIR = "/Users/clarksonwthornburgh/Desktop/Whinfell_BUILD_Cousins/data/hydration"
BARCHART_OUT_DIR = "/Users/clarksonwthornburgh/Desktop/Whinfell_BUILD_Cousins/data/barchart/v1"

MODES = {
    "am": {
        "title": "Whinfell Daily Launcher — AM",
        "button": "Run Whinfell Daily AM",
        "script": "whinfell_daily_am.sh",
        "success_hint": "Next: Import Latest Hydration Bundle in Transmission Control.",
    },
    "eod": {
        "title": "Whinfell Daily Launcher — EOD",
        "button": "Run Whinfell Daily EOD",
        "script": "whinfell_daily_eod.sh",
        "success_hint": "Next: Save State + handover note in Transmission Control.",
    },
}

STATUS_STYLES = {
    "Idle": ("#6b7280", "#1a1a1a"),
    "Running": ("#3d8bfd", "#0f2744"),
    "Success": ("#22c55e", "#0f2a1a"),
    "Error": ("#ef4444", "#2a0f0f"),
}


class WhinfellDailyLauncher(tk.Tk):
    def __init__(self, mode: str = "am") -> None:
        super().__init__()
        self._mode = mode if mode in MODES else "am"
        self._config = MODES[self._mode]
        self._daily_shell = f"cd {PROJECT_DIR} && ./{self._config['script']}"
        self.title(self._config["title"])
        self.configure(bg="#0f1419")
        self.minsize(640, 480)
        self._proc: subprocess.Popen[str] | None = None
        self._running = False

        self._title_font = tkfont.Font(family="Helvetica", size=20, weight="bold")
        self._btn_font = tkfont.Font(family="Helvetica", size=16, weight="bold")
        self._sec_font = tkfont.Font(family="Helvetica", size=13, weight="bold")
        self._log_font = tkfont.Font(family="Menlo", size=12)
        self._status_font = tkfont.Font(family="Helvetica", size=14, weight="bold")

        self._build_ui()
        self._set_status("Idle")
        self.protocol("WM_DELETE_WINDOW", self._on_close)
        self._activate_window()

    def _activate_window(self) -> None:
        """Bring window to front on macOS (fixes ghost/unclickable window from .command launch)."""
        self.update_idletasks()
        self.deiconify()
        self.lift()
        self.attributes("-topmost", True)
        self.after(150, lambda: self.attributes("-topmost", False))
        self.focus_force()
        if sys.platform == "darwin":
            self.after(200, self._macos_frontmost)

    def _macos_frontmost(self) -> None:
        pid = os.getpid()
        try:
            subprocess.run(
                [
                    "osascript",
                    "-e",
                    f'tell application "System Events" to set frontmost of '
                    f'first process whose unix id is {pid} to true',
                ],
                check=False,
                capture_output=True,
                timeout=3,
            )
        except Exception:
            pass

    def _build_ui(self) -> None:
        top = tk.Frame(self, bg="#1a2332", padx=16, pady=12)
        top.pack(fill=tk.X)

        tk.Label(
            top,
            text=self._config["title"],
            font=self._title_font,
            fg="#e8edf4",
            bg="#1a2332",
        ).pack(anchor=tk.W)

        self.status_frame = tk.Frame(top, bg="#1a2332")
        self.status_frame.pack(fill=tk.X, pady=(10, 0))
        tk.Label(
            self.status_frame,
            text="Status:",
            font=self._sec_font,
            fg="#8b9cb3",
            bg="#1a2332",
        ).pack(side=tk.LEFT)
        self.status_label = tk.Label(
            self.status_frame,
            text="Idle",
            font=self._status_font,
            fg="#6b7280",
            bg="#1a1a1a",
            padx=12,
            pady=4,
        )
        self.status_label.pack(side=tk.LEFT, padx=(8, 0))

        body = tk.Frame(self, bg="#0f1419", padx=16, pady=12)
        body.pack(fill=tk.BOTH, expand=True)

        self.run_btn = tk.Button(
            body,
            text=self._config["button"],
            font=self._btn_font,
            fg="#ffffff",
            bg="#2563eb",
            activebackground="#1d4ed8",
            activeforeground="#ffffff",
            relief=tk.FLAT,
            padx=20,
            pady=14,
            cursor="hand2",
            command=self._run_daily,
        )
        self.run_btn.pack(fill=tk.X, pady=(0, 8))

        self.barchart_btn = tk.Button(
            body,
            text="Run Barchart Hydration (barchart-only)",
            font=self._sec_font,
            fg="#e8edf4",
            bg="#1e4d3a",
            activebackground="#25634b",
            activeforeground="#e8edf4",
            relief=tk.FLAT,
            padx=14,
            pady=10,
            cursor="hand2",
            command=self._run_barchart_hydration,
        )
        self.barchart_btn.pack(fill=tk.X, pady=(0, 12))

        row = tk.Frame(body, bg="#0f1419")
        row.pack(fill=tk.X, pady=(0, 12))
        tk.Button(
            row,
            text="Open Hydration Folder",
            font=self._sec_font,
            fg="#e8edf4",
            bg="#243044",
            activebackground="#2d3a4f",
            activeforeground="#e8edf4",
            relief=tk.FLAT,
            padx=14,
            pady=10,
            cursor="hand2",
            command=lambda: self._open_folder(HYDRATION_DIR),
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 6))
        tk.Button(
            row,
            text="Open Project Folder",
            font=self._sec_font,
            fg="#e8edf4",
            bg="#243044",
            activebackground="#2d3a4f",
            activeforeground="#e8edf4",
            relief=tk.FLAT,
            padx=14,
            pady=10,
            cursor="hand2",
            command=lambda: self._open_folder(PROJECT_DIR),
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(6, 0))

        tk.Label(
            body,
            text="Live log",
            font=self._sec_font,
            fg="#8b9cb3",
            bg="#0f1419",
        ).pack(anchor=tk.W, pady=(0, 4))

        self.log = scrolledtext.ScrolledText(
            body,
            font=self._log_font,
            fg="#e8edf4",
            bg="#0a0e14",
            insertbackground="#e8edf4",
            relief=tk.FLAT,
            wrap=tk.WORD,
            height=16,
        )
        self.log.pack(fill=tk.BOTH, expand=True)
        self.log.configure(state=tk.NORMAL)

    def _set_status(self, state: str) -> None:
        fg, bg = STATUS_STYLES.get(state, STATUS_STYLES["Idle"])
        self.status_label.configure(text=state, fg=fg, bg=bg)

    def _append_log(self, text: str) -> None:
        self.log.insert(tk.END, text)
        self.log.see(tk.END)

    def _open_folder(self, path: str) -> None:
        try:
            subprocess.run(["open", path], check=True)
            self._append_log(f"\n[launcher] Opened folder: {path}\n")
        except subprocess.CalledProcessError as exc:
            self._set_status("Error")
            self._append_log(f"\n[launcher] ERROR opening folder ({exc.returncode}): {path}\n")

    def _run_daily(self) -> None:
        if self._running:
            self._append_log("\n[launcher] Already running — wait for completion.\n")
            return

        self._running = True
        self.run_btn.configure(state=tk.DISABLED, bg="#1e40af")
        self.barchart_btn.configure(state=tk.DISABLED)
        self._set_status("Running")
        self._append_log("\n" + "=" * 60 + "\n")
        self._append_log(f"[launcher] Starting {self._config['button']}…\n")
        self._append_log(f"[launcher] Command: /bin/zsh -lc '{self._daily_shell}'\n")
        self._append_log("=" * 60 + "\n")

        thread = threading.Thread(target=self._execute_daily, daemon=True)
        thread.start()

    def _run_barchart_hydration(self) -> None:
        if self._running:
            self._append_log("\n[launcher] Already running — wait for completion.\n")
            return

        self._running = True
        self.run_btn.configure(state=tk.DISABLED)
        self.barchart_btn.configure(state=tk.DISABLED, bg="#14532d")
        self._set_status("Running")
        cmd = f"cd {PROJECT_DIR} && /usr/bin/python3 run_batch_collect.py barchart-only"
        self._append_log("\n" + "=" * 60 + "\n")
        self._append_log("[launcher] Starting Barchart-only hydration…\n")
        self._append_log(f"[launcher] Command: /bin/zsh -lc '{cmd}'\n")
        self._append_log("=" * 60 + "\n")
        thread = threading.Thread(target=self._execute_shell, args=(cmd,), daemon=True)
        thread.start()

    def _execute_shell(self, shell_cmd: str) -> None:
        exit_code = 1
        try:
            self._proc = subprocess.Popen(
                ["/bin/zsh", "-lc", shell_cmd],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
            )
            assert self._proc.stdout is not None
            for line in self._proc.stdout:
                self.after(0, self._append_log, line)
            exit_code = self._proc.wait()
        except Exception as exc:
            self.after(0, self._append_log, f"\n[launcher] ERROR: {exc}\n")
            exit_code = 1
        finally:
            self._proc = None
            self.after(0, self._finish_barchart_run, exit_code)

    def _finish_barchart_run(self, exit_code: int) -> None:
        self._running = False
        self.run_btn.configure(state=tk.NORMAL, bg="#2563eb")
        self.barchart_btn.configure(state=tk.NORMAL, bg="#1e4d3a")
        if exit_code == 0:
            self._set_status("Success")
            self._append_log("\n[launcher] Barchart hydration completed successfully.\n")
            self._append_log(f"[launcher] Outputs: {BARCHART_OUT_DIR}\n")
        else:
            self._set_status("Error")
            self._append_log(f"\n[launcher] ERROR — barchart-only exited with code {exit_code}\n")

    def _execute_daily(self) -> None:
        exit_code = 1
        try:
            self._proc = subprocess.Popen(
                ["/bin/zsh", "-lc", self._daily_shell],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
            )
            assert self._proc.stdout is not None
            for line in self._proc.stdout:
                self.after(0, self._append_log, line)
            exit_code = self._proc.wait()
        except Exception as exc:
            self.after(0, self._append_log, f"\n[launcher] ERROR: {exc}\n")
            exit_code = 1
        finally:
            self._proc = None
            self.after(0, self._finish_run, exit_code)

    def _finish_run(self, exit_code: int) -> None:
        self._running = False
        self.run_btn.configure(state=tk.NORMAL, bg="#2563eb")
        self.barchart_btn.configure(state=tk.NORMAL)
        if exit_code == 0:
            self._set_status("Success")
            self._append_log(f"\n[launcher] {self._config['button']} completed successfully.\n")
            self._append_log(f"[launcher] {self._config['success_hint']}\n")
        else:
            self._set_status("Error")
            self._append_log(f"\n[launcher] ERROR — command exited with code {exit_code}\n")

    def _on_close(self) -> None:
        if self._proc is not None and self._proc.poll() is None:
            self._append_log("\n[launcher] Run in progress — close after completion.\n")
            return
        self.destroy()


def _log_startup(mode: str) -> None:
    try:
        from datetime import datetime
        from pathlib import Path

        log = Path.home() / "Desktop" / "whinfell_launcher.log"
        with log.open("a", encoding="utf-8") as fh:
            fh.write(f"GUI starting mode={mode} pid={os.getpid()} at {datetime.now().isoformat()}\n")
    except OSError:
        pass


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Whinfell Daily Launcher")
    parser.add_argument("--eod", action="store_true", help="End-of-day handoff mode")
    args = parser.parse_args(argv)
    mode = "eod" if args.eod else "am"
    _log_startup(mode)
    try:
        app = WhinfellDailyLauncher(mode=mode)
        app.mainloop()
    except Exception as exc:
        try:
            subprocess.run(
                [
                    "osascript",
                    "-e",
                    f'display alert "Whinfell Launcher crashed" message "{exc}"',
                ],
                check=False,
            )
        except Exception:
            pass
        raise


if __name__ == "__main__":
    main()