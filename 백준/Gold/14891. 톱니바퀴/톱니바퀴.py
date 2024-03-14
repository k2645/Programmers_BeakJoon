import sys
from collections import deque

def leftGear(gearNum, directions):
    while gearNum > 0:
        if gears[gearNum][2] == gears[gearNum + 1][6]:
            directions[gearNum] = 0
            return
        else:
            directions[gearNum] = directions[gearNum + 1] * -1
        gearNum -= 1

def rightGear(gearNum, directions):
    while gearNum < 5:
        if gears[gearNum][6] == gears[gearNum - 1][2]:
            directions[gearNum] = 0
            return
        else:
            directions[gearNum] = directions[gearNum - 1] * -1
        gearNum += 1

gears = [0]
for _ in range(4):
    gears.append(deque(map(int, list(sys.stdin.readline().strip()))))
K = int(sys.stdin.readline())
for _ in range(K):
    gearNum, direction = map(int, sys.stdin.readline().split())
    directions = [0] * 5
    directions[gearNum] = direction
    leftGear(gearNum - 1, directions)
    rightGear(gearNum + 1, directions)
    for i in range(1, 5):
        gears[i].rotate(directions[i])

result = 0
for i in range(1, 5):
    if gears[i][0] == 1:
        result += 2 ** (i - 1)
print(result)