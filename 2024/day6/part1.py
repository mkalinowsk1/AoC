with open("2024/inputs/day6.in") as file:
    grid = [line.strip() for line in file]

nodes = []
rows = len(grid)
cols = len(grid[0])

class Node():
    def __init__(self, x, y, tile = False, guard= False, obstacle = False, visited = False):
        self.x = x
        self.y = y
        self.tile = tile
        self.guard = guard
        self.obstacle = obstacle
        self.visited = visited

guard_position = None
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == ".":
            nodes.append(Node(i,j,tile = True))
        elif grid[i][j] == "#":
            nodes.append(Node(i,j,obstacle = True))
        else:
            nodes.append(Node(i,j,guard=True))
            guard_position = (i, j)


directions = [(-1, 0), (0, 1), (1, 0),(0, -1)]
current_direction = 0

visited_tiles = set()
visited_tiles.add(guard_position)

x, y = guard_position
while True:
    dx, dy = directions[current_direction]
    nx, ny = x + dx, y + dy

    if 0 <= nx < rows and 0 <= ny < cols:
        if grid[nx][ny] == "#":
            current_direction = (current_direction + 1) % 4
        else:
            x, y = nx, ny
            visited_tiles.add((x, y))
    else:
        break
print(len(visited_tiles))

