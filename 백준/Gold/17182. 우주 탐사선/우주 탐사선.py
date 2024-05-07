import sys

def floyd():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

def back(start, visited, time):
    global ans
    for i in range(N):
        if i not in visited:
            visited.add(i)
            back(i, visited, time + dist[start][i])
            if len(visited) == N:
                ans = min(ans, time + dist[start][i])
            visited.remove(i)

N, K = map(int, sys.stdin.readline().split())
dist = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dist = floyd()

ans = float("inf")
back(K, set([K]), 0)
print(ans)

