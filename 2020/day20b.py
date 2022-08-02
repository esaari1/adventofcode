import numpy as np

f = open('input3.txt', 'r')

line = f.readline()
data = []

while line:
	data.append([int(x) for x in line.strip()])
	line = f.readline()
f.close()

a = np.array([ list(word) for word in data ])
#a = np.rot90(a)
#a = np.flip(a, 0)

data = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
[1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,1],
[0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0]
]

pattern = np.array(data)

xmax = a.shape[1] - pattern.shape[1] + 1
ymax = a.shape[0] - pattern.shape[0] + 1

tgt = np.count_nonzero(pattern == 1)

result = 0
for j in range(2):
	for i in range(4):
		a2 = a.copy()

		for x in range(xmax):
			for y in range(ymax):
				subA = a[y:y+3,x:x+20]
				s = np.add(pattern, subA)
				count = np.count_nonzero(s == 2)

				if count == tgt:
					result += 1
					a2[y:y+3,x:x+20] = np.add(a[y:y+3,x:x+20], pattern)
		if result > 0:
			print(result)
			print(np.count_nonzero(a2 == 1))
			exit(0)

		a = np.rot90(a)

	a = np.rot90(a)
	a = np.flip(a, 0)
