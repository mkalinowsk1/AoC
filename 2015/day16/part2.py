from collections import Counter

with open("input.in") as fin:
	file = fin.read().split("\n")

AuntSue = {
	"children": "3",
	"cats": "7",
	"samoyeds": "2",
	"pomeranians": "3",
	"akitas": "0",
	"vizslas": "0",
	"goldfish": "5",
	"trees": "3",
	"cars": "2",
	"perfumes": "1"
}

	# children = 0
	# cats = 0
	# samoyeds = 0
	# pomeranians =  0
	# akitas = 0
	# vizslas = 0
	# goldfish = 0
	# trees = 0
	# cars = 0
	# perfumes = 0

possible_aunts = []
aunts = []
counter = 0
for line in file:
	line = " ".join(line.split(": ")).split(" ")
	aunt_num = line[1]
	aunts.append({line[2]:line[3].replace(",",""),
			   line[4]:line[5].replace(",",""),
			   line[6]: line[7].replace(",","")})
for aunt in aunts:
	counter += 1
	for key in aunt.keys():
		if key == "cats" or key == "threes":
			if AuntSue[key] < aunt[key]:
				possible_aunts.append(counter)
		elif key == "pomeranians" or key == "goldfish":
			if AuntSue[key] > aunt[key]:
				possible_aunts.append(counter)
		elif AuntSue[key] == aunt[key]:
			possible_aunts.append(counter)

print(Counter(possible_aunts))