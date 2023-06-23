'''
1. 합배열 만들기
2. 합배열을 m으로 나눈 나머지 값들의 배열로 업데이트
3. 업데이트된 합배열에서 같은값인 쌍 도출하기
combination 함수는 되도록 사용하지 않기 !! -> 시간복잡도 : n! / r! / (n - r)! (개커요..)
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

A = list(map(int, input().split()))
S = [0] * n
C = [0] * m
answer = 0

S[0] = A[0]
for i in range(1, n):
    S[i] = S[i - 1] + A[i]

for i in range(n):
    remainder = S[i] % m
    if remainder == 0:
        answer += 1
    C[remainder] += 1

for i in range(m):
    if C[i] != 0:
        answer += C[i] * (C[i] - 1) // 2

print(answer)