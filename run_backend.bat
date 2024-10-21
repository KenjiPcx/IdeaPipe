@echo off
:: Activate virtual environment
call venv\Scripts\activate

:: Install dependencies
pip install -r requirements.txt

:: Run the FastAPI server
uvicorn app.main:app --reload