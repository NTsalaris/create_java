@echo off
echo call creatjava.py

python createjava.py ::change to python3 if not work
if %errorlevel% neq 0 (
  echo Compilation failed.
  pause
  exit /b %errorlevel%
)

pause