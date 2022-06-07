@echo off
::Author: ninhld
::Create on: 2022/04/30

::show all input argument 
::for %%I IN (%*) DO ECHO %%I

::------------------------------------------------------
::     App info
::------------------------------------------------------
set appversion=1.0.0

::------------------------------------------------------
::     3rd empty
::------------------------------------------------------
set app7z="C:\Program Files\7-Zip\7z.exe"

::------------------------------------------------------
::     Argument parser
::------------------------------------------------------
::Get main parameter
set appname=%0
set cmd=%1
set subfolder=%2


::Switch command
IF "%cmd%"=="help" goto showhelp
IF "%cmd%"=="version" goto showversion
IF "%cmd%"=="install" goto install
IF "%cmd%"=="uninstall" goto uninstall

IF "%cmd%"=="ls" goto listall
IF "%cmd%"=="lsf" goto listfile
IF "%cmd%"=="lsd" goto listdirectory
IF "%cmd%"=="cpf" goto copyfile
IF "%cmd%"=="exf" goto extractfile
IF "%cmd%"=="delf" goto deletefile
IF "%cmd%"=="deld" goto deletedirectory

goto showhelp




::------------------------------------------------------
::     Show version
::------------------------------------------------------
:showversion
echo %appname% %appversion%
goto commonexit



::------------------------------------------------------
::     Show Help
::------------------------------------------------------
:showhelp
echo Usage:
echo   1. List both file and folder
echo      %appname% ls [/s]
echo:
echo   2. List all file
echo      %appname% lsf [/s] [file filter (Ex: *test.txt)]
echo:
echo   3. List all folder
echo      %appname% lsd [/s] [folder filter (Ex: *import*)]
echo:
echo   4. Copy file
echo      %appname% cpf [/s] [file filter (Ex: *test.txt)]
echo:
echo   5. Extract zip or 7zip file
echo      %appname% exf [/s] [file filter (Ex: *test.7z)]
echo:
echo   6. Delete all file
echo      %appname% delf [/s] [file filter (Ex: *test.txt)]
echo:
echo   7. Delete all folder
echo      %appname% deld [/s] [folder filter (Ex: *import*)]
echo:
echo   8. Install this app to [%appdata%\%appname%] folder
echo      %appname% install
echo:
echo   9. Uninstall this app from [%appdata%\%appname%] folder
echo      %appname% uninstall
echo:
echo Parameter descriptions:
echo 	/s : Include sub-folder
echo:
pause
goto commonexit




::------------------------------------------------------
::     1.List all file & directory
::------------------------------------------------------
:listall
dir /b %subfolder%
goto commonexit



::------------------------------------------------------
::     2.List all file
::------------------------------------------------------
:listfile
::check input argument
set file_ext=%3
if "%subfolder%" == "/s" (
	set  subfolder=/r
) else (
	set  subfolder=
	set file_ext=%2
)

if "%file_ext%" == "" set  file_ext=*.*

::scan
for %subfolder% %%f in (%file_ext%) do (
	echo %%f
)
goto commonexit



::------------------------------------------------------
::     3.List all directory
::------------------------------------------------------
:listdirectory
set folder_filter=%3
if "%subfolder%" == "/s" (
	set  subfolder=/r
) else (
	set  subfolder=
	set folder_filter=%2
)

if "%folder_filter%" == "" set  folder_filter=*

::scan
for /d %subfolder% %%x in (%folder_filter%) do (
	echo %%x
)
goto commonexit



::------------------------------------------------------
::     4.Copy file
::------------------------------------------------------
:copyfile
::check argument
set file_ext=%3
if "%subfolder%" == "/s" (
	set  subfolder=/r
) else (
	set  subfolder=
	set file_ext=%2
)

if "%file_ext%" == "" set  file_ext=*.*

::scan file
set isfileexists=false
echo ----- List file below will be copied ------
for %subfolder% %%f in (%file_ext%) do (
	echo %%f
	set isfileexists=true
)
echo -------------------------------------------

::check file exists
if "%isfileexists%" == "false" (
	echo Notthing to copy !
	goto commonexit
)

:: Enter copy destination folder
echo Please input copy destination folder:
set desfolder=
set /p desfolder=

if "%desfolder%" == "" (
	echo Cancel !
	goto commonexit
)

if not exist %desfolder%\ (
	mkdir %desfolder%
)
if not exist %desfolder%\ (
    echo Destination folder not exist !
	goto commonexit
) 
	
::copy
echo Do you want copy (yes/no): no
set confirmyesorno=no
set /p confirmyesorno=
if "%confirmyesorno%"=="yes" (
	for %subfolder% %%f in (%file_ext%) do (
		echo Copying... %%f
		copy "%%f" "%desfolder%"
	)
	echo Copied !
) else (
	echo Cancel !
)
goto commonexit




::------------------------------------------------------
::     5.Extract zip or 7z file
::------------------------------------------------------
:extractfile

::check 7zip application
if not exist %app7z% (
	echo 7zip application have not already installed.
	echo Please install 7zip first and tray again !
	goto commonexit
)


