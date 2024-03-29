
@echo off
SETLOCAL

echo Input scale width (default): 680

set mode=680
set /p mode=

call mydatetime.cmd

for %%f in (*.*) do (
	ffmpeg -i "%%f" -vf "scale=%mode%:-2" "%%f-w%mode%_%today%.mp4"
)

ENDLOCAL