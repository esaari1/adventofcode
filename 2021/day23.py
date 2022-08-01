emap = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000
}

roomChars = ['A', 'B', 'C', 'D']

goal = '...........AAAABBBBCCCCDDDD'

visited = {}
minEnergy = None

def destinationIdx(c):
    if c == 'A':
        return 0
    if c == 'B':
        return 1
    elif c == 'C':
        return 2
    return 3


def move(state, energy, states):
    states.append(state)
    #print(state, energy)
    global minEnergy

    if minEnergy is not None and energy > minEnergy:
        return

    if state == goal:
        if (minEnergy is None or energy < minEnergy):
            print(energy)
            print(states)
            minEnergy = energy
        return

    if state in visited:
        if visited[state] < energy:
            return

    visited[state] = energy

    hallway = state[0:11]
    rooms = ['', '', '', '']
    rooms[0] = state[11:15]
    rooms[1] = state[15:19]
    rooms[2] = state[19:23]
    rooms[3] = state[23:]

    # check hallway
    for idx in range(len(hallway)):
        if hallway[idx] != '.':
            c = hallway[idx]

            # check if can move to destination
            destIdx = destinationIdx(c)
            hdestIdx = (2*destIdx) + 2

            if rooms[destIdx] in ['....', f'{c}...', f'{c}{c}..', f'{c}{c}{c}.']:
                # check for block
                sidx = min(idx, hdestIdx)
                eidx = max(idx, hdestIdx)
                hidx = sidx
                canGo = True

                while hidx < eidx:
                    if hidx != idx and hallway[hidx] != '.':
                        canGo = False
                        break
                    hidx += 1

                if canGo:
                    dpos = 3
                    if rooms[destIdx] == f'{c}{c}..':
                        dpos = 2
                    elif rooms[destIdx] == f'{c}...':
                        dpos = 1
                    elif rooms[destIdx] == '....':
                        dpos = 0
                    newstate = f'{hallway[:idx]}.{hallway[idx+1:]}'
                    for x in range(4):
                        if x == destIdx:
                            if rooms[destIdx] == '....':
                                newstate += f'{c}...'
                            elif rooms[destIdx] == f'{c}...':
                                newstate += f'{c}{c}..'
                            elif rooms[destIdx] == f'{c}{c}..':
                                newstate += f'{c}{c}{c}.'
                            else:
                                newstate += f'{c}{c}{c}{c}'
                        else:
                            newstate += rooms[x]

                    #print('HALL', newstate, eidx - sidx + 1 + (1 - dpos))
                    move(newstate, energy + ((eidx - sidx + 1 + (3 - dpos)) * emap[c]), states[:])

    for ridx in range(4):
        room = rooms[ridx]
        roomChar = roomChars[ridx]

        if room == '....':
            continue
        if room == f'{roomChar}{roomChar}{roomChar}.':
            continue
        if room == f'{roomChar}{roomChar}..':
            continue
        if room == f'{roomChar}...':
            continue

        c = room[0]
        pos = 0
        newroom = '....'
        if room[3] != '.':
            c = room[3]
            pos = 3
            newroom = f'{room[0]}{room[1]}{room[2]}.'
        elif room[2] != '.':
            c = room[2]
            pos = 2
            newroom = f'{room[0]}{room[1]}..'
        elif room[1] != '.':
            c = room[1]
            pos = 1
            newroom = f'{room[0]}...'

        # check if can move to destination
        destIdx = destinationIdx(c)

        if rooms[destIdx] in ['...', f'{c}...', f'{c}{c}..', f'{c}{c}{c}.']:
            # check for block
            sidx = min(ridx, destIdx)
            eidx = max(ridx, destIdx)
            hidx = 3 + (2 * sidx)
            canGo = True

            while hidx < 3 + (2 * eidx):
                if hallway[hidx] != '.':
                    canGo = False
                    break
                hidx += 2

            if canGo:
                dpos = 3
                if rooms[destIdx] == f'{c}{c}..':
                    dpos = 2
                elif rooms[destIdx] == f'{c}...':
                    dpos = 1
                elif rooms[destIdx] == '....':
                    dpos = 0
                newstate = hallway
                for x in range(4):
                    if x == ridx:
                        newstate += newroom
                    elif x == destIdx:
                        if rooms[destIdx] == '....':
                            newstate += f'{c}...'
                        elif rooms[destIdx] == f'{c}...':
                            newstate += f'{c}{c}..'
                        elif rooms[destIdx] == f'{c}{c}..':
                            newstate += f'{c}{c}{c}.'
                        else:
                            newstate += f'{c}{c}{c}{c}'
                    else:
                        newstate += rooms[x]

                #print('GO', pos, dpos, newstate, ((eidx*2+2) - (sidx*2+2) + 2 + (3 - pos) + (3 - dpos)) * emap[c])
                move(newstate, energy + (((eidx*2+2) - (sidx*2+2) + 2 + (3 - pos) + (3 - dpos)) * emap[c]), states[:])
                continue

        lefts = []
        rights = []

        if ridx == 0:
            lefts = [1, 0]
            rights = [3, 5, 7, 9, 10]
        elif ridx == 1:
            lefts = [3, 1, 0]
            rights = [5, 7, 9, 10]
        elif ridx == 2:
            lefts = [5, 3, 1, 0]
            rights = [7, 9, 10]
        else:
            lefts = [7, 5, 3, 1, 0]
            rights = [9, 10]

        for i in lefts:
            if hallway[i] == '.':
                newstate = f'{hallway[0:i]}{c}{hallway[i+1:]}'
                for j in range(ridx):
                    newstate += rooms[j]
                newstate += newroom
                for j in range(ridx + 1, 4):
                    newstate += rooms[j]
                #print(newstate, (((2 * ridx) + 3) - i + (3 - pos)) * emap[c])
                move(newstate, energy + ((((2 * ridx) + 3) - i + (3 - pos)) * emap[c]), states[:])
            else:
                break

        for i in rights:
            if hallway[i] == '.':
                newstate = f'{hallway[0:i]}{c}{hallway[i+1:]}'
                for j in range(ridx):
                    newstate += rooms[j]
                newstate += newroom
                for j in range(ridx + 1, 4):
                    newstate += rooms[j]
                #print(newstate, (i - ((2 * ridx) + 2) + 1 + (3 - pos)) * emap[c])
                move(newstate, energy + ((i - ((2 * ridx) + 2) + 1 + (3 - pos)) * emap[c]), states[:])
            else:
                break

    states.pop()

#move('...........BBBDA...C...D...', 0, [])
#move('...........ADDBDBCCCABBACAD', 0, [])
move('...........BDDCABCDDABACCAB', 0, [])
print(minEnergy)
