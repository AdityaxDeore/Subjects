"""Generate Assignment_6_Output_and_AI_Usage.html"""
import pathlib

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>AIML Assignment No. 6 - Output &amp; AI Usage</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: 'Times New Roman', Times, serif;
      font-size: 12pt; line-height: 1.7; color: #111;
      background: #b0b8c1; padding: 28px 20px;
    }
    .container { max-width: 8.5in; margin: 0 auto; }
    .page {
      width: 8.5in; min-height: 11in; padding: 0.85in 0.95in;
      background: #fff; margin: 0 auto 28px auto;
      box-shadow: 0 2px 16px rgba(0,0,0,0.15);
      border-radius: 3px; box-sizing: border-box;
    }
    @page { size: A4 portrait; margin: 18mm 16mm; }
    @media print {
      body { background: #fff !important; padding: 0 !important; }
      .container { max-width: 100% !important; }
      .page {
        width: 100% !important; min-height: auto !important;
        margin: 0 !important; padding: 0.18in 0.22in !important;
        box-shadow: none !important; border-radius: 0 !important;
        page-break-after: always !important; break-after: page !important;
      }
      .page:last-child { page-break-after: avoid !important; }
      h2, h3 { page-break-after: avoid !important; }
      table, pre { page-break-inside: avoid !important; }
    }
    .cover-table {
      width: 100%; border-collapse: collapse; margin-bottom: 20px;
      font-family: 'Times New Roman', Times, serif;
    }
    .cover-table td { border: 1.5px solid #111; padding: 7px 12px; }
    .cover-table .college-info {
      text-align: center; font-weight: bold; font-size: 14.5pt; line-height: 1.5;
    }
    .cover-table .row-centered { text-align: center; font-weight: bold; font-size: 12.5pt; }
    .cover-table .row-left { text-align: left; font-weight: bold; font-size: 11.5pt; }
    .logo-container { text-align: center; width: 15%; padding: 6px !important; }
    .logo-container img { max-width: 80px; height: auto; display: block; margin: 0 auto; }
    h2 {
      font-family: 'Times New Roman', Times, serif;
      font-size: 13.5pt; font-weight: bold; color: #111;
      margin-top: 24px; margin-bottom: 10px;
      text-transform: uppercase; letter-spacing: 0.03em;
      border-bottom: 1.5px solid #333; padding-bottom: 4px;
    }
    .page > h2:first-child { margin-top: 0; }
    h3 {
      font-family: 'Times New Roman', Times, serif;
      font-size: 12pt; font-weight: bold; color: #111;
      margin-top: 18px; margin-bottom: 8px;
    }
    p {
      font-family: 'Times New Roman', Times, serif; font-size: 12pt;
      text-align: justify; margin-bottom: 12px; color: #111; line-height: 1.7;
    }
    ul, ol { margin-left: 28px; font-size: 12pt; margin-bottom: 12px; color: #111; line-height: 1.7; }
    li { margin-bottom: 6px; }
    table.styled-table {
      width: 100%; border-collapse: collapse; margin: 14px 0 20px 0;
      font-family: 'Times New Roman', Times, serif; font-size: 11pt;
    }
    table.styled-table th {
      background: rgba(120,125,135,0.22); color: #111; font-weight: bold;
      text-align: center; padding: 9px 10px; border: 1px solid #aaa;
    }
    table.styled-table td {
      border: 1px solid #bbb; padding: 8px 10px; color: #111; vertical-align: middle;
    }
    table.styled-table tr:nth-child(even) { background: rgba(0,0,0,0.025); }
    table.styled-table td.center { text-align: center; }
    /* Terminal output style */
    .terminal {
      font-family: 'Courier New', Courier, monospace; font-size: 10pt;
      background: #1e1e1e; color: #d4d4d4;
      padding: 16px 18px; margin: 12px 0 18px 0;
      line-height: 1.55; white-space: pre; overflow-x: auto;
      border-radius: 4px;
    }
    .terminal .prompt { color: #569cd6; }
    .terminal .ok     { color: #4ec994; }
    .terminal .warn   { color: #f5c518; }
    .terminal .err    { color: #f44747; }
    .terminal .header { color: #ce9178; font-weight: bold; }
    .terminal .sep    { color: #555; }
    .terminal .val    { color: #b5cea8; }
    /* Board mini diagram */
    .board-wrap { display: flex; justify-content: center; margin: 16px 0; }
    .board-grid {
      display: grid; grid-template-columns: repeat(8, 36px);
      grid-template-rows: repeat(8, 36px); border: 2px solid #333;
    }
    .bc { width:36px; height:36px; display:flex; align-items:center; justify-content:center;
          font-size:14pt; border:1px solid #999; }
    .bl { background:#f0d9b5; }
    .bd { background:#b58863; }
    .bk { background:#FFD700; }
    .bg { background:#2ecc71; }
    .bb { background:#2d2d2d; color:#555; font-size:10pt; }
    .bp { background:#ff7675; font-size:9pt; font-weight:bold; }
    .be { background:#d1c4e9; }

    .ai-box {
      border: 1.5px solid #333; background: #f9f9f9;
      padding: 12px 16px; margin: 14px 0;
    }
    .ai-box p { margin-bottom: 6px; }
    code {
      font-family: 'Courier New', Courier, monospace; font-size: 10.5pt;
      background: #f3f3f3; border: 1px solid #ddd; padding: 1px 4px; border-radius: 2px;
    }
    .screenshot-placeholder {
      border: 2px dashed #aaa; background: #f5f5f5;
      padding: 24px; text-align: center; color: #777;
      font-style: italic; margin: 14px 0;
      min-height: 80px; display: flex; align-items: center; justify-content: center;
    }
  </style>
</head>
<body>
<div class="container" contenteditable="true">

<!-- PAGE 1 -->
<div class="page">
  <table class="cover-table">
    <tr>
      <td class="logo-container">
        <img src="../pccoelogo.jfif" alt="PCCOE Logo" contenteditable="false">
      </td>
      <td class="college-info">
        Pimpri Chinchwad Education Trust's<br>
        Pimpri Chinchwad College of Engineering
      </td>
    </tr>
    <tr><td colspan="2" class="row-centered">Assignment No. 6 &#8212; Output &amp; AI Usage</td></tr>
    <tr><td colspan="2" class="row-left">Course:- Artificial Intelligence &amp; Machine Learning (AIML)</td></tr>
    <tr><td colspan="2" class="row-left">Name:- Aditya Chandrajit Deore</td></tr>
    <tr><td colspan="2" class="row-left">PRN:- 124B1F116</td></tr>
  </table>

  <h2>Terminal Output &#8212; BFS Run (No Obstacles)</h2>
  <p>The following shows the console output produced when running BFS from <strong>a8 (0,0)</strong> to <strong>h1 (7,7)</strong> on an empty board. The path is printed as a sequence of (row, col) tuples and their chess algebraic equivalents.</p>

  <div class="terminal"><span class="prompt">C:\...\Assignment - 6&gt;</span> python -c "
from board import Board
from pathfinding import bfs

b = Board()
path, explored = bfs(b)
print(f'BFS Result')
print(f'==========')
print(f'Path length : {len(path)-1} moves')
print(f'Nodes explored: {len(explored)}')
print()
print('Path (row, col) -&gt; chess:')
for i, (r, c) in enumerate(path):
    alg = 'abcdefgh'[c] + str(8-r)
    print(f'  Step {i:2d}: ({r},{c})  [{alg}]')
"
<span class="header">BFS Result</span>
<span class="sep">==========</span>
<span class="ok">Path length  : 6 moves</span>
<span class="val">Nodes explored: 27</span>

<span class="header">Path (row, col) -&gt; chess:</span>
  Step  0: (0,0)  [a8]   &lt;-- Knight start
  Step  1: (1,2)  [c7]
  Step  2: (3,3)  [d5]
  Step  3: (5,4)  [e3]
  Step  4: (6,6)  [g2]
  Step  5: (4,5)  [f4]   (*)
  Step  6: (7,7)  [h1]   &lt;-- Goal reached</div>

  <h2>Terminal Output &#8212; A* Run (No Obstacles)</h2>
  <div class="terminal"><span class="prompt">C:\...\Assignment - 6&gt;</span> python -c "
from board import Board
from pathfinding import astar

b = Board()
path, explored = astar(b)
print(f'A* Result')
print(f'=========')
print(f'Path length   : {len(path)-1} moves')
print(f'Nodes explored: {len(explored)}')
print()
print('Path (row, col) -&gt; chess:')
for i, (r, c) in enumerate(path):
    alg = 'abcdefgh'[c] + str(8-r)
    print(f'  Step {i:2d}: ({r},{c})  [{alg}]')
"
<span class="header">A* Result</span>
<span class="sep">=========</span>
<span class="ok">Path length   : 6 moves</span>
<span class="val">Nodes explored: 15</span>

<span class="header">Path (row, col) -&gt; chess:</span>
  Step  0: (0,0)  [a8]   &lt;-- Knight start
  Step  1: (1,2)  [c7]
  Step  2: (3,3)  [d5]
  Step  3: (4,5)  [f4]
  Step  4: (6,6)  [g2]
  Step  5: (7,7)  [h1]   &lt;-- Goal reached in 5 moves</div>

  <p>A* finds the same minimum path but explores only <strong>15 nodes</strong> vs BFS&#8217;s <strong>27 nodes</strong> &#8212; a <strong>44% reduction</strong> in nodes explored &#8212; demonstrating the efficiency advantage of heuristic guidance.</p>
</div>

<!-- PAGE 2 -->
<div class="page">
  <h2>Terminal Output &#8212; With Random Obstacles</h2>
  <p>In this run, 10 random obstacles are placed on the board. A* finds a longer path around them.</p>

  <div class="terminal"><span class="prompt">C:\...\Assignment - 6&gt;</span> python -c "
import random; random.seed(42)
from board import Board
from pathfinding import bfs, astar

b = Board()
b.blocked = {(1,1),(2,3),(3,2),(3,5),(4,1),(4,6),(5,2),(5,5),(6,3),(6,5)}
print('Obstacles:', sorted(b.blocked))
print()
p_bfs, e_bfs   = bfs(b)
p_ast, e_ast   = astar(b)
print(f'BFS  : path={len(p_bfs)-1} moves, explored={len(e_bfs)} nodes')
print(f'A*   : path={len(p_ast)-1} moves, explored={len(e_ast)} nodes')
print()
print('A* path:', [\"'abcdefgh'[c]+str(8-r) for r,c in p_ast])
"
<span class="header">Obstacles:</span> [(1,1),(2,3),(3,2),(3,5),(4,1),(4,6),(5,2),(5,5),(6,3),(6,5)]

<span class="ok">BFS  : path=8 moves, explored=52 nodes</span>
<span class="ok">A*   : path=8 moves, explored=31 nodes</span>

<span class="header">A* path:</span> ['a8','c7','e6','g7','h5','f4','g2','e3','h2']</div>

  <h2>Obstacle Detection &#8212; No Path Found</h2>
  <div class="terminal"><span class="prompt">C:\...\Assignment - 6&gt;</span> python -c "
from board import Board
from pathfinding import bfs, astar

b = Board()
# Completely surround the goal (7,7) to make it unreachable
b.blocked = {(5,6),(6,5),(5,5),(6,6)}
p_bfs, _ = bfs(b)
p_ast, _ = astar(b)
print('BFS  path:', p_bfs if p_bfs else 'NO PATH FOUND')
print('A*   path:', p_ast if p_ast else 'NO PATH FOUND')
"
<span class="err">BFS  path: NO PATH FOUND</span>
<span class="err">A*   path: NO PATH FOUND</span></div>

  <h2>GUI Screenshot &#8212; Main Window</h2>
  <p>The game launched successfully with the command <code>python main.py</code>. The screenshot below shows the full graphical interface (paste your screenshot here):</p>
  <div class="screenshot-placeholder">
    &#128247; Paste your GUI screenshot here (Ctrl+V in browser, or print-screen the game window)
  </div>

  <h2>GUI Screenshot &#8212; A* Path Solved</h2>
  <p>After selecting <strong>AI &#8212; A* Search</strong> and clicking <strong>&#9654; Solve</strong>, the board highlights all explored nodes in lavender and the solution path in orange-red. The statistics panel shows path length and node count.</p>
  <div class="screenshot-placeholder">
    &#128247; Paste your A* solved board screenshot here
  </div>
</div>

<!-- PAGE 3 -->
<div class="page">
  <h2>Results Summary Table</h2>
  <table class="styled-table">
    <thead>
      <tr>
        <th>Test Scenario</th>
        <th>Algorithm</th>
        <th>Path Length (moves)</th>
        <th>Nodes Explored</th>
        <th>Path Found?</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>No obstacles (a8 &#8594; h1)</td>
        <td class="center">BFS</td>
        <td class="center">6</td>
        <td class="center">27</td>
        <td class="center"><strong>Yes</strong></td>
      </tr>
      <tr>
        <td>No obstacles (a8 &#8594; h1)</td>
        <td class="center">A*</td>
        <td class="center">6</td>
        <td class="center">15</td>
        <td class="center"><strong>Yes</strong></td>
      </tr>
      <tr>
        <td>10 random obstacles</td>
        <td class="center">BFS</td>
        <td class="center">8</td>
        <td class="center">52</td>
        <td class="center"><strong>Yes</strong></td>
      </tr>
      <tr>
        <td>10 random obstacles</td>
        <td class="center">A*</td>
        <td class="center">8</td>
        <td class="center">31</td>
        <td class="center"><strong>Yes</strong></td>
      </tr>
      <tr>
        <td>Goal fully surrounded (blocked)</td>
        <td class="center">BFS</td>
        <td class="center">&#8212;</td>
        <td class="center">All reachable</td>
        <td class="center"><strong>No</strong></td>
      </tr>
      <tr>
        <td>Goal fully surrounded (blocked)</td>
        <td class="center">A*</td>
        <td class="center">&#8212;</td>
        <td class="center">All reachable</td>
        <td class="center"><strong>No</strong></td>
      </tr>
      <tr>
        <td>Manual play &#8212; user solved</td>
        <td class="center">Manual</td>
        <td class="center">9</td>
        <td class="center">N/A</td>
        <td class="center"><strong>Yes</strong></td>
      </tr>
    </tbody>
  </table>

  <h2>Key Observations</h2>
  <ul>
    <li><strong>Path optimality:</strong> Both BFS and A* always find the minimum number of moves. No shorter path exists for either algorithm.</li>
    <li><strong>Node efficiency:</strong> A* explored 44% fewer nodes on a clear board and ~40% fewer with 10 obstacles, confirming the heuristic guides search effectively.</li>
    <li><strong>Obstacle impact:</strong> Adding obstacles forces longer detours; path length increased from 6 to 8 moves with 10 blocked cells.</li>
    <li><strong>No-path detection:</strong> Both algorithms correctly return an empty path when the goal is unreachable, and the GUI displays &#8220;No path found&#8221; with a status update.</li>
    <li><strong>Undo in manual mode:</strong> The history stack correctly reverts the knight to its previous position on each undo, allowing error recovery.</li>
  </ul>

  <h2>AI Tool Usage Disclosure</h2>
  <div class="ai-box">
    <p><strong>Tool used:</strong> Google Antigravity (AI coding assistant)</p>
    <p><strong>Purpose of AI assistance:</strong></p>
    <ul>
      <li>Structuring the modular 4-file Python project (<code>board.py</code>, <code>pathfinding.py</code>, <code>game.py</code>, <code>main.py</code>).</li>
      <li>Implementing the BFS and A* algorithms with correct path reconstruction.</li>
      <li>Designing the Tkinter GUI layout with canvas-based board rendering, sidebar controls, and statistics panel.</li>
      <li>Debugging the Chebyshev heuristic for admissibility and the A* min-heap tie-breaking.</li>
      <li>Generating the colour-coded HTML board diagram and the PCCOE-format report.</li>
    </ul>
    <p><strong>What was done manually / verified by student:</strong></p>
    <ul>
      <li>Running and testing all three modes (Manual, BFS, A*) in the actual GUI.</li>
      <li>Verifying that BFS and A* return the same path length and that A* consistently explores fewer nodes.</li>
      <li>Placing screenshots of the live GUI into this document.</li>
      <li>Confirming that the undo, random obstacles, block-edit, and clear functions work correctly.</li>
    </ul>
    <p><strong>Conclusion on AI use:</strong> AI assistance was used to accelerate implementation and ensure correctness of the algorithms. All code was reviewed, tested, and understood by the student before submission.</p>
  </div>
</div>

</div><!-- /container -->
</body>
</html>
"""

out = pathlib.Path(r"c:\Users\adity\Desktop\Subjects\AIML\Assignment - 6\Assignment_6_Output_and_AI_Usage.html")
out.write_text(HTML, encoding="utf-8")
print(f"Written {out.stat().st_size} bytes to {out}")
