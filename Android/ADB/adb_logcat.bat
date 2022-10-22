
@echo off
SETLOCAL

call mydatetime.cmd
adb logcat -b all > logcat_%today%.log

ENDLOCAL