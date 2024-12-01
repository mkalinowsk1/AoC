with open("input.in") as fin:
	file = fin.read().split()

ans = 0

for line in file:
	code_len = len(line)
	decoded_string = bytes(line, "utf-8").decode("unicode_escape")
	if decoded_string.startswith('"') and decoded_string.endswith('"'):
		decoded_string = decoded_string[1:-1]

	decoded_string = decoded_string.replace(r'\\"', '\"')

	ans += (code_len - len(decoded_string))

print(ans)