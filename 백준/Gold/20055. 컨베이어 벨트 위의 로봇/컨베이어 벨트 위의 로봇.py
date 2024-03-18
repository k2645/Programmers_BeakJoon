import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
durabilities = deque(list(map(int, sys.stdin.readline().split())))
robots = deque([False] * N)
stage = 0
robotNum = 0
while durabilities.count(0) < K:
    stage += 1
    durabilities.rotate(1)
    robots.rotate(1)
    if robots[N - 1] == True:
        robots[N - 1] = False
    for i in range(N - 2, -1, -1):
        if robots[i] == True and robots[i + 1] == False and durabilities[i + 1] > 0:
            robots[i] = False
            if i + 1 != N - 1:
                robots[i + 1] = True
            durabilities[i + 1] -= 1
    if durabilities[0] != 0:
        robots[0] = True
        durabilities[0] -= 1

print(stage)