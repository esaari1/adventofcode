import numpy as np

a = np.zeros((6, 50), dtype=int)

for row in a:
	print(str(row).replace('\n', '').replace(' ', '').replace('0', '.').replace('1', '#'))
print()

for line in open('input.txt'):
	parts = line.strip().split(' ')
	if parts[0] == 'rect':
		cols, rows = parts[1].split('x')
		a[0:int(rows),0:int(cols)] = 1
	else:
		amount = int(parts[-1])
		idx = int(parts[2].split('=')[1])
		if parts[1] == 'column':
			a[:,idx] = np.roll(a[:,idx], amount)
		else:
			a[idx] = np.roll(a[idx], amount)

	for row in a:
		print(str(row).replace('\n', '').replace(' ', '').replace('0', '.').replace('1', '#'))
	print()

print(np.count_nonzero(a))
