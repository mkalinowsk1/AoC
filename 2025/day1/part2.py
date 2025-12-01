with open ("input.in") as fin:
	line = fin.read().split("\n")

dial_count = 50
zeros_count = 0

for rotation in line:
	dir, num = rotation[0], rotation[1:]
	crossings = 0
	if dir == "L":
		if dial_count == 0:
			crossings = int(num) // 100
		else:
			dis_to_zero = dial_count
			if int(num) >= dis_to_zero:
				crossings += 1
				rem_dist = int(num) - dis_to_zero
				crossings += rem_dist // 100
		
	else:
		if dial_count == 0:
			crossings = int(num) // 100
		else:
			dis_to_zero = 100 - dial_count
			if int(num) >= dis_to_zero:
				crossings += 1
				rem_dist = int(num) - dis_to_zero
				crossings += rem_dist // 100
	zeros_count += crossings

	if dir == "L":
		dial_count = (dial_count - int(num)) % 100
	else:
		dial_count = (dial_count + int(num)) % 100
print("zeros: ",zeros_count)
