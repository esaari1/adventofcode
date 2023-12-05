part1 = 0

vals = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

s = '9964pfxmmr474'
print (s.rfind('4'))

with open('input.txt') as f:
    for line in f:
        m = {}
        l = line.strip()
        for k in vals.keys():
            idx = l.find(k)
            if idx >= 0:
                m[idx] = vals[k]
            idx = l.rfind(k)
            if idx >= 0:
                m[idx] = vals[k]
        print(l, m[min(m.keys())], + m[max(m.keys())], m)
        part1 += m[min(m.keys())] * 10 + m[max(m.keys())]
print(part1)
