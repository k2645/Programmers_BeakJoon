import sys
from collections import deque

def checkPossible(mapSize, map, row = 0, col = 0):
    visitiedQueue = deque([(row, col)])
    while visitiedQueue:
        now = visitiedQueue.popleft()
        row = now[0]
        col = now[1]
        if map[row][col] == -1:
            return True
        jumpSize = map[row][col]
        if jumpSize == 0:
            continue
        if row + jumpSize < mapSize:
            visitiedQueue.append((row + jumpSize, col))
        if col + jumpSize < mapSize:
            visitiedQueue.append((row, col + jumpSize))
    return False

mapSize = int(sys.stdin.readline())
map = [list(map(int, sys.stdin.readline().split())) for _ in range(mapSize)]
if checkPossible(mapSize, map):
    print("HaruHaru")
else:
    print("Hing")
