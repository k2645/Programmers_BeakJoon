import sys
from collections import deque

def findLand(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        now = queue.popleft()
        for node in graph[now]:
            if visited[node] == False:
                queue.append(node)
                visited[node] = True

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    graph = {n: set() for n in range(w * h)}
    visited = dict()
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    mapList = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if mapList[i][j] == 1:
                visited[i * w + j] = False
                for x, y in directions:
                    dx, dy = i + x, j + y
                    if 0 <= dx < h and 0 <= dy < w:
                        if mapList[dx][dy] == 1:
                            graph[i * w + j].add(dx * w + dy)
                            graph[dx * w + dy].add(i * w + j)
    count = 0
    for start in visited:
        if visited[start] == False:
            findLand(graph, start, visited)
            count += 1
    print(count)