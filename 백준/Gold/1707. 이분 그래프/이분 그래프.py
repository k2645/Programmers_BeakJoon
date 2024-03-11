import sys
from collections import deque

def isBipartiteGraph(graph, start, visited):
    L, R = set(), set()
    queue = deque([(start, 0)])
    visited[start] = True
    while queue:
        now, num = queue.popleft()
        array1, array2 = (L, R) if num == 0 else (R, L)
        array1.add(now)
        for node in graph[now]:
            if len(graph[node] & array2) != 0:
                return False
            if not visited[node]:
                visited[node] = True
                flag = 1 if num == 0 else 0
                queue.append((node, flag))
    return True


K = int(sys.stdin.readline())
for _ in range(K):
    V, E = map(int, sys.stdin.readline().split())
    graph = {n: set() for n in range(V)}
    for _ in range(E):
        u, v = map(int, sys.stdin.readline().split())
        graph[u - 1].add(v - 1)
        graph[v - 1].add(u - 1)
    visited = [False] * V
    result = []
    for i in range(V):
        if not visited[i]:
            result.append(isBipartiteGraph(graph, i, visited))
    if all(result):
        print("YES")
    else:
        print("NO")
