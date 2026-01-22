import time
import heapq

def heuristic(a, b):
    return abs(a.row - b.row) + abs(a.col - b.col)

def astar(app):
    start = app.start
    end = app.end

    open_set = []
    heapq.heappush(open_set, (0, start))

    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}

    open_set_hash = {start}

    while open_set:
        _, current = heapq.heappop(open_set)
        open_set_hash.remove(current)

        current.visited = True
        app.draw()
        app.root.update()
        time.sleep(app.speed.get() / 1000)

        if current == end:
            return True

        for neighbor in app.grid.neighbors(current):
            temp_g = g_score[current] + 1

            if neighbor not in g_score or temp_g < g_score[neighbor]:
                neighbor.parent = current
                g_score[neighbor] = temp_g
                f = temp_g + heuristic(neighbor, end)
                f_score[neighbor] = f

                if neighbor not in open_set_hash:
                    heapq.heappush(open_set, (f, neighbor))
                    open_set_hash.add(neighbor)

    return False