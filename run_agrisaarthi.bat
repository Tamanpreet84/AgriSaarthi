@echo off
title AgriSaarthi Platform Unified Launcher (ASP.NET Core & SQL Server)
color 0A

:: Resolve Root Directory (works from agrisaarthi folder, New folder (2), or Desktop)
set "ROOT_DIR=%~dp0"
if not exist "%ROOT_DIR%backend\AgriSaarthi.Api" (
    set "ROOT_DIR=C:\Users\taman\OneDrive\Desktop\agrisaarthi\"
)

echo ======================================================================
echo             AGRISAARTHI PLATFORM UNIFIED LAUNCHER
echo          ASP.NET Core 10 · SQL Server LocalDB · React · AI
echo                        KNOW MORE - GROW MORE
echo ======================================================================
echo Project Root: %ROOT_DIR%
echo.

echo [1/5] Ensuring Microsoft SQL Server LocalDB is active...
sqllocaldb start mssqllocaldb >nul 2>&1
echo       SQL Server instance 'mssqllocaldb' is ready.

echo.
echo [2/5] Starting AI Prediction Service (FastAPI) on port 8000...
if exist "%ROOT_DIR%ai-service\venv\Scripts\python.exe" (
    start "AgriSaarthi AI Microservice (Port 8000)" /min cmd /c "cd /d "%ROOT_DIR%ai-service" && .\venv\Scripts\python -m uvicorn main:app --host 0.0.0.0 --port 8000"
) else (
    start "AgriSaarthi AI Microservice (Port 8000)" /min cmd /c "cd /d "%ROOT_DIR%ai-service" && python -m uvicorn main:app --host 0.0.0.0 --port 8000"
)
echo       AI service running on http://localhost:8000

echo.
echo [3/5] Starting React Frontend on port 5173...
start "AgriSaarthi React Frontend (Port 5173)" /min cmd /c "cd /d "%ROOT_DIR%frontend" && npm run dev"
echo       React + Vite frontend running on http://localhost:5173

echo.
echo [4/5] Launching Browser in 4 seconds...
start /min cmd /c "timeout /t 4 >nul && start http://localhost:5173/register && start http://localhost:5000/market-prices"

echo.
echo [5/5] Launching ASP.NET Core 10 Web Application (C# & Razor) on port 5000...
echo.
echo ======================================================================
echo  Web Portal (Razor Views): http://localhost:5000
echo  Live Mandi Rates:         http://localhost:5000/market-prices
echo  Disease Detection:        http://localhost:5000/disease-detection
echo  React Frontend:           http://localhost:5173
echo  Backend REST API:         http://localhost:5000/api
echo  Swagger / Health Check:   http://localhost:5000/api/health
echo ======================================================================
echo  Press Ctrl+C to stop the ASP.NET Core server.
echo ======================================================================
echo.

cd /d "%ROOT_DIR%backend\AgriSaarthi.Api"
dotnet run --launch-profile http

pause
