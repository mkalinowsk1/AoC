with open ("input.in") as fin:
	line = fin.read().split("\n")

sum = 0

for bank in line:
	left, right = 0, len(bank) - 1
	max_joltage = 0

	for i in range(len(bank)):
		for j in range(i + 1, len(bank)):
			largest_num = bank[i] + bank[j]

			if int(largest_num) > max_joltage:
				max_joltage = int(largest_num)
	sum += max_joltage

print(sum)