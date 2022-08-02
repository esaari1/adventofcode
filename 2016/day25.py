import math

count = 10

def run(a):
    cnt = 0
    expect = 0
    d = a
    c = 4
    b = 643

    s = ''

    d = d + (b * c)

    a = d

    while True:
        b = a

        a = math.floor(b/2)
        if b % 2 == 0:
            c = 2
        else:
            c = 1

        if c == 1:
            b = 1
        else:
            b = 0

        if b == expect:
            s = s + str(b)
            expect = (expect + 1) % 2
            cnt += 1
            if cnt == count:
                return True
        else:
            print(a, cnt)
            print(s)
            return False

a = 1
while True:
    m = run(a)
    if m:
        print(a)
        exit(0)

    a += 1
