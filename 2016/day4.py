from collections import Counter

def translate(name, roomID):
	roomID = roomID % 26

	newName = ''
	for c in name:
		if c == '-':
			newName += ' '
		else:
			o = ord(c) + roomID
			if o > ordZ:
				o -= ordDelta
			newName += chr(o)
	return newName


result = 0
ordZ = ord('z')
ordDelta = ordZ - ord('a') + 1

for line in open('input.txt'):
	room, checksum = line.strip()[:-1].split('[')
	name, roomID = room[:room.rindex('-')], int(room[room.rindex('-')+1:])
	c = Counter(name)
	del c['-']

	elems = c.most_common()
	elems.sort(key=lambda x: x[0])
	elems.sort(key=lambda x: x[1], reverse=True)

	tst = ''
	for x in elems[:5]:
		tst += x[0]

	if tst == checksum:
		result += roomID

		newName = translate(name, roomID)
		#print(newName, roomID)
		if newName.startswith('north'):
			print(newName, roomID)

print(result)
