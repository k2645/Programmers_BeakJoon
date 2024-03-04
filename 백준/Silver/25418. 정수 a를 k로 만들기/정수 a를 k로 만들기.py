import sys

A, K = map(int, sys.stdin.readline().split())
result = 0

while K != A:
    if K % 2 == 0 and K / 2 >= A:
        K = K / 2
    else:
        K -= 1
    result += 1

print(result)