inputs = [9, 9, 9, 9,
9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
inputs = [0] * 9
idx = -1

# 1
z = inputs[0] + 12
print(z)
# 2
z = z * 26 + inputs[1] + 7
print(z)
# 3
z = z * 26 + inputs[2] + 8
print(z)
# 4
z = z * 26 + inputs[3] + 8
print(z)
# 5
z = z * 26 + inputs[4] + 15
print(z)
# 6
x = inputs[4] - 1
z = int(z / 26)
print(z)
exit(0)
if x != inputs[5]:
    z = z * 26 + inputs[5] + 12

# 7
z = z * 26 + inputs[6] + 8

# 8
x = inputs[6] - 3
z = int(z / 26)
if x != inputs[7]:
    z = z * 26 + inputs[7] + 13

# 9
x = z % 26 - 13
z = int(z / 26)
if x != inputs[8]:
    z = z * 26 + inputs[8] + 3

# 10
z = z * 26 + inputs[9] + 13

# 11
x = inputs[9] + 5
z = int(z / 26)
if x != inputs[10]:
    z = z * 26 + inputs[10] + 3

# 12
x = z % 26 - 1
z = int(z / 26)
if x != inputs[11]:
    z = z * 26 + inputs[11] + 9

# 13
x = z % 26 - 4
z = int(z / 26)
if x != inputs[12]:
    z = z * 26 + inputs[12] + 4

# 14
# z must be multiple of 26

x = z % 26 - 14
z = int(z / 26)

if x != inputs[13]: # THIS MUST BE FALSE
    z = z * 26 + inputs[13] + 13

exit(0)

def input(): # 1 thru 9
    global idx
    idx += 1
    return inputs[idx]

def run():
    x = 0
    y = 0
    z = 0

    # 1
    w = input()
    z = w + 12 # z between 13 and 21


    # 2
    w = input()
    z = z * 26 # z between 338 and 546
    z = z + w + 7 # z between 346 and 562


    # 3
    w = input()
    z = z * 26
    z = z + w + 8


    # 4
    w = input()
    z = z * 26
    z = z + w + 8


    # 5
    w = input()
    z = z * 26
    z = z + w + 15

    # 6
    w = input()
    x = z % 26
    z = int(z / 26)
    x = x - 16

    if x != w:
        z = z * 26
        z = z + w + 12

    # 7
    w = input()
    z = z * 26
    z = z + w + 8


    # 8
    w = input()
    x = z % 26
    z = int(z / 26)
    x = x - 11

    if x != w:
        z = z * 26
        z = z + w + 13


    # 9
    w = input()
    x = z % 26
    z = int(z / 26)
    x = x - 13

    if x != w:
        z = z * 26
        z = z + w + 3


    # 10
    w = input()
    z = z * 26
    z = z + w + 13


    # 11
    w = input()
    x = z % 26
    z = int(z / 26)
    x = x - 8

    if x != w:
        x = 1
        z = z * 26
        z = z + w + 3


    # 12
    w = input()
    x = z % 26
    z = int(z / 26)
    x = x - 1

    if x != w:
        z = z * 26
        z = z + w + 9


    # 13
    w = input()
    x = z % 26
    z = int(z / 26)
    x = x - 4

    if x != w:
        z = z * 26
        z = z + w + 4


    # 14
    w = input()
    x = z % 26 # x between 0 and 25
    z = int(z / 26)
    x = x - 14 # x between -14 and 11

    if x != w: # THIS MUST BE FALSE
        z = z * 26
        z = z + w + 13

    return z

i1 = 9
i2 = 9
i3 = 9
i4 = 9
i5 = 9

z = ((((i1 + 12) * 26 + i2 + 7) * 26 + i3 + 8) * 26 + i4 + 8) * 26 + i5 + 15
print(z)
exit(0)

while True:
    idx = -1
    z = run()
    print(inputs, z)
    if z == 0:
        exit(0)

    i = 13
    while True:
        inputs[i] -= 1
        if inputs[i] == 0:
            inputs[i] = 9
            i -= 1
        else:
            break


