#!/bin/zsh
# Open Transmission Ladder Deep Dive in default browser.
PAGE="/Users/clarksonwthornburgh/Desktop/Whinfell_BUILD_Cousins/08_Deliverables/whinfell-transmission-ladder-deep-dive.html"
if [[ ! -f "$PAGE" ]]; then
  /usr/bin/osascript -e 'display alert "Deep Dive page not found" message "Expected: 08_Deliverables/whinfell-transmission-ladder-deep-dive.html"'
  read "?Press Enter to close..."
  exit 1
fi
/usr/bin/open "$PAGE"
exit 0