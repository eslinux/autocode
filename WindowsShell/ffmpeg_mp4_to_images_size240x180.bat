
@echo off
SETLOCAL

ffmpeg -i "%1" -vf fps=30 -s 240x180 "frame%%4d.png"

ENDLOCAL