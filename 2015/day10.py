import itertools

def expand(x):
	s = ''
	for k, g in itertools.groupby(x):
		s += str(len(list(g))) + str(k)
	return s


i = "1113222113"
c = 1

for idx in range(50):
	c += 1
	i = expand(i)

print(len(i))