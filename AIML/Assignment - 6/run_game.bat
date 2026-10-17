@echo off
title Chess Knight Escape — AI Pathfinding Game
cd /d "%~dp0"
echo.
echo  =========================================
echo   Chess Knight Escape : AI Pathfinding
echo   BFS and A* Search Implementation
echo  =========================================
echo.
echo  Starting game...
echo.
python main.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo  [ERROR] Game failed to start.
    echo  Make sure Python is installed and on PATH.
    pause
)
