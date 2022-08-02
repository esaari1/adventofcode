import hashlib
import queue

salt = 'abc'
salt = 'ngcjuoqr'
pos = 0

threes = {}

def checkRepeats(s, pos):
    global threes

    fives = []
    prev = ''
    count = 1
    match = False
    for c in s:
        if c == prev:
            count += 1
        else:
            if count >= 5:
                fives.append(prev)
            if count >= 3 and not match:
                match = True
                if prev not in threes:
                    threes[prev] = []
                threes[prev].append(pos)
            prev = c
            count = 1

    if count >= 5:
        fives.append(prev)
    if count >= 3 and not match:
        if prev not in threes:
            threes[prev] = []
        threes[prev].append(pos)

    return fives

matches = []

while True:
    hex = salt + str(pos)
    #print(pos)
    hex = hashlib.md5(hex.encode('utf-8')).hexdigest()

    for i in range(2016):
         hex = hashlib.md5(hex.encode('utf-8')).hexdigest()

    fives = checkRepeats(hex, pos)
    for f in fives:
        #print(f, pos, threes[f], len(matches))

        if f in threes:
            while (len(threes[f]) > 0) and (threes[f][0] < pos):
                t = threes[f][0]
                threes[f] = threes[f][1:]

                if (t + 1000) >= pos:
                    print('found ', pos, t, len(matches))
                    matches.append(t)

    matches.sort()

    if len(matches) >= 64 and (pos - matches[-1]) > 1000:
        print('ANS = ', matches[63])
        exit()

    pos += 1

#20219