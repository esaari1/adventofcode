import numpy as np

m = {}

class Entry:
	def __init__(self, arg1 = '', arg2 = '', op = '', value = np.nan):
		self.arg1 = arg1
		self.arg2 = arg2
		self.op = op
		self.value = value


def isInt(s):
	try:
		int(s)
		return True
	except ValueError:
		return False

def getValue(key):
	if isInt(key):
		# number
		return np.uint16(key)

	if not key in m:
		print('Bad key: ', key)
		exit(1)

	entry = m[key]
	if not np.isnan(entry.value):
		return entry.value

	value = np.uint16(0)
	op = entry.op

	if op == '': # direct assignment
		value = np.uint16(getValue(entry.arg1))

	elif op == 'NOT':
		value = ~np.uint16(getValue(entry.arg1))

	elif op == 'LSHIFT':
		value = np.uint16(getValue(entry.arg1)) << np.uint16(getValue(entry.arg2))

	elif op == 'RSHIFT':
		value = np.uint16(getValue(entry.arg1)) >> np.uint16(getValue(entry.arg2))

	elif op == 'AND':
		value = np.uint16(getValue(entry.arg1)) & np.uint16(getValue(entry.arg2))

	elif op == 'OR':
		value = np.uint16(getValue(entry.arg1)) | np.uint16(getValue(entry.arg2))

	m[key].value = value
	return value


#m['x'] = Entry(value = 123)
#x = np.uint16(123)
#print(x, x << 2, ~x)
#print(m['x'].value)

f = open('input.txt', 'r')

line = f.readline()

while line:
	line = line.strip()

	parts = line.split(' ')
	if len(parts) == 3:
		# direct assignment
		if isInt(parts[0]):
			m[parts[2]] = Entry(value = np.uint16(parts[0]))
		else:
			m[parts[2]] = Entry(arg1 = parts[0])

	elif len(parts) == 4:
		# not
		m[parts[3]] = Entry(arg1 = parts[1], op = 'NOT')

	elif len(parts) == 5:
		# two argument operators
		m[parts[4]] = Entry(arg1 = parts[0], arg2 = parts[2], op = parts[1])

	else:
		print(line)
		exit(1)

	line = f.readline()

f.close()

# part b
m['b'] = Entry(value = np.uint16(16076))

print(getValue('a'))
