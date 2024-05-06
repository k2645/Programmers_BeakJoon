import sys

def floyd():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
dist = [[float("inf")] * n for _ in range(n)]
for i in range(n):
    dist[i][i] = 0

for _ in range(m):
    s, e, w = map(int, sys.stdin.readline().split())
    dist[s - 1][e - 1] = min(w, dist[s - 1][e - 1])

ans = floyd()
for i in range(n):
    for j in range(n):
        if ans[i][j] == float("inf"):
            ans[i][j] = 0
        print(ans[i][j], end = " ")
    print()