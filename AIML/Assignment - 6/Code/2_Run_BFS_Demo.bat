@echo off
title BFS Demo — Chess Knight Escape
cd /d "%~dp0"
echo.
echo  =====================================================
echo    BFS DEMO : Breadth-First Search on Knight Board
echo    a8 (0,0) to h1 (7,7)
echo  =====================================================
echo.
python -c "
from board import Board
from pathfinding import bfs

FILES = 'abcdefgh'

def cell(r,c): return FILES[c] + str(8-r)

# ----- Test 1: Clear board -----
print('=' * 52)
print('  TEST 1 : Clear board  (a8 -> h1)')
print('=' * 52)
b = Board()
path, explored = bfs(b)
print(f'  Path length    : {len(path)-1} moves')
print(f'  Nodes explored : {len(explored)}')
print(f'  Path  : {\" -> \".join(cell(r,c) for r,c in path)}')
print()

# ----- Test 2: 10 random obstacles -----
import random; random.seed(7)
print('=' * 52)
print('  TEST 2 : 10 Random obstacles  (a8 -> h1)')
print('=' * 52)
b2 = Board()
cands = [(r,c) for r in range(8) for c in range(8) if (r,c) not in ((0,0),(7,7))]
b2.blocked = set(random.sample(cands, 10))
path2, exp2 = bfs(b2)
print(f'  Obstacles      : {sorted(b2.blocked)}')
print(f'  Path length    : {len(path2)-1} moves')
print(f'  Nodes explored : {len(exp2)}')
print(f'  Path  : {\" -> \".join(cell(r,c) for r,c in path2)}')
print()

# ----- Test 3: Goal unreachable -----
print('=' * 52)
print('  TEST 3 : Goal surrounded (failure terminal)')
print('=' * 52)
b3 = Board()
b3.blocked = {(5,6),(6,5),(5,5),(6,6)}
path3, exp3 = bfs(b3)
print(f'  Nodes explored : {len(exp3)}')
if path3:
    print(f'  Path  : {\" -> \".join(cell(r,c) for r,c in path3)}')
else:
    print('  Result : NO PATH FOUND (failure terminal state)')
print()
"
if %ERRORLEVEL% NEQ 0 pause
echo.
echo  Done. Press any key to close.
pause > nul
