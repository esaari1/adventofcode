def balance(node):
    total = weights[node]
    cweights = []
    for child in children[node]:
        cweight = balance(child)
        total += cweight
        cweights.append(cweight)

    if all(x == cweights[0] for x in cweights):
        pass
    else:
        print(node, cweights)
        for child in children[node]:
            print(child, totals[child], weights[child])
        exit(0)

    totals[node] = total
    return total

f = open('input.txt')

programs = {}
children = {}
children['root'] = []

weights = {}
totals = {}

weights['root'] = 0

line = f.readline()

while line:
    line = line.strip()
    parts = line.split('->')

    subparts = parts[0].split(' ')
    program = subparts[0].strip()
    weight = int(subparts[1].strip()[1:-1])
    weights[program] = weight

    if program not in children:
        children[program] = []

    if program not in programs:
        programs[program] = True
        children['root'].append(program)

    if len(parts) > 1:
        subs = parts[1].split(',')

        for sub in subs:
            s = sub.strip()
            programs[s] = True

            children[program].append(s)
            if s in children['root']:
                children['root'].remove(s)

    line = f.readline()

f.close()
print(children['root'])
balance('root')
