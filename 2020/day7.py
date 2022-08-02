m = {}

f = open('input.txt', 'r')

line = f.readline()
while line:
	line = line.strip()

	if line.endswith('no other bags.'):
		line = f.readline()
		continue

	parts = line.split('contain')
	kparts = parts[0].strip().split(' ')
	key = kparts[0] + ' ' + kparts[1]

	vals = parts[1].split(',')
	vmap = {}
	for v in vals:
		v = v.strip()
		valparts = v.split(' ')
		bagname = valparts[1] + ' ' + valparts[2]
		vmap[bagname] = int(valparts[0])

	m[key] = vmap
	line = f.readline()

f.close()

def getCount(bag):
	count = 0
	if bag not in m:
		return count

	subbags = m[bag]

	for subbag in subbags:
		count = count + subbags[subbag] + (subbags[subbag] * getCount(subbag))

	return count

count = getCount('shiny gold')
print(count)
