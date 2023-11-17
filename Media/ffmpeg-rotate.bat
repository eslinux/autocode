
@echo off
SETLOCAL

echo 1: right-90
echo 2: left-90
echo 3: right-180
echo 4: left-90-flipped vertically 
echo 5: right-90-flipped vertically
echo Input rotate mode: 1


set mode=1
set /p mode=

set infile=%1
set outfile=%infile%-rot-%mode%.mp4

::right-90
IF "%mode%" == "1" (
    ffmpeg -i "%infile%" -vf "transpose=1" "%outfile%.mp4"
)



::left-90
IF "%mode%" == "2" (
    ffmpeg -i "%infile%" -vf "transpose=2" "%outfile%.mp4"
)


::right-180
IF "%mode%" == "3" (
    ffmpeg -i "%infile%" -vf "transpose=1,transpose=1" "%outfile%.mp4"
)



::left-90-flipped vertically 
IF "%mode%" == "4" (
    ffmpeg -i "%infile%" -vf "transpose=0" "%outfile%.mp4"
)



::right-90-flipped vertically 
IF "%mode%" == "5" (
    ffmpeg -i "%infile%" -vf "transpose=3" "%outfile%.mp4"
)


ENDLOCAL