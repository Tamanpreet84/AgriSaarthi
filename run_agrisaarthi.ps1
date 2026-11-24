Write-Host "======================================================================" -ForegroundColor Green
Write-Host "                     AGRISAARTHI PLATFORM" -ForegroundColor Green
Write-Host "                    KNOW MORE - GROW MORE" -ForegroundColor Yellow
Write-Host "======================================================================" -ForegroundColor Green
Write-Host ""

Write-Host "[1/4] Ensuring SQL Server LocalDB is active..." -ForegroundColor Cyan
sqllocaldb start mssqllocaldb

Write-Host "[2/4] Starting AI Service (FastAPI) on port 8000..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PSScriptRoot\ai-service'; .\venv\Scripts\python -m uvicorn main:app --host 0.0.0.0 --port 8000"

Write-Host "[3/4] Starting Frontend (React + Vite) on port 5173..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PSScriptRoot\frontend'; npm run dev"

Write-Host "[4/4] Starting Backend (ASP.NET Core Web API) on port 5000..." -ForegroundColor Cyan
cd "$PSScriptRoot\backend\AgriSaarthi.Api"
dotnet run --launch-profile http
