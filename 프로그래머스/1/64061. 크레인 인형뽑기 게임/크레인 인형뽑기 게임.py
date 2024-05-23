'''
인형을 담는 리스트 필요
moves를 돌면서 해당 column의 가장 위에 있는 숫자 (0이 아닌 아무 숫자) 리스트에 추가
'''

def solution(board, moves):
    
    column_location = [0] * len(board)
    for i in range(len(board)):
        for j in range(len(board)):
            if board[j][i] != 0:
                column_location[i] = j
                break
    
    doll_list = []
    answer = 0
    for move in moves:
        if column_location[move - 1] < len(board):
            doll = board[column_location[move - 1]][move - 1]
            board[column_location[move - 1]][move - 1] = 0
            column_location[move - 1] += 1
            if doll_list and doll_list[-1] == doll:
                doll_list.pop()
                answer += 2
            else:
                doll_list.append(doll)
        
    return answer