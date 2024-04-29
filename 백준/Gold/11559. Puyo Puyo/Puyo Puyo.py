import sys

'''
Color chart: R, G, B, P, Y
dfs 사용해서 상하좌우 붙어있는 같은 color 블록 세트 찾기. (이때, 블록세트 모두 찾아야함.)
찾은 블록들 .으로 바꿈
맨 아래줄부터 차례대로 아래로 내리기
'''

puyo = [list(sys.stdin.readline().strip()) for _ in range(12)]
puyos = [] # 뿌요가 있는 모튼 위치

for i in range(12):
    for j in range(6):
        if puyo[i][j] != '.':
            puyos.append((i, j))
def dfs(block, visited, type):
    global puyo

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    x, y = block
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 12 and 0 <= ny < 6 and (nx, ny) not in visited and puyo[nx][ny] == type:
            visited.append((nx, ny))
            dfs((nx, ny), visited, type)

    return visited

ans = 0
while True:
    # 뿌요 없애기
    visited = []
    removed_puyos = []
    for p in puyos:
        if p not in visited:
            v = dfs((p[0],p[1]), [(p[0],p[1])], puyo[p[0]][p[1]])
            visited += v
            if len(v) >= 4:
                removed_puyos += v
                for vx, vy in v:
                    puyo[vx][vy] = '.'
    if not removed_puyos: # 더이상 없앨 뿌요가 없으면 탈출
        break
    else:
        ans += 1
        puyos = list(set(puyos) - set(removed_puyos))

    # 뿌요 내리기
    for j in range(6):
        for i in range(10, -1, -1):
            if (i, j) in puyos:
                puyos.remove((i, j))
                while i < 11 and puyo[i + 1][j] == '.':
                    puyo[i][j], puyo[i + 1][j] = puyo[i + 1][j], puyo[i][j]
                    i += 1
                puyos.append((i, j))

print(ans)