from math import ceil, floor

class Weapon:
	def __init__(self, c, d):
		self.cost = c
		self.dmg = d

class Armor:
	def __init__(self, c, a):
		self.cost = c
		self.arm = a

class Ring:
	def __init__(self, c, d, a):
		self.cost = c
		self.dmg = d
		self.a = a

weapons = [
	Weapon(8, 4),
	Weapon(10, 5),
	Weapon(25, 6),
	Weapon(40, 7),
	Weapon(74, 8)
]

armors = [
	Armor(13, 1),
	Armor(31, 2),
	Armor(53, 3),
	Armor(75, 4),
	Armor(102, 5),
]

drings = [
	Ring(25, 1, 0),
	Ring(50, 2, 0),
	Ring(100, 3, 0)
]

arings = [
	Ring(20, 0, 1),
	Ring(40, 0, 2),
	Ring(80, 0, 3),
]

answer = 0

def getCost(myDMG, dmgCost):
	protection = 9 - myDMG
	if protection <= 0:
		return dmgCost

	minArmor = protection - 3
	minArmor = max(minArmor, 0)

	mincost = 10000

	for i in range(minArmor, protection):
		if i < 6:
			if i > 0:
				acost = armors[i - 1].cost
			else:
				acost = 0
			if protection - 1 > 0:
				rcost = arings[(protection - i) - 1].cost
			else:
				rcost = 0
			mincost = min(mincost, dmgCost + acost + rcost)

	return mincost

def cost2(myDMG, dmgCost):
	maxProtection = 8 - myDMG
	if maxProtection < 0:
		return 0

	minArmor = maxProtection - 3
	minArmor = max(minArmor, 0)

	maxcost = 0
	for i in range(minArmor, maxProtection):
		if i > 0:
			acost = armors[i - 1].cost
		else:
			acost = 0
		if maxProtection - i > 0:
			rcost = arings[(maxProtection - i)  - 1].cost
		else:
			rcost = 0
		maxcost = max(maxcost, dmgCost + acost + rcost)
	return maxcost

if False:
	for w in weapons:
		mine = w.dmg - 2
		cost = getCost(mine, w.cost)
		answer = min(answer, cost)

		for ring in drings:
			cost = getCost(mine + ring.dmg, w.cost + ring.cost)
			answer = min(answer, cost)

	print(answer)

for w in weapons:
	myDMG = w.dmg - 2
	cost = cost2(myDMG, w.cost)
	answer = max(answer, cost)

	for ring in drings:
		cost = cost2(myDMG + ring.dmg, w.cost + ring.cost)
		answer = max(answer, cost)

print(answer)
