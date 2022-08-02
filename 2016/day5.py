from hashlib import md5

a = 'abc'
a = 'abbhdwsy'
i = 0
pw = ['-'] * 8
found = 0

print(pw)

while found < 8:
	s = a + str(i)
	hash = md5(s.encode()).hexdigest()
	if hash.startswith('00000'):
		pos = hash[5]
		if pos in ['0','1','2','3','4','5','6','7']:
			if pw[int(pos)] == '-':
				pw[int(pos)] = hash[6]
				print(pw)
				found += 1
	i += 1

print(''.join(pw))
