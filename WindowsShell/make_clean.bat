@echo off
::------------
:: Delete ./*/{bin, obj, x64, debug, release} folder
::------------
::del /q /f /s "./AsyncSocketClient/bin"
::rmdir /q /s "./AsyncSocketClient/obj"

for /d %%x in (*) do (
	rmdir /q /s  "./%%x/bin"
	rmdir /q /s  "./%%x/obj"
	rmdir /q /s  "./%%x/x64"
	rmdir /q /s  "./%%x/debug"
	rmdir /q /s  "./%%x/release"
)