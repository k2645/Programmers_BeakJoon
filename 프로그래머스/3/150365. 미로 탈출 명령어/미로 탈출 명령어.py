'''
알파벳 순서: d l r u
'''
import sys
sys.setrecursionlimit(5000)

def isImpossible(start, end, k): # k: 움직일 수 있는 거리
    move = k - abs(start[0] - end[0]) - abs(start[1] - end[1])
    if move % 2 != 0 or move < 0:
        return True
    else:
        return False

def back(now, end, string, k, str_arr, n, m):
    if k == 0:
        if str_arr and string < str_arr[0]:
            str_arr.pop()
            str_arr.append(string)
        elif not str_arr:
            str_arr.append(string)
        return
    directions = [(1, 0), (0, -1), (0, 1), (-1, 0)]
    char = ['d', 'l', 'r', 'u']
    x, y = now
    for i, dirc in enumerate(directions):
        nx, ny = x + dirc[0], y + dirc[1]
        if 0 < nx <= n and 0 < ny <= m and not isImpossible((nx, ny), end, k - 1):
            back((nx, ny), end, string + char[i], k - 1, str_arr, n, m)
            break
    

def solution(n, m, x, y, r, c, k):
    if isImpossible((x, y), (r, c), k):
        return "impossible"
    
    ans_arr = []
    back((x, y), (r, c), "", k, ans_arr, n, m)

    return ans_arr[0]