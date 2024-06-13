import sys

def back(x, y, visited_len, visited):
    global ans, board
    ans = max(ans, visited_len)
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C and not visited[ord(board[nx][ny]) - 65]:
            visited[ord(board[nx][ny]) - 65] = True
            back(nx, ny, visited_len + 1, visited)
            visited[ord(board[nx][ny]) - 65] = False


R, C = map(int, sys.stdin.readline().split())
board = [list(str(sys.stdin.readline().strip())) for _ in range(R)]

visited = [False] * 26
visited[ord(board[0][0]) - 65] = True
ans = 1
back(0, 0, 1, visited)
print(ans)