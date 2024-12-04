import re

with open("2024/inputs/day3.in") as f:
	data = f.read()

result = 0
pattern = r"mul\(\d+,\d+\)"
matches = re.findall(pattern, data)

for match in matches:
	args = match[4:-1].split(",")
	result += (int(args[0]) * int(args[1]))
print(result)
