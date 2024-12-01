def presents_per_house(house_num):
	return 11 * sum(house_num // elf for elf in range(1, 51) if house_num % elf == 0)

house_num = 786240
INPUT = 34000000
presents_delivered = 0
while presents_delivered < INPUT:
	print(house_num)
	presents_delivered = presents_per_house(house_num)
	print(f"{presents_delivered=}")
	house_num += 1
print(house_num-1)