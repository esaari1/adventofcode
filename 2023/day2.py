import math

maxs = {
    'red': 12,
    'green': 13,
    'blue': 14
}

part1 = 0
part2 = 0

with open('input.txt') as f:
    for line in f:
        id, turns = line.strip().split(':')
        id = int(id[5:])
        mins = {}
        valid = True

        for turn in turns.split('; '):
            for cube in turn.split(', '):
                count = int(cube.strip().split(' ')[0])
                color = cube.strip().split(' ')[1]
                if count > maxs[color]:
                    valid = False
                mins[color] = max(mins.get(color, 0), count)

        if valid:
            part1 += id
        part2 += math.prod(list(mins.values()))

print(part1)
print(part2)