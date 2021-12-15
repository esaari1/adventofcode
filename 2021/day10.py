import math

score = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

part2score = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

matches = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

f = open('input.txt')

line = f.readline()

ans = 0
part2 = []

while line:
    stack = []
    line = line.strip()
    corrupt = False

    for c in line:
        if c in matches:
            stack.append(c)
        else:
            start = stack.pop()
            if matches[start] != c:
                ans += score[c]
                corrupt = True
                break

    if len(stack) > 0 and not corrupt:
        stack.reverse()
        val = 0
        for c in stack:
            val = (val * 5) + part2score[matches[c]]
        part2.append(val)

    line = f.readline()

f.close()
part2.sort()

idx = math.floor(len(part2) / 2)
print(part2[idx])
