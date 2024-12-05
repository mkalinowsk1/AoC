with open("2024/inputs/day5_1.in") as f:
	file = f.read().split("\n")

with open("2024/inputs/day5_2.in") as fin:
	file2 = fin.read().split("\n")

af = {}
not_right_updates = []
corrected_updates = []
ans = 0

for pair in file:
	before, after = pair.split("|")
	af.setdefault(before, []).append(after)

def checkIfNotRight(file):
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
            continue
        else:
             not_right_updates.append(update)
        
def correctUpdate(updates):
     for update in updates:
        for i in range(len(update)):
            for j in range(i + 1, len(update)):
                if update[j] not in af.get(update[i], []):
                    update[i], update[j] = update[j], update[i]
        corrected_updates.append(update)

checkIfNotRight(file2)
correctUpdate(not_right_updates)

for update in corrected_updates:
    middle = (len(update) - 1) // 2
    ans += int(update[middle])

print(ans)