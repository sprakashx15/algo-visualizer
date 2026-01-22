class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.wall = False
        self.visited = False
        self.start = False
        self.end = False
        self.parent = None

    def reset(self):
        self.visited = False
        self.parent = None

    def __lt__(self, other):
        return False
