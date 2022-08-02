yourtix  = list(map(int,open(day_16_path3).read().split(',')))
tickets  = [ list(map(int,line.split(','))) for line in open(day_16_path2).readlines() ]
rules    = re.findall('(.+): (.+)-(.+) or (.+)-(.+)\n', open(day_16_path1).read())
rules    = { name:[range(int(a),int(b)+1), range(int(c),int(d)+1)] for name,a,b,c,d in rules}
valid    = [ t for t in tickets if all( any(n in rule[0] or n in rule[1] for rule in rules.values()) for n in t) ]
possible = { name: { j for j in range(20) if all((v[j] in rule[0] or v[j] in rule[1]) for v in valid) } for name,rule in rules.items() }

result,used = [],set()
for p in sorted(possible, key=lambda l: len(possible[l])):
    if p.startswith('departure'): result.append((possible[p]-used).pop())
    used.update(possible[p])
print(prod([ yourtix[x] for x in result ]))