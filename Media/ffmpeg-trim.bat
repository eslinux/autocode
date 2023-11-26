
echo ffmpeg-trim.bat "from"  "to_duration"  "infile"
::ffmpeg-trim.bat 00:05 00:15 myfile.mov
::ffmpeg-trim.bat 0:5 0:15 myfile.mov
::ffmpeg-trim.bat 5 15 myfile.mov


@echo off
SETLOCAL

echo Trim mode:
echo 1: from-to
echo 2: from-duration
echo Input trim mode (default): 1

set mode=1
set /p mode=

set from=%1
set to_duration=%2
set infile=%3

call mydatetime.cmd
	
::from-to
::ffmpeg -i "%infile%" -ss %from% -to %to_duration% -c:v copy -c:a copy "%infile%_from-to_%today%.mp4"
::ffmpeg -i "%infile%" -ss %from% -to %to_duration% -c:v libx264 "%infile%_from-to_%today%.mp4"
IF "%mode%" == "1" (
	ffmpeg -i "%infile%" -ss %from% -to %to_duration% -c:v libx264 "%infile%_from-to_%today%.mp4"
)

::from-duration
::ffmpeg -i "%infile%" -ss %from% -t %to_duration% -c:v copy -c:a copy "%infile%_from-duration_%today%.mp4"
IF "%mode%" == "2" (
	ffmpeg -i "%infile%" -ss %from% -t %to_duration% -c:v libx264 "%infile%_from-duration_%today%.mp4"
)

ENDLOCAL