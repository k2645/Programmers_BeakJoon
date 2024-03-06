import sys
from collections import deque

def cabbageBFS(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for node in graph[v]:
            if not visited[node]:
                queue.append(node)
                visited[node] = True

T = int(sys.stdin.readline())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    visited = dict()
    cabbageGraph = dict()
    for _ in range(K):
        bridge = list(map(int, sys.stdin.readline().split()))
        num = bridge[0] + bridge[1] * M
        cabbageGraph[num] = []
        visited[num] = False

    for node in cabbageGraph:
        x, y = node % M, node // M
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N:
                closedNode = nx + ny * M
                if closedNode in cabbageGraph:
                    cabbageGraph[closedNode].append(node)
                    cabbageGraph[node].append(closedNode)

    count = 0
    for node in visited:
        if visited[node] == False:
            cabbageBFS(cabbageGraph, node, visited)
            count += 1

    print(count)
