@echo off
setlocal enabledelayedexpansion

set "REPO_URL=https://github.com/SPPL23/NetworkTopologyCalculator/raw/main/dist/NetCalc.exe"
set "EXE_NAME=netcalc.exe"

echo -------------------------------------------------------
echo Network Topology Calculator Installer
echo -------------------------------------------------------
echo.
echo [Y] - Download %EXE_NAME% to this folder
echo [N] - Cancel and exit
echo.

choice /C YN /M "Proceed with download?"

if %ERRORLEVEL% EQU 2 (
    echo.
    echo Installation cancelled.
    pause
    exit /b
)

echo.
echo Downloading file via BITS...

:: Download to a temporary file first
bitsadmin /transfer "NetCalcDownload" /download /priority FOREGROUND "%REPO_URL%" "%CD%\temp_download.exe" >nul

if not exist "temp_download.exe" (
    echo.
    echo [ERROR] Download failed. 
    echo Please check your internet or Windows Security settings.
    pause
    exit /b
)

:: Ensure the target filename is exactly netcalc.exe
if exist "%EXE_NAME%" del /f /q "%EXE_NAME%"
ren "temp_download.exe" "%EXE_NAME%"

echo Success! %EXE_NAME% is ready.
echo.
echo -------------------------------------------------------
echo Environment Variable Setup (PowerShell Method)
echo -------------------------------------------------------
echo.
echo [Y] - Add this folder to your User PATH
echo [N] - Skip
echo.

choice /C YN /M "Do you want to set the environment variable?"

if %ERRORLEVEL% EQU 1 (
    echo.
    echo Updating User PATH via PowerShell...
    
    :: This version handles paths with spaces perfectly
    powershell -NoProfile -Command ^
        "$dir = [System.IO.Path]::GetFullPath('%CD%');" ^
        "$oldPath = [Environment]::GetEnvironmentVariable('PATH', 'User');" ^
        "if ($oldPath -split ';' -notcontains $dir) {" ^
            "$newPath = if ([string]::IsNullOrWhiteSpace($oldPath)) { $dir } else { $oldPath + ';' + $dir };" ^
            "[Environment]::SetEnvironmentVariable('PATH', $newPath, 'User');" ^
            "Write-Host 'Success: Path added to User variables.';" ^
        "} else {" ^
            "Write-Host 'Notice: Path already exists in User variables.';" ^
        "}"
) else (
    echo Skipping environment variable setup.
)

echo.
echo -------------------------------------------------------
echo INSTALLATION COMPLETE
echo -------------------------------------------------------
echo 1. CLOSE THIS WINDOW.
echo 2. OPEN A NEW COMMAND PROMPT.
echo 3. TYPE 'netcalc' TO RUN.
echo -------------------------------------------------------
echo Opening installation folder...
explorer .

pause
endlocal
