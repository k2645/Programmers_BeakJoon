import sys
from collections import deque

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

dp = [0] * N
dp[0] = 1
for i in range(1, N):
    max_dp = 0
    for j in range(i):
        if A[j] < A[i]:
            max_dp = max(max_dp, dp[j])
    dp[i] = max_dp + 1

n = max(dp)
print(n)
ans_arr = deque([])
for i in range(N - 1, -1, -1):
    if dp[i] == n:
        ans_arr.appendleft(str(A[i]))
        n -= 1
print(" ".join(ans_arr))