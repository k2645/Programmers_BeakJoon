import sys

N, K = map(int, sys.stdin.readline().split())
virus_grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
S, X, Y = map(int, sys.stdin.readline().split())

def virus_bfs(viruses):
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    new_virus = []
    for vx, vy in viruses:
        for dx, dy in directions:
            nx, ny = vx + dx, vy + dy
            if 0 <= nx < N and 0 <= ny < N and virus_grid[nx][ny] == 0:
                virus_grid[nx][ny] = type
                new_virus.append((nx, ny))
    return new_virus


virus_graph = dict()
# 그래프 생성
for i in range(N):
    for j in range(N):
        type = virus_grid[i][j]
        if type != 0:
            if type in virus_graph:
                virus_graph[type].append((i, j))
            else:
                virus_graph[type] = [(i, j)]

for _ in range(S):
    for type in sorted(virus_graph):
        virus_graph[type] = virus_bfs(virus_graph[type])

print(virus_grid[X - 1][Y - 1])