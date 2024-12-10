with open("2024/inputs/day9.in") as file:
	data = file.read()

disc = []
index = 0
ans = 0

for i in range(len(data)):
	if i % 2 == 0:
		for j in range(int(data[i])):
			disc.append(index)
		index += 1
	else:
		for k in range(int(data[i])):
			disc.append("-1")

i = 0
while i < len(disc):
    if disc[i] == "-1":
        disc[i] = disc[-1]
        disc = disc[:-1]
    else:
        i += 1

for i in range(len(disc)):
	ans += i * int(disc[i])

print(ans)