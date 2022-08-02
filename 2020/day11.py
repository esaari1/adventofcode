import numpy as np

def left(d, r, c):
	while c > 0:
		c -= 1
		if d[r][c] == '#':
			return 1
		if d[r][c] == 'L':
			return 0
	return 0

def right(d, r, c):
	while c < rows - 1:
		c += 1
		if d[r][c] == '#':
			return 1
		if d[r][c] == 'L':
			return 0
	return 0

def up(d, r, c):
	while r > 0:
		r -= 1
		if d[r][c] == '#':
			return 1
		if d[r][c] == 'L':
			return 0
	return 0

def down(d, r, c):
	while r < rows - 1:
		r += 1
		if d[r][c] == '#':
			return 1
		if d[r][c] == 'L':
			return 0
	return 0

def upLeft(d, r, c):
	while r > 0 and c > 0:
		c -= 1
		r -= 1
		if d[r][c] == '#':
			return 1
		if d[r][c] == 'L':
			return 0
	return 0

def upRight(d, r, c):
	while r > 0 and c < rows - 1:
		c += 1
		r -= 1
		if d[r][c] == '#':
			return 1
		if d[r][c] == 'L':
			return 0
	return 0


def downLeft(d, r, c):
	while r < rows - 1 and c > 0:
		c -= 1
		r += 1
		if d[r][c] == '#':
			return 1
		if d[r][c] == 'L':
			return 0
	return 0

def downRight(d, r, c):
	while r < rows - 1 and c < rows - 1:
		c += 1
		r += 1
		if d[r][c] == '#':
			return 1
		if d[r][c] == 'L':
			return 0
	return 0


def neightborCount(d, row, col):
	count = left(d, row, col)
	count += right(d, row, col)
	count += up(d, row, col)
	count += down(d, row, col)
	count += upLeft(d, row, col)
	count += upRight(d, row, col)
	count += downLeft(d, row, col)
	count += downRight(d, row, col)

	return count

data = []

f = open('input.txt', 'r')
line = f.readline()
rows = len(line) - 1

while line:
	data.append(line.strip())
	line = f.readline()

f.close()

a = np.array([ list(word) for word in data ])
b = a.copy()

while True:
	for r in range(rows):
		for c in range(rows):
			if a[r][c] == '.':
				continue
			count = neightborCount(a, r, c)
			if a[r][c] == 'L' and count == 0:
				b[r][c] = '#'
			if a[r][c] == '#':
				if count >= 5:
					b[r][c] = 'L'

	if np.array_equal(a, b):
		print(np.count_nonzero(a == '#'))
		exit(0)
	a = b.copy()
