# get chars in s1 not in s2
def charDiff(s1, s2):
    chars = {}
    for c in s1:
        chars[c] = True
    for c in s2:
        del chars[c]

    return list(chars.keys())

# check if s1 contains s2
def contains(s1, s2):
    chars = {}
    for c in s2:
        chars[c] = True
    count = 0
    for c in s1:
        if c in chars:
            count += 1
        if count == len(s2):
            return True
    return False

def process(data):
    samples = data.strip().split(' ')

    values = {}
    counts = {
        5: [],
        6: []
    }
    letters = {}
    m = {}

    for s in samples:
        if len(s) == 2:
            values[1] = s
            m[s] = 1
        elif len(s) == 3:
            values[7] = s
            m[s] = 7
        elif len(s) == 4:
            values[4] = s
            m[s] = 4
        elif len(s) == 7:
            values[8] = s
            m[s] = 8
        elif len(s) == 5:
            counts[5].append(s)
        elif len(s) == 6:
            counts[6].append(s)


    for val in counts[5]:
        if contains(val, values[1]):
            values[3] = val
            m[val] = 3
            break
    counts[5].remove(values[3])

    for val in counts[6]:
        if contains(val, values[3]):
            values[9] = val
            m[val] = 9
        elif contains(val, values[7]):
            values[0] = val
            m[val] = 0

    counts[6].remove(values[9])
    counts[6].remove(values[0])

    values[6] = counts[6][0]
    m[values[6]] = 6

    for val in counts[5]:
        if contains(values[6], val):
            values[5] = val
            m[val] = 5
            break
    counts[5].remove(values[5])
    values[2] = counts[5][0]
    m[values[2]] = 2

    letters[charDiff(values[7], values[1])[0]] = 'a'
    letters[charDiff(values[9], values[3])[0]] = 'b'
    letters[charDiff(values[8], values[6])[0]] = 'c'
    letters[charDiff(values[8], values[0])[0]] = 'd'
    letters[charDiff(values[8], values[9])[0]] = 'e'

    d = charDiff(values[8], values[2])
    if d[0] not in letters:
        letters[d[0]] = 'f'
    else:
        letters[d[1]] = 'f'

    diffs = charDiff(values[0], values[7])
    for d in diffs:
        if d not in letters:
            letters[d] = 'g'

    return letters

numMap = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9
}

with open('input.txt') as f:
    sum = 0
    for line in f:
        (data, digits) = line.strip().split('|')
        letters = process(data)

        data = digits.strip().split(' ')
        val = 0
        for idx in range(len(data)):
            digit = data[idx]
            arr = []
            for c in digit:
                arr.append(letters[c])

            arr.sort()
            num = ''.join(arr)

            val = val + (numMap[num] * (10 ** (3 - idx)))

        sum += val

print(sum)