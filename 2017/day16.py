f = open('input.txt')
input = f.readline().strip().split(',')
f.close()

#input = ['s1', 'x3/4', 'pe/b']

s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
t = ''
x = 0

while True:
    for i in input:
        if i[0] == 's':
            amount = int(i[1:])
            s = s[-amount:] + s[:-amount]

        elif i[0] == 'x':
            (a, b) = (int(x) for x in i[1:].split('/'))
            t = s[a]
            s[a] = s[b]
            s[b] = t

        elif i[0] == 'p':
            (a, b) = i[1:].split('/')
            a = s.index(a)
            b = s.index(b)
            t = s[a]
            s[a] = s[b]
            s[b] = t

    t =''.join(s)
    if t == 'abcdefghijklmnop':
        break
    x += 1

n = 1000000000 % (x + 1)

for i in range(n):
    for i in input:
        if i[0] == 's':
            amount = int(i[1:])
            s = s[-amount:] + s[:-amount]

        elif i[0] == 'x':
            (a, b) = (int(x) for x in i[1:].split('/'))
            t = s[a]
            s[a] = s[b]
            s[b] = t

        elif i[0] == 'p':
            (a, b) = i[1:].split('/')
            a = s.index(a)
            b = s.index(b)
            t = s[a]
            s[a] = s[b]
            s[b] = t

t =''.join(s)
print(t)
