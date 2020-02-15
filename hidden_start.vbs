Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "screen_static.bat" & Chr(34), 0
Set WshShell = Nothing