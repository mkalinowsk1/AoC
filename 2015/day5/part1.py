with open("input.in") as fin:
	file = fin.read().split()

def min_three_vowels(s):
	vowels = ["a","e","i","o","u"]
	num_of_vowels = 0
	for char in s:
		if char in vowels:
			num_of_vowels += 1
	if num_of_vowels >= 3:
		return True
	return False

def twice_in_row(s):
	tletters = ["aa", "bb", "cc", "dd", "ee","ff", "gg", "hh", "ii",
			 "jj","kk","ll","mm","nn","oo","pp","qq","rr","ss","tt",
			 "uu","vv","ww","xx","yy","zz"]
	for i in range(len(s)-1):
		if s[i]+s[i+1] in tletters:
			return True
	return False

def banned(s):
	banned = ["ab", "cd", "pq","xy"]
	for i in range(len(s)-1):
		if s[i]+s[i+1] in banned:
			return False
	return True
nice = 0
for line in file:
	if min_three_vowels(line) and twice_in_row(line) and banned(line):
		nice += 1
print(nice)