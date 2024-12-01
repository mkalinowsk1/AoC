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
possible_aunts = []

for line in file:
	line = " ".join(line.split(": ")).split(" ")
	aunt_num = line[1]
	if AuntSue[line[2]] == line[3].replace(",", "") and AuntSue[line[4]] == line[5].replace(",", "") and AuntSue[line[6]] == line[7].replace(",", ""):
		possible_aunts.append(aunt_num)

print(possible_aunts)