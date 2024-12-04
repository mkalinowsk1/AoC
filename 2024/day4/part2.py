with open("2024/inputs/day4.in") as f:
	file = f.read().split("\n")

def makeGrid(file):
	grid = []
	for i in range(len(file)):
		grid.append(list(file[i]))
	return grid

def isValid(x,y, sizeX, sizeY):
	return 0 <= x < sizeX and 0 <= y < sizeY

def findWordInDirection(grid, n, m, word, index, x, y, dirX, dirY):
	if index == len(word):
		return True
	
	if isValid(x, y, n, m) and word[index] == grid[x][y]:
		return findWordInDirection(grid, n, m, word, index + 1, x + dirX, y + dirY, dirX, dirY)
	
	return False

def searchWord(grid):
	ans = []
	n = len(grid)
	m = len(grid[0])
	
	directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
	
	for i in range(n):
		for j in range(m):
			if grid[i][j] == "A":
				positions = []
				for dirX, dirY in directions:
					neighbor_x = i + dirX
					neighbor_y = j + dirY
					if isValid(neighbor_x, neighbor_y, n, m):
						positions.append(grid[neighbor_x][neighbor_y])
				if len(positions) == 4:
					if (
						{positions[0], positions[3]} == {"M", "S"} and
						{positions[1], positions[2]} == {"M", "S"}
					):
						ans.append([i, j])
	return ans


if __name__ == "__main__":
	grid = makeGrid(file)
	ans = searchWord(grid)
	print(len(ans))


