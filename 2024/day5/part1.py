with open("2024/inputs/day5_1.in") as f:
	file = f.read().split("\n")

with open("2024/inputs/day5_2.in") as fin:
	file2 = fin.read().split("\n")

af = {}
right_updates = []
ans = 0

for pair in file:
	before, after = pair.split("|")
	af.setdefault(before, []).append(after)



def checkIfRight(file):
    for update in file:
        update = update.split(",")
        is_right = True
        for i in range(len(update)):
            for j in range(i + 1, len(update)):
                if update[j] not in af.get(update[i], []):
                    is_right = False
                    break
            if not is_right:
                break
        if is_right:
            right_updates.append(update)

checkIfRight(file2)

for update in right_updates:
    middle = (len(update) - 1) // 2
    ans += int(update[middle])

print(ans)