import re

with open("2024/inputs/day3.in") as f:
	data = f.read()

result = 0
pattern = r"mul\(\d+,\d+\)|don't\(\)|do\(\)"
matches = re.findall(pattern, data)

on = True

for match in matches:
	if match == "don't()":
		on = False
		continue
	elif match == "do()":
		on = True
		continue
	if on:
		args = match[4:-1].split(",")
		result += (int(args[0]) * int(args[1]))

print(result)

		