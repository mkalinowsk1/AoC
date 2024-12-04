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

def searchWord(grid, word):
	ans = []
	n = len(grid)
	m = len(grid[0])

	directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
			   (1, 1), (1, -1), (-1, 1), (-1, -1)]
	
	for i in range(n):
		for j in range(m):
			if grid[i][j] == word[0]:
				for dirX, dirY in directions:
					if findWordInDirection(grid, n, m, word, 0, i, j, dirX, dirY):
						ans.append([i, j])
	return ans


if __name__ == "__main__":
	grid = makeGrid(file)
	word = "XMAS"
	ans = searchWord(grid, word)
	print(len(ans))


