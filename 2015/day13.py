import itertools

class Node:
	def __init__(self, name):
		self.name = name
		self.neighbors = {}

	def __str__(self):
		print(self.name)
		for n in self.neighbors:
			print('\t' + n.name + ' ' + str(self.neighbors[n]))
		#return self.name + ' ' + str(len(self.neighbors))
		return ''

	def addNeighbor(self, node, weight):
		if node in self.neighbors:
			self.neighbors[node] += weight
		else:
			self.neighbors[node] = weight

	def getNeighbors(self):
		return self.neighbors.keys()

	def getWeight(self, neighbor):
		return self.neighbors[neighbor]

class Graph:
	def __init__(self):
		self.nodes = {}

	def __str__(self):
		for n in self.nodes:
			print(self.nodes[n])
		return ''

	def addEdge(self, name1, name2, weight):
		if not name1 in self.nodes:
			self.nodes[name1] = Node(name1)
		if not name2 in self.nodes:
			self.nodes[name2] = Node(name2)

		self.nodes[name1].addNeighbor(self.nodes[name2], weight)
		self.nodes[name2].addNeighbor(self.nodes[name1], weight)

	def pathLength(self, order):
		names = list(self.nodes.keys())
		length = 0
		idx = 0

		while idx < len(order) - 1:
			node1 = self.nodes[names[order[idx]]]
			node2 = self.nodes[names[order[idx+1]]]

			if not node2 in node1.neighbors:
				return None
			length += node2.neighbors[node1]
			idx += 1

		node1 = self.nodes[names[order[-1]]]
		node2 = self.nodes[names[order[0]]]
		if not node2 in node1.neighbors:
			return None

		length += node2.neighbors[node1]
		return length

g = Graph()
f = open('input.txt', 'r')
line = f.readline()

while line:
	line = line.strip()
	parts = line.split(' ')

	weight = int(parts[3])
	if parts[2] == 'lose':
		weight = -weight

	name1 = parts[0]
	name2 = parts[10][:-1]

	g.addEdge(name1, name2, weight)

	line = f.readline()

f.close()

result = 0

keys = list(g.nodes.keys())
for n in keys:
	print(n)
	g.addEdge("EWS", n, 0)

print(g)

ls = list(range(len(g.nodes)))
p = itertools.permutations(ls)
for x in p:
	l = g.pathLength(x)
	if l is not None:
		if l > result:
			result = l
print(result)
