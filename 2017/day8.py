def doCheck(reg2, test, testVal):
    if test == '>':
        return regs[reg2] > testVal
    if test == '>=':
        return regs[reg2] >= testVal
    if test == '<':
        return regs[reg2] < testVal
    if test == '<=':
        return regs[reg2] <= testVal
    if test == '==':
        return regs[reg2] == testVal
    if test == '!=':
        return regs[reg2] != testVal

    print('UNKNOWN ', test)
    exit(0)

f = open('input.txt')

regs = {}
line = f.readline()

ans2 = 0

while line:
    (reg, op, amount, iff, reg2, test, testVal) = line.strip().split(' ')

    if reg not in regs:
        regs[reg] = 0
    if reg2 not in regs:
        regs[reg2] = 0

    amount = int(amount)
    testVal = int(testVal)

    if doCheck(reg2, test, testVal):
        if op == 'inc':
            regs[reg] += amount
        else:
            regs[reg] -= amount

        if ans2 < regs[reg]:
            ans2 = regs[reg]

    line = f.readline()

f.close()

ans = 0
for k in regs:
    if regs[k] > ans:
        ans = regs[k]

print(ans)
print(ans2)
