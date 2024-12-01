with open ("input.in") as fin:
	path = fin.read()
point = [0, 0]
visited = [[0, 0]]
for char in path:
	if char == "^":
		point[1] += 1
	if char == "v":
		point[1] -= 1
	if char == ">":
		point[0] += 1
	if char == "<":
		point[0] -= 1
	if point not in visited:
		visited.append(point[:])

print(len(visited))