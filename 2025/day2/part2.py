with open ("input.in") as fin:
	line = fin.read().split(",")

sum = 0
ranges = []
largest_num = 0
for r in line:
	start, end = r.split("-")
	ranges.append((int(start), int(end)))

	if int(end) > largest_num:
		largest_num = int(end)

print(ranges)

def generate_invalid_ids(largest):
	invalids = set()
	for k in range(2, len(str(largest)) + 1):
		x = 1
		while True:
			x_str = str(x)

			i_str = x_str * k
			I = int(i_str)

			if I > largest:
				break
			invalids.add(I)
			x += 1
	return invalids

possible_invalid_ids = generate_invalid_ids(largest_num)


for r in ranges:
	for id in possible_invalid_ids:
		if id >= r[0] and id <= r[1]:
			sum += id



print(sum)

