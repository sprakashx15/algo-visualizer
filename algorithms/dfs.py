import time

def dfs(app):
    stack = [app.start]
    visited = {app.start}

    while stack:
        current = stack.pop()
        current.visited = True

        app.draw()
        app.root.update()
        time.sleep(app.speed.get()/1000)

        if current == app.end:
            return True

        for neighbor in app.grid.neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                neighbor.parent = current
                stack.append(neighbor)
    return False