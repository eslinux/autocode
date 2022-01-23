@echo off


::============================================================
::  Delete file by file extension
::============================================================
REM %1 is the directory to recurse through and *.txt *.xls are the file extension to remove
for /R "%1" %%f in (*.txt *.xls) do (
    REM Path (sans drive) is given by %%~pf ; drive is given by %%~df
    REM file name (sans ext) is given by %%~nf ; to 'rename' files, move them
    rem copy "%%~df%%~pf%%~nf.%2" "%%~df%%~pf%%~nf"
    rem echo "%%~df%%~pf%%~nf.%2" copied to "%%~df%%~pf%%~nf"
	echo Deleting... %%f
	del /q /f /s %%f
)