'''
dp!!!
n번째 삼각형에서 마름모꼴 뭐시기 될 경우
dp[0] = 1
dp[1] = 3 if top[0] == 0 else 4 -> 1
dp[2] = (dp[1] - dp[0]) * 4(or 3) + dp[0] * 3(or 2)
dp[3] = (dp[2] - dp[1]) * 4(or 3) + dp[1] * 3(or 2)
'''
def solution(n, tops):
    
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 3 if tops[0] == 0 else 4
    for i in range(2, n + 1):
        if tops[i - 1] == 1: # 뿔이 있는 경우
            dp[i] = (dp[i - 1] - dp[i - 2]) * 4 + dp[i - 2] * 3
        else:
            dp[i] = (dp[i - 1] - dp[i - 2]) * 3 + dp[i - 2] * 2
    
    return dp[-1] % 10007