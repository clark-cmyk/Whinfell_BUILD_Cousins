#!/bin/zsh
PROJECT="/Users/clarksonwthornburgh/Desktop/Whinfell_BUILD_Cousins"
LOG="$HOME/Desktop/whinfell_launcher.log"
cd "$PROJECT" || { echo "Cannot cd to $PROJECT"; read "?Press Enter..."; exit 1; }

/usr/bin/osascript -e 'display notification "Opening Whinfell Daily EOD…" with title "Whinfell"' 2>/dev/null || true

echo "" >>"$LOG"
echo "=== EOD command launch $(date) ===" >>"$LOG"

if ! /usr/bin/python3 -c "import tkinter" 2>>"$LOG"; then
  /usr/bin/osascript -e 'display alert "Tkinter missing" message "Install Xcode CLT: xcode-select --install"'
  read "?Tkinter not found. Press Enter to close..."
  exit 1
fi

/usr/bin/python3 Whinfell_Daily_Launcher.py --eod 2>>"$LOG"
CODE=$?
echo "exit=$CODE" >>"$LOG"
if [[ $CODE -ne 0 ]]; then
  /usr/bin/osascript -e "display alert \"Whinfell EOD failed (exit $CODE)\" message \"See Desktop/whinfell_launcher.log\""
  read "?Press Enter to close..."
fi
exit $CODE