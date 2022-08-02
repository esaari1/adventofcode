i = 20151125
r = 1
c = 1

while True:
#for x in range(2):
	r = c + 1
	c = 1
	while r > 0:
		i = (i * 252533) % 33554393
		if r == 2947 and c == 3029:
			print(i)
			exit(0)

		r -= 1
		if r > 0:
			c += 1
