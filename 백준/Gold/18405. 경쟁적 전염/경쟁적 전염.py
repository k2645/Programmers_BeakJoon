import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
virus_grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
S, X, Y = map(int, sys.stdin.readline().split())

def virus_bfs(virus_graph, S, X, Y):
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    virus = deque(virus_graph)
    while virus:
        type, x, y, time = virus.popleft()
        if time == S:
            break
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and virus_grid[nx][ny] == 0:
                virus_grid[nx][ny] = type
                virus.append((type, nx, ny, time + 1))
    return virus_grid[X - 1][Y - 1]

virus_graph = []
for i in range(N):
    for j in range(N):
        if virus_grid[i][j] != 0:
            virus_graph.append((virus_grid[i][j], i, j, 0))
virus_graph.sort()
print(virus_bfs(virus_graph, S, X, Y))