::check argument
set file_ext=%3
if "%subfolder%" == "/s" (
	set  subfolder=/r
) else (
	set  subfolder=
	set file_ext=%2
)

if "%file_ext%" == "" set  file_ext=*.7z *.zip

::scan file
set isfileexists=false
echo ----- List file below will be extracted ------
for %subfolder% %%f in (%file_ext%) do (
	echo %%f
	set isfileexists=true
)
echo -------------------------------------------

::check file exists
if "%isfileexists%" == "false" (
	echo Notthing to extract !
	goto commonexit
)

:: Enter copy destination folder
echo Please input extract destination folder:
set desfolder=
set /p desfolder=

if "%desfolder%" == "" (
	echo Cancel !
	goto commonexit
)

if not exist %desfolder%\ (
	mkdir %desfolder%
)
if not exist %desfolder%\ (
    echo Destination folder not exist !
	goto commonexit
) 

::extract setting: extract to "folder\"
echo Extract to "filenamefolder\" (yes/no): yes
set isextractto=yes
set /p isextractto=
if "%isextractto%" == "" (
	isextractto=yes
)

::extract setting: extract overwrite
echo Extract overwrite (yes/no): yes
set isextractoverwrite=yes
set /p isextractoverwrite=
if "%isextractoverwrite%" == "yes" (
	set isextractoverwrite=-y x
) else (
	set isextractoverwrite=x
)

::extract
echo Do you want start extract (yes/no): no
set confirmyesorno=no
set /p confirmyesorno=
if "%confirmyesorno%"=="yes" (
	for %subfolder% %%f in (%file_ext%) do (
		echo -------------------------------------------
		if "%isextractto%" == "yes" (
			echo Extracting... %app7z% %isextractoverwrite% "%%f" -o"%desfolder%\%%~nf\"
			%app7z% %isextractoverwrite% "%%f" -o"%desfolder%\%%~nf\"
		) else (
			echo Extracting... %app7z% %isextractoverwrite% "%%f" -o"%desfolder%"
			%app7z% %isextractoverwrite% "%%f" -o"%desfolder%"
		)
		echo -------------------------------------------
	)
	echo Extacted !
) else (
	echo Cancel !
)

goto commonexit


::------------------------------------------------------
::     6.Delete all file
::------------------------------------------------------
:deletefile
::check argument
set file_ext=%3
if "%subfolder%" == "/s" (
	set  subfolder=/r
) else (
	set  subfolder=
	set file_ext=%2
)

if "%file_ext%" == "" set  file_ext=*.*

::scan file
set isfileexists=false
echo ----- List file below will be delete ------
for %subfolder% %%f in (%file_ext%) do (
	echo %%f
	set isfileexists=true
)
echo -------------------------------------------

::check file exists
if "%isfileexists%" == "false" (
	echo Notthing to delete !
	goto commonexit
)

::detete
echo Do you want delete (yes/no): no
set confirmyesorno=no
set /p confirmyesorno=
if "%confirmyesorno%"=="yes" (
	for %subfolder% %%f in (%file_ext%) do (
		echo Deleting... %%f
		del /q /f "%%f"
	)
	echo Deleted !
) else (
	echo Cancel !
)
goto commonexit



::------------------------------------------------------
::     7.Delete all directory
::------------------------------------------------------
:deletedirectory
::check argument
set folder_filter=%3
if "%subfolder%" == "/s" (
	set  subfolder=/r
) else (
	set  subfolder=
	set folder_filter=%2
)

if "%folder_filter%" == "" set  folder_filter=*

::scan
set isfolderexists=false
echo ----- List folder below will be delete ------
for /d %subfolder% %%x in (%folder_filter%) do (
	echo %%x
	set isfolderexists=true
)
echo -------------------------------------------

::check folder exit
if "%isfolderexists%" == "false" (
	echo Nothing to delete !
	goto commonexit
)

::delete
echo Do you want delete (yes/no): no
set confirmyesorno=no
set /p confirmyesorno=
if "%confirmyesorno%"=="yes" (
	for /d %subfolder% %%x in (%folder_filter%) do (
		echo Deleting... %%x
		rmdir /q /s "%%x"
	)
	echo Deleted !
) else (
	echo Cancel !
)

goto commonexit


::------------------------------------------------------
::     8.Install this app to %appdata% folder
::------------------------------------------------------
:install
cd %~dp0
set install_folder=%appdata%\%appname%
if not exist %install_folder%\ (
    echo Creating installation folder: %install_folder%
	mkdir %install_folder%
) 

echo Copying [%appname%.bat] to [%install_folder%]
copy %appname%.bat %install_folder%\%appname%.bat

echo "%PATH%" | findstr "%install_folder%">nul && (
    echo Update finished !
) || (
	setx PATH "%PATH%;%install_folder%\;"
	echo Install finished !
)
goto commonexit


::------------------------------------------------------
::     9.Uninstall this app from %appdata% folder
::------------------------------------------------------
:uninstall
set install_folder=%appdata%\%appname%
echo Uninstall %install_folder%\%appname%.bat 
del %install_folder%\%appname%.bat
goto commonexit


::------------------------------------------------------
::     Exit
::------------------------------------------------------
:commonexit
echo:

