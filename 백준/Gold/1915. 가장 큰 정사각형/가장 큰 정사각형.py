import sys

n, m = map(int, sys.stdin.readline().split())
board = [list(str(sys.stdin.readline().strip())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]

max_length = 0
for i in range(m):
    dp[0][i] = int(board[0][i])
    max_length = max(max_length, dp[0][i])

for i in range(n):
    dp[i][0] = int(board[i][0])
    max_length = max(max_length, dp[i][0])

for i in range(1, n):
    for j in range(1, m):
        if board[i][j] == '0':
            dp[i][j] = 0
        else:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
            max_length = max(max_length, dp[i][j])

print(max_length ** 2)
