f = open('input.txt', 'r')

line = f.readline()
count = 0


while line:
	p = ''
	m = {}

	cond1 = False
	cond2 = False
	line.strip()

	for i in range(len(line)):
		if i > 1:
			if line[i] == line[i-2]:
				cond2 = True

		if p != '':
			pc = p + line[i]
			if pc not in m:
				m[pc] = i
			else:
				if i > m[pc] + 1:
					cond1 = True

		p = line[i]

	if cond1 and cond2:
		count += 1

	line = f.readline()

f.close()
print count
