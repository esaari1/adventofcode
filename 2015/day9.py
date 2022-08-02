import itertools

class Node:
	def __init__(self, name):
		self.name = name
		self.neighbors = {}

	def __str__(self):
		return self.name + ' ' + str(len(self.neighbors))

	def addNeighbor(self, node, weight):
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

	def pathLength(self, order, m):
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

		return length

f = open('input.txt')

line = f.readline()
g = Graph()

while line:
	line = line.strip()
	parts = line.split(' ')
	g.addEdge(parts[0], parts[2], int(parts[4]))
	line = f.readline()

f.close()

ls = list(range(len(g.nodes)))

p = itertools.permutations(ls)
#min = 1000000000
m = 0
for x in p:
	l = g.pathLength(x, m)
	if l is not None and l > m:
		m = l

print (m)