from math import floor, ceil
import numpy as np

ews = np.zeros((128 * 8))

def getSeat(bp):
	row = [0, 127]
	col = [0, 7]
	for c in bp:
		if c == 'F':
			row[1] = floor(((row[1] - row[0]) / 2) + row[0])
		elif c == 'B':
			row[0] = ceil(((row[1] - row[0]) / 2) + row[0])
		elif c == 'L':
			col[1] = floor(((col[1] - col[0]) / 2) + col[0])
		else:
			col[0] = ceil(((col[1] - col[0]) / 2) + col[0])
	return row[0] * 8 + col[0]

f = open("input.txt", "r")
line = f.readline()

a = 0
while line:
	seat = getSeat(line)
	ews[seat] = 1
	a = max(a, seat)
	line = f.readline()

f.close()
print(a)
print(np.where(ews == 0))
