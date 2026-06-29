on run
	set projectPath to "/Users/clarksonwthornburgh/Desktop/Whinfell_BUILD_Cousins"
	set logPath to (POSIX path of (path to desktop)) & "whinfell_launcher.log"
	do shell script "echo '' >> " & quoted form of logPath & " && echo '=== EOD applescript launch '$(date)' ===' >> " & quoted form of logPath
	tell application "Terminal"
		activate
		do script "cd " & quoted form of projectPath & " && /usr/bin/python3 Whinfell_Daily_Launcher.py --eod"
	end tell
end run