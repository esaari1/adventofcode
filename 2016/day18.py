import numpy

input = '.^^.^.^^^^'
rows = 10

input = '.^..^....^....^^.^^.^.^^.^.....^.^..^...^^^^^^.^^^^.^.^^^^^^^.^^^^^..^.^^^.^^..^.^^.^....^.^...^^.^.'
rows = 40
rows = 400000

a = numpy.zeros(len(input) + 2, dtype=int)
b = numpy.zeros(len(input) + 2, dtype=int)

for idx, i in enumerate(input):
    if i == '^':
        a[idx+1] = 1

count = (a.size - 2 - numpy.count_nonzero(a))
for r in range(1, rows):
    for c in range(1, len(input) + 1):
        if a[c-1] != a[c+1]:
            b[c] = 1
    count = count + (b.size - 2 - numpy.count_nonzero(b))
    a = b
    b = numpy.zeros(len(input) + 2, dtype=int)

print(count)