import sys

def floyd():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

n, m, r = map(int, sys.stdin.readline().split())
items = list(map(int, sys.stdin.readline().split()))
dist = [[float("inf")] * n for _ in range(n)]
for i in range(n):
    dist[i][i] = 0

for _ in range(r):
    s, e, w = map(int, sys.stdin.readline().split())
    dist[s - 1][e - 1] = min(w, dist[s - 1][e - 1])
    dist[e - 1][s - 1] = min(w, dist[e - 1][s - 1])

floyd = floyd()
ans = 0
for i in range(n):
    a = 0
    for j in range(n):
        if floyd[i][j] <= m:
            a += items[j]
    ans = max(a, ans)
print(ans)