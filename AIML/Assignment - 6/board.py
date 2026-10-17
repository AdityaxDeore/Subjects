"""
board.py — Chess Knight Escape
Manages the 8x8 board state: cells, knight/goal positions, blocked squares.
"""

KNIGHT_MOVES = [
    (-2, -1), (-2, +1),
    (-1, -2), (-1, +2),
    (+1, -2), (+1, +2),
    (+2, -1), (+2, +1),
]


class Board:
    """Represents the 8×8 chessboard."""

    SIZE = 8

    def __init__(self):
        self.blocked: set[tuple[int, int]] = set()
        self.knight: tuple[int, int] = (0, 0)   # top-left corner
        self.goal: tuple[int, int]   = (7, 7)   # bottom-right corner

    # ------------------------------------------------------------------
    # State helpers
    # ------------------------------------------------------------------
    def reset(self):
        """Clear blocked cells and reset knight/goal to defaults."""
        self.blocked.clear()
        self.knight = (0, 0)
        self.goal   = (7, 7)

    def is_valid(self, row: int, col: int) -> bool:
        """Return True if (row, col) is inside the board."""
        return 0 <= row < self.SIZE and 0 <= col < self.SIZE

    def is_blocked(self, row: int, col: int) -> bool:
        return (row, col) in self.blocked

    def toggle_block(self, row: int, col: int):
        """Toggle a cell's blocked status (cannot block knight or goal)."""
        if (row, col) in (self.knight, self.goal):
            return
        if (row, col) in self.blocked:
            self.blocked.discard((row, col))
        else:
            self.blocked.add((row, col))

    # ------------------------------------------------------------------
    # Knight movement
    # ------------------------------------------------------------------
    def get_neighbors(self, row: int, col: int) -> list[tuple[int, int]]:
        """Return all valid, unblocked squares reachable by a knight from (row, col)."""
        result = []
        for dr, dc in KNIGHT_MOVES:
            nr, nc = row + dr, col + dc
            if self.is_valid(nr, nc) and not self.is_blocked(nr, nc):
                result.append((nr, nc))
        return result

    # ------------------------------------------------------------------
    # Coordinate helpers (for UI)
    # ------------------------------------------------------------------
    @staticmethod
    def cell_to_chess(row: int, col: int) -> str:
        """Convert (row, col) → algebraic notation, e.g. (0,0) → 'a8'."""
        files = "abcdefgh"
        return f"{files[col]}{8 - row}"

    @staticmethod
    def chess_to_cell(notation: str) -> tuple[int, int]:
        """Convert algebraic notation → (row, col), e.g. 'a8' → (0,0)."""
        files = "abcdefgh"
        col = files.index(notation[0].lower())
        row = 8 - int(notation[1])
        return row, col
