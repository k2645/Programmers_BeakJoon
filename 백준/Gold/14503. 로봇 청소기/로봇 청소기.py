import sys

N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())

room = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def NearCheck(r, c):
    near = [False, False, False, False]
    if 0 <= r - 1 and room[r - 1][c] == 0: # 북 check
        near[0] = True
    if c + 1 < M and room[r][c + 1] == 0: # 동 check
        near[1] = True
    if r + 1 < N and room[r + 1][c] == 0: # 남 check
        near[2] = True
    if 0 <= c - 1 and room[r][c - 1] == 0: # 서 check
        near[3] = True
    return near

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
x, y = r, c
ans = 0
while True:
    if room[x][y] == 0:
        room[x][y] = -1
        ans += 1
    near = NearCheck(x, y)
    if all(not n for n in near):
        dx, dy = directions[d]
        nx = x - dx
        ny = y - dy
        if 0 <= nx < N and 0 <= ny < M and room[nx][ny] != 1:
            x, y = nx, ny
            continue
        else:
            break
    else:
        d = (d - 1) % 4
        while not near[d]:
            d = (d - 1) % 4
        x += directions[d][0]
        y += directions[d][1]
        
print(ans)