from collections import deque

c = {}
idx = [16, 1, 0, 18, 12, 14, 19]
#idx = [0, 3, 6]
for i in range(len(idx)):
	c[idx[i]] = i

p = {}
l = 16
count = len(idx)

while count < 30000000:

	if l in p:
		d = c[l] - p[l]
		if d in c:
			p[d] = c[d]
		c[d] = count
		l = d
	else:
		if 0 in c:
			p[0] = c[0]
		c[0] = count
		l = 0

	count += 1

print(l)