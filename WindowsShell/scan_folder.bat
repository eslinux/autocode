@echo off

echo Input copy destination folder:
set /p des_dir=""

echo %des_dir%
mkdir %des_dir%
if not exist %des_dir%\ (
    echo Could not create description folder
	exit 1
) else (
	echo Created folder OK
)

::deep=0 current folder
for /d %%x in (*) do (
    ::go to deep=1
	cd %%x
	for /d %%y in (*) do (
		echo copying... %cd%\%%x\%%y to %des_dir%
		::copy deep=3 to des folder
		xcopy %%y\ %des_dir% /E /H /C /I /Y /Q
	)
	cd ..
)
