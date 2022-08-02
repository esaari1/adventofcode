input = {
	"children": 3,
	'cats': 7,
	'samoyeds': 2,
	'pomeranians': 3,
	'akitas': 0,
	'vizslas': 0,
	'goldfish': 5,
	'trees': 3,
	'cars': 2,
	'perfumes': 1
}

def isMatch(line):
	parts = line.split(' ')
	idx = 2
	while idx < len(parts):
		key = parts[idx][:-1]
		idx += 1
		value = int(parts[idx][:-1])
		idx += 1

		if key == 'cats' or key == 'trees':
			if input[key] >= value:
				return False
		elif key == 'pomeranians' or key == 'goldfish':
			if input[key] <= value:
				return False
		else:
			if input[key] != value:
				return False

	print(parts[1])

f = open('input.txt', 'r')

line = f.readline()

while line:
	isMatch(line)
	line = f.readline()

f.close()
