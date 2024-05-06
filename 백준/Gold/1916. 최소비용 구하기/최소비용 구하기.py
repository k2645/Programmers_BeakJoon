import sys
import heapq

def dijkstra(start, end):
    dist = [float("inf")] * (N + 1)
    visited = set()
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        distance, node = heapq.heappop(heap)
        if node not in visited:
            dist[node] = distance
            visited.add(node)
            if node == end:
                return dist[node]
            for destination in range(N + 1):
                if destination not in visited and dist[destination] > adj[node][destination] + dist[node]:
                    heapq.heappush(heap, (adj[node][destination] + dist[node], destination))

    return float("inf")

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
adj = [[float("inf")] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    s, e, w = map(int, sys.stdin.readline().split())
    adj[s][e] = min(w, adj[s][e])
start, end = map(int, sys.stdin.readline().split())

print(dijkstra(start, end))
