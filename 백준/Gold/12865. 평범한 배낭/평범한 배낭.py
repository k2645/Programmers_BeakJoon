import sys

N, K = map(int, sys.stdin.readline().split())
objects = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = {0: 0}
for i in range(N):
    new_w, new_v = objects[i]
    temp = {}
    for acc_w, acc_v in dp.items():
        if acc_w + new_w <= K and acc_v + new_v > dp.get(acc_w + new_w, 0):
            temp[acc_w + new_w] = acc_v + new_v
    dp.update(temp)

print(max(dp.values()))
