import sys

def floyd(dist):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

N, R = map(int, sys.stdin.readline().split())
city = set(sys.stdin.readline().split())
city = {n: i for i, n in enumerate(city)}
M = int(sys.stdin.readline())
travel = [city[i] for i in list(sys.stdin.readline().split())]
K = int(sys.stdin.readline())

free_ticket = set(["Mugunghwa", "ITX-Saemaeul", "ITX-Cheongchun"])
half_ticket = set(["S-Train", "V-Train"])

dist = [[float("inf")] * N for _ in range(N)]
naeillo_dist = [[float("inf")] * N for _ in range(N)]
for _ in range(K):
    trans, start, end, price = sys.stdin.readline().split()
    start, end = city[start], city[end]
    dist[start][end] = min(float(price), dist[start][end])
    dist[end][start] = min(float(price), dist[end][start])
    if trans in free_ticket:
        naeillo_dist[start][end] = 0
        naeillo_dist[end][start] = 0
    elif trans in half_ticket:
        naeillo_dist[start][end] = min(float(price) / 2, naeillo_dist[start][end])
        naeillo_dist[end][start] = min(float(price) / 2, naeillo_dist[end][start])
    else:
        naeillo_dist[start][end] = min(float(price), naeillo_dist[start][end])
        naeillo_dist[end][start] = min(float(price), naeillo_dist[end][start])


dist = floyd(dist)
naeillo_dist = floyd(naeillo_dist)

price = 0
naeillo_price = R
for i in range(len(travel) - 1):
    s, e = travel[i], travel[i + 1]
    price += dist[s][e]
    naeillo_price += naeillo_dist[s][e]

if price > naeillo_price:
    print("Yes")
else:
    print("No")