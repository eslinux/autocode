@echo off
SETLOCAL
::Author: ninhld
::Create on: 2022/04/30

::show all input argument 
::for %%I IN (%*) DO ECHO %%I




::------------------------------------------------------
::     App info
::------------------------------------------------------
set appversion=1.1.0

::------------------------------------------------------
::     3rd empty
::------------------------------------------------------
set app7z="C:\Program Files\7-Zip\7z.exe"

::------------------------------------------------------
::     Internal variable
::------------------------------------------------------
set /A target_counter=0

::------------------------------------------------------
::     Argument parser
::------------------------------------------------------
::Get main parameter
set appname=%0
set cmd=%1

::read include subfolder setting
set include_subfolders=/r
if "%2" == "-ns" (
	set include_subfolders=
	SHIFT 
)
SHIFT

::read target filter setting
set target_filter=
:arg_target_filter_start
if "%1"=="" (goto :arg_target_filter_end)
set target_filter=%target_filter% %1
SHIFT
goto :arg_target_filter_start
:arg_target_filter_end


::Switch command
IF "%cmd%"=="help" goto showhelp
IF "%cmd%"=="version" goto showversion
IF "%cmd%"=="install" goto install
IF "%cmd%"=="uninstall" goto uninstall

IF "%cmd%"=="ls" goto listall
IF "%cmd%"=="lsf" goto listfile
IF "%cmd%"=="lsd" goto listdirectory
IF "%cmd%"=="cpf" goto copyfile
IF "%cmd%"=="cpfx" goto copyxfile
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
echo      %appname% ls [-ns]
echo:
echo   2. List all file
echo      %appname% lsf [-ns] [file filter (Ex: *test.txt)]
echo:
echo   3. List all folder
echo      %appname% lsd [-ns] [folder filter (Ex: *import*)]
echo:
echo   4. Copy file
echo      %appname% cpf [-ns] [file filter (Ex: *test.txt)]
echo:
echo   5. Copy file with folders and subfolders recursively
echo      %appname% cpfx src_folder\*.log des_folder 
echo:
echo   6. Extract zip or 7zip file
echo      %appname% exf [-ns] [file filter (Ex: *test.7z)]
echo:
echo   7. Delete all file
echo      %appname% delf [-ns] [file filter (Ex: *test.txt)]
echo:
echo   8. Delete all folder
echo      %appname% deld [-ns] [folder filter (Ex: *import*)]
::echo:
::echo   9. Install this app to [%appdata%\%appname%] folder
::echo      %appname% install
::echo:
::echo   10. Uninstall this app from [%appdata%\%appname%] folder
::echo      %appname% uninstall
echo:
echo Parameter descriptions:
echo 	-ns : Do not include sub-folder. Option parameter
echo:
pause
goto commonexit




::------------------------------------------------------
::     1.List all file & directory
::------------------------------------------------------
:listall
if "%include_subfolders%" == "/r" set include_subfolders=/s
echo ------ List of folder and files ------ 
dir /b %include_subfolders%
echo --------------------------------------
goto commonexit



::------------------------------------------------------
::     2.List all file
::------------------------------------------------------
:listfile
::check input argument
if "%target_filter%" == "" set  target_filter=*.*

::scan
echo ----------- List of files ----------
for %include_subfolders% %%f in (%target_filter%) do (
	set /A target_counter=target_counter+1
	echo %%f
)
echo ------------(%target_counter% files)---------------
goto commonexit



::------------------------------------------------------
::     3.List all directory
::------------------------------------------------------
:listdirectory
if "%target_filter%" == "" set  target_filter=*

::scan
echo ----------- List of folder -----------
for /d %include_subfolders% %%x in (%target_filter%) do (
	set /A target_counter=target_counter+1
	echo %%x
)
echo ------------(%target_counter% folders)---------------
goto commonexit



::------------------------------------------------------
::     4.Copy file
::------------------------------------------------------
:copyfile
::check argument
if "%target_filter%" == "" set  target_filter=*.*

::scan file
echo ----- List file below will be copied ------
for %include_subfolders% %%f in (%target_filter%) do (
	set /A target_counter=target_counter+1
	echo %%f
)
echo ----------------(%target_counter% files)-----------------

