#!/bin/zsh
set -euo pipefail

PROJECT="/Users/clarksonwthornburgh/Desktop/Whinfell_BUILD_Cousins"
DESKTOP="$HOME/Desktop"

echo "Deploying Whinfell launchers to Desktop..."

cp "$PROJECT/Whinfell_Daily_AM.command" "$DESKTOP/"
cp "$PROJECT/Whinfell_Daily_EOD.command" "$DESKTOP/"
cp "$PROJECT/Whinfell_Diagnose_Launcher.command" "$DESKTOP/"
cp "$PROJECT/Whinfell_Transmission_Control.command" "$DESKTOP/"
cp "$PROJECT/Whinfell_Open_Hydration_Folder.command" "$DESKTOP/"

chmod +x "$DESKTOP/Whinfell_Daily_AM.command"
chmod +x "$DESKTOP/Whinfell_Daily_EOD.command"
chmod +x "$DESKTOP/Whinfell_Diagnose_Launcher.command"
chmod +x "$DESKTOP/Whinfell_Transmission_Control.command"
chmod +x "$DESKTOP/Whinfell_Open_Hydration_Folder.command"

# AppleScript apps — most reliable double-click path on macOS (opens Terminal + GUI).
rm -rf "$DESKTOP/Whinfell Daily AM.app" "$DESKTOP/Whinfell Daily EOD.app" "$DESKTOP/Whinfell Transmission Control.app"
osacompile -o "/tmp/Whinfell_Daily_AM.app" "$PROJECT/scripts/Whinfell_Daily_AM.applescript"
osacompile -o "/tmp/Whinfell_Daily_EOD.app" "$PROJECT/scripts/Whinfell_Daily_EOD.applescript"
osacompile -o "/tmp/Whinfell_Transmission_Control.app" "$PROJECT/scripts/Whinfell_Transmission_Control.applescript"
mv "/tmp/Whinfell_Daily_AM.app" "$DESKTOP/Whinfell Daily AM.app"
mv "/tmp/Whinfell_Daily_EOD.app" "$DESKTOP/Whinfell Daily EOD.app"
mv "/tmp/Whinfell_Transmission_Control.app" "$DESKTOP/Whinfell Transmission Control.app"

# Remove old shell-script .app bundles (unreliable on double-click).
rm -rf "$DESKTOP/Whinfell_Daily_AM.app" "$DESKTOP/Whinfell_Daily_EOD.app"

# Remove quarantine / iCloud flags that block double-click execution.
xattr -cr "$DESKTOP/Whinfell_Daily_AM.command" \
  "$DESKTOP/Whinfell_Daily_EOD.command" \
  "$DESKTOP/Whinfell_Diagnose_Launcher.command" \
  "$DESKTOP/Whinfell_Transmission_Control.command" \
  "$DESKTOP/Whinfell_Open_Hydration_Folder.command" \
  "$DESKTOP/Whinfell Daily AM.app" \
  "$DESKTOP/Whinfell Daily EOD.app" \
  "$DESKTOP/Whinfell Transmission Control.app" 2>/dev/null || true

echo "Done. On Desktop use:"
echo "  • Whinfell_Open_Hydration_Folder.command (before Import — opens Finder + copies JSON)"
echo "  • Whinfell Transmission Control.app  (open TC only — use while Perplexity collects)"
echo "  • Whinfell Daily AM.app   (full morning chain — Terminal + GUI)"
echo "  • Whinfell_Daily_AM.command (alternate)"
echo "  • Whinfell_Diagnose_Launcher.command (run first if anything fails)"