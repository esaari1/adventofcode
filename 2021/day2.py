f = open('input.txt')

line = f.readline()

pos = 0
depth = 0
aim = 0

while line:
    (dir, distance) = line.strip().split(' ')
    distance = int(distance)

    if dir == 'forward':
        pos += distance
        depth += (aim * distance)
    elif dir == 'down':
        aim += distance
    else:
        aim -= distance
    line = f.readline()

f.close()

print(pos * depth)
