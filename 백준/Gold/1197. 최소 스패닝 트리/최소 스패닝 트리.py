import sys

def find_set(x): # 재귀로 부모 노드 찾아가는 과정
    if tree[x] != x:
        tree[x] = find_set(tree[x])
    return tree[x]

def union(x, y): # 노드의 관계를 이어주는 과정
    tree[find_set(y)] = find_set(x)

V, E = map(int, sys.stdin.readline().split())
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(E)]
edges.sort(key=lambda x: x[2])
tree = [i for i in range(V + 1)]

ans = 0
cnt = 0

for x, y, w in edges:
    if find_set(x) != find_set(y):
        union(x, y)
        ans += w
        cnt += 1
        if cnt == V - 1:
            break

print(ans)