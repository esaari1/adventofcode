import math

# vals = (
#     (4, 5),
#     (1, 2),
#     (2, 3)
# )

vals = (
    (2, 5),
    (7, 13),
    (10, 17),
    (2, 3),
    (9, 19),
    (0, 7),
    (0, 11)
)

t = 0
d = 1
for idx, v in enumerate(vals):
    while (t + idx+1 + v[0]) % v[1] != 0:
        t += d
    d = math.lcm(d, v[1])

print(t)
