import numpy as np

cups = np.arange(1, 1000001, 1, int)
cups[0:9] = [3,8,9,1,2,5,4,6,7]
#cups = np.array([3,8,9,1,2,5,4,6,7])
#cups = np.array([8,5,3,1,9,2,6,4,7])
current = 0
destination = 0

def getDesination(currentVal):
	v = curremtVal - 1
	while v > 0:
		dests = np.where(cups == v)[0]
		if len(dests) == 1:
			return dests[0]
		v -= 1
	return np.argmax(cups)

for i in range(10000000):
	# print()
	print('move',i+1)
	# print(cups)
	# remove cups
	removed = cups[current+1:current+4]
	cups = np.append(cups[:current+1], cups[current+4:])
	curremtVal = cups[current]

	if len(removed) == 2:
		removed = np.append(removed, cups[0])
		cups = cups[1:]
	elif len(removed) == 1:
		removed = np.append(removed, cups[0])
		removed = np.append(removed, cups[1])
		cups = cups[2:]
	elif len(removed) == 0:
		removed = cups[0:3]
		cups = cups[3:]

	# print('Curr', current, curremtVal)
	# print('Rem', removed)
	# print('Cups', cups)

	# get destination
	destination = getDesination(curremtVal)
	# print('Dest',destination, cups[destination])

	# add removed back in
	cups= np.insert(cups, destination+1, removed)

	# Shift to keep current cup in original position
	if curremtVal != cups[current]:
		# print('ROLL', curremtVal, cups[current], current, np.where(cups == curremtVal)[0][0])
		roll = current - np.where(cups == curremtVal)[0][0]
		cups = np.roll(cups, roll)

	# get next current
	current = (current + 1) % len(cups)

print()
#print(cups)


idx = np.where(cups == 1)[0][0]
print(cups[idx], cups[idx + 1], cups[idx + 2])
#cups = np.roll(cups, -start)[:-1]
#print(''.join([str(x) for x in cups]))
