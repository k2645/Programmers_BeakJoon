'''
1. 삽입 정렬(insertion sort) 사용
'''
import sys

input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
sorted_list = []
answer = 0

for idx, i in enumerate(P):
    if idx == 0:
        sorted_list.append(i)
    else:
        if sorted_list[-1] <= i:
            sorted_list.append(i)
        else:
            for index, j in enumerate(sorted_list):
                if i <= j:
                    sorted_list.insert(index, i)
                    break

for i in range(len(sorted_list)):
    answer += sorted_list[i] * (N - i)

print(answer)