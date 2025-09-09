#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Remote Currency Exchange Execution for Supply Chain Backdoor Simulation

.DESCRIPTION
    Executes the currency exchange library on remote Docker environments
    while logging results locally for supply chain attack simulation.

.PARAMETER RemoteHost
    Remote Docker host IP address or hostname

.PARAMETER Scan
    Scan local network for available Docker hosts

.PARAMETER NetworkRange
    Network range to scan (default: 192.168.1)

.EXAMPLE
    .\remote_execute.ps1 -RemoteHost 192.168.1.100

.EXAMPLE
    .\remote_execute.ps1 -Scan -NetworkRange "192.168.1"
#>

param(
    [string]$RemoteHost,
    [switch]$Scan,
    [string]$NetworkRange = "192.168.1"
)

Write-Host "🎯 Remote Currency Exchange Execution" -ForegroundColor Cyan
Write-Host "=====================================" -ForegroundColor Cyan

if ($Scan) {
    Write-Host "[INFO] Scanning network range: $NetworkRange.1-254" -ForegroundColor Green
    python remote_docker.py --scan $NetworkRange
} elseif ($RemoteHost) {
    Write-Host "[INFO] Executing on remote host: $RemoteHost" -ForegroundColor Green
    python remote_docker.py $RemoteHost
} else {
    Write-Host "Usage:" -ForegroundColor Yellow
    Write-Host "  .\remote_execute.ps1 -RemoteHost <ip>     Execute on specific remote Docker host" -ForegroundColor White
    Write-Host "  .\remote_execute.ps1 -Scan [-NetworkRange <range>]  Scan local network" -ForegroundColor White
    Write-Host ""
    Write-Host "Examples:" -ForegroundColor Yellow
    Write-Host "  .\remote_execute.ps1 -RemoteHost 192.168.1.100" -ForegroundColor White
    Write-Host "  .\remote_execute.ps1 -Scan -NetworkRange '192.168.1'" -ForegroundColor White
    return
}

# Check local logs
Write-Host ""
Write-Host "[INFO] Checking local logs..." -ForegroundColor Green

if (Test-Path ".remote_execution.log") {
    Write-Host "[LOG] Recent remote executions:" -ForegroundColor Blue
    Get-Content .remote_execution.log -Tail 3 | ForEach-Object {
        Write-Host "  $_" -ForegroundColor Gray
    }
} else {
    Write-Host "[LOG] No remote execution log found" -ForegroundColor Yellow
}

# Check system metrics
if (Test-Path ".system_metrics.log") {
    Write-Host ""
    Write-Host "[METRICS] Recent system metrics:" -ForegroundColor Blue
    Get-Content .system_metrics.log -Tail 2 | ForEach-Object {
        Write-Host "  $_" -ForegroundColor Gray
    }
}

Write-Host ""
Write-Host "✅ Remote execution completed" -ForegroundColor Green
