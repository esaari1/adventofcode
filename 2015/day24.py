import itertools

def getMatch(vals, third):
	match = []
	minLength = None

	for i in range(1, len(vals) + 1):
		sets = itertools.combinations(vals, i)
		for set in sets:
			s = sum(set)
			if s == third:
				if minLength is None or minLength == len(set):
					match.append(set)
					minLength = len(set)
				else:
					return match

def qe(set):
	qe = 1
	for s in set:
		qe *= s
	return qe

f = open('input.txt', 'r')

l = f.readline()
s = 0
vals = []
while l:
	i = int(l)
	s += i
	vals.append(i)
	l = f.readline()

third = s / 4
match = getMatch(vals, third)

minQE = None
for m in match:
	q = qe(m)
	if minQE is None or minQE > q:
		minQE = q
print(minQE)
