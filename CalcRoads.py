#!/usr/bin/env python
# Author: weikun
# Created Time: Wed 06 Mar 2019 02:21:56 PM CST


lines = ((1, 2), (1, 3), (1, 6), (2, 4), (3, 5), (4, 5), (4, 6), (5, 6))
nodes = range(1, 7)

def Connect(n1, n2):
    global lines
    return (n1, n2) in lines or (n2, n1) in lines

def CanCatch(roads):
    global lines, nodes
    repeatRoads = roads[-2::-2]
    police, thief = roads[-1]

    if police == thief or Connect(police, thief):
        print roads
        return True

    for nextPolice in [n for n in nodes if (n != police) and Connect(n, police)]:
        if (nextPolice, thief) in repeatRoads:
            continue

        if CanEscape(roads + [(nextPolice, thief)]):
            continue
        else:
            return True
    else:
        return False

def CanEscape(roads):
    global lines, nodes
    repeatRoads = roads[-2::-2]
    police, thief = roads[-1]

    if police == thief:
        print roads
        return False

    for nextThief in [n for n in nodes if (n != thief) and Connect(n, thief)]:
        if (police, nextThief) in repeatRoads:
            return True

        if CanCatch(roads + [(police, nextThief)]):
            continue
        else:
            return True
    else:
        return False


print CanCatch([(6, 3)])


