with open ("input.in") as fin:
	line = fin.read().split("\n")

dial_count = 50
zeros_count = 0

for rotation in line:
	dir, num = rotation[0], rotation[1:]
	if dir == "L":
		if dial_count == 0:
			zeros_count += 1
		dial_count -= int(num)
		if dial_count < 0:
			dial_count = 100 + (dial_count % -100)
		if dial_count == 100:
			dial_count = 0
		
	else:
		if dial_count == 0:
			zeros_count += 1
		dial_count += int(num)
		if dial_count > 100:
			dial_count = dial_count % 100
		if dial_count == 100:
			dial_count = 0


print(zeros_count)
