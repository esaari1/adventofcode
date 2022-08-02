import numpy as np

np.set_printoptions(threshold=np.inf)

data = []
rows = 100
steps = 100


def neightborCount(d, row, col):
	count = 0
	for r in range(row - 1, row + 2):
		if r < 0:
			continue
		if r >= rows:
			continue

		for c in range(col - 1, col + 2):
			if c < 0:
				continue
			if c >= rows:
				continue
			if r == row and c == col:
				continue

			if d[r][c] == '#':
				count += 1
	return count

def isCorner(r, c):
	if r == 0 and c == 0:
		return True
	if r == 0 and c == rows - 1:
		return True
	if r == rows - 1 and c == 0:
		return True
	if r == rows - 1 and c == rows - 1:
		return True
	return False

f = open('input.txt', 'r')
line = f.readline()

while line:
	data.append(line.strip())
	line = f.readline()

f.close()

a = np.array([ list(word) for word in data ])
a[0][0] = '#'
a[0][rows-1] = '#'
a[rows-1][0] = '#'
a[rows-1][rows-1] = '#'

b = a.copy()

for i in range(steps):
	for r in range(rows):
		for c in range(rows):
			if isCorner(r, c):
				continue
			count = neightborCount(a, r, c)
			if a[r][c] == '.' and count == 3:
				b[r][c] = '#'
			if a[r][c] == '#':
				if count != 2 and count != 3:
					b[r][c] = '.'

	a = b.copy()

print(a)
print(np.count_nonzero(a == '#'))
