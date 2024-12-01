with open("input.in") as fin:
	file = fin.read().split("\n")

reindeers = []
for line in file:
	line = line.split()
	reindeers.append((line[0],int(line[3]),int(line[6]),int(line[-2])))

time = 2503
distances = {reindeer[0]: 0 for reindeer in reindeers}
points = {reindeer[0]: 0 for reindeer in reindeers}

for second in range(1, time + 1):
	for reindeer in reindeers:
		name, speed, fly_time, rest_time = reindeer
		cycle_time = fly_time + rest_time
		time_in_current_cycle = second % cycle_time

		if time_in_current_cycle <= fly_time and time_in_current_cycle != 0:
			distances[name] += speed

	max_distance = max(distances.values())

	for name, distance in distances.items():
		if distance == max_distance:
			points[name] += 1

print(max(points.values()))