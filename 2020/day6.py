f = open('input.txt', 'r')

line = f.readline()
group = set('abcdefghijklmnopqrstuvwxyz')
count = 0

while line:
	line = line.strip()

	if len(line) == 0:
		count += len(group)
		group = set('abcdefghijklmnopqrstuvwxyz')
	else:
		#group = group + line
		group = group.intersection(set(line))

	line = f.readline()

f.close()
count += len(group)
print(count)
