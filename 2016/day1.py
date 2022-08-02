input = 'R3, L5, R2, L2, R1, L3, R1, R3, L4, R3, L1, L1, R1, L3, R2, L3, L2, R1, R1, L1, R4, L1, L4, R3, L2, L2, R1, L1, R5, R4, R2, L5, L2, R5, R5, L2, R3, R1, R1, L3, R1, L4, L4, L190, L5, L2, R4, L5, R4, R5, L4, R1, R2, L5, R50, L2, R1, R73, R1, L2, R191, R2, L4, R1, L5, L5, R5, L3, L5, L4, R4, R5, L4, R4, R4, R5, L2, L5, R3, L4, L4, L5, R2, R2, R2, R4, L3, R4, R5, L3, R5, L2, R3, L1, R2, R2, L3, L1, R5, L3, L5, R2, R4, R1, L1, L5, R3, R2, L3, L4, L5, L1, R3, L5, L2, R2, L3, L4, L1, R1, R4, R2, R2, R4, R2, R2, L3, L3, L4, R4, L4, L4, R1, L4, L4, R1, L2, R5, R2, R3, R3, L2, L5, R3, L3, R5, L2, R3, R2, L4, L3, L1, R2, L2, L3, L5, R3, L1, L3, L4, L3'
#input = 'R8, R4, R4, R8'

input = [x.strip() for x in input.split(',')]

x = 0
y = 0
dx = 0
dy = 1

# for part 2
seen = {}

for i in input:
	if i[0] == 'R':
		t = dx
		dx = dy
		dy = -t
	else:
		t = dx
		dx = -dy
		dy = t

	delta = int(i[1:])
	for d in range(1, delta + 1):
		x += dx
		y += dy
		k = str(x) + ',' + str(y)
		if k in seen:
			print('S', x, y, abs(x) + abs(y))
			exit(0)
		seen[k] = True

print('E', abs(x)+abs(y))
