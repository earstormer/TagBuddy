# Quick UI to PY code conversion

$scriptPath = split-path -parent $MyInvocation.MyCommand.Definition
C:\Users\$env:UserName\AppData\Local\Programs\Python\Python36\Scripts\pyuic5.exe $scriptPath\GUI.ui -o $scriptPath\InterfaceMain.py