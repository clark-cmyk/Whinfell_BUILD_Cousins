#!/bin/zsh
PROJECT="/Users/clarksonwthornburgh/Desktop/Whinfell_BUILD_Cousins"
LOG="$HOME/Desktop/whinfell_launcher.log"
MSG="Whinfell Launcher Diagnostics\n\n"

check() {
  if eval "$2" >/dev/null 2>&1; then
    MSG+="$1: OK\n"
  else
    MSG+="$1: FAIL\n"
  fi
}

check "Project folder" "test -d '$PROJECT'"
check "Launcher script" "test -f '$PROJECT/Whinfell_Daily_Launcher.py'"
check "AM shell script" "test -x '$PROJECT/whinfell_daily_am.sh'"
check "Python3" "test -x /usr/bin/python3"
check "Tkinter" "/usr/bin/python3 -c 'import tkinter'"
check "AM app bundle" "test -x '$PROJECT/Whinfell_Daily_AM.app/Contents/MacOS/launcher'"

{
  echo ""
  echo "=== Diagnose $(date) ==="
  echo -e "$MSG"
} >>"$LOG"

/usr/bin/osascript -e "display dialog \"$MSG\" buttons {\"OK\"} default button \"OK\" with title \"Whinfell Diagnostics\""