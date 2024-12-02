with open("2024/inputs/day2.in") as fin:
	file = fin.read().split("\n")

safe_count = 0

def check_line_safety(nums):
	problems_count = 0

	def is_valid(nums):
		if (all((nums[i] < nums[i + 1] and abs(nums[i] - nums[i + 1]) <= 3) for i in range(len(nums) - 1))):
			return True
		elif (all((nums[i] > nums[i + 1] and abs(nums[i] - nums[i + 1]) <= 3) for i in range(len(nums) - 1))):
			return True
		
		return False
	
	if is_valid(nums):
		return True
	
	for i in range(len(nums)):
		modified_list = nums[:i] + nums[i + 1:]
		if is_valid(modified_list):
			return True

	return False



for line in file:
	nums = line.split(" ")
	nums = [int(item) for item in nums]
	if check_line_safety(nums):
		safe_count += 1
print(safe_count)


