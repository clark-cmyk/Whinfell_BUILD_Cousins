#!/bin/zsh
# Open Transmission Control in default browser (no Terminal work required).
TC="/Users/clarksonwthornburgh/Desktop/Whinfell_BUILD_Cousins/08_Deliverables/Whinfell_Transmission_Control.html"
if [[ ! -f "$TC" ]]; then
  /usr/bin/osascript -e 'display alert "Transmission Control not found" message "Expected: Whinfell_BUILD_Cousins/08_Deliverables/Whinfell_Transmission_Control.html"'
  read "?Press Enter to close..."
  exit 1
fi
/usr/bin/open "$TC"
exit 0