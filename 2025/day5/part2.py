with open ("input.in") as fin:
	lines = fin.read().strip().split("\n")


id_ranges_str = []
ans = 0
fresh_ids = set()

for i in range(len(lines)):
	if lines[i] == "":
		split = i
		break
		
	id_ranges_str.append(lines[i])

ranges = []
for r_str in id_ranges_str:
	start, end = r_str.split("-")
	ranges.append((int(start), int(end)))
		
			
ranges.sort(key = lambda x: x[0])

merged_ranges = []

current_start, current_end = ranges[0]

for next_start, next_end in ranges[1:]:
	if next_start <= current_end + 1:
		current_end = max(current_end, next_end)
	else:
		merged_ranges.append((current_start, current_end))
		current_start, current_end = next_start, next_end
merged_ranges.append((current_start, current_end))

for start, end in merged_ranges:
	ans += (end - start + 1)

print(ans)