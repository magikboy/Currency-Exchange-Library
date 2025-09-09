@echo off
echo 🎯 Remote Currency Exchange Execution
echo =====================================

if "%1"=="" (
    echo Usage:
    echo   %0 ^<remote_ip^>        Execute on specific remote Docker host
    echo   %0 --scan [network]    Scan local network for Docker hosts
    echo.
    echo Examples:
    echo   %0 192.168.1.100
    echo   %0 --scan 192.168.1
    pause
    exit /b 1
)

echo [INFO] Starting remote execution...
python remote_docker.py %*

echo.
echo [INFO] Checking local logs...
if exist .remote_execution.log (
    echo [LOG] Recent remote executions:
    powershell "Get-Content .remote_execution.log -Tail 3"
) else (
    echo [LOG] No remote execution log found
)

echo.
echo ✅ Remote execution completed
pause
