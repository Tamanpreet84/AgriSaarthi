@echo off
title AgriSaarthi ASP.NET Core & SQL Server Platform
color 0A
echo ======================================================================
echo             AGRISAARTHI ASP.NET CORE & SQL SERVER SYSTEM
echo                        KNOW MORE - GROW MORE
echo ======================================================================
echo.

echo [1/4] Ensuring Microsoft SQL Server LocalDB is active...
sqllocaldb start mssqllocaldb >nul 2>&1

echo.
echo [2/4] Starting AI Prediction Service (FastAPI) on port 8000...
start "AgriSaarthi AI Microservice" /min cmd /c "cd /d "%~dp0ai-service" && .\venv\Scripts\python -m uvicorn main:app --host 0.0.0.0 --port 8000"

echo.
echo [3/4] Starting React Frontend on port 5173...
start "AgriSaarthi React Frontend" /min cmd /c "cd /d "%~dp0frontend" && npm run dev"

echo.
echo [4/4] Launching ASP.NET Core 10 Web Application (C# & Razor) on port 5000...
echo.
echo ======================================================================
echo  ASP.NET Core Razor Portal: http://localhost:5000
echo  React + Vite Frontend:     http://localhost:5173
echo  Backend REST API:          http://localhost:5000/api
echo ======================================================================
echo.
cd /d "%~dp0backend\AgriSaarthi.Api"
dotnet run --launch-profile http

pause
