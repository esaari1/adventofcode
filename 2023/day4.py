import math

part1 = 0
wins = []

with open('input.txt') as f:
    for l in f:
        l = l.split(': ')[1].split(' | ')
        s1 = set(int(x.strip()) for x in l[0].split(' ') if len(x) > 0)
        s2 = set(int(x.strip()) for x in l[1].split(' ') if len(x) > 0)
        n = len(s1.intersection(s2))
        wins.append(n)

        if n > 0:
            part1 += math.pow(2, n-1)

print(part1)

counts = [1] * len(wins)

for idx in range(len(wins)):
    for x in range(idx + 1, idx + 1 + wins[idx]):
        counts[x] += counts[idx]

print(sum(counts))