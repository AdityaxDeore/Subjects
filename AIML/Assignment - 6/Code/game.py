"""
game.py — Chess Knight Escape
Core game-state machine: modes, turn management, result tracking.
"""

import random
from board import Board
from pathfinding import bfs, astar


class GameMode:
    MANUAL    = "manual"
    AI_BFS    = "ai_bfs"
    AI_ASTAR  = "ai_astar"


class GameState:
    IDLE      = "idle"
    PLAYING   = "playing"
    SOLVED    = "solved"
    NO_PATH   = "no_path"


class Game:
    """
    Orchestrates one round of Chess Knight Escape.

    Responsibilities
    ----------------
    - Holds a Board instance.
    - Tracks move history (for undo) and step count.
    - In AI mode, computes and stores the full path so the GUI can
      animate it step by step.
    """

    def __init__(self):
        self.board      = Board()
        self.mode       = GameMode.MANUAL
        self.state      = GameState.IDLE

        # Move history: list of (row, col) positions BEFORE each move
        self._history: list[tuple[int, int]] = []
        self.moves: int = 0

        # AI path (computed on solve())
        self.ai_path:     list[tuple[int, int]] = []
        self.ai_explored: list[tuple[int, int]] = []
        self._ai_step_idx: int = 0   # next index to animate

        # Stats for last solve
        self.stats: dict = {}

    # ------------------------------------------------------------------
    # Setup
    # ------------------------------------------------------------------
    def new_game(self, mode: str = GameMode.MANUAL,
                 knight_pos: tuple = (0, 0),
                 goal_pos:   tuple = (7, 7)):
        """Reset everything and start a fresh game."""
        self.board.reset()
        self.board.knight = knight_pos
        self.board.goal   = goal_pos
        self.mode         = mode
        self.state        = GameState.PLAYING
        self._history.clear()
        self.moves        = 0
        self.ai_path.clear()
        self.ai_explored.clear()
        self._ai_step_idx = 0
        self.stats        = {}

    def randomize_obstacles(self, count: int = 10):
        """Place `count` random blocked cells (excluding knight and goal)."""
        self.board.blocked.clear()
        candidates = [
            (r, c)
            for r in range(Board.SIZE)
            for c in range(Board.SIZE)
            if (r, c) not in (self.board.knight, self.board.goal)
        ]
        chosen = random.sample(candidates, min(count, len(candidates)))
        for cell in chosen:
            self.board.blocked.add(cell)

    # ------------------------------------------------------------------
    # Manual mode
    # ------------------------------------------------------------------
    def get_valid_moves(self) -> list[tuple[int, int]]:
        """Return legal knight moves from current position."""
        return self.board.get_neighbors(*self.board.knight)

    def move_to(self, row: int, col: int) -> bool:
        """
        Attempt a manual move. Returns True if move was legal.
        Handles win detection.
        """
        if self.state != GameState.PLAYING:
            return False
        if (row, col) not in self.get_valid_moves():
            return False

        self._history.append(self.board.knight)
        self.board.knight = (row, col)
        self.moves += 1

        if self.board.knight == self.board.goal:
            self.state = GameState.SOLVED
            self.stats = {"moves": self.moves}

        return True

    def undo(self) -> bool:
        """Undo last manual move. Returns True if successful."""
        if not self._history or self.state != GameState.PLAYING:
            return False
        self.board.knight = self._history.pop()
        self.moves = max(0, self.moves - 1)
        return True

    # ------------------------------------------------------------------
    # AI mode
    # ------------------------------------------------------------------
    def solve(self) -> bool:
        """
        Run BFS or A* based on current mode.
        Stores the full path for step-by-step animation.
        Returns True if a path was found.
        """
        if self.mode == GameMode.AI_BFS:
            path, explored = bfs(self.board)
        else:
            path, explored = astar(self.board)

        self.ai_path     = path
        self.ai_explored = explored
        self._ai_step_idx = 0

        if path:
            self.state = GameState.PLAYING
            self.stats = {
                "algorithm":  self.mode,
                "path_len":   len(path) - 1,   # moves = cells - 1
                "nodes_explored": len(explored),
            }
            return True
        else:
            self.state = GameState.NO_PATH
            return False

    def ai_step(self) -> tuple[int, int] | None:
        """
        Advance the knight one step along the pre-computed AI path.
        Returns the new position, or None if already at the end.
        """
        if not self.ai_path or self._ai_step_idx >= len(self.ai_path) - 1:
            return None

        self._ai_step_idx += 1
        self.board.knight = self.ai_path[self._ai_step_idx]
        self.moves += 1

        if self.board.knight == self.board.goal:
            self.state = GameState.SOLVED

        return self.board.knight

    def ai_run_all(self):
        """Jump the knight instantly to the goal along the AI path."""
        while self.ai_step() is not None:
            pass

    # ------------------------------------------------------------------
    # Misc
    # ------------------------------------------------------------------
    def is_playing(self) -> bool:
        return self.state == GameState.PLAYING
