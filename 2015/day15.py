data = [
	[-1, -2, 6, 3, 8],
	[2, 3, -2, -1, 3]
]

data2 = [
	[4, -2, 0, 0, 5],
	[0, 5, -1, 0, 8],
	[-1, 0, 5, 0, 6],
	[0, 0, -2, 2, 1]
]


final = 0

def real():
	global final
	for i in range(101):
		for j in range(101 - i):
			for k in range(101 - i - j):
				m = 100 - i - j - k

				x = 4
				calories = (data2[0][x] * i) + (data2[1][x] * j) + (data2[2][x] * k) + (data2[3][x] * m)
				if calories == 500:
					a = 1
					for x in range(4):
						b = (data2[0][x] * i) + (data2[1][x] * j) + (data2[2][x] * k) + (data2[3][x] * m)
						b = max(b, 0)
						a *= b
					if a > final:
						final = a

def test():
	global final
	for i in range(101):
		j = 100 - i

		calories = (data[0][4] * i) + (data[1][4] * j)

		if calories == 500:
			a = 1
			for x in range(4):
				b = (data[0][x] * i) + (data[1][x] * j)
				b = max(b, 0)
				a *= b
			if a > final:
				final = a

#test()
real()
print(final)
