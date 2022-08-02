f = open('input.txt', 'r')

line = f.readline()

valid = 0
while line:
	parts = line.split(' ')
	l = list(parts[2])
	c = parts[1][:-1]
	r = parts[0].split('-')
	count = l.count(c)

#	if count >= int(r[0]) and count <= int(r[1]):
#		valid += 1

	idx1 = int(r[0]) - 1
	idx2 = int(r[1]) - 1

	if l[idx1] == c and l[idx2] != c:
		valid += 1
	elif l[idx2] == c and l[idx1] != c:
		valid += 1

	line = f.readline()

f.close()
print(valid)
