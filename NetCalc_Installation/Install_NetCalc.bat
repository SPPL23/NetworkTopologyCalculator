@echo off
setlocal enabledelayedexpansion

:: Configuration
set "REPO_URL=https://github.com/SPPL23/NetworkTopologyCalculator/raw/main/dist/NetCalc.exe"
set "EXE_NAME=netcalc.exe"
set "TEMP_FILE=temp_download.exe"

echo =======================================================
echo Network Topology Calculator: Automatic Installer
echo =======================================================
echo.

:: 1. Download Section
echo [1/3] Downloading %EXE_NAME%...
if exist "%TEMP_FILE%" del /f /q "%TEMP_FILE%"

bitsadmin /transfer "NetCalcDownload" /download /priority FOREGROUND "%REPO_URL%" "%CD%\%TEMP_FILE%" >nul

if not exist "%TEMP_FILE%" (
    echo.
    echo [ERROR] Download failed. 
    echo Please check your internet connection or Windows Security settings.
    pause
    exit /b
)

:: 2. File Finalization
echo [2/3] Finalizing file...
if exist "%EXE_NAME%" del /f /q "%EXE_NAME%"
ren "%TEMP_FILE%" "%EXE_NAME%"

:: 3. Environment Variable Setup
echo [3/3] Updating User PATH...

powershell -NoProfile -Command ^
    "$dir = [System.IO.Path]::GetFullPath('%CD%');" ^
    "$oldPath = [Environment]::GetEnvironmentVariable('PATH', 'User');" ^
    "if ($oldPath -split ';' -notcontains $dir) {" ^
        "$newPath = if ([string]::IsNullOrWhiteSpace($oldPath)) { $dir } else { $oldPath + ';' + $dir };" ^
        "[Environment]::SetEnvironmentVariable('PATH', $newPath, 'User');" ^
        "Write-Host 'Success: Folder added to PATH.';" ^
    "} else {" ^
        "Write-Host 'Notice: Folder already exists in PATH.';" ^
    "}"

echo.
echo =======================================================
echo INSTALLATION COMPLETE
echo =======================================================
echo 1. Close this window.
echo 2. Open a NEW Command Prompt (to refresh PATH).
echo 3. Type 'netcalc' to run your calculator.
echo =======================================================
echo Opening installation folder...
explorer .

timeout /t 5
endlocal
