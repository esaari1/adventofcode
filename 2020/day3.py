import numpy as np

f = open('input.txt', 'r')

data = []
line = f.readline()
while line:
	data.append(line.strip())
	line = f.readline()

f.close()

a = np.array([ list(word) for word in data ])
[rows, cols] = a.shape

cdelta = [1, 3, 5, 7, 1]
rdelta = [1, 1, 1, 1, 2]

total = 1

for idx in range(len(cdelta)):
	count = 0
	r = 0
	c = 0

	while r < rows:
		c = (c + cdelta[idx]) % cols
		r += rdelta[idx]
		if r < rows:
			if a[r][c] == '#':
				count += 1

	total *= count
print(total)
