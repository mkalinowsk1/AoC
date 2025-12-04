from functools import lru_cache

with open ("input.in") as fin:
	lines= fin.read().split("\n")

sum = 0

#@lru_cache(None)
def get_max_jolt(line, pick):
	if pick == 0:
		return ""
	
	n = len(line)
	if n == pick:
		return line
	
	c1 = line[0] + get_max_jolt(line[1:], pick - 1)
	c2 = get_max_jolt(line[1:], pick)

	return max(c1, c2)

for line in lines:
	max_jolt = get_max_jolt(line, 12)
	sum += int(max_jolt)

print(sum)