from cell import Cell

class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[Cell(r, c) for c in range(cols)] for r in range(rows)]

    def get_cell(self, row, col):
        return self.grid[row][col]

    def neighbors(self, cell):
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        result = []
        for dr, dc in directions:
            r, c = cell.row + dr, cell.col + dc
            if 0 <= r < self.rows and 0 <= c < self.cols:
                neighbor = self.grid[r][c]
                if not neighbor.wall:
                    result.append(neighbor)
        return result
