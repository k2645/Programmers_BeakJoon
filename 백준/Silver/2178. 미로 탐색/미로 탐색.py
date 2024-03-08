import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
maze = []
for _ in range(N):
    row = sys.stdin.readline().strip()
    maze.append([int(char) for char in row])

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
queue = deque([(0, 0, 1)])
maze[0][0] = 0
while queue:
    x, y, count = queue.popleft()
    if x == N - 1 and y == M - 1:
        print(count)
        break
    for i, j in directions:
        nx, ny = x + i, y + j
        if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1:
            queue.append((nx, ny, count + 1))
            maze[nx][ny] = 0