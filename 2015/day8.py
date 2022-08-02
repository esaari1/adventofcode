f = open('input.txt', 'r')

def getLength(s):
	s2 = s[1:len(s) - 1]

	count = 0
	idx = 0
	while idx < len(s2):
		if s2[idx] == "\\":
			idx += 1
			if s2[idx] == "\\" or s2[idx] == "\"":
				idx += 1
			elif s2[idx] == "x":
				idx += 3
		else:
			idx += 1

		count += 1

	return len(s) - count


def getLengthB(s):
	idx = 0

	# start
	s2 = "\"\\\""

	subs = s[1:len(s) - 1]
	idx = 0
	while idx < len(subs):
		if subs[idx] == "\\":
			s2 += "\\\\"
		elif subs[idx] == "\"":
			s2 += "\\\""
		else:
			s2 += subs[idx]
		idx += 1

	# end
	s2 += "\\\"\""
	return len(s2) - len(s)

total = 0
line = f.readline()
while line:
	line = line.strip()
	total += getLengthB(line)
	line = f.readline()

f.close()
print(total)
