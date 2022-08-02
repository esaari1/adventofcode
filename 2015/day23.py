instr = [
	'jio a, +18',
	'inc a',
	'tpl a',
	'inc a',
	'tpl a',
	'tpl a',
	'tpl a',
	'inc a',
	'tpl a',
	'inc a',
	'tpl a',
	'inc a',
	'inc a',
	'tpl a',
	'tpl a',
	'tpl a',
	'inc a',
	'jmp +22',
	'tpl a',
	'inc a',
	'tpl a',
	'inc a',
	'inc a',
	'tpl a',
	'inc a',
	'tpl a',
	'inc a',
	'inc a',
	'tpl a',
	'tpl a',
	'inc a',
	'inc a',
	'tpl a',
	'inc a',
	'inc a',
	'tpl a',
	'inc a',
	'inc a',
	'tpl a',
	'jio a, +8',
	'inc b',
	'jie a, +4',
	'tpl a',
	'inc a',
	'jmp +2',
	'hlf a',
	'jmp -7'
]

a = 1
b = 0
i = 0

while True:
	if i < 0 or i >= len(instr):
		print(b)
		exit(0)

	p = instr[i].split(' ')
	if p[0] == 'hlf':
		if p[1] == 'a':
			a = a / 2
		else:
			b = b / 2
		i += 1
	elif p[0] == 'tpl':
		if p[1] == 'a':
			a = a * 3
		else:
			b = b * 3
		i += 1
	elif p[0] == 'inc':
		if p[1] == 'a':
			a = a + 1
		else:
			b = b + 1
		i += 1
	elif p[0] == 'jmp':
		i = i + int(p[1])
	elif p[0] == 'jie':
		if p[1] == 'a,':
			if a % 2 == 0:
				i = i + int(p[2])
			else:
				i += 1
		else:
			if b % 2 == 0:
				i = i + int(p[2])
			else:
				i += 1
	elif p[0] == 'jio':
		if p[1] == 'a,':
			if a == 1:
				i = i + int(p[2])
			else:
				i += 1
		else:
			if b == 1:
				i = i + int(p[2])
			else:
				i += 1
	else:
		print('bad')
		exit(0)
