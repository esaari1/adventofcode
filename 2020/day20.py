import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

pieces = {}
handled = {}
edges = {}

LEFT = 0
RIGHT = 1
TOP = 2
BOTTOM = 3

minX = 0
maxX = 0
minY = 0
maxY = 0

def matchPieces(h, piece1, piece2):
	global edges
	if LEFT not in edges[h]:
		m = matchEdge(piece1, piece2, LEFT)
		if m is not None:
			return m, LEFT

	if RIGHT not in edges[h]:
		m = matchEdge(piece1, piece2, RIGHT)
		if m is not None:
			return m, RIGHT

	if TOP not in edges[h]:
		m = matchEdge(piece1, piece2, TOP)
		if m is not None:
			return m, TOP

	if BOTTOM not in edges[h]:
		m = matchEdge(piece1, piece2, BOTTOM)
		if m is not None:
			return m, BOTTOM
	return None, None

def matchEdge(piece1, piece2, side):
	for j in range(2):
		for i in range(4):
			s1 = []
			s2 = []
			if side == LEFT:
				s1 = piece1[:,0]
				s2 = piece2[:,9]
			elif side == RIGHT:
				s1 = piece1[:,9]
				s2 = piece2[:,0]
			elif side == TOP:
				s1 = piece1[0]
				s2 = piece2[9]
			else:
				s1 = piece1[9]
				s2 = piece2[0]
			if (s1 == s2).all():
				return piece2

			piece2 = np.rot90(piece2)
		piece2 = np.rot90(piece2)
		piece2 = np.flip(piece2, 0)

	return None

def doRun():
	global minX, maxX, minY, maxY
	newH = {}
	for h in handled:
		for k in pieces:
			if k in handled:
				continue

			match, side = matchPieces(h, pieces[h], pieces[k])
			if match is not None:
				edges[h][side] = True

				pos = handled[h]
				pieces[k] = match
				if side == LEFT:
					newH[k] = [pos[0] - 1, pos[1]]
				elif side == RIGHT:
					newH[k] = [pos[0] + 1, pos[1]]
				elif side == TOP:
					newH[k] = [pos[0], pos[1] - 1]
				else:
					newH[k] = [pos[0], pos[1] + 1]

				minX = min(minX, newH[k][0])
				maxX = max(maxX, newH[k][0])
				minY = min(minY, newH[k][1])
				maxY = max(maxY, newH[k][1])

	return newH

f = open('input.txt', 'r')

line = f.readline()

tileID = 0
data = []
while line:
	line = line.strip()

	if line.startswith('Tile'):
		tileID = int(line.split(' ')[1][:-1])
	elif line == '':
		pieces[tileID] = np.array([ list(word) for word in data ])
		edges[tileID] = {}
		data = []
	else:
		data.append(line)

	line = f.readline()

f.close()
pieces[tileID] = np.array([ list(word) for word in data ])
edges[tileID] = {}

#handled[2311] = [0,0]
handled[1409] = [0,0]

while len(handled) < len(pieces):
	print(len(handled), len(pieces))

	newH = doRun()
	for h in newH:
		handled[h] = newH[h]

result = 1
for h in handled:
	if handled[h][0] in [minX, maxX] and handled[h][1] in [minY, maxY]:
		result *= h

print(result)
print(minX, maxX, minY, maxY)
sizeX = (maxX - minX + 1) * 8
sizeY = (maxY - minY + 1) * 8
print(sizeX, sizeY)

a = np.empty((sizeX, sizeY), dtype=str)

for k in handled:
	y = handled[k][0] + abs(minX)
	x = handled[k][1] + abs(minY)
	a[x*8:x*8+8,y*8:y*8+8] = pieces[k][1:-1,1:-1]

a = np.array2string(a, max_line_width=np.inf)

print(a)
