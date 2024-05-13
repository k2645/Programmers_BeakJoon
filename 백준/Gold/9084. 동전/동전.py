import sys

'''
v1, v2를 사용해서 M을 만들 수 있는 방법의 수
'''

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    values = map(int, sys.stdin.readline().split())
    M = int(sys.stdin.readline())
    dp = [0] * (M + 1)
    for v in values:
        if v <= M:
            dp[v] += 1
        for i in range(v, M + 1):
            dp[i] += dp[i - v]

    print(dp[M])

