with open("2024/inputs/day6.in") as file:
    grid = [list(line.strip()) for line in file]

rows = len(grid)
cols = len(grid[0])

guard_position = None
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == "^":
            guard_position = (i, j)
            break


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def simulate_with_obstruction(grid, start_pos):
    """Simulate guard's movement to check for a loop."""
    x, y = start_pos
    direction = 0 
    visited = set()  

    while True:
        state = (x, y, direction)
        if state in visited:
            return True  
        visited.add(state)

        dx, dy = directions[direction]
        nx, ny = x + dx, y + dy

        if 0 <= nx < rows and 0 <= ny < cols:
            if grid[nx][ny] == "#":  
                direction = (direction + 1) % 4  
            else:  
                x, y = nx, ny
        else:
            return False 

valid_positions = []
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == "." and (i, j) != guard_position:  
            valid_positions.append((i, j))

count = 0
for x, y in valid_positions:
    grid[x][y] = "#"
    if simulate_with_obstruction(grid, guard_position):
        count += 1
    grid[x][y] = "."

print("Number of ways to add an obstruction to create a loop:", count)
