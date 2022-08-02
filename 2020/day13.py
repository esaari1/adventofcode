from math import ceil

depart = 1000391
buses = [19,37,383,23,13,29,457,41,17]

#depart = 939
input = '7,13,x,x,59,x,31,19'

def part1():
	delta = None
	mbus = 0

	for bus in buses:
		t = int(ceil(depart / float(bus)) * bus)
		td =  t - depart
		if delta is None or delta > td:
			delta = td
			mbus = bus
	print(mbus * delta)

i = 100000000000000 / 457

while True:
	i += 1
	t = 457 * i

	if (t - 31) % 383 != 0:
		continue

	if (t + 10) % 41 != 0:
		continue

	if (t - 37) % 37 != 0:
		continue

	if (t - 2) % 29 != 0:
		continue
	print(2)
	if (t - 23) % 23 != 0:
		continue
	print(3)
	if (t - 50) % 19 != 0:
		continue

	if (t + 17) % 17 != 0:
		continue

	if (t - 18) % 13 == 0:
		print(t - 50)
		exit(0)
