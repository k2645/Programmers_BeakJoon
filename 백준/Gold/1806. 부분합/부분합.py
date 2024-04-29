import sys

'''
부분합 -> 투포인터?
1. left, right 0부터 시작

2. right 한칸씩 전진
3. S이상이 되면 S이상을 만족 할 때까지 left ++
5. 2번으로 돌아가기
'''

N, S = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

min_length = N + 1
left, right = 0, 0
num_sum = 0
while right < N and min_length > 1:
    num_sum += num_list[right]
    if num_sum >= S:
        while num_sum - num_list[left] >= S and left < right:
            num_sum -= num_list[left]
            left += 1
        min_length = min(right - left + 1, min_length)
    right += 1

if min_length == N + 1:
    print(0)
else:
    print(min_length)