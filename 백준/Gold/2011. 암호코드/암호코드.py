import sys

N = list(map(int, list(sys.stdin.readline().strip())))

if N[0] == 0:
    print(0)

else:
    dp = [[0, 0] for _ in range(len(N))] # 한자릿수, 두자릿수
    dp[0][0] += 1
    prev = [N[0]]
    for i in range(1, len(N)):
        if not prev:
            break
        tmp_prev = set()
        for num in prev:
            if num < 10:
                if num * 10 + N[i] <= 26:
                    dp[i][1] += dp[i - 1][0]
                    tmp_prev.add(num * 10 + N[i])
                if N[i] != 0:
                    dp[i][0] += dp[i - 1][0]
                    tmp_prev.add(N[i])
            else:
                if N[i] != 0:
                    dp[i][0] += dp[i - 1][1]
                    tmp_prev.add(N[i])
        prev = sorted(list(tmp_prev))

    print(sum(dp[-1]) % 1000000)