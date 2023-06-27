'''
1. 스택에 새로 들어오는 수가 top에 존재하는 수보다 크면 그 수는 오큰수가 된다.
2. 오큰수를 구한 후 수열에서 오큰수가 존재하지 않는 숫아에 -1을 출력한다.
'''

import sys

input = sys.stdin.readline

A = int(input())
N = list(map(int, input().split()))
NGE = [-1 for _ in range(A)]
stack = []

for i in range(A):
    while stack and N[i] > N[stack[-1]]:
        top = stack.pop()
        NGE[top] = N[i]
    stack.append(i)

for i in NGE:
    print(i, end = " ")