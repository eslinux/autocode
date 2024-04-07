@echo off
SETLOCAL

::Enable virtual environment (for example ".venv") and show version
set apps_dir=%~dp0
call "%apps_dir%.venv\Scripts\activate.bat"
python -V
pip -V

::run python script here
::python %apps_dir%test_openpyxl.py

::Deactive 
call "%apps_dir%.venv\Scripts\deactivate.bat"
ENDLOCAL
