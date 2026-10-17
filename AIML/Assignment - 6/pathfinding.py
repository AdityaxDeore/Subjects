"""
pathfinding.py — Chess Knight Escape
BFS (Breadth-First Search) and A* Search implementations.
Both return the shortest path as a list of (row, col) tuples,
or an empty list if no path exists.
"""

from collections import deque
import heapq
from board import Board


# ══════════════════════════════════════════════════════════════════════
#  Helper
# ══════════════════════════════════════════════════════════════════════

def _reconstruct(came_from: dict, start: tuple, goal: tuple) -> list:
    """Trace back from goal → start and return path in start→goal order."""
    path = []
    node = goal
    while node != start:
        path.append(node)
        node = came_from[node]
    path.append(start)
    path.reverse()
    return path


# ══════════════════════════════════════════════════════════════════════
#  BFS
# ══════════════════════════════════════════════════════════════════════

def bfs(board: Board) -> tuple[list, list[tuple]]:
    """
    Breadth-First Search from board.knight to board.goal.

    Returns
    -------
    path       : list of (row,col) from start to goal (empty if unreachable)
    visited    : all nodes explored (in order)
    """
    start = board.knight
    goal  = board.goal

    if start == goal:
        return [start], [start]

    queue      = deque([start])
    came_from  = {start: None}
    visited_order = [start]

    while queue:
        current = queue.popleft()

        if current == goal:
            path = _reconstruct(came_from, start, goal)
            return path, visited_order

        for nb in board.get_neighbors(*current):
            if nb not in came_from:
                came_from[nb] = current
                visited_order.append(nb)
                queue.append(nb)

    return [], visited_order   # unreachable


# ══════════════════════════════════════════════════════════════════════
#  A* Search
# ══════════════════════════════════════════════════════════════════════

def _heuristic(node: tuple, goal: tuple) -> float:
    """
    Chebyshev-based admissible heuristic for knight moves.
    Divides the Chebyshev distance by the maximum advance per move (≈2).
    """
    dr = abs(node[0] - goal[0])
    dc = abs(node[1] - goal[1])
    return max(dr, dc) / 2.0


def astar(board: Board) -> tuple[list, list[tuple]]:
    """
    A* Search from board.knight to board.goal.

    Returns
    -------
    path       : list of (row,col) from start to goal (empty if unreachable)
    visited    : all nodes explored (in order of expansion)
    """
    start = board.knight
    goal  = board.goal

    if start == goal:
        return [start], [start]

    # (f_score, g_score, node)
    h0 = _heuristic(start, goal)
    open_heap  = [(h0, 0, start)]
    came_from  = {}
    g_score    = {start: 0}
    visited_order = []

    while open_heap:
        f, g, current = heapq.heappop(open_heap)

        if current in came_from and g > g_score.get(current, float('inf')):
            continue   # stale entry

        visited_order.append(current)

        if current == goal:
            path = _reconstruct(came_from, start, goal)
            return path, visited_order

        for nb in board.get_neighbors(*current):
            tentative_g = g + 1   # each knight move costs 1
            if tentative_g < g_score.get(nb, float('inf')):
                g_score[nb] = tentative_g
                came_from[nb] = current
                h = _heuristic(nb, goal)
                heapq.heappush(open_heap, (tentative_g + h, tentative_g, nb))

    return [], visited_order   # unreachable
