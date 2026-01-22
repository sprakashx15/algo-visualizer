import time
from collections import deque

def bfs(app):
    queue = deque([app.start])
    visited = {app.start}

    while queue:
        current = queue.popleft()
        current.visited = True
        
        app.draw()
        app.root.update()
        time.sleep(app.speed.get() / 1000)
        
        if current == app.end:
            return True

        for neighbor in app.grid.neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                neighbor.parent = current
                queue.append(neighbor)
    return False