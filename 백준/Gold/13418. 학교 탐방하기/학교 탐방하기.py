import sys

def find_set(x): # 재귀로 부모 노드 찾아가는 과정
    if tree[x] != x:
        tree[x] = find_set(tree[x])
    return tree[x]

def union(x, y): # 노드의 관계를 이어주는 과정
    if rank[x] > rank[y]:
        tree[y] = x
    else:
        tree[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1

N, M = map(int, sys.stdin.readline().split())
a, b, c = map(int, sys.stdin.readline().split())
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

if c == 0:
    worst, best = 1, 1
else:
    worst, best = 0, 0

cnt = 0
edges.sort(key=lambda x: x[2])
tree = [i for i in range(N + 1)]
rank = [0] * (N + 1)
for x, y, w in edges:
    if find_set(x) != find_set(y):
        union(find_set(x), find_set(y))
        if w == 0:
            worst += 1
        cnt += 1
        if cnt == N - 1:
            break

cnt = 0
edges.sort(key=lambda x: x[2], reverse=True)
tree = [i for i in range(N + 1)]
rank = [0] * (N + 1)
for x, y, w in edges:
    if find_set(x) != find_set(y):
        union(find_set(x), find_set(y))
        if w == 0:
            best += 1
        cnt += 1
        if cnt == N - 1:
            break

print((worst**2) - (best**2))
