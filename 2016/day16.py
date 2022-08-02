import numpy

a = numpy.array((1, 0, 0, 0, 0))
s = 20

a = numpy.array((1,0,1,1,1,0,1,1,1,1,1,0,0,1,1,1,1))
s = 272
s = 35651584

z = numpy.zeros(1, dtype=numpy.int)
print('Part 1')
while a.size < s:
    b = numpy.flip(a)
    b = numpy.where(b == 0, 1, 0)
    a = numpy.concatenate((a, z, b))
a = a[:s]

print('Part 2')
checksum = a.tolist()

while len(checksum) % 2 == 0:
    c2 = checksum
    checksum = []

    for i in range(0, len(c2), 2):
        if c2[i] == c2[i+1]:
            checksum.append(1)
        else:
            checksum.append(0)

print(''.join(str(c) for c in checksum))
