# Tkinter Calculator App

A simple calculator desktop app using Python's Tkinter, split into multiple files for maintainability.

## Structure
- `app.py`: Entry point to launch the calculator.
- `gui.py`: Contains the GUI logic and layout.
- `logic.py`: Handles safe evaluation of math expressions.
- `resources/`: Contains the icon image and resource loader.

## Requirements
- Python 3.7+
- `Pillow` (for icon display)

## Install dependencies
```powershell
pip install pillow
```

## Run the app
```powershell
python app.py
```


## Build to CalculatorApp.exe
```powershell
powershell -ExecutionPolicy Bypass -File build_exe.ps1
```
CalculatorApp.exe will be build in to dist folder.


## Notes
- The calculator supports basic math and some functions (sin, cos, pi, etc.).
- The icon is loaded from a base64-encoded PNG.
