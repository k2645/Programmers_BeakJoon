'''
DP? 수학
'''

def solution(n):
    ans = [[0] * i for i in range(1, n + 1)]
    dirc = [(1, 0), (0, 1), (-1, -1)]
    x, y = 0, 0
    t = 0
    num = 1
    while num <= (n * (n + 1)) // 2:
        ans[x][y] = num
        num += 1
        dx, dy = dirc[t]
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and ans[nx][ny] == 0:
            x, y = nx, ny
        else:
            t = (t + 1) % 3
            dx, dy = dirc[t]
            x, y = x + dx, y + dy
    
    return sum(ans, [])