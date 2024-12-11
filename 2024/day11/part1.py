with open("2024/inputs/day11.in") as fin:
	stones = fin.read().strip().split(" ")

stones = list(map(int, stones))
def apply_rules(stones):
	i = 0
	while i < len(stones):
		if stones[i] == 0:
			stones[i] = 1
		elif len(str(stones[i])) % 2 == 0:
			s = str(stones[i])
			left_num, right_num = s[:len(s)//2], s[len(s)//2:]
			stones[i] = int(left_num)
			stones.insert(i + 1, int(right_num))
			i += 1 
		else:
			stones[i] = stones[i] * 2024
		i += 1

for i in range(25):
	apply_rules(stones)

print(len(stones))