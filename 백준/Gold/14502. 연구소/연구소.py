import copy
import sys
from collections import deque
from itertools import combinations

def barrier(virusMap, x, y, barrierable):
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and virusMap[nx][ny] == 0:
            virusMap[nx][ny] = 1
            barrierable.add((nx, ny))
            barrier(virusMap, nx, ny, barrierable)
    return barrierable

def findNoneVirus(virusMap):
    viruseQueue = deque(viruses)
    while viruseQueue:
        x, y = viruseQueue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and virusMap[nx][ny] == 0:
                viruseQueue.append((nx, ny))
                virusMap[nx][ny] = 2
    result = 0
    for row in virusMap:
        result += row.count(0)
    return result

N, M = map(int, sys.stdin.readline().split())
originalVirusMap = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
viruses = [(i, j) for i, row in enumerate(originalVirusMap) for j, value in enumerate(row) if value == 2]
directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
barrierable = set()
for virus in viruses:
    virusMap = copy.deepcopy(originalVirusMap)
    barrier(virusMap, virus[0], virus[1], barrierable)

maxResult = 0
for barriers in list(combinations(barrierable, 3)):
    virusMap = copy.deepcopy(originalVirusMap)
    for i, j in barriers:
        virusMap[i][j] = 1
    result = findNoneVirus(virusMap)
    if maxResult < result:
        maxResult = result

print(maxResult)