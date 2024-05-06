import sys
import heapq

def dijkstra():
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dist = [[float("inf")] * M for _ in range(N)]
    visited = set()
    heap = []
    heapq.heappush(heap, (0, (0, 0)))
    while heap:
        distance, node = heapq.heappop(heap)
        if node not in visited:
            x, y = node
            visited.add(node)
            dist[x][y] = distance
            if node == (N - 1, M - 1):
                break
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in visited and dist[nx][ny] > dist[x][y] + board[nx][ny]:
                    heapq.heappush(heap, (board[nx][ny] + dist[x][y], (nx, ny)))

    return dist[N - 1][M - 1]

M, N = map(int, sys.stdin.readline().split())
board = []
for _ in range(N):
    board.append(list(map(int, list(sys.stdin.readline().strip()))))

print(dijkstra())