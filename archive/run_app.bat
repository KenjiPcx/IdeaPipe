@echo off
:: Run backend
start cmd /k run_backend.bat

:: Wait a bit for the backend to start
timeout /t 5

:: Run frontend
start cmd /k run_frontend.bat