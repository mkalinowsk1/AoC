
with open("input.in") as fin:
	file = fin.read().split("\n")


instructions = []
a = 1
# For part 2 a starts with 1 instead of 0
b = 0
j = 0
for i,line in enumerate(file):
	instructions.append(line)
	instructions[i] = instructions[i].split(" ")
while j < (len(instructions)):
	if instructions[j][0] == "hlf":
		if instructions[j][1] == "a":
			a = a//2
		else:
			b = b//2
		j += 1
	if instructions[j][0] == "tpl":
		if instructions[j][1] == "a":
			a = a * 3
		else:
			b = b * 3
		j += 1
	if instructions[j][0] == "inc":
		if instructions[j][1] == "a":
			a += 1
		else:
			b += 1
		j += 1
	if instructions[j][0] == "jmp":
		if int(instructions[j][1]) > 0:
			j += int(instructions[j][1]) 
		else: 
			j += int(instructions[j][1]) 
	if instructions[j][0] == "jie":
		if (instructions[j][1] == "a" and a % 2 == 0) or (instructions[j][1] == "b" and b % 2 == 0) :
			j += int(instructions[j][2]) 
		else:
			j += 1
	
	if instructions[j][0] == "jio":
		if (instructions[j][1] == "a" and a == 1) or (instructions[j][1] == "b" and b == 1):
			j += int(instructions[j][2]) 
		else:
			j += 1
	print(j)
print(f"a:{a}, b:{b}")