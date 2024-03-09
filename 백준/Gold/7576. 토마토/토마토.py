import sys
from collections import deque

def ripenTomato(ripeTomatos):
    tomatoQueue = deque(ripeTomatos)
    ripenDay = 0
    while tomatoQueue:
        x, y, day = tomatoQueue.popleft()
        ripenDay = day if ripenDay < day else ripenDay
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and tomatos[nx][ny] == 0:
                tomatoQueue.append((nx, ny, day + 1))
                tomatos[nx][ny] = 1
    if any(0 in l for l in tomatos):
        return -1
    else:
        return ripenDay

M, N = map(int, sys.stdin.readline().split())
tomatos = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
ripeTomatos = []
for i in range(N):
    for j in list(filter(lambda x: tomatos[i][x] == 1, range(M))):
        ripeTomatos.append((i, j, 0))

if all(0 not in l for l in tomatos) and any(1 in l for l in tomatos):
    print(0)
else:
    print(ripenTomato(ripeTomatos))