::check file exists
if "%target_counter%" == "0" (
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

if not exist "%desfolder%"\ (
	mkdir "%desfolder%"
)
if not exist "%desfolder%"\ (
    echo Destination folder not exist !
	goto commonexit
) 

::copy
echo Do you want copy (yes/no): no
set confirmyesorno=no
set /p confirmyesorno=
if "%confirmyesorno%"=="yes" (
	for %include_subfolders% %%f in (%target_filter%) do (
		echo Copying... [%%f]
		copy "%%f" "%desfolder%"
	)
) else (
	echo Cancel !
)

goto commonexit



::------------------------------------------------------
::     5.Copies folders and subfolders recursively excluding the empty one.
::------------------------------------------------------
:copyxfile
XCOPY %target_filter% /S /Y
goto commonexit


::------------------------------------------------------
::     6.Extract zip or 7z file
::------------------------------------------------------
:extractfile

::check 7zip application
if not exist %app7z% (
	echo 7zip application have not already installed.
	echo Please install 7zip first and tray again !
	goto commonexit
)


::check argument
if "%target_filter%" == "" set  target_filter=*.7z *.zip

::scan file
echo ----- List file below will be extracted ------
for %include_subfolders% %%f in (%target_filter%) do (
	set /A target_counter=target_counter+1
	echo %%f
)
echo -----------------(%target_counter% files)------------------

::check file exists
if "%target_counter%" == "0" (
	echo Notthing to extract !
	goto commonexit
)


:: Enter copy destination folder
echo Please input extract destination folder: %cd%
set desfolder=%cd%
set /p desfolder=

if "%desfolder%" == "" (
	echo Cancel !
	goto commonexit
)

if not exist "%desfolder%"\ (
	mkdir "%desfolder%"
)
if not exist "%desfolder%"\ (
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
	for %include_subfolders% %%f in (%target_filter%) do (
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
) else (
	echo Cancel !
)

goto commonexit


::------------------------------------------------------
::     7.Delete all file
::------------------------------------------------------
:deletefile
::check argument
if "%target_filter%" == "" set  target_filter=*.*


::scan file
echo ------- List file below will be deleted -------
for %include_subfolders% %%f in (%target_filter%) do (
	set /A target_counter=target_counter+1
	echo %%f
)
echo -----------------(%target_counter% files)------------------

::check file exists
if "%target_counter%" == "0" (
	echo Notthing to delete !
	goto commonexit
)


::detete
echo Do you want delete (yes/no): no
set confirmyesorno=no
set /p confirmyesorno=
if "%confirmyesorno%"=="yes" (
	for %include_subfolders% %%f in (%target_filter%) do (
		echo Deleting... [%%f]
		del /q /f "%%f"
	)
) else (
	echo Cancel !
)
goto commonexit



::------------------------------------------------------
::     8.Delete all directory
::------------------------------------------------------
:deletedirectory
::check argument
if "%target_filter%" == "" set  target_filter=*

::scan
echo ----- List folder below will be delete ------
for /d %include_subfolders% %%x in (%target_filter%) do (
	set /A target_counter=target_counter+1
	echo %%x
)
echo -------------------------------------------

::check folder exit
if "%target_counter%" == "0" (
	echo Notthing to delete !
	goto commonexit
)

::delete
echo Do you want delete (yes/no): no
set confirmyesorno=no
set /p confirmyesorno=
if "%confirmyesorno%"=="yes" (
	for /d %include_subfolders% %%x in (%target_filter%) do (
		echo Deleting... [%%x]
		rmdir /q /s "%%x"
	)
) else (
	echo Cancel !
)

goto commonexit


::------------------------------------------------------
::     9.Install this app to %appdata% folder
::------------------------------------------------------
:::install
::cd %~dp0
::set install_folder=%appdata%\%appname%
::if not exist %install_folder%\ (
::    echo Creating installation folder: %install_folder%
::	mkdir %install_folder%
::) 
::
::echo Copying [%appname%.bat] to [%install_folder%]
::copy %appname%.bat %install_folder%\%appname%.bat
::
::echo "%PATH%" | findstr "%install_folder%">nul && (
::    echo Update finished !
::) || (
::	setx PATH "%PATH%;%install_folder%\;"
::	echo Install finished !
::)
::goto commonexit


::------------------------------------------------------
::     10.Uninstall this app from %appdata% folder
::------------------------------------------------------
:::uninstall
::set install_folder=%appdata%\%appname%
::echo Uninstall %install_folder%\%appname%.bat 
::del %install_folder%\%appname%.bat
::goto commonexit


::------------------------------------------------------
::     Exit
::------------------------------------------------------
:commonexit
echo:

ENDLOCAL