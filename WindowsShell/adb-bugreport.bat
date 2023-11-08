
@echo off
SETLOCAL

call mydatetime.cmd
adb bugreport bugreport_%today%.zip

ENDLOCAL