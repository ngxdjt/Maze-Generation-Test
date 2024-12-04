import numpy as np
import random

def create_maze(dim):
    maze = np.ones((dim*2+1, dim*2+1))

    x, y = (0, 0)
    maze[2*x+1, 2*y+1] = 0

    stack = [(x, y)]
    while len(stack) > 0:
        x, y = stack[-1]

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx >= 0 and ny >= 0 and nx < dim and ny < dim and maze[2*nx+1, 2*ny+1] == 1:
                maze[2*nx+1, 2*ny+1] = 0
                maze[2*x+1+dx, 2*y+1+dy] = 0
                stack.append((nx, ny))
                break
        else:
            stack.pop()

    maze[1, 0] = 0
    maze[-2, -1] = 0

    maze = maze.tolist()

    for row in maze:
        row[:] = [x if x != 1 else 'x' for x in row]
        row[:] = [x if x != 0 else ' ' for x in row]

    return maze

maze = create_maze(16)

for row in maze:
    print(str(row).replace("[", "").replace("]", "").replace(",", "").replace("'", ""))