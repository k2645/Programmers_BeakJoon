'''
시뮬. 구현.
'''

def solution(m, n, board):
    for i in range(m):
        board[i] = list(board[i])
    
    ans = 0
    while True:
        pang = []
        for i in range(m - 1): # 터질 퍼즐 중 첫 번째 위치 저장
            for j in range(n - 1):
                if board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1] and board[i][j] != 0:
                    pang.append((i, j))
        if not pang:
            break
        
        dirc = [(0, 0), (1, 0), (0, 1), (1, 1)]
        for x, y in pang: # 퍼즐 터트리기
            for dx, dy in dirc:
                if board[x + dx][y + dy] != 0:
                    board[x + dx][y + dy] = 0
                    ans += 1
        
        for j in range(n): # 퍼즐 아래로 내리기
            for i in range(m - 1, 0, -1):
                k = 1
                while board[i][j] == 0 and i - k >= 0:
                    board[i][j], board[i - k][j] = board[i - k][j], board[i][j]
                    k += 1
            
    return ans