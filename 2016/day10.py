class Object():
	def __init__(self, id):
		self.id = id
		self.values = []
		self.lowDest = None
		self.highDest = None

	def update(self):
		self.values.sort()
		if self.values[0] == 17 and self.values[1] == 61:
			print('ANS', self.id)
		if self.lowDest:
			self.lowDest.values.append(self.values[0])
		if self.highDest:
			self.highDest.values.append(self.values[1])
		self.values = []

def getObject(id, objs):
	if id not in objs:
		objs[id] = Object(id)
	return objs[id]

bots = {}
outputs = {}

for line in open('input.txt'):
	parts = line.strip().split(' ')

	if parts[0] == 'value':
		id = int(parts[-1])
		getObject(id, bots).values.append(int(parts[1]))
	else:
		sourceID = int(parts[1])
		lowID = int(parts[6])
		highID = int(parts[-1])

		if parts[5] == 'bot':
			getObject(sourceID, bots).lowDest = getObject(lowID, bots)
		else:
			getObject(sourceID, bots).lowDest = getObject(lowID, outputs)

		if parts[-2] == 'bot':
			getObject(sourceID, bots).highDest = getObject(highID, bots)
		else:
			getObject(sourceID, bots).highDest = getObject(highID, outputs)

bot_lst = list(bots.values())
run = True

while run:
	run = False
	f = filter(lambda b: len(b.values) == 2, bot_lst)
	for b in f:
		b.update()
		run = True

print(outputs[0].values, outputs[1].values, outputs[2].values)
m = 1
for o in outputs[0].values:
	m *= o
for o in outputs[1].values:
	m *= o
for o in outputs[2].values:
	m *= o
print(m)
