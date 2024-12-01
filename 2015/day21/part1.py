import itertools

class Weapon:
	def __init__(self, cost, damage):
		self.cost = cost
		self.damage = damage
		self.defense = 0

class Armor:
	def __init__(self, cost, defense):
		self.cost = cost
		self.defense = defense
		self.damage = 0

class Ring:
	def __init__(self, cost, damage, defense):
		self.cost = cost
		self.damage = damage
		self.defense = defense

Dagger = Weapon(8,4)
Shortsword = Weapon(10,5)
Warhammer = Weapon(25,6)
Longsword = Weapon(40,7)
Greataxe = Weapon(74,8)

Leather = Armor(13, 1)
Chainmail = Armor(31, 2)
Splintmail = Armor(53,3)
Bandedmail = Armor(75,4)
Platemail = Armor(102,5)

Damage1ring = Ring(25, 1, 0)
Damage2ring = Ring(50, 2, 0)
Damage3ring = Ring(100, 3, 0)

Defense1ring = Ring(20, 0, 1)
Defense2ring = Ring(40, 0, 2)
Defense3ring = Ring(80, 0, 3)

weapons = [Dagger, Shortsword, Warhammer, Longsword, Greataxe]
armor = [Leather, Chainmail, Splintmail, Bandedmail, Platemail]
rings = [Damage1ring, Damage2ring, Damage3ring, Defense1ring, Defense2ring, Defense3ring]

weapons_combinations = list(itertools.combinations(weapons, 1))

# Step 2: Generate combinations from second list (0 or 1 item)
armor_combinations = list(itertools.chain.from_iterable(itertools.combinations(armor, r) for r in range(2)))

# Step 3: Generate combinations from third list (0, 1, or 2 items)
rings_combinations = list(itertools.chain.from_iterable(itertools.combinations(rings, r) for r in range(3)))

# Step 4: Use itertools.product to generate the Cartesian product of all combinations
all_combinations = itertools.product(weapons_combinations, armor_combinations, rings_combinations)

win_combs = []
costs = []

def simulate_fight(dmg, df):
	boss_hp = 100
	boss_damage = 8
	boss_armor = 2
	
	my_hp = 100
	my_damage = dmg
	my_armor = df

	while boss_hp > 0 and my_hp > 0:
		my_dmg_dealt = my_damage - boss_armor
		boss_dmg_dealt = boss_damage - my_armor
		if my_dmg_dealt <= 0:
			boss_hp -= 1
		else:
			boss_hp -= my_damage - boss_armor
		if boss_dmg_dealt <= 0:
			my_hp -= 1
		else:
			my_hp -= boss_damage - my_armor
	if boss_hp > 0:
		return False
	return True



for comb in all_combinations:
	dmg = 0
	df = 0
	total_cost = 0

	weapon = comb[0][0]
	dmg += weapon.damage
	total_cost += weapon.cost

	if comb[1]:
		armor_piece = comb[1][0]
		df += armor_piece.defense
		total_cost += armor_piece.cost

	for ring in comb[2]:
		dmg += ring.damage
		df += ring.defense
		total_cost += ring.cost

	if simulate_fight(dmg, df):
		win_combs.append(comb)
		costs.append(total_cost)

print(min(costs))
	
	


	
	