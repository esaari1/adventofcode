f = open('input.txt', 'r')
lines = f.readlines()
f.close()

ints = list(map(int, lines))

for idx in range(len(ints) - 2):
	for idx2 in range(idx+1, len(ints) - 1):
		for idx3 in range(idx2+1, len(ints)):
			if ints[idx] + ints[idx2] + ints[idx3] == 2020:
				print(ints[idx], ints[idx2], ints[idx3], ints[idx] * ints[idx2] * ints[idx3])
				exit(0)
