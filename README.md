# 🧭 Pathfinding Algorithm Visualizer

A pathfinding visualizer built using Tkinter, designed to visually demonstrate how classic graph algorithms explore a maze and find (or fail to find) a path between two points.

This project focuses on clarity, interactivity, and clean visualization rather than raw performance.
 
## ✨ Features

## 🔍 Pathfinding Algorithms

Breadth-First Search (BFS)

Depth-First Search (DFS)

A* Search (with Manhattan heuristic)

## 🧱 Maze & Grid

Interactive grid (click to add/remove walls)

Random maze generation

Start & End node placement

## 🎛 Visualization Controls

Adjustable speed slider

Clear path without removing walls

Full grid reset

Line-based path rendering (clean & readable)

# 🖼 Screenshots

(Add screenshots or a GIF here)

Example:

![Pathfinding Visualizer Demo](screenshots/demo.gif)

## 🛠 Tech Stack

Language: Python 3

GUI: Tkinter (built-in)

Algorithms: BFS, DFS, A*

Data Structures: Queue, Stack, Priority Queue (heap)

No external dependencies required.

## ▶️ How to Run
1️⃣ Clone the repository
git clone https://github.com/<your-username>/algo-visualizer.git
cd algo-visualizer

2️⃣ Run the application
python main.py


Make sure Python 3.8+ is installed.

## 🧑‍🧭 How to Use

Left click on the grid:

First click → Start node (green)

Second click → End node (red)

Subsequent clicks → Toggle walls

Use the control panel to:

Adjust visualization speed

Run BFS / DFS / A*

Generate a random maze

Clear path or reset grid

If no valid path exists, a message will be displayed.


## 📌 Project Structure

algo_visualizer/

├── main.py

├── grid.py

├── cell.py

├── algorithms/

│   ├── bfs.py

│   ├── dfs.py

│   └── astar.py

└── README.md

## 🙌 Acknowledgements

Inspired by classic pathfinding visualizers and graph algorithm demonstrations.

## 📄 License

This project is open-source and free to use for learning and educational purposes.
