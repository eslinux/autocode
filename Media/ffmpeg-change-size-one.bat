
@echo off
SETLOCAL

echo Input scale width (default): 680

set infile=%1
set mode=680
set /p mode=

call mydatetime.cmd


ffmpeg -i "%infile%" -vf "scale=%mode%:-2" "%infile%-w%mode%_%today%.mp4"


ENDLOCAL