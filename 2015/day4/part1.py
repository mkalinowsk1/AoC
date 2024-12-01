import hashlib
num = 0
input = "ckczppom"
result = hashlib.md5(input.encode())
while result.hexdigest()[:5] != "00000":
	input = "ckczppom"
	num += 1
	input += str(num)
	result = hashlib.md5(input.encode())
	
print(num)