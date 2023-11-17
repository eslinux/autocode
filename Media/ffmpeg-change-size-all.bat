
@echo off
SETLOCAL

echo Scale width: 680

set mode=680
set /p mode=

for %%f in (*.*) do (
	ffmpeg -i "%%f" -vf "scale=%mode%:-2" "%%f-w%mode%.mp4"
)

ENDLOCAL