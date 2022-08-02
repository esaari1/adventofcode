def checkLine1(line):
	inBracket = False
	hasAbba = False
	for idx in range(len(line) - 3):
		if line[idx] == '[':
			inBracket = True
		elif line[idx] == ']':
			inBracket = False
		else:
			s = line[idx:idx+4]
			if s[0] == s[3] and s[1] == s[2] and s[0] != s[1]:
				if inBracket:
					return 0
				else:
					hasAbba = True
	if hasAbba:
		return 1
	return 0

def checkLine2(line):
	aba = []
	bab = []
	inBracket = False

	for idx in range(len(line) - 2):
		if line[idx] == '[':
			inBracket = True
		elif line[idx] == ']':
			inBracket = False
		else:
			s = line[idx:idx+3]
			if s[0] == s[2]:
				if inBracket:
					bab.append(s)
				else:
					aba.append(s)
	for a in aba:
		for b in bab:
			if a[0] == b[1] and a[1] == b[0]:
				return 1
	return 0

result = 0
for line in open('input.txt'):
	line = line.strip()
	result += checkLine2(line)
print(result)
