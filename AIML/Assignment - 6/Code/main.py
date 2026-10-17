"""
main.py — Chess Knight Escape
Full Tkinter GUI:
  • 8×8 chessboard drawn on a Canvas
  • Manual play: click highlighted squares to move the knight
  • AI BFS / AI A* modes: step-by-step or instant solve
  • Block-edit mode: left-click cells to toggle obstacles
  • Random obstacles, Undo, New Game controls
  • Stats panel showing moves, path length, nodes explored
  • Colour-coded: knight=gold, goal=green, blocked=charcoal,
    valid-moves=sky-blue, AI-explored=lavender, AI-path=orange
"""

import tkinter as tk
from tkinter import ttk, messagebox
import random
import sys

# Ensure local imports work when run from the assignment folder
sys.path.insert(0, ".")

from board import Board
from game  import Game, GameMode, GameState


# ── Palette ────────────────────────────────────────────────────────────
CLR_LIGHT   = "#f0d9b5"   # light square
CLR_DARK    = "#b58863"   # dark square
CLR_BLOCK   = "#2d2d2d"   # blocked cell
CLR_KNIGHT  = "#FFD700"   # knight highlight
CLR_GOAL    = "#2ecc71"   # goal highlight
CLR_VALID   = "#74b9ff"   # valid move hints
CLR_EXPLORE = "#d1c4e9"   # BFS/A* explored node
CLR_PATH    = "#ff7675"   # solution path
CLR_BORDER  = "#333333"
CELL_SIZE   = 72          # pixels per cell
BOARD_PX    = Board.SIZE * CELL_SIZE

KNIGHT_UNICODE = "♞"
GOAL_UNICODE   = "★"


class KnightEscapeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chess Knight Escape — AI Pathfinding Game")
        self.resizable(False, False)
        self.configure(bg="#1a1a2e")

        self.game = Game()

        # Tkinter variable for algorithm choice
        self._mode_var = tk.StringVar(value=GameMode.MANUAL)
        # Tkinter variable for obstacle count
        self._obstacle_var = tk.IntVar(value=10)
        # Block-edit toggle
        self._edit_mode = tk.BooleanVar(value=False)

        # Animation state
        self._anim_id = None
        self._anim_delay = 350   # ms between AI steps

        self._build_ui()
        self._new_game()

    # ══════════════════════════════════════════════════════════════════
    #  UI Construction
    # ══════════════════════════════════════════════════════════════════
    def _build_ui(self):
        # ── Left: board canvas ─────────────────────────────────────
        left = tk.Frame(self, bg="#1a1a2e", padx=12, pady=12)
        left.grid(row=0, column=0, sticky="ns")

        title_lbl = tk.Label(
            left, text="♞  Chess Knight Escape",
            font=("Segoe UI", 18, "bold"),
            bg="#1a1a2e", fg="#FFD700"
        )
        title_lbl.pack(pady=(0, 8))

        self.canvas = tk.Canvas(
            left, width=BOARD_PX, height=BOARD_PX,
            bd=0, highlightthickness=2,
            highlightbackground="#FFD700",
            cursor="hand2"
        )
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self._on_canvas_click)

        # File / rank labels
        self._draw_labels(left)

        # Status bar
        self.status_var = tk.StringVar(value="New game — select a mode and click Solve or click a highlighted square.")
        status_bar = tk.Label(
            left, textvariable=self.status_var,
            font=("Segoe UI", 9), bg="#0f3460", fg="#e0e0e0",
            anchor="w", padx=8, pady=4, wraplength=BOARD_PX
        )
        status_bar.pack(fill="x", pady=(6, 0))

        # ── Right: controls ────────────────────────────────────────
        right = tk.Frame(self, bg="#16213e", padx=14, pady=14)
        right.grid(row=0, column=1, sticky="ns", padx=(0, 12), pady=12)

        self._build_mode_panel(right)
        self._build_obstacle_panel(right)
        self._build_action_panel(right)
        self._build_stats_panel(right)
        self._build_legend(right)

    def _draw_labels(self, parent):
        lbl_frame = tk.Frame(parent, bg="#1a1a2e")
        lbl_frame.pack(fill="x")
        files = "a b c d e f g h".split()
        for i, f in enumerate(files):
            tk.Label(
                lbl_frame, text=f,
                font=("Consolas", 9), bg="#1a1a2e", fg="#aaa",
                width=4
            ).grid(row=0, column=i)

    def _sep(self, parent):
        ttk.Separator(parent, orient="horizontal").pack(fill="x", pady=10)

    def _section(self, parent, title):
        tk.Label(
            parent, text=title,
            font=("Segoe UI", 10, "bold"),
            bg="#16213e", fg="#FFD700"
        ).pack(anchor="w", pady=(6, 2))

    def _build_mode_panel(self, parent):
        self._section(parent, "Algorithm")
        for text, val in [
            ("Manual Play",   GameMode.MANUAL),
            ("AI — BFS",      GameMode.AI_BFS),
            ("AI — A* Search",GameMode.AI_ASTAR),
        ]:
            tk.Radiobutton(
                parent, text=text, variable=self._mode_var, value=val,
                font=("Segoe UI", 10),
                bg="#16213e", fg="#e0e0e0",
                selectcolor="#0f3460",
                activebackground="#16213e", activeforeground="#FFD700"
            ).pack(anchor="w")

        self._sep(parent)

    def _build_obstacle_panel(self, parent):
        self._section(parent, "Obstacles")
        row = tk.Frame(parent, bg="#16213e")
        row.pack(fill="x", pady=2)

        tk.Label(row, text="Count:", bg="#16213e", fg="#ccc",
                 font=("Segoe UI", 9)).pack(side="left")
        tk.Spinbox(
            row, from_=0, to=30, textvariable=self._obstacle_var,
            width=4, font=("Segoe UI", 9)
        ).pack(side="left", padx=6)

        tk.Button(
            parent, text="🎲 Random Obstacles",
            font=("Segoe UI", 9, "bold"),
            bg="#0f3460", fg="white", relief="flat",
            activebackground="#1a5276",
            command=self._do_random_obstacles
        ).pack(fill="x", pady=3)

        self.edit_btn = tk.Checkbutton(
            parent, text="✏ Edit-Block Mode (click cells)",
            variable=self._edit_mode,
            font=("Segoe UI", 9),
            bg="#16213e", fg="#e0e0e0",
            selectcolor="#0f3460",
            activebackground="#16213e", activeforeground="#FFD700"
        )
        self.edit_btn.pack(anchor="w", pady=2)

        tk.Button(
            parent, text="🧹 Clear Obstacles",
            font=("Segoe UI", 9),
            bg="#1c3a52", fg="white", relief="flat",
            command=self._do_clear_obstacles
        ).pack(fill="x", pady=2)

        self._sep(parent)

    def _build_action_panel(self, parent):
        self._section(parent, "Actions")

        tk.Button(
            parent, text="▶  Solve / New Game",
            font=("Segoe UI", 11, "bold"),
            bg="#27ae60", fg="white", relief="flat",
            activebackground="#1e8449",
            command=self._do_solve
        ).pack(fill="x", pady=4)

        row2 = tk.Frame(parent, bg="#16213e")
        row2.pack(fill="x", pady=2)

        tk.Button(
            row2, text="⏭ Step",
            font=("Segoe UI", 9, "bold"),
            bg="#2980b9", fg="white", relief="flat",
            command=self._do_ai_step
        ).pack(side="left", expand=True, fill="x", padx=(0, 3))

        tk.Button(
            row2, text="⏩ Run All",
            font=("Segoe UI", 9, "bold"),
            bg="#8e44ad", fg="white", relief="flat",
            command=self._do_ai_run_all
        ).pack(side="left", expand=True, fill="x")

        row3 = tk.Frame(parent, bg="#16213e")
        row3.pack(fill="x", pady=2)

        tk.Button(
            row3, text="↩ Undo",
            font=("Segoe UI", 9),
            bg="#c0392b", fg="white", relief="flat",
            command=self._do_undo
        ).pack(side="left", expand=True, fill="x", padx=(0, 3))

        tk.Button(
            row3, text="🔄 Reset",
            font=("Segoe UI", 9),
            bg="#7f8c8d", fg="white", relief="flat",
            command=self._new_game
        ).pack(side="left", expand=True, fill="x")

        self._sep(parent)

    def _build_stats_panel(self, parent):
        self._section(parent, "Statistics")
        self.stats_frame = tk.Frame(parent, bg="#0f3460",
                                    relief="flat", padx=10, pady=8)
        self.stats_frame.pack(fill="x")

        def stat_row(label, var):
            f = tk.Frame(self.stats_frame, bg="#0f3460")
            f.pack(fill="x", pady=1)
            tk.Label(f, text=label, font=("Segoe UI", 9),
                     bg="#0f3460", fg="#aaa", width=16, anchor="w").pack(side="left")
            tk.Label(f, textvariable=var, font=("Consolas", 10, "bold"),
                     bg="#0f3460", fg="#FFD700", anchor="e").pack(side="right")

        self._stat_mode    = tk.StringVar(value="—")
        self._stat_moves   = tk.StringVar(value="—")
        self._stat_path    = tk.StringVar(value="—")
        self._stat_nodes   = tk.StringVar(value="—")
        self._stat_status  = tk.StringVar(value="Idle")

        stat_row("Mode:",           self._stat_mode)
        stat_row("Moves made:",     self._stat_moves)
        stat_row("Path length:",    self._stat_path)
        stat_row("Nodes explored:", self._stat_nodes)
        stat_row("Status:",         self._stat_status)

        self._sep(parent)

    def _build_legend(self, parent):
        self._section(parent, "Legend")
        items = [
            (CLR_KNIGHT,  "Knight"),
            (CLR_GOAL,    "Goal / Destination"),
            (CLR_VALID,   "Valid moves"),
            (CLR_EXPLORE, "AI explored nodes"),
            (CLR_PATH,    "Solution path"),
            (CLR_BLOCK,   "Blocked cell"),
        ]
        for color, label in items:
            f = tk.Frame(parent, bg="#16213e")
            f.pack(anchor="w", fill="x", pady=1)
            tk.Label(f, bg=color, width=3,
                     relief="solid", bd=1).pack(side="left", padx=(0, 6))
            tk.Label(f, text=label, font=("Segoe UI", 9),
                     bg="#16213e", fg="#ccc").pack(side="left")

    # ══════════════════════════════════════════════════════════════════
    #  Drawing
    # ══════════════════════════════════════════════════════════════════
    def _draw_board(self):
        self.canvas.delete("all")
        board = self.game.board
        valid = set(self.game.get_valid_moves()) if self.game.is_playing() and self.game.mode == GameMode.MANUAL else set()
        ai_exp  = set(self.game.ai_explored)
        ai_path = set(self.game.ai_path)

        for row in range(Board.SIZE):
            for col in range(Board.SIZE):
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE

                pos = (row, col)

                # Determine base colour
                if pos == board.knight:
                    fill = CLR_KNIGHT
                elif pos == board.goal:
                    fill = CLR_GOAL
                elif board.is_blocked(row, col):
                    fill = CLR_BLOCK
                elif pos in valid:
                    fill = CLR_VALID
                elif pos in ai_path:
                    fill = CLR_PATH
                elif pos in ai_exp:
                    fill = CLR_EXPLORE
                else:
                    fill = CLR_LIGHT if (row + col) % 2 == 0 else CLR_DARK

                self.canvas.create_rectangle(x1, y1, x2, y2,
                                             fill=fill, outline=CLR_BORDER, width=1)

                # Knight symbol
                if pos == board.knight:
                    self.canvas.create_text(
                        x1 + CELL_SIZE // 2, y1 + CELL_SIZE // 2,
                        text=KNIGHT_UNICODE, font=("Segoe UI", 28, "bold"),
                        fill="#1a1a2e"
                    )
                # Goal symbol
                elif pos == board.goal:
                    self.canvas.create_text(
                        x1 + CELL_SIZE // 2, y1 + CELL_SIZE // 2,
                        text=GOAL_UNICODE, font=("Segoe UI", 24, "bold"),
                        fill="#1a1a2e"
                    )
                # Block pattern
                elif board.is_blocked(row, col):
                    self.canvas.create_text(
                        x1 + CELL_SIZE // 2, y1 + CELL_SIZE // 2,
                        text="✕", font=("Segoe UI", 18, "bold"),
                        fill="#555"
                    )

                # Path step number (small)
                if pos in ai_path and pos not in (board.knight, board.goal):
                    idx = self.game.ai_path.index(pos)
                    self.canvas.create_text(
                        x2 - 10, y1 + 12,
                        text=str(idx), font=("Consolas", 7),
                        fill="#333"
                    )

        # Coordinate ranks on the left (8..1)
        for row in range(Board.SIZE):
            y = row * CELL_SIZE + CELL_SIZE // 2
            self.canvas.create_text(5, y, text=str(8 - row),
                                    font=("Consolas", 8), fill="#999", anchor="w")

    def _update_stats(self):
        mode_map = {
            GameMode.MANUAL:   "Manual",
            GameMode.AI_BFS:   "BFS",
            GameMode.AI_ASTAR: "A*",
        }
        self._stat_mode.set(mode_map.get(self.game.mode, "—"))
        self._stat_moves.set(str(self.game.moves) if self.game.moves else "0")

        s = self.game.stats
        self._stat_path.set(str(s.get("path_len", "—")))
        self._stat_nodes.set(str(s.get("nodes_explored", "—")))

        state_map = {
            GameState.IDLE:    "Idle",
            GameState.PLAYING: "Playing",
            GameState.SOLVED:  "✔ Solved!",
            GameState.NO_PATH: "✘ No path",
        }
        self._stat_status.set(state_map.get(self.game.state, "—"))

    # ══════════════════════════════════════════════════════════════════
    #  Event Handlers
    # ══════════════════════════════════════════════════════════════════
    def _on_canvas_click(self, event):
        col = event.x // CELL_SIZE
        row = event.y // CELL_SIZE
        if not (0 <= row < Board.SIZE and 0 <= col < Board.SIZE):
            return

        if self._edit_mode.get():
            self.game.board.toggle_block(row, col)
            self._draw_board()
            return

        if self.game.mode != GameMode.MANUAL:
            return
        if not self.game.is_playing():
            return

        if self.game.move_to(row, col):
            self._draw_board()
            self._update_stats()
            if self.game.state == GameState.SOLVED:
                self.status_var.set(f"🏆 Solved! You reached the goal in {self.game.moves} move(s).")
            else:
                pos = self.game.board.knight
                self.status_var.set(
                    f"Knight at {Board.cell_to_chess(*pos)}  |  "
                    f"Moves: {self.game.moves}"
                )
        else:
            self.status_var.set("Invalid move. Click a highlighted (blue) square.")

    # ── Action buttons ─────────────────────────────────────────────
    def _new_game(self):
        self._cancel_anim()
        self.game.new_game(mode=self._mode_var.get())
        self._draw_board()
        self._update_stats()
        self.status_var.set(
            "Manual mode: click highlighted squares to move." if self.game.mode == GameMode.MANUAL
            else "AI mode ready. Click ▶ Solve to compute the path, then Step or Run All."
        )

    def _do_solve(self):
        self._cancel_anim()
        mode = self._mode_var.get()
        self.game.mode = mode

        if mode == GameMode.MANUAL:
            # Start fresh manual game
            self.game.new_game(mode=mode)
            self._draw_board()
            self._update_stats()
            self.status_var.set("Manual mode: click highlighted (blue) squares to move the knight.")
            return

        # AI solve
        found = self.game.solve()
        self._draw_board()
        self._update_stats()

        if found:
            plen = len(self.game.ai_path) - 1
            exp  = len(self.game.ai_explored)
            algo = "BFS" if mode == GameMode.AI_BFS else "A*"
            self.status_var.set(
                f"{algo} found a path of {plen} move(s) "
                f"(explored {exp} node(s)).  "
                f"Use ⏭ Step or ⏩ Run All to animate."
            )
        else:
            self.status_var.set("❌ No path found — the goal is unreachable. Try clearing some obstacles.")

    def _do_ai_step(self):
        if self.game.mode == GameMode.MANUAL:
            return
        if not self.game.ai_path:
            self.status_var.set("Click ▶ Solve first to compute the AI path.")
            return
        pos = self.game.ai_step()
        if pos is None:
            self.status_var.set("Already at the end of the path.")
        else:
            self.status_var.set(
                f"Step {self.game._ai_step_idx}/{len(self.game.ai_path)-1} → {Board.cell_to_chess(*pos)}"
            )
        self._draw_board()
        self._update_stats()
        if self.game.state == GameState.SOLVED:
            self.status_var.set(f"🏆 Goal reached in {self.game.moves} move(s)!")

    def _do_ai_run_all(self):
        """Animate the AI path step by step with a delay."""
        if self.game.mode == GameMode.MANUAL:
            return
        if not self.game.ai_path:
            self.status_var.set("Click ▶ Solve first.")
            return
        self._cancel_anim()
        self._animate_ai()

    def _animate_ai(self):
        if self.game.state == GameState.SOLVED or not self.game.ai_path:
            self._update_stats()
            self.status_var.set(f"🏆 Goal reached in {self.game.moves} move(s)!")
            return

        pos = self.game.ai_step()
        if pos is None:
            self._update_stats()
            self.status_var.set(f"🏆 Goal reached in {self.game.moves} move(s)!")
            return

        self._draw_board()
        self._update_stats()
        self.status_var.set(
            f"Animating… step {self.game._ai_step_idx}/{len(self.game.ai_path)-1} → {Board.cell_to_chess(*pos)}"
        )
        self._anim_id = self.after(self._anim_delay, self._animate_ai)

    def _cancel_anim(self):
        if self._anim_id:
            self.after_cancel(self._anim_id)
            self._anim_id = None

    def _do_undo(self):
        self._cancel_anim()
        if self.game.undo():
            self._draw_board()
            self._update_stats()
            self.status_var.set(f"Undo — now at {Board.cell_to_chess(*self.game.board.knight)}.")
        else:
            self.status_var.set("Nothing to undo.")

    def _do_random_obstacles(self):
        self._cancel_anim()
        n = self._obstacle_var.get()
        self.game.randomize_obstacles(n)
        # clear AI path since board changed
        self.game.ai_path.clear()
        self.game.ai_explored.clear()
        self._draw_board()
        self.status_var.set(f"{n} random obstacle(s) placed. Re-run Solve if in AI mode.")

    def _do_clear_obstacles(self):
        self._cancel_anim()
        self.game.board.blocked.clear()
        self.game.ai_path.clear()
        self.game.ai_explored.clear()
        self._draw_board()
        self.status_var.set("All obstacles cleared.")


# ══════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    app = KnightEscapeApp()
    app.mainloop()
