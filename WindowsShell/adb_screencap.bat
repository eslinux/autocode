
@echo off
SETLOCAL


adb shell screencap -p /sdcard/screencap.png && adb pull /sdcard/screencap.png
call mydatetime.cmd
ren screencap.png screencap_%today%.png

ENDLOCAL