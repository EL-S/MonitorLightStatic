Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "close_screen_static.bat" & Chr(34), 0
Set WshShell = Nothing