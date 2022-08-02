# too low 753115, 1178174
m = {}
l = []

for line in open('input.txt'):
    parts = line.strip().split('-')
    m[int(parts[0])] = int(parts[1])
    l.append(int(parts[0]))

l.sort()

i = 1

while l[i] < (m[l[i - 1]] + 2) and  l[i - 1] < (m[l[i]] + 2):
    #print(l[i - 1], m[l[i - 1]], l[i], m[l[i]])
    i += 1

#print(l[i - 1], m[l[i - 1]], l[i], m[l[i]])

# part 1
if l[i] < (m[l[i - 1]] + 2):
    print(m[l[i]] + 1)
else:
    print(m[l[i-1]] + 1)

low = l[0]
high = m[l[0]]
i = 1
count = 0

while i < len(l):
    if (high + 1) < l[i]:
        count += l[i] - high - 1
        low = l[i]

    if m[l[i]] > high:
        high = m[l[i]]
    i += 1

print(count)
