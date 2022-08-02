a = 116
b = 299

# a = 65
# b = 8921

a = (a * 16807) % 2147483647
b = (b * 48271) % 2147483647

matches = 0

for x in range(5000000):
    print(x, ' of 5,000,000')
    while (a % 4) != 0:
        a = (a * 16807) % 2147483647

    while (b % 8) != 0:
        b = (b * 48271) % 2147483647

    if (a & 0xFFFF) == (b & 0xFFFF):
        matches += 1

    a = (a * 16807) % 2147483647
    b = (b * 48271) % 2147483647

print(matches)
