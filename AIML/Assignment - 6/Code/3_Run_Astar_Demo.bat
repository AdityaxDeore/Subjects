@echo off
title A* Demo — Chess Knight Escape
cd /d "%~dp0"
echo.
echo  =====================================================
echo    A* DEMO : A* Search on Knight Board
echo    Chebyshev Heuristic  h(n) = max(dr,dc) / 2
echo  =====================================================
echo.
python -c "
from board import Board
from pathfinding import astar

FILES = 'abcdefgh'

def cell(r,c): return FILES[c] + str(8-r)
def h(r,c,gr,gc): return max(abs(r-gr),abs(c-gc))/2

# ----- Test 1: Clear board -----
print('=' * 52)
print('  TEST 1 : Clear board  (a8 -> h1)')
print('=' * 52)
b = Board()
path, explored = astar(b)
print(f'  Path length    : {len(path)-1} moves')
print(f'  Nodes explored : {len(explored)}')
print(f'  Path  : {\" -> \".join(cell(r,c) for r,c in path)}')
print()
print('  Step-by-step f=g+h along path:')
gr, gc = b.goal
for i,(r,c) in enumerate(path):
    hv = h(r,c,gr,gc)
    print(f'    Step {i}: {cell(r,c):4s}  g={i}  h={hv:.1f}  f={i+hv:.1f}')
print()

# ----- Test 2: 10 random obstacles -----
import random; random.seed(7)
print('=' * 52)
print('  TEST 2 : 10 Random obstacles  (a8 -> h1)')
print('=' * 52)
b2 = Board()
cands = [(r,c) for r in range(8) for c in range(8) if (r,c) not in ((0,0),(7,7))]
b2.blocked = set(random.sample(cands, 10))
path2, exp2 = astar(b2)
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
path3, exp3 = astar(b3)
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
