import sys

N, K = map(int, sys.stdin.readline().split())
objects = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for w in range(1, K + 1):
        weight, value = objects[i - 1]
        if weight <= w:
            dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
        else:
            dp[i][w] = dp[i - 1][w]
print(dp[N][K])