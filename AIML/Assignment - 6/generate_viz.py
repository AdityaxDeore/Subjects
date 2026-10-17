"""
generate_viz.py — Generate all report visualizations for Assignment 6
Produces 4 PNG files used by Assignment_6_Report.html
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import numpy as np
from board import Board
from pathfinding import bfs, astar

FILES  = "abcdefgh"
BOARD  = Board.SIZE

# ── colours (match GUI palette exactly) ──────────────────────────────
C_LIGHT   = "#f0d9b5"
C_DARK    = "#b58863"
C_KNIGHT  = "#FFD700"
C_GOAL    = "#2ecc71"
C_BLOCKED = "#2d2d2d"
C_VALID   = "#74b9ff"
C_EXPLORE = "#d1c4e9"
C_PATH    = "#ff7675"
C_BORDER  = "#333333"

def cell_color(r, c):
    return C_LIGHT if (r + c) % 2 == 0 else C_DARK

def draw_board(ax, board, path=(), explored=(), blocked=(), title="",
               highlight_valid=None, step_numbers=True):
    """Draw an 8×8 board on axes ax."""
    set_path = set(path)
    set_exp  = set(explored) - set_path
    set_blk  = blocked if blocked else board.blocked

    for r in range(BOARD):
        for c in range(BOARD):
            pos = (r, c)
            if pos == board.knight:          fill = C_KNIGHT
            elif pos == board.goal:          fill = C_GOAL
            elif pos in set_blk:             fill = C_BLOCKED
            elif pos in set_path:            fill = C_PATH
            elif pos in set_exp:             fill = C_EXPLORE
            elif highlight_valid and pos in highlight_valid: fill = C_VALID
            else:                            fill = cell_color(r, c)

            rect = plt.Rectangle((c, BOARD-1-r), 1, 1,
                                  facecolor=fill, edgecolor=C_BORDER, linewidth=0.8)
            ax.add_patch(rect)

            # Step number on path cells
            if step_numbers and pos in set_path:
                idx = list(path).index(pos)
                ax.text(c+0.5, BOARD-1-r+0.5, str(idx),
                        ha='center', va='center',
                        fontsize=7, fontweight='bold', color='#111',
                        fontfamily='monospace')

            # Knight symbol
            if pos == board.knight:
                ax.text(c+0.5, BOARD-1-r+0.5, '♞',
                        ha='center', va='center', fontsize=18, color='#1a1a2e')
            elif pos == board.goal:
                ax.text(c+0.5, BOARD-1-r+0.5, '★',
                        ha='center', va='center', fontsize=14, color='#1a1a2e')
            elif pos in set_blk:
                ax.text(c+0.5, BOARD-1-r+0.5, '✕',
                        ha='center', va='center', fontsize=11, color='#666')

    # Axes labels
    ax.set_xlim(0, BOARD)
    ax.set_ylim(0, BOARD)
    ax.set_xticks([c+0.5 for c in range(BOARD)])
    ax.set_xticklabels(list(FILES), fontsize=9)
    ax.set_yticks([r+0.5 for r in range(BOARD)])
    ax.set_yticklabels([str(i) for i in range(1, BOARD+1)], fontsize=9)
    ax.set_aspect('equal')
    if title:
        ax.set_title(title, fontsize=11, fontweight='bold', pad=6)


# ════════════════════════════════════════════════════════════════════
# Figure 1: BFS vs A* side-by-side (clear board)
# ════════════════════════════════════════════════════════════════════
b = Board()
path_bfs, exp_bfs = bfs(b)
path_ast, exp_ast = astar(b)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6.5))
fig.patch.set_facecolor('#f8f8f8')

draw_board(ax1, b, path=path_bfs, explored=exp_bfs, title=f"BFS  —  {len(path_bfs)-1} moves  |  {len(exp_bfs)} nodes explored")
draw_board(ax2, b, path=path_ast, explored=exp_ast, title=f"A*   —  {len(path_ast)-1} moves  |  {len(exp_ast)} nodes explored")

# Legend
legend_items = [
    mpatches.Patch(facecolor=C_KNIGHT,  edgecolor='#333', label='Knight (start)'),
    mpatches.Patch(facecolor=C_GOAL,    edgecolor='#333', label='Goal'),
    mpatches.Patch(facecolor=C_PATH,    edgecolor='#333', label='Solution path'),
    mpatches.Patch(facecolor=C_EXPLORE, edgecolor='#333', label='Explored nodes'),
]
fig.legend(handles=legend_items, loc='lower center', ncol=4,
           fontsize=10, frameon=True, edgecolor='#aaa',
           bbox_to_anchor=(0.5, 0.01))
fig.suptitle("Figure 1: BFS vs A* — Exploration Maps (a8 → h1, No Obstacles)",
             fontsize=13, fontweight='bold', y=0.98)
plt.tight_layout(rect=[0, 0.07, 1, 0.96])
plt.savefig("viz_bfs_vs_astar_clear.png", dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print("Saved viz_bfs_vs_astar_clear.png")


# ════════════════════════════════════════════════════════════════════
# Figure 2: BFS vs A* side-by-side (10 obstacles)
# ════════════════════════════════════════════════════════════════════
import random; random.seed(7)
b2 = Board()
candidates = [(r,c) for r in range(8) for c in range(8)
              if (r,c) not in ((0,0),(7,7))]
b2.blocked = set(random.sample(candidates, 10))

path_bfs2, exp_bfs2 = bfs(b2)
path_ast2, exp_ast2 = astar(b2)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6.5))
fig.patch.set_facecolor('#f8f8f8')

if path_bfs2:
    t1 = f"BFS  —  {len(path_bfs2)-1} moves  |  {len(exp_bfs2)} nodes"
else:
    t1 = "BFS — NO PATH FOUND"
if path_ast2:
    t2 = f"A*   —  {len(path_ast2)-1} moves  |  {len(exp_ast2)} nodes"
else:
    t2 = "A* — NO PATH FOUND"

draw_board(ax1, b2, path=path_bfs2, explored=exp_bfs2, title=t1)
draw_board(ax2, b2, path=path_ast2, explored=exp_ast2, title=t2)

legend_items = [
    mpatches.Patch(facecolor=C_KNIGHT,  edgecolor='#333', label='Knight (start)'),
    mpatches.Patch(facecolor=C_GOAL,    edgecolor='#333', label='Goal'),
    mpatches.Patch(facecolor=C_PATH,    edgecolor='#333', label='Solution path'),
    mpatches.Patch(facecolor=C_EXPLORE, edgecolor='#333', label='Explored nodes'),
    mpatches.Patch(facecolor=C_BLOCKED, edgecolor='#333', label='Blocked cell'),
]
fig.legend(handles=legend_items, loc='lower center', ncol=5,
           fontsize=10, frameon=True, edgecolor='#aaa',
           bbox_to_anchor=(0.5, 0.01))
fig.suptitle("Figure 2: BFS vs A* — Exploration Maps (a8 → h1, 10 Random Obstacles)",
             fontsize=13, fontweight='bold', y=0.98)
plt.tight_layout(rect=[0, 0.07, 1, 0.96])
plt.savefig("viz_bfs_vs_astar_obstacles.png", dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print("Saved viz_bfs_vs_astar_obstacles.png")


# ════════════════════════════════════════════════════════════════════
# Figure 3: Knight move graph from a single cell (d4 = row 4, col 3)
# ════════════════════════════════════════════════════════════════════
from board import KNIGHT_MOVES

fig, ax = plt.subplots(figsize=(7, 7))
fig.patch.set_facecolor('#f8f8f8')

b3 = Board()
b3.knight = (4, 3)   # d4
b3.goal   = (0, 7)

valid = b3.get_neighbors(*b3.knight)

draw_board(ax, b3, highlight_valid=valid, step_numbers=False,
           title="Figure 3: Knight at d4 — All 8 Possible L-Shaped Moves Highlighted in Blue")

# Draw arrows from knight to each valid move
kr, kc = b3.knight
for (nr, nc) in valid:
    dx = nc - kc
    dy = -(nr - kr)
    ax.annotate("",
        xy=(nc+0.5, BOARD-1-nr+0.5),
        xytext=(kc+0.5, BOARD-1-kr+0.5),
        arrowprops=dict(arrowstyle='->', color='#1a1a2e', lw=2, connectionstyle='arc3,rad=0.1'))

plt.tight_layout()
plt.savefig("viz_knight_moves.png", dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print("Saved viz_knight_moves.png")


# ════════════════════════════════════════════════════════════════════
# Figure 4: Node efficiency comparison bar chart (multiple scenarios)
# ════════════════════════════════════════════════════════════════════

scenarios = []
# Scenario 1: clear
b = Board()
pb, eb = bfs(b);  pa, ea = astar(b)
scenarios.append(("No obstacles\n(a8→h1)", len(pb)-1, len(eb), len(pa)-1, len(ea)))

# Scenario 2: 10 obstacles seed=7
b2_test = Board(); b2_test.blocked = b2.blocked.copy()
pb2, eb2 = bfs(b2_test); pa2, ea2 = astar(b2_test)
scenarios.append(("10 obstacles\n(a8→h1)", len(pb2)-1 if pb2 else -1, len(eb2), len(pa2)-1 if pa2 else -1, len(ea2)))

# Scenario 3: different start/goal — b8 to g1
b3t = Board(); b3t.knight=(0,1); b3t.goal=(6,6)
pb3, eb3 = bfs(b3t); pa3, ea3 = astar(b3t)
scenarios.append(("No obstacles\n(b8→g2)", len(pb3)-1 if pb3 else -1, len(eb3), len(pa3)-1 if pa3 else -1, len(ea3)))

# Scenario 4: 15 obstacles
import random; random.seed(42)
b4 = Board()
cands4 = [(r,c) for r in range(8) for c in range(8) if (r,c) not in ((0,0),(7,7))]
b4.blocked = set(random.sample(cands4, 15))
pb4, eb4 = bfs(b4); pa4, ea4 = astar(b4)
scenarios.append(("15 obstacles\n(a8→h1)", len(pb4)-1 if pb4 else -1, len(eb4), len(pa4)-1 if pa4 else -1, len(ea4)))

labels    = [s[0] for s in scenarios]
bfs_nodes = [s[2] for s in scenarios]
ast_nodes = [s[4] for s in scenarios]
bfs_moves = [s[1] for s in scenarios]
ast_moves = [s[3] for s in scenarios]

x = np.arange(len(labels))
w = 0.35

fig, (ax_nodes, ax_moves) = plt.subplots(1, 2, figsize=(13, 5.5))
fig.patch.set_facecolor('#f8f8f8')

# Nodes explored
bars1 = ax_nodes.bar(x - w/2, bfs_nodes, w, label='BFS', color='#74b9ff', edgecolor='#333', linewidth=0.8)
bars2 = ax_nodes.bar(x + w/2, ast_nodes, w, label='A*',  color='#ff7675', edgecolor='#333', linewidth=0.8)
for bar in bars1:
    ax_nodes.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.5,
                  str(int(bar.get_height())), ha='center', va='bottom', fontsize=10, fontweight='bold')
for bar in bars2:
    ax_nodes.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.5,
                  str(int(bar.get_height())), ha='center', va='bottom', fontsize=10, fontweight='bold', color='#c0392b')
ax_nodes.set_xticks(x); ax_nodes.set_xticklabels(labels, fontsize=9)
ax_nodes.set_ylabel("Nodes Explored", fontsize=11)
ax_nodes.set_title("Nodes Explored: BFS vs A*", fontsize=12, fontweight='bold')
ax_nodes.legend(fontsize=10); ax_nodes.set_ylim(0, max(bfs_nodes)*1.18)
ax_nodes.grid(axis='y', alpha=0.35)

# Path lengths
bars3 = ax_moves.bar(x - w/2, [m if m>=0 else 0 for m in bfs_moves], w,
                     label='BFS', color='#74b9ff', edgecolor='#333', linewidth=0.8)
bars4 = ax_moves.bar(x + w/2, [m if m>=0 else 0 for m in ast_moves], w,
                     label='A*',  color='#ff7675', edgecolor='#333', linewidth=0.8)
for bar, val in zip(bars3, bfs_moves):
    lbl = str(val) if val >= 0 else 'N/A'
    ax_moves.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.1,
                  lbl, ha='center', va='bottom', fontsize=10, fontweight='bold')
for bar, val in zip(bars4, ast_moves):
    lbl = str(val) if val >= 0 else 'N/A'
    ax_moves.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.1,
                  lbl, ha='center', va='bottom', fontsize=10, fontweight='bold', color='#c0392b')
ax_moves.set_xticks(x); ax_moves.set_xticklabels(labels, fontsize=9)
ax_moves.set_ylabel("Path Length (moves)", fontsize=11)
ax_moves.set_title("Path Length: BFS vs A*", fontsize=12, fontweight='bold')
ax_moves.legend(fontsize=10); ax_moves.set_ylim(0, max(max(bfs_moves),max(ast_moves))+3)
ax_moves.grid(axis='y', alpha=0.35)

fig.suptitle("Figure 4: BFS vs A* Performance Across Multiple Test Scenarios",
             fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig("viz_performance_comparison.png", dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print("Saved viz_performance_comparison.png")

# Print summary for report
print("\nScenario summary:")
for s in scenarios:
    print(f"  {s[0].replace(chr(10),' ')}: BFS moves={s[1]}, nodes={s[2]} | A* moves={s[3]}, nodes={s[4]}")
