sdeck1 = [
39,
15,
13,
23,
12,
49,
36,
44,
8,
21,
28,
37,
40,
42,
6,
47,
2,
38,
18,
31,
20,
10,
16,
43,
5
]

sdeck2 = [
29,
26,
19,
35,
34,
4,
41,
11,
3,
50,
33,
22,
48,
7,
17,
32,
27,
45,
46,
9,
25,
30,
1,
24,
14
]


sdeck1a = [
9,
2,
6,
3,
1
]

sdeck2a = [
5,
8,
4,
7,
10
]

def getResult(deck):
	r = 0
	for i in range(len(deck)):
		r = r + deck[i] * (len(deck) - i)
	print(r)

def part1():
	global deck1, deck2

	while len(deck1) > 0 and len(deck2) > 0:
		d1 = deck1[0]
		d2 = deck2[0]
		deck1 = deck1[1:]
		deck2 = deck2[1:]

		if d1 > d2:
			deck1.append(d1)
			deck1.append(d2)
		else:
			deck2.append(d2)
			deck2.append(d1)

def part2(deck1, deck2, game):
	past = {}

	while len(deck1) > 0 and len(deck2) > 0:
		state = ','.join(str(x) for x in deck1) + ':' + ','.join(str(x) for x in deck2)
		if state in past:
			return deck1, deck2, 0
		past[state] = True

		d1 = deck1[0]
		d2 = deck2[0]
		deck1 = deck1[1:]
		deck2 = deck2[1:]

		if d1 <= len(deck1) and d2 <= len(deck2):
			w1, w2, winner = part2(deck1[:d1], deck2[:d2], game + 1)
			if winner == 0:
				deck1.append(d1)
				deck1.append(d2)
			else:
				deck2.append(d2)
				deck2.append(d1)
		else:
			if d1 > d2:
				deck1.append(d1)
				deck1.append(d2)
			else:
				deck2.append(d2)
				deck2.append(d1)

	w = 0
	if len(deck2) > 0:
		w = 1
	return deck1, deck2, w

#part1()
deck1, deck2, w = part2(sdeck1, sdeck2, 1)
if len(deck1) > 0:
	getResult(deck1)
else:
	getResult(deck2)
