@echo off
::--------------------------------------------------------------------------------
:: copy release file from build folder to new "Release_yyyymmdd_hhmmss" folder
::--------------------------------------------------------------------------------



::get time yyyymmdd_hhmmss
for /f "skip=1" %%x in ('wmic os get localdatetime') do if not defined MyDate set MyDate=%%x
for /f %%x in ('wmic path win32_localtime get /format:list ^| findstr "="') do set %%x
set fmonth=00%Month%
set fday=00%Day%
set today=%Year%%fmonth:~-2%%fday:~-2%_%time:~0,2%%time:~3,2%%time:~6,2%
echo %today%

::create folder
set release_dir=".\x64\Release_%today%"
mkdir %release_dir%


::copy file from Release -> Release_yyyymmdd_hhmmss
copy ".\x64\Release\*.dll" "%release_dir%\*.dll"
copy ".\x64\Release\*.exe" "%release_dir%\*.exe"
copy ".\x64\Release\*.ini" "%release_dir%\*.ini"