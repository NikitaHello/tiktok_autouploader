@echo off
echo. > Logging\app.log
echo Starting manager.py > Logging\log.txt
call venv\Scripts\activate.bat
python manager.py