with open("2024/inputs/day10.in") as file:
	f = file.read().strip().split("\n")

grid = [list(map(int, line)) for line in f]

def find_paths(grid):
	rows, cols = len(grid), len(grid[0])
	start_points = [(r,c) for r in range(rows) for c in range(cols) if grid[r][c] == 0]
	end_val = 9
	paths = []

	def is_valid(r, c, visited, current_val):
		return (
            0 <= r < rows and 0 <= c < cols and 
            (r, c) not in visited and 
            grid[r][c] == current_val + 1
        )
	
	def dfs(r, c, current_val, path, visited):
		# If we reached the height 9, we append the current path to the list
		
		
		visited.add((r, c))
		path.append((r, c))

		for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Up, Down, Left, Right
			nr, nc = r + dr, c + dc
			if is_valid(nr, nc, visited, current_val):
				dfs(nr, nc, current_val + 1, path, visited)

		if current_val == end_val:
			paths.append(path[:])
			return
			
		visited.remove((r, c))
		path.pop()

		

	# Perform DFS from each trailhead (height 0)
	for sr, sc in start_points:
		dfs(sr, sc, 0, [], set())
	
	


	return paths

print(len(find_paths(grid)))