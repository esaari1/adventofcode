from copy import deepcopy

class Spell(object):
	def __init__(self, cost, dmg = 0, heal = 0, duration = 0, arm = 0, recharge = 0):
		self.cost = cost
		self.dmg = dmg
		self.heal = heal
		self.duration = duration
		self.arm = arm
		self.recharge = recharge

	def __str__(self):
		return str(self.cost)

class State(object):
	def __init__(self, hp, mana, bhp, bdmg):
		self.hp = hp
		self.arm = 0
		self.mana = mana
		self.bhp = bhp
		self.bdmg = bdmg
		self.spells = {}

	def __str__(self):
		return 'hp = %d, arm = %d, mana = %d, bhp = %d, bdmg = %d, spells = %d' % (self.hp, self.arm, self.mana, self.bhp, self.bdmg, len(self.spells))

	def canCast(self, spell):
		if spell.cost in self.spells:
			return False
		return self.mana >= spell.cost

	def apply(self, spell):
		self.mana -= spell.cost
		self.arm = 0
		if spell.duration > 0:
			self.spells[spell.cost] = spell.duration
			self.arm += spell.arm
		else:
			self.bhp -= spell.dmg
			self.hp += spell.heal

	def updateSpells(self):
		doneSpells = []
		self.arm = 0
		for cost in self.spells:
			self.bhp -= spells[cost].dmg
			self.mana += spells[cost].recharge
			self.arm += spells[cost].arm
			self.spells[cost] -= 1
			if self.spells[cost] == 0:
				doneSpells.append(cost)

		for cost in doneSpells:
			del self.spells[cost]

spells = {}
spells[53] = Spell(53, dmg = 4)
spells[73] = Spell(cost = 73, dmg = 2, heal = 2)
spells[113] = Spell(cost = 113, arm = 7, duration = 6)
spells[173] = Spell(cost = 173, dmg = 3, duration = 6)
spells[229] = Spell(cost = 229, recharge = 101, duration = 5)

bestScore = 100000000

def round(state, used, r):
	global bestScore
	state.hp -= 1
	if state.hp <= 0:
		# lose
		# print(r, 'LOSE')
		# print()
		return

	stateCopy = deepcopy(state)

	for cost in spells:
		# Player turn
		#print(r, '1 Player', state)
		state.updateSpells()
		#print(r, '2 Player', state)

		if used + cost > bestScore:
			continue
		if state.canCast(spells[cost]):
			state.apply(spells[cost])
			#print(r, '3 Player CAST', cost, state)

			# boss turn
			state.hp -= 1
			if state.hp <= 0:
				state.hp += 1
				continue
			state.updateSpells()
			#print(r, '1 Boss', state)
			if state.bhp <= 0:
				# win
				win = used + cost
				#print(r, 'WIN', win)
				#print()
				bestScore = min(bestScore, win)
				return

			state.hp = state.hp - (state.bdmg - state.arm)
			#print(r, '2 Boss', state)
			round(state, used + cost, r + 1)

		state = deepcopy(stateCopy)
	#print()

state = State(50, 500, 58, 9)
#state = State(10, 250, 13, 8)
#state = State(10, 250, 14, 8)
round(state, 0, 1)
print(bestScore)
