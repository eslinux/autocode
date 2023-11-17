
@echo off
SETLOCAL

set infile=%1
ffmpeg -i "%infile%" -vf fps=30 -s 240x180 "frame%%4d.png"

ENDLOCAL