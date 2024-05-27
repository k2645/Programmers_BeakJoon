'''
한 줄에 한 개씩 존재해야 한다.
한 열에 한 개씩 존재해야 한다.
어떤 조건이 더 붙어야할까... 대각선 상에 존재하면 안된다.
N//2 까지 돌리고 X2 해주기
'''

import sys
import math

def Nqueen(r, queens, col, up_diagonal, down_diagonal):
    global ans
    if len(queens) == N:
        ans += 1
        return

    for i in range(N):
        if not col[i] and not up_diagonal[r + i] and not down_diagonal[N - 1 - r + i]:
            queens.append((r, i))
            col[i] = True
            up_diagonal[r + i] = True
            down_diagonal[N - 1 - r + i] = True
            Nqueen(r + 1, queens, col, up_diagonal, down_diagonal)
            col[i] = False
            up_diagonal[r + i] = False
            down_diagonal[N - 1 - r + i] = False
            queens.remove((r, i))

N = int(sys.stdin.readline())
ans = 0
col = [False for _ in range(N)]
up_diagonal = [False for _ in range(2 * N)]
down_diagonal = [False for _ in range(2 * N)]
Nqueen(0, [], col, up_diagonal, down_diagonal)

print(ans)