f = open('input.txt', 'r')

def isValid(line):
    parts = line.strip().split()
    m = {}

    for p in parts:
        p = ''.join(sorted(p)) # part 2
        if p in m:
            return False
        m[p] = True

    return True

ans = 0
line = f.readline()
while line:
    if isValid(line):
        ans += 1

    line = f.readline()

f.close()
print(ans)
