black = {}

def move(dirs):
	dx = 0
	dy = 0
	l = list(dirs)
	i = 0
	while i < len(l):
		if l[i] == 'n':
			dy += 2
			i += 1
			if l[i] == 'w':
				dx -= 1
			if l[i] == 'e':
				dx += 1
		elif l[i] == 's':
			dy -= 2
			i += 1
			if l[i] == 'w':
				dx -= 1
			if l[i] == 'e':
				dx += 1
		elif l[i] == 'w':
			dx -= 2
		elif l[i] == 'e':
			dx += 2
		i += 1

	h = (dx,dy)
	if h not in black:
		black[h] = True
	else:
		del black[h]

def blackNeighbors(x, y):
	count = 0
	if (x-2, y) in black:
		count += 1
	if (x+2, y) in black:
		count += 1
	if (x-1,y+2) in black:
		count += 1
	if (x+1,y+2) in black:
		count += 1
	if (x-1,y-2) in black:
		count += 1
	if (x+1,y-2) in black:
		count += 1
	return count

def getMinMax():
	minX = min(black, key=lambda x: x[0])[0] - 2
	maxX = max(black, key=lambda x: x[0])[0] + 2
	minY = min(black, key=lambda x: x[1])[1] - 2
	maxY = max(black, key=lambda x: x[1])[1] + 2
	return minX, maxX, minY, maxY

def isBlack(x, y):
	neighbors = blackNeighbors(x, y)
	if (x, y) in black:
		if neighbors == 1 or neighbors == 2:
			return True
	else:
		if neighbors == 2:
			return True
	return False

for line in open('input.txt'):
	move(line.strip())

print(len(black))

for i in range(100):
	newBlack = {}
	minX, maxX, minY, maxY = getMinMax()

	for x in range(0, maxX + 1, 2):
		if isBlack(x, 0):
			newBlack[(x, 0)] = True

	for x in range(0, minX - 1, -2):
		if isBlack(x, 0):
			newBlack[(x, 0)] = True

	xoffset = 1
	for y in range(2, maxY + 1, 2):
		for x in range(xoffset, maxX + 1, 2):
			if isBlack(x, y):
				newBlack[(x, y)] = True

		for x in range(-xoffset, minX - 1, -2):
			if isBlack(x, y):
				newBlack[(x, y)] = True

		xoffset = 1 - xoffset

	xoffset = 1
	for y in range(-2, minY - 1, -2):
		for x in range(xoffset, maxX + 1, 2):
			if isBlack(x, y):
				newBlack[(x, y)] = True

		for x in range(-xoffset, minX - 1, -2):
			if isBlack(x, y):
				newBlack[(x, y)] = True

		xoffset = 1 - xoffset
	black = newBlack.copy()

print(len(black))