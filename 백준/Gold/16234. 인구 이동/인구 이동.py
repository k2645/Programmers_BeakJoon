import sys
from collections import deque

def distributePopulation(start, visited):
    queue = deque([start])
    visited[start[0]][start[1]] = True
    populations = 0
    country = []
    while queue:
        x, y, p = queue.popleft()
        populations += p
        country.append((x, y))
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False:
                np = countryPopulation[nx][ny]
                if L <= abs(np - p) <= R:
                    visited[nx][ny] = True
                    queue.append((nx, ny, np))
    distribution = populations // len(country)
    for i, j in country:
        countryPopulation[i][j] = distribution

N, L, R = map(int, sys.stdin.readline().split())
countryPopulation = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
day = 0
while True:
    visited = [[False] * N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                distributePopulation((i, j, countryPopulation[i][j]), visited)
                count += 1
    if count == N * N:
        break
    day += 1
print(day)