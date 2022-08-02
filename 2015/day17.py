input = [50,44,11,49,42,46,18,32,26,40,21,7,18,43,10,47,36,24,22,40]
#input = [20, 15, 10, 5, 5]

target = 150
#target = 25

class Stack:
	def __init__(self):
		self.s = []

	def push(self, i):
		self.s.append(i)

	def last(self):
		return self.s[-1]

	def pop(self):
		if len(self.s) == 0:
			return None
		return self.s.pop()

	def clear(self):
		self.s = []

	def value(self):
		v = 0
		for x in self.s:
			v += input[x]
		return v

	def next(self):
		i = self.pop()
		while i == len(input) - 1:
			i = self.pop()
			if i is None:
				return
		self.push(i + 1)

	def __str__(self):
		ews = [input[x] for x in self.s]
		v = sum(input[x] for x in self.s)
		return str(self.s) + ' ' + str(ews) + ' ' + str(v)

count = 0
s = Stack()

lengthMap = {}

s.push(0)

while len(s.s) > 0:
	while s.value() < target and s.last() < len(input) - 1:
		s.push(s.last() + 1)
	if s.value() == target:
		count += 1
		if len(s.s) not in lengthMap:
			lengthMap[len(s.s)] = 1
		else:
			lengthMap[len(s.s)] += 1
	s.next()

print(count)
keys = list(lengthMap.keys())
keys.sort()
print(lengthMap[keys[0]])
