def isTriangle(lst):
	s = sum(lst)
	if all(s - x > x for x in lst):
		return 1
	return 0

def part1():
	result = 0
	for line in open('input.txt'):
		lst = [int(x.strip()) for x in line.split(' ') if x != '']
		result += isTriangle(lst)

	print(result)

def part2():
	result = 0
	l1 = []
	l2 = []
	l3 = []
	for line in open('input.txt'):
		lst = [int(x.strip()) for x in line.split(' ') if x != '']
		l1.append(lst[0])
		l2.append(lst[1])
		l3.append(lst[2])

		if len(l1) == 3:
			result += isTriangle(l1)
			result += isTriangle(l2)
			result += isTriangle(l3)
			l1 = []
			l2 = []
			l3 = []

	print(result)

part1()
part2()
