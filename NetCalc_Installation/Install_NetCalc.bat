@echo off
setlocal enabledelayedexpansion

set "REPO_URL=https://github.com/SPPL23/NetworkTopologyCalculator/raw/main/dist/NetCalc.exe"
set "EXE_NAME=NetCalc.exe"

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
echo Downloading %EXE_NAME% via BITS...

:: Using BITSAdmin (Trusted Windows Service)
bitsadmin /transfer "NetCalcDownload" /download /priority FOREGROUND "%REPO_URL%" "%CD%\%EXE_NAME%"

if not exist "%EXE_NAME%" (
    echo.
    echo [ERROR] BITS download failed. 
    echo Windows Security is heavily restricting file creation.
    echo Please manually download NetCalc.exe from the repository.
    pause
    exit /b
)

echo Success! %EXE_NAME% downloaded.
echo.
echo -------------------------------------------------------
echo Environment Variable Setup
echo -------------------------------------------------------
echo.
echo [Y] - Add this folder to your User PATH
echo [N] - Skip
echo.

choice /C YN /M "Do you want to set the environment variable?"

if %ERRORLEVEL% EQU 1 (
    echo Updating User PATH...
    set "CLEAN_PATH=%CD%"
    echo !PATH! | findstr /I /C:"!CLEAN_PATH!" >nul
    if !ERRORLEVEL! NEQ 0 (
        setx PATH "!PATH!;!CLEAN_PATH!"
        echo Success! PATH updated.
    ) else (
        echo Path already exists in environment variables.
    )
) else (
    echo Skipping environment variable setup.
)

echo.
echo Process complete!
explorer .

pause
endlocal