with open ("input.in") as fin:
	line = fin.read().strip().split("\n")

grid_of_lists = []
for row_string in line:
    grid_of_lists.append(list(row_string)) 

grid = [list(row_string) for row_string in line]
	

ROWS = len(grid)
COLS = len(grid[0])
ans = 0

can_remove = False

adjacency = [(i,j) for i in (-1,0,1) for j in (-1,0,1) if not (i == j == 0)] 

def get_adjacent_cells(r_coord, c_coord):
    for dr, dc in adjacency:
        nr, nc = r_coord + dr, c_coord + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS: 
            yield grid[nr][nc]

while not can_remove:
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] != '@': 
                continue
            num_of_at_neighbors = 0
            
            for neighbor_char in get_adjacent_cells(r, c):
                if neighbor_char == "@" or neighbor_char == "X":
                    num_of_at_neighbors += 1
                    
            if num_of_at_neighbors < 4:
                ans += 1
                grid[r][c] = "X"
                
    can_remove = True

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "X":
                grid[r][c] = '.'
                can_remove = False
    


print(ans)