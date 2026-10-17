@echo off
title BFS vs A* Comparison — Chess Knight Escape
cd /d "%~dp0"
echo.
echo  =====================================================
echo    BFS vs A* : Full Comparison Across 5 Scenarios
echo    AIML Assignment No. 6  ^|  PRN: 124B1F116
echo  =====================================================
echo.
python -c "
from board import Board
from pathfinding import bfs, astar
import random

FILES = 'abcdefgh'
def cell(r,c): return FILES[c] + str(8-r)

def run_both(b, label):
    pb, eb = bfs(b)
    pa, ea = astar(b)
    ml_b = len(pb)-1 if pb else -1
    ml_a = len(pa)-1 if pa else -1
    saving = round((1 - len(ea)/len(eb))*100) if eb else 0
    terminal = 'GOAL (solved)' if pb else 'FAILURE (no path)'
    print(f'  Scenario: {label}')
    print(f'  Terminal State : {terminal}')
    print(f'  BFS  -> moves={ml_b if ml_b>=0 else \"N/A\":>3},  nodes={len(eb):>3}')
    print(f'  A*   -> moves={ml_a if ml_a>=0 else \"N/A\":>3},  nodes={len(ea):>3}  ({saving:+}% vs BFS)')
    if pb:
        print(f'  Path : {\" -> \".join(cell(r,c) for r,c in pb)}')
    print()

print()

# Scenario 1
b1 = Board()
run_both(b1, 'Clear board  (a8 -> h1)  |  0 obstacles')

# Scenario 2
random.seed(7)
b2 = Board()
cands = [(r,c) for r in range(8) for c in range(8) if (r,c) not in ((0,0),(7,7))]
b2.blocked = set(random.sample(cands, 10))
run_both(b2, 'Sparse obstacles  (a8 -> h1)  |  10 obstacles')

# Scenario 3
b3 = Board(); b3.knight=(0,1); b3.goal=(6,6)
run_both(b3, 'Different positions  (b8 -> g2)  |  0 obstacles')

# Scenario 4
random.seed(42)
b4 = Board()
b4.blocked = set(random.sample(cands, 15))
run_both(b4, 'Dense obstacles  (a8 -> h1)  |  15 obstacles')

# Scenario 5
b5 = Board()
b5.blocked = {(5,6),(6,5),(5,5),(6,6)}
run_both(b5, 'Goal surrounded  (a8 -> h1)  |  4 obstacles around goal')
"
if %ERRORLEVEL% NEQ 0 pause
echo.
echo  Done. Press any key to close.
pause > nul
