import numpy as np
np.set_printoptions(threshold=np.inf)
with open("input.in") as fin:
	file = fin.read().split("\n")

grid = np.zeros((1000,1000))

for line in file:
	full_command = line.split(" ")
	if full_command[0] == 'toggle':
		starting_cords = full_command[1]
		going_coords = full_command[-1]
		sx,sy = starting_cords.split(",")
		gx, gy = going_coords.split(",")
		for i in range(int(sx),int(gx)):
			for j in range(int(sy),int(gy)+1):
				if grid[i][j] == 0:
					grid[i][j] = 1
				else:
					grid[i][j] = 0
	else:
		switch = full_command[1]
		starting_cords = full_command[2]
		going_coords = full_command[-1]
		sx,sy = starting_cords.split(",")
		gx, gy = going_coords.split(",")
		if switch == 'off':
			for i in range(int(sx),int(gx)+1):
				for j in range(int(sy),int(gy)+1):
					grid[i][j] = 0
		else:
			for i in range(int(sx),int(gx)+1):
				for j in range(int(sy),int(gy)+1):
					grid[i][j] = 1


print(np.sum(grid))

