class Deer:
	def __init__(self, name, speed, time1, time2):
		self.name = name
		self.speed = speed
		self.time1 = time1
		self.time2 = time2
		self.cycle = self.time1 + self.time2
		self.cycleDist = self.time1 * self.speed
		self.dist = 0
		self.points =  0

	def distance(self, t):
		numCycles = int(t / self.cycle)
		remainder = t - (numCycles * self.cycle)

		dist = numCycles * self.cycleDist
		if remainder > self.time1:
			dist += self.cycleDist
		else:
			dist += self.speed * (self.time1 - remainder)

		#self.dist = dist

	def distance2(self, t):
		d = t % self.cycle
		#print(self.name, t+1, d)
		if d < self.time1:
			self.dist += self.speed

	def __str__(self):
		return self.name + ' ' + str(self.dist) + ' ' + str(self.points) + ' ' + str(self.speed)

f = open('input.txt', 'r')

line = f.readline()

deers = []

while line:
	line = line.strip()
	parts = line.split(' ')
	name = parts[0]
	speed = int(parts[3])
	time1 = int(parts[6])
	time2 = int(parts[13])

	deers.append(Deer(name, speed, time1, time2))

	line = f.readline()

f.close()

for t in range(2503):
	for d in deers:
		d.distance2(t)

	m1 = max(deers, key = lambda x: x.dist)

	for d in deers:
		if d.dist == m1.dist:
			d.points += 1

deers.sort(key = lambda x: x.points)
for d in deers:
	print(d)

exit(0)

for d in deers:
	d.distance(2503)

deers.sort(key = lambda x: x.dist)
for d in deers:
	print(d)
