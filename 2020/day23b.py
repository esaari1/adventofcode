class Cup:
	def __init__(self, id):
		self.id = id
		self.next = None

input = [3,8,9,1,2,5,4,6,7]
input = [8,5,3,1,9,2,6,4,7]
for i in range(10,1000001):
	input.append(i)

cups = {}
for i in input:
	cup = Cup(i)
	cups[i] = cup

# link cups
for i in range(len(input) - 1):
	cups[input[i]].next = cups[input[i + 1]]
cups[input[-1]].next = cups[input[0]]

currCup = cups[input[0]]
i = 0

while i < 10000000:
	i += 1
	#print('move',i+1)
	removed = [currCup.next.id, currCup.next.next.id, currCup.next.next.next.id]
	currCup.next = currCup.next.next.next.next

	dest = currCup.id - 1

	if dest == 0:
		dest = 1000000
	while dest in removed:
		dest -= 1
		if dest == 0:
			dest = 1000000

	destCup = cups[dest]
	cups[removed[2]].next = destCup.next
	destCup.next = cups[removed[0]]
	currCup = currCup.next

c = cups[1]
print(c.next.id, c.next.next.id)
print(c.next.id * c.next.next.id)
# result = ''
# c = cups[1].next
# while c.id != 1:
# 	result += str(c.id)
# 	c = c.next
# print(result)