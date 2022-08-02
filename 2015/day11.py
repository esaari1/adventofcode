import re

def isClean(s):
	if 'i' in s or 'o' in s or 'l' in s:
		return False
	return True

def addOne(c, t = True):
	c = chr(ord(c) + 1)
	if t and (c == 'i' or c == 'o' or c == 'l'):
		c = chr(ord(c) + 1)
	return c

def increment(s):
	l = list(s)
	idx = len(l) - 1
	while l[idx] == 'z':
		l[idx] = 'a'
		idx -= 1
	l[idx] = addOne(l[idx])
	return "".join(l)

def isValid(s):
	if not isClean(s):
		return False

	# find pairs
	m = re.findall(r'((\w)\2{1,})', s)
	if len(m) == 0:
		return False
	if len(m) == 1:
		if len(m[0][0]) < 4:
			return False

	# check for character run
	idx = 2
	l = list(s)
	while idx < len(l):
		p1 = addOne(l[idx - 1], False)
		if p1 == l[idx]:
			p2 = addOne(l[idx - 2], False)
			if p2 == l[idx - 1]:
				return True

		idx += 1

	return False

s = 'cqjxxyzz'
v = False
while not v:
	s = increment(s)
	v = isValid(s)
print(s)
