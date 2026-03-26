@echo off
setlocal enabledelayedexpansion

set "REPO_URL=https://github.com/SPPL23/NetworkTopologyCalculator/raw/main/dist/NetCalc.exe"
set "EXE_NAME=netcalc.exe"

echo -------------------------------------------------------
echo Network Topology Calculator: Automatic Setup
echo -------------------------------------------------------
echo.

:: 1. Download
echo Downloading %EXE_NAME%...
bitsadmin /transfer "NetCalcDownload" /download /priority FOREGROUND "%REPO_URL%" "%CD%\temp_download.exe" >nul

if not exist "temp_download.exe" (
    echo.
    echo [ERROR] Download failed. 
    echo Please check your internet or Windows Security settings.
    pause
    exit /b
)

:: 2. Finalize File
if exist "%EXE_NAME%" del /f /q "%EXE_NAME%"
ren "temp_download.exe" "%EXE_NAME%"
echo Success! %EXE_NAME% is ready.

:: 3. Automatic Path Setup
echo.
echo Updating User PATH...

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

timeout /t 3
endlocal
