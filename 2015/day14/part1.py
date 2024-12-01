with open("input.in") as fin:
	file = fin.read().split("\n")


reindeers = []
distances = []
for line in file:
	line = line.split()
	reindeers.append((line[0],line[3],line[6],line[-2]))
print(reindeers[1])
for reindeer in reindeers:
	time = 2503
	distance = 0
	while time > 0:
		time -= int(reindeer[2])
		distance += int(reindeer[1])*int(reindeer[2])
		time -= int(reindeer[-1])
	distances.append(distance)
print(max(distances))