import numpy as np

#np.set_printoptions(threshold=sys.maxsize)

a = np.zeros((1000, 1000), dtype=int)

f = open('input.txt', 'r')

line = f.readline()
while line:
	parts = line.split(' ')
	if len(parts) == 5:
		corner1 = parts[2].split(',')
		corner2 = parts[4].split(',')
		set = -1
		if parts[1] == 'on':
			set = 1

		r1, c1 = corner1
		r2, c2 = corner2
		a[int(r1):int(r2)+1, int(c1):int(c2)+1] += set
		a[a<0] = 0
	elif len(parts) == 4:
		corner1 = parts[1].split(',')
		corner2 = parts[3].split(',')

		r1, c1 = corner1
		r2, c2 = corner2
		a[int(r1):int(r2)+1, int(c1):int(c2)+1] += 2
	else:
		print(line)
		exit(1)
		
	line = f.readline()

f.close()

#print(a)
unique, counts = np.unique(a, return_counts=True)

count = 0
for idx in range(len(unique)):
	count = count + (unique[idx] * counts[idx])
print(count)
