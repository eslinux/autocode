@echo off
::read line by line from text file
for /f "tokens=*" %%a in (input.txt) do (
  echo %%a
)
pause
