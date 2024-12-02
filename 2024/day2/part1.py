with open("2024/inputs/day2.in") as fin:
	file = fin.read().split("\n")

safe_count = 0

for line in file:
	nums = line.split(" ")
	nums = [int(item) for item in nums]
	if (all((nums[i] < nums[i + 1] and abs(nums[i] - nums[i + 1]) <= 3) for i in range(len(nums) - 1))):
		safe_count += 1
	elif (all((nums[i] > nums[i + 1] and abs(nums[i] - nums[i + 1]) <= 3) for i in range(len(nums) - 1))):
		safe_count += 1
print(safe_count)