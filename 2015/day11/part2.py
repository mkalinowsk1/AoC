def inc_threes(s):
	threes = ['abc','bcd','cde','def','efg','fgh','ghi','hij','ijk',
		   'jkl','klm','lmn','mno','nop','opq','pqr','qrs','rst','stu',
		   'tuv','uvw','vwx','xyz']
	for th in threes:
		if th in s:
			return True
	return False

def banned_letters(s):
	banned_letters = ['i','o','l']
	for letter in banned_letters:
		if letter in s:
			return False
	return True

def pairs(s):
	pairs = ['aa','bb','cc','dd','ee','ff','gg','hh','ii','jj',
		  'kk','ll','mm','nn','oo','pp','qq','rr','ss','tt','uu',
		  'vv','ww','xx','yy','zz']
	counter = 0
	for pair in pairs:
		if pair in s:
			counter += 1
	if counter >= 2:
		return True
	return False

def inc_pass(s):
	if password == '':
		return ''
	
	last_char = s[-1]

	if last_char == 'z':
		return inc_pass(s[:-1]) + 'a'
	else:
		return s[:-1] + chr(ord(last_char) + 1)
	


password = "vzbxxzaa"
while not (inc_threes(password) and banned_letters(password) and pairs(password)):
	password = inc_pass(password)
print(password)
