arr = [0, 2, 7, 0]
arr = [2,   8,   8,   5,   4,   2,   3,   1,   5,   5,   1,   2,   15,  13,  5,   14]
visited = {}

moves = 0
check = ''

while True:
    visited[str(arr)] = True
    moves += 1
    m = max(arr)
    i = arr.index(m)

    arr[i] = 0
    i += 1
    if i == len(arr):
        i = 0

    while m > 0:
        arr[i] += 1
        m -= 1
        i += 1
        if i == len(arr):
            i = 0

    if str(arr) == check:
        break

    if check == '' and str(arr) in visited:
        check = str(arr)
        moves = 0

print(moves)
