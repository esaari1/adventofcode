import regex as re

m = {}
e = {}

def expand(key):
	vals = m[key]
	result = []

	for v in vals:
		r1 = []
		parts = v.split(' ')
		for p in parts:
			if p[0] == '"':
				return [p[1]]
			if not p in e:
				e[p] = expand(p)
			if len(r1) == 0:
				r1 = e[p]
			else:
				if key == '0' or key == '11':
					return [r1, e[p]]
				r2 = []
				for r in r1:
					for q in e[p]:
						r2.append(r + q)
				r1 = r2

		result.extend(r1)

	return result

def expand2(key):
	parts = m[key].strip().split(' ')
	print(key, parts)
	if parts[0] == '"a"' or parts[0] == '"b"':
		return parts[0][1]
	pattern = '('

	for p in parts:
		if p == '|':
			pattern += '|'
		else:
			pattern += expand2(p)
	pattern += ')'
	return pattern

f = open('input.txt', 'r')

line = f.readline()

while line:
	line = line.strip()
	p = line.split(':')
	key = p[0]
	m[key] = p[1]
	line = f.readline()

m['8']  = "42 | 42 42 | 42 42 42 | 42 42 42 42 | 42 42 42 42 42 | 42 42 42 42 42 42"
m['11'] = "42 31 | 42 42 31 31 | 42 42 42 31 31 31 | 42 42 42 42 31 31 31 31 | 42 42 42 42 42 31 31 31 31 31 | 42 42 42 42 42 42 31 31 31 31 31 31"

f.close()
pattern = expand2('0')

#pattern = '^' + pattern + '$'

prog = re.compile(pattern)

count = 0
f = open('input2.txt', 'r')
line = f.readline()
while line:
	line = line.strip()

	m = prog.fullmatch(line)
	if m is not None:
		count += 1

	line = f.readline()

f.close()
print(count)
