import sys

N, d, k, c = map(int, sys.stdin.readline().split())
rotate = [int(sys.stdin.readline()) for _ in range(N)]

max_count = 0
for i in range(N):
    if i + k <= N:
        sushi = rotate[i:i + k]
    else:
        sushi = rotate[i:N] + rotate[0:k - (N - i)]
    sushi.append(c)
    max_count = max(len(set(sushi)), max_count)
print(max_count)