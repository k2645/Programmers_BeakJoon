import sys

'''
[승, 무, 패]
승, 무, 패끼리 묶기
승이 있는 만큼 다른 나라에서 -1씩
이떄 패가 많은 나라부터 순서대로 -1씩 하도록..

3 0 2 3 0 2 3 0 2 2 0 3 2 0 3 2 0 3
'''

def dfs(game):
    global win, draw, lose, match

    # 모든 게임을 다 확인했다면 결과 확인
    if game == 15:
        if win.count(0) == 6 and draw.count(0) == 6 and lose.count(0) == 6:
            return True
        else:
            return False

    # 팀 i와 팀 j가 경기를 치르는 경우
    i, j = match[game]

    # i가 이기고 j가 지는 경우
    win[i] -= 1
    lose[j] -= 1
    if win[i] >= 0 and lose[j] >= 0 and dfs(game + 1):
        return True
    win[i] += 1
    lose[j] += 1

    # 비기는 경우
    draw[i] -= 1
    draw[j] -= 1
    if draw[i] >= 0 and draw[j] >= 0 and dfs(game + 1):
        return True
    draw[i] += 1
    draw[j] += 1

    # i가 지고 j가 이기는 경우
    lose[i] -= 1
    win[j] -= 1
    if lose[i] >= 0 and win[j] >= 0 and dfs(game + 1):
        return True
    lose[i] += 1
    win[j] += 1

    # 모든 경우를 확인했으나 조건을 만족하는 경우를 찾지 못한 경우
    return False


ans = []
match = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]
for _ in range(4):
    game = list(map(int, sys.stdin.readline().split()))
    win = []
    draw = []
    lose = []
    for i in range(6):
        win.append(game[i * 3])
        draw.append(game[(i * 3) + 1])
        lose.append(game[(i * 3) + 2])
    if dfs(0):
        ans.append('1')
    else:
        ans.append('0')

print(' '.join(ans))