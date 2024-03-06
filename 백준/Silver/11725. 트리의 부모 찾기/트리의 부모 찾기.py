import sys
from collections import deque

def findParent(graph, start, visited, parentNode):
    queue = deque([start])
    visited[start] = True
    while queue:
        now = queue.popleft()
        for node in graph[now]:
            if not visited[node]:
                queue.append(node)
                visited[node] = True
                parentNode[node] = now + 1

N = int(sys.stdin.readline())
graph = {n: [] for n in range(N)}
for _ in range(N - 1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

parentList = [0] * N
findParent(graph, 0, [False] * N, parentList)

for i in range(N - 1):
    print(parentList[i + 1])