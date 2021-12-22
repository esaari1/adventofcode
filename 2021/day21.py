positions = [4, 8]
# positions = [4, 5]
scores = [0, 0]

def part1():
    rollCount = 0
    currRoll = 0
    player = 0

    while True: # rollCount < 20:
        rollCount += 3

        for i in range(3):
            currRoll += 1
            if currRoll > 100:
                currRoll = 1

            positions[player] += currRoll
            while positions[player] > 10:
                positions[player] = positions[player] - 10

            #print(player, currRoll, positions[player])

        scores[player] += positions[player]
        print(player, scores[player])
        if scores[player] >= 1000:
            player = 1 - player
            print(player, scores[player], rollCount)
            print(scores[player] * rollCount)
            exit(0)

        player = 1 - player

def turn(player, pos1, pos2, scr1, scr2, universes):
    if scr1 >= 21:
        return (universes, 0)
    if scr2 >= 21:
        return (0, universes)

    uw1 = 0
    uw2 = 0

    npos1 = pos1
    npos2 = pos2
    nscr1 = scr1
    nscr2 = scr2

    for idx in range(len(turns)):
        if player == 0:
            npos1 = pos1 + turns[idx]
            if npos1 > 10:
                npos1 = npos1 - 10
            nscr1 = scr1 + npos1

        else:
            npos2 = pos2 + turns[idx]
            if npos2 > 10:
                npos2 = npos2 - 10
            nscr2 = scr2 + npos2

        (u1, u2) = turn(1 - player, npos1, npos2, nscr1, nscr2, universes * multiples[idx])
        uw1 += u1
        uw2 += u2

    print(uw1, uw2)
    return uw1, uw2


turns = [3, 4, 5, 6, 7, 8, 9]
multiples = [1, 3, 6, 7, 6, 3, 1]

def part2():
    (win1, win2) = turn(0, 4, 5, 0, 0, 1)
    print('FINAL', win1, win2)

part2()
