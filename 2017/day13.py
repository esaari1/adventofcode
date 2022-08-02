import copy

def attempt():
    packet = 0
    while packet <= maxPacket:
        if packet in layers and layers[packet].pos == 0:
            return False

        for k in layers:
            layers[k].move()

        packet += 1

    return True

def advance(delay):
    for i in range(delay):
        for k in layers:
            layers[k].move()


class Layer:
    def __init__(self, range):
        self.range = range
        self.pos = 0
        self.dir = 1

    def move(self):
        if self.dir == 1:
            if self.pos == self.range - 1:
                self.pos -= 1
                self.dir = 0
            else:
                self.pos += 1
        else:
            if self.pos == 0:
                self.pos += 1
                self.dir = 1
            else:
                self.pos -= 1

    def __str__(self):
        return f'{self.pos}'


f = open('input.txt')

master = {}

maxPacket = 0

line = f.readline()
while line:
    (depth, r) = line.strip().split(': ')
    # master[int(depth)] = Layer(int(r))
    master[int(depth)] = int(r)
    maxPacket = int(depth)
    line = f.readline()

f.close()

size = 5000000
s = set(range(size))

for d in master:
    r = master[d]
    step = (r - 1) * 2
    start = step - d

    s2 = set(range(start, size, step))
    s.difference_update(s2)

print(min(s))
# delay = 1

# while True:
#     print('delay = ', delay)
#     layers = copy.deepcopy(master)
#     advance(delay)
#     if attempt():
#         print(delay)
#         exit(0)

#     delay += 1
