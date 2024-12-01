with open ("input.in") as fin:
	path = fin.read()


santa_path = path[::2]
robot_path = path[1::2]
s_point = [0, 0]
r_point = [0, 0]
visited = [[0, 0]]
for char in santa_path:
	if char == "^":
		s_point[1] += 1
	if char == "v":
		s_point[1] -= 1
	if char == ">":
		s_point[0] += 1
	if char == "<":
		s_point[0] -= 1
	if s_point not in visited:
		visited.append(s_point[:])

for char in robot_path:
	if char == "^":
		r_point[1] += 1
	if char == "v":
		r_point[1] -= 1
	if char == ">":
		r_point[0] += 1
	if char == "<":
		r_point[0] -= 1
	if r_point not in visited:
		visited.append(r_point[:])

print(len(visited))