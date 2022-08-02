keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def validYear(v, minVal, maxVal):
	if len(v) != 4:
		return False
	try:
		i = int(v)
		if (i >= minVal) and (i <= maxVal):
			return True
	except Exception:
		return False
	return False

def validHeight(v):
	if v.endswith('cm'):
		try:
			i = int(v[:-2])
			return i >= 150 and i <= 193
		except:
			return False
	elif v.endswith('in'):
		try:
			i = int(v[:-2])
			return i >= 59 and i <= 76
		except:
			return False

	return False

def isValid(k, v):
	if k == 'byr':
		return validYear(v, 1920, 2002)

	elif k == 'iyr':
		return validYear(v, 2010, 2020)

	elif k == 'eyr':
		return validYear(v, 2020, 2030)

	elif k == 'hgt':
		return validHeight(v)

	elif k == 'hcl':
		if v.startswith('#'):
			try:
				i = int(v[1:], 16)
				return True
			except:
				return False

	elif k == 'ecl':
		return v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

	elif k == 'pid':
		if len(v) == 9:
			try:
				i = int(v)
				return True
			except:
				return False

	return False

def check(m):
	for k in keys:
		if k not in m:
			return 0

		if not isValid(k, m[k]):
			return 0

	return 1

f = open('input.txt', 'r')

m = {}
count = 0
line = f.readline()
while line:
	line = line.strip()
	if len(line) == 0:
		count += check(m)
		m = {}
	else:
		parts = line.split()
		for p in parts:
			[k,v] = p.split(':')
			m[k] = v
	line = f.readline()

count += check(m)

f.close()
print(count)
