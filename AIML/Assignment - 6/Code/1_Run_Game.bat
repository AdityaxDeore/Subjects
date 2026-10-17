@echo off
title Chess Knight Escape — AI Pathfinding Game
cd /d "%~dp0"
echo.
echo  =====================================================
echo    Chess Knight Escape : AI Pathfinding Game
echo    BFS and A* Search Implementation
echo    AIML Assignment No. 6  ^|  PRN: 124B1F116
echo  =====================================================
echo.
echo  [1] board.py        - Board state and move rules
echo  [2] pathfinding.py  - BFS and A* algorithms
echo  [3] game.py         - Game state machine
echo  [4] main.py         - GUI (Tkinter)
echo.
echo  Launching game window...
echo.
python main.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo  [ERROR] Could not launch the game.
    echo  Make sure Python 3 is installed and added to PATH.
    echo.
    pause
)
