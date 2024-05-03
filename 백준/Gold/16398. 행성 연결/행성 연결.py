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

N = int(sys.stdin.readline())
edges = []
for i in range(N):
    l = list(map(int, sys.stdin.readline().split()))
    for j in range(i + 1, N):
        edges.append([i, j, l[j]])

edges.sort(key=lambda x: x[2])
tree = [i for i in range(N)]
rank = [0] * (N + 1)

ans = 0
cnt = 0

for x, y, w in edges:
    if find_set(x) != find_set(y):
        union(find_set(x), find_set(y))
        ans += w
        cnt += 1
        if cnt == N - 1:
            break

print(ans)