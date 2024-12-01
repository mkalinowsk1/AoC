import re

with open("input.in") as fin:
	file = fin.read().split()

def pairs(s):
	pair_positions = {}
	for i in range(len(s) - 1):
		pair = s[i:i+2]
		if pair in pair_positions and pair_positions[pair] < i - 1:
			return True
		pair_positions[pair] = i
	return False
	
def one_between(s):
	for i in range(len(s)-2):
		if s[i] == s[i+2]:
			return True
	return False

pattern1 = re.compile(r'(.{2}).*\1')
pattern2 = re.compile(r'(.).\1')


nice = 0
for line in file:
	if pattern1.search(line) and pattern2.search(line):
		nice += 1

# line = "ieodomkazucvgmuy"
# print(one_between(line))
# if pairs(line) and one_between(line):
#  	nice += 1
print(nice)


