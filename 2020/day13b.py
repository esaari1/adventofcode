def reverseMod(val, m):
	v = val
	val = val % m
	print('E0', v, val, m)
	i = 1
	v = 0

	while True:
		v += val
		#print ('E1', v, i, m, v % m)
		if v % m == 1:
			return i
		i += 1

	return i

input = '7,13,x,x,59,x,31,19'
#input = '3,4,5,7'
input = '19,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,383,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29,x,457,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,17'

input = input.replace('x', '1')
vals = [int(x) for x in input.split(',')]
prod = 1

for v in vals:
	prod *= v

print(prod)

x = 0

for i in range(0, len(vals)):
	if vals[i] == 1:
		continue
	print(i, vals[i])

	m = prod / vals[i]
	y = reverseMod(m, vals[i])

	print('E2', i, vals[i], m, y)

	a = 1
	if i == 3:
		a = 0
	a = (vals[i] - i)
	x = x + (a * m * y)

print(x, prod, x % prod)

