letters = []
for i in range(8):
	letters.append({})

for line in open('input.txt'):
	lst = list(line.strip())

	for i in range(len(lst)):
		letters[i][lst[i]] = letters[i].get(lst[i], 0) + 1

for group in letters:
	print(sorted(group.items(), key=lambda item: item[1], reverse=False)[0][0], end='')

print()
