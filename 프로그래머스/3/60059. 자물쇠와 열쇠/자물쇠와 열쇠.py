'''
lock 빈칸 모양이랑 일치하는 경우 파악
1. 빈칸을 포함하는 최대 사각형 파악 (예제의 경우 2X2)
2. 최대 사각형을 Key에서 90도씩 돌려가며 모든 경우 확인?

1. lock 빈칸의 모양 배열 만들기. (dfs로 첫 빈칸(아무거나 기준)어떻게 빈칸이 생성되었는지? ex. (0,0), (1, -1)) 이때, 어디가 뚫려있는지 어디가 막혀있는지 파악해야함
2. lock 배열 모양을 가지고 key의 칸들 돌기. (백트래킹)
'''
# 90도 돌리기(시계)
def rotate(N, key):
    rotate_key = set()
    for k in key:
        rotate_key.add((k[1], N - 1 - k[0]))
    return rotate_key

def solution(key, lock):
    
    M = len(key)
    N = len(lock)
    key_shape = set() # 키 모양 확인
    for i in range(M):
        for j in range(M):
            if key[i][j] == 1:
                key_shape.add((i, j))
    lock_shape = [] # 자물쇠 모양 확인
    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0:
                lock_shape.append((i, j))
    
    if not lock_shape:
        return True
    
    for _ in range(4):
        for k in key_shape:
            dx, dy = lock_shape[0][0] - k[0], lock_shape[0][1] - k[1]
            move_key = set(map(lambda x: (x[0] + dx, x[1] + dy), key_shape))
            if move_key & set(lock_shape) == set(lock_shape) and not any(list(map(lambda x: 0 <= x[0] < N and 0 <= x[1] < N, move_key - set(lock_shape)))):
                return True
        key_shape = rotate(N, key_shape)
    
    return False