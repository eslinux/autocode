@echo off
SETLOCAL

::Enable virtual environment
set apps_dir=%~dp0
call "%apps_dir%.venv\Scripts\activate.bat"


::python %apps_dir%test_openpyxl.py
::echo "%apps_dir%.venv\Scripts\activate.bat"
python -V
pip -V


call "%apps_dir%.venv\Scripts\deactivate.bat"
ENDLOCAL
