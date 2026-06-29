#!/bin/zsh
HYDRATION="/Users/clarksonwthornburgh/Desktop/Whinfell_BUILD_Cousins/data/hydration"
SRC="$HYDRATION/latest.json"
DESKTOP_COPY="$HOME/Desktop/Whinfell_Hydration_latest.json"
DOWNLOADS_COPY="$HOME/Downloads/Whinfell_Hydration_latest.json"

if [[ -f "$SRC" ]]; then
  cp "$SRC" "$DESKTOP_COPY"
  cp "$SRC" "$DOWNLOADS_COPY"
fi

open "$HYDRATION"
/usr/bin/osascript -e 'display dialog "Hydration folder opened in Finder.\n\nFor Import in Transmission Control, select:\n• Whinfell_Hydration_latest.json (Desktop or Downloads)\n\nOR navigate to:\ndata/hydration/latest.json\n\nNote: whinfell_drop is CSV downloads only — not for import." buttons {"OK"} default button "OK" with title "Whinfell Hydration"' 2>/dev/null || true
exit 0