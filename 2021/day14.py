# input = 'NNCB'
input = 'FSHBKOOPCFSFKONFNFBB'
entries = {}
counts = {}

# read ib mappings
with open('input.txt') as f:
    for line in f:
        (pair, middle) = line.strip().split(' -> ')
        entries[pair] = middle

# get count of unique pairs in input string
# count characters in input string
pc = {}
for i in range(len(input) - 1):
    counts[input[i]] = counts.get(input[i], 0) + 1
    pair = input[i:i+2]
    pc[pair] = pc.get(pair, 0) + 1

# count last char in input string
counts[input[-1]] = counts.get(input[-1], 0) + 1

for x in range(40):
    newpc = {}

    # loop over unique pairs
    for pair in pc:
        # get mapping char. increment irs count
        c = entries[pair]
        counts[c] = counts.get(c, 0) + pc[pair]

        # add new pairs to new pair map
        newpc[pair[0] + c] = newpc.get(pair[0] + c, 0) + pc[pair]
        newpc[c + pair[1]] = newpc.get(c + pair[1], 0) + pc[pair]

    # replace old pair map with new one
    pc = newpc

l = list(counts.values())
l.sort()
print(l[-1] - l[0])
