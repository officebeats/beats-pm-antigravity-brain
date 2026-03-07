@echo off
echo Starting Beats PM Brain Companion App...
echo.

:: Start backend
echo [1/2] Starting FastAPI backend on http://localhost:8000
start "Beats PM Backend" cmd /k "cd /d %~dp0backend && pip install -r requirements.txt -q && uvicorn main:app --reload --port 8000"

:: Wait a moment for backend to start
timeout /t 3 /nobreak >nul

:: Start frontend
echo [2/2] Starting React frontend on http://localhost:5173
start "Beats PM Frontend" cmd /k "cd /d %~dp0frontend && npm install --silent && npm run dev"

echo.
echo App starting... open http://localhost:5173 in your browser.
echo Close the two terminal windows to stop the app.
