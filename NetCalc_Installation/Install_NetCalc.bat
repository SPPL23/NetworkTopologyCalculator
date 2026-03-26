@echo off
setlocal enabledelayedexpansion

set "REPO_URL=https://github.com/SPPL23/NetworkTopologyCalculator/raw/main/dist/NetCalc.exe"
set "EXE_NAME=NetCalc.exe"

echo -------------------------------------------------------
echo Network Topology Calculator: Automatic Setup
echo -------------------------------------------------------
echo.

:: 1. Download
echo Downloading %EXE_NAME%...
:: We now download directly to %EXE_NAME%
bitsadmin /transfer "NetCalcDownload" /download /priority FOREGROUND "%REPO_URL%" "%CD%\%EXE_NAME%" >nul

if not exist "%EXE_NAME%" (
    echo.
    echo [ERROR] Download failed. 
    echo Please check your internet or Windows Security settings.
    pause
    exit /b
)

:: 2. Finalize File
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
echo 3. TYPE 'NetCalc' TO RUN.
echo -------------------------------------------------------
echo Opening installation folder...
explorer .

timeout /t 3
endlocal
