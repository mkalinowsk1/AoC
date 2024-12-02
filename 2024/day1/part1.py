with open("./inputs/day1.in") as fin:
	file = fin.read().split("\n")

left_collumn = []
right_collumn = []

total_distance = 0

for line in file:
	left, right = line.split("   ")
	left_collumn.append(int(left))
	right_collumn.append(int(right))

left_collumn.sort()
right_collumn.sort()

for i in range(len(left_collumn)):
	total_distance += abs(left_collumn[i] - right_collumn[i])

print(total_distance)
