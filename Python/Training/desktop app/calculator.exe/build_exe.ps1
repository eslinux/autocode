# PowerShell script to build calculator app to a single .exe using PyInstaller
# cd to project folder
# run command:
# powershell -ExecutionPolicy Bypass -File build_exe.ps1

# Ensure you are in the calculator directory
Set-Location -Path $PSScriptRoot

# Remove previous build/dist if exists
if (Test-Path dist) { Remove-Item -Recurse -Force dist }
if (Test-Path build) { Remove-Item -Recurse -Force build }
if (Test-Path calculator.spec) { Remove-Item calculator.spec }

# Build the .exe
pyinstaller --onefile --noconsole --name CalculatorApp app.py


# pyinstaller --onefile --noconsole --add-data "resources;resources" --hidden-import=gui --name CalculatorApp app.py

Write-Host "Build complete. The .exe is in the 'dist' folder."
