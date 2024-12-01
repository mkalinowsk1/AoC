from itertools import combinations

with open("input.in") as fin:
	file = fin.read().split("\n")
len_of_combo = set()
numbers = []
how_many_comb_4 = 0
targer_sum = 150
for num in file:
	numbers.append(int(num))

def find_combinations(nums, target):
	result = []
	for r in range(1, len(nums) + 1):
		for comb in combinations(nums, r):
			if sum(comb) == target:
				result.append(comb)

	return result

combin_sum = find_combinations(numbers, targer_sum)
for combo in combin_sum:
	if len(combo) == 4:
		how_many_comb_4 += 1
print(how_many_comb_4)

