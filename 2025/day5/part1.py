with open ("input.in") as fin:
	lines = fin.read().strip().split("\n")


id_ranges = []
product_ids = []
split = 0
ans = 0

for i in range(len(lines)):
	if lines[i] == "":
		split = i
		break
		
	id_ranges.append(lines[i])

for i in range(split + 1, len(lines)):
	product_ids.append(lines[i])
		
for id in product_ids:
	for r in id_ranges:
		start, end = r.split("-")
		if int(id) <= int(end) and int(id) >= int(start):
			ans += 1
			break
			

print(ans)