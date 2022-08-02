card = 5764801
door = 17807724

card = 10441485
door = 1004920

print('CARD')
i = 1
cardIdx = 0
while i != card:
	cardIdx += 1
	i = i * 7 % 20201227

print('DOOR')
i = 1
doorIdx = 0
while i != door:
	doorIdx += 1
	i = i * 7 % 20201227

print(cardIdx, doorIdx)

i = 1
for x in range(cardIdx):
	i = i * door % 20201227

print(i)
