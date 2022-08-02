f = open('day2.txt', 'r')

total = 0
line = f.readline()

while line:
	line = line.strip()

	sides = line.split('x')
	sides = map(int, sides)
	sides.sort()

	a = sides[0] + sides[0] + sides[1] + sides[1] + (sides[0] * sides[1] * sides[2])
	total += a

	line = f.readline()

f.close()
print total