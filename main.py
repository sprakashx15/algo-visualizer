import tkinter as tk
import random
import tkinter.messagebox as msg

from grid import Grid
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.astar import astar


ROWS, COLS = 20, 20
CELL_SIZE = 30

# Modern dark theme colors
COLORS = {
    "empty": "#ffffff",
    "wall": "#000000",
    "start": "#00c853",
    "end": "#d50000",
    "visited": "#5db9e4",
    "path": "#e65918"
}


class App:
    def __init__(self, root):
        self.root = root
        self.root.configure(bg="#1e1e1e")

        self.grid = Grid(ROWS, COLS)
        self.start = None
        self.end = None

        # ---------- MAIN LAYOUT ----------
        self.main_frame = tk.Frame(root, bg="#1e1e1e")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # LEFT: Maze
        self.left_frame = tk.Frame(self.main_frame, bg="#1e1e1e")
        self.left_frame.pack(side=tk.LEFT, padx=10, pady=10)

        # RIGHT: Controls
        self.right_frame = tk.Frame(self.main_frame, bg="#252526", width=220)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

        # ---------- CANVAS ----------
        self.canvas = tk.Canvas(
            self.left_frame,
            width=COLS * CELL_SIZE,
            height=ROWS * CELL_SIZE,
            bg=COLORS["empty"],
            highlightthickness=0
        )
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.left_click)

        # ---------- SPEED ----------
        self.speed = tk.IntVar(value=50)

        tk.Label(
            self.right_frame,
            text="Speed",
            bg="#252625",
            fg="white",
            font=("Segoe UI", 12, "bold")
        ).pack(pady=(10, 5))

        tk.Scale(
            self.right_frame,
            from_=1,
            to=100,
            orient=tk.HORIZONTAL,
            variable=self.speed,
            bg="#bcea79",
            fg="white",
            troughcolor="#f1e8e8",
            highlightthickness=0
        ).pack(pady=(0, 10))

        # ---------- BUTTONS ----------
        self.styled_button("Run BFS", self.run_bfs).pack(fill="x", pady=4)
        self.styled_button("Run DFS", self.run_dfs).pack(fill="x", pady=4)
        self.styled_button("Run A*", self.run_astar).pack(fill="x", pady=4)

        tk.Frame(self.right_frame, height=10, bg="#8888F3").pack()

        self.styled_button("Generate Maze", self.generate_maze).pack(fill="x", pady=4)
        self.styled_button("Clear Path", self.clear_path).pack(fill="x", pady=4)
        self.styled_button("Reset Grid", self.reset_grid).pack(fill="x", pady=4)

        self.draw()

    # ---------- UI HELPERS ----------
    def styled_button(self, text, command):
        return tk.Button(
            self.right_frame,
            text=text,
            command=command,
            font=("Segoe UI", 10),
            bg="#bcea79",
            fg="black",
            activebackground="#007acc",
            activeforeground="white",
            relief=tk.FLAT,
            padx=10,
            pady=6
        )

    # ---------- RUNNERS ----------
    def run_bfs(self):
        if not self.start or not self.end:
            msg.showwarning("Error", "Please select Start and End points")
            return
        self.clear_path()
        found=bfs(self)
        if not found:
            msg.showinfo("No Path","No path exist from Start and End points")
            return
        
        self.draw_path()

    def run_dfs(self):
        if not self.start or not self.end:
            msg.showwarning("Error", "Please select Start and End points")
            return
        self.clear_path()
        found=dfs(self)
        if not found:
            msg.showinfo("No Path","No path exist from Start and End points")
            return
        
        self.draw_path()

    def run_astar(self):
        if not self.start or not self.end:
            msg.showwarning("Error", "Please select Start and End points")
            return
        self.clear_path()
        found=astar(self)
        if not found:
            msg.showinfo("No Path","No path exist from Start and End ponits")
            return
        
        self.draw_path()

    # ---------- MAZE LOGIC ----------
    def generate_maze(self):
        self.clear_path()
        for row in self.grid.grid:
            for cell in row:
                if cell.start or cell.end:
                    continue
                cell.wall = random.random() < 0.35
        self.draw()

    def clear_path(self):
        for row in self.grid.grid:
            for cell in row:
                cell.visited = False
                cell.parent = None
        self.draw()

    def reset_grid(self):
        for row in self.grid.grid:
            for cell in row:
                cell.wall = False
                cell.visited = False
                cell.parent = None
                cell.start = False
                cell.end = False
        self.start = None
        self.end = None
        self.draw()

    # ---------- DRAWING ----------
    def draw(self):
        self.canvas.delete("all")
        for r in range(ROWS):
            for c in range(COLS):
                cell = self.grid.get_cell(r, c)
                color = COLORS["empty"]

                if cell.wall:
                    color = COLORS["wall"]
                elif cell.start:
                    color = COLORS["start"]
                elif cell.end:
                    color = COLORS["end"]
                elif cell.visited:
                    color = COLORS["visited"]

                x1 = c * CELL_SIZE
                y1 = r * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE

                self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill=color,
                    outline="#2d2d2d"
                )

    def draw_path(self):
        cur = self.end
        while cur.parent:
            parent = cur.parent

            x1 = cur.col * CELL_SIZE + CELL_SIZE // 2
            y1 = cur.row * CELL_SIZE + CELL_SIZE // 2
            x2 = parent.col * CELL_SIZE + CELL_SIZE // 2
            y2 = parent.row * CELL_SIZE + CELL_SIZE // 2

            self.canvas.create_line(
                x1, y1, x2, y2,
                fill="#e2510e",   # path color (yellow)
                width=5           # line thickness
            )

            cur = parent
            self.root.update()

    # ---------- MOUSE ----------
    def left_click(self, event):
        row = event.y // CELL_SIZE
        col = event.x // CELL_SIZE
        cell = self.grid.get_cell(row, col)

        if not self.start:
            self.start = cell
            cell.start = True
        elif not self.end:
            self.end = cell
            cell.end = True
        else:
            cell.wall = not cell.wall

        self.draw()


# ---------- RUN ----------
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Maze Solver - Pathfinding Visualizer")
    App(root)
    root.mainloop()
