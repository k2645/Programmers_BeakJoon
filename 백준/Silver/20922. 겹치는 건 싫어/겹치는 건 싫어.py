import sys

N, K = map(int, sys.stdin.readline().split())
sequence = list(map(int, sys.stdin.readline().split()))
numbers = dict()

left = 0
max_length = 0
for right in range(N):
    if sequence[right] in numbers:
        numbers[sequence[right]] += 1
    else:
        numbers[sequence[right]] = 1
    while numbers[sequence[right]] > K and left < right:
        numbers[sequence[left]] -= 1
        left += 1
    max_length = max(right - left + 1, max_length)

print(max_length)