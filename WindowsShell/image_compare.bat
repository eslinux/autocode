@echo off

for %%f in (*.png *.jpg *.bmp) do (
	call :magick_cmp "%%f"
)

:magick_cmp
	FOR /F %%A in ('magick.exe compare -metric AE girl1.jpg %1 null: 2^>^&1') DO set pixelDiff=%%A
	echo %pixelDiff%, %1







