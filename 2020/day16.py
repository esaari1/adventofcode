f = open('input.txt', 'r')

isrule = True
isticket = False
l = f.readline()
rulemap = {}
result = 0

def validVal(val, rulemap):
	for rules in rulemap:
		for r in rulemap[rules]:
			if val in range(r[0], r[1]):
				return True
	return False

def interset(l1, l2):
	r = []
	for i in l1:
		if i in l2:
			r.append(i)
		else:
			r.append('')
	return r

valids = []
while l:
	l = l.strip()
	if len(l) == 0:
		isrule = False

	if isrule:
		p = l.split(':')
		rname = p[0]
		p2 = p[1].strip().split(' ')
		rulemap[rname] = [
			[int(x) for x in p2[0].split('-')],
			[int(x) for x in p2[2].split('-')]
		]
		rulemap[rname][0][1] += 1
		rulemap[rname][1][1] += 1

	if l == 'nearby tickets:':
		isticket = True
	elif isticket:
		validTicket = True
		vals = [int(x) for x in l.split(',')]
		for val in vals:
			if not validVal(val, rulemap):
				validTicket = False
				break

		if validTicket:
			valids.append(vals)

	l = f.readline()

f.close()

results = [None] * 20



for v in valids:
	for idx in range(20):
		match = set([])
		for name, r in rulemap.items():
			if v[idx] in range(r[0][0], r[0][1]) or v[idx] in range(r[1][0], r[1][1]):
				match.add(name)
		if results[idx] is None:
			results[idx] = match
		else:
			results[idx] = interset(results[idx], match)

for r in results:
	print(r)
