foods = []
links = {}

class Food:
	def __init__(self, id):
		self.id = id
		self.ingredients = {}
		self.allergens = {}

	def __str__(self):
		return str(self.id) + ' '  + ','.join(self.ingredients) + ' ' + ','.join(self.allergens)

def remove(i, a):
	links[a] = i
	for food in foods:
		if i in food.ingredients:
			food.ingredients.remove(i)
		if a in food.allergens:
			food.allergens.remove(a)


def search():
	match = filter(lambda x: len(x.allergens) == 1, foods)
	i = None
	a = None
	for m in match:
		i = m.ingredients
		a = m.allergens.pop()
		m.allergens.add(a)

		match2 = filter(lambda x: x.id != m.id and a in x.allergens, foods)
		for m2 in match2:
			i = i.intersection(m2.ingredients)

			if  len(i) == 1:
				i = i.pop()
				remove(i, a)
				i = None

	match = filter(lambda x: len(x.allergens) == 1, foods)
	for m in match:
		a = m.allergens.pop()
		m.allergens.add(a)

		if len(m.ingredients) == 1:
			i = m.ingredients.pop()
			remove(i, a)

		match2 = filter(lambda x: x.id != m.id and a in x.allergens, foods)
		for m2 in match2:
			i = m.ingredients.intersection(m2.ingredients)
			if len(i) == 1:
				i = i.pop()
				remove(i, a)

f = open('input.txt', 'r')
line = f.readline()

all = set([])

print('Reading input')
id = 1
while line:
	line = line.strip()

	food = Food(id)
	id += 1

	parts = line.split('(')
	food.ingredients = set(parts[0].strip().split(' '))
	food.allergens = set([x.strip() for x in parts[1][9:-1].split(',')])
	foods.append(food)

	all = all.union(food.allergens)

	line = f.readline()

f.close()

print('Processing')

allergenMatch = filter(lambda x: len(x.allergens) > 0, foods)
allergenMatch = [item for item in allergenMatch if item]
while len(allergenMatch) > 0:
	print(len(allergenMatch))
	search()
	allergenMatch = filter(lambda x: len(x.allergens) > 0, foods)
	allergenMatch = [item for item in allergenMatch if item]

print("Summing")

count = 0
for food in foods:
	#print(food)
	count += len(food.ingredients)
print(count)

keys = list(links.keys())
keys.sort()

ans = ''
for k in keys:
	print(k, links[k])
	ans += links[k] + ','

print(ans)
