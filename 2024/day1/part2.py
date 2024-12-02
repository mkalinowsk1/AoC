with open("./inputs/day1.in") as fin:
	file = fin.read().split("\n")

left_collumn = []
right_collumn = []

similarity_score = 0

for line in file:
	left, right = line.split("   ")
	left_collumn.append(int(left))
	right_collumn.append(int(right))


for i in range(len(left_collumn)):
	similarity_score += left_collumn[i] * right_collumn.count(left_collumn[i])

print(similarity_score)