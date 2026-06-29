on run
	set tcPath to "/Users/clarksonwthornburgh/Desktop/Whinfell_BUILD_Cousins/08_Deliverables/Whinfell_Transmission_Control.html"
	do shell script "test -f " & quoted form of tcPath & " && open " & quoted form of tcPath
end run