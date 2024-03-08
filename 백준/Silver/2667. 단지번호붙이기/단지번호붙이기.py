import sys
from collections import deque

def findComplex(start):
    houseCount = 0
    queue = deque([start])
    complexMap[start[0]][start[1]] = 0
    while queue:
        x, y = queue.popleft()
        houseCount += 1
        for i, j in directions:
            nx, ny = x + i, y + j
            if 0 <= nx < N and 0 <= ny < N and complexMap[nx][ny]:
                queue.append((nx, ny))
                complexMap[nx][ny] = 0
    return houseCount

N = int(sys.stdin.readline())
complexMap = [[int(digit) for digit in str(sys.stdin.readline().strip())] for _ in range(N)]

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
complexHouse = []
for i in range(N):
    for j in range(N):
        if complexMap[i][j] == 1:
            complexHouse.append(findComplex((i, j)))

print(len(complexHouse))
for houseCount in sorted(complexHouse):
    print(houseCount)