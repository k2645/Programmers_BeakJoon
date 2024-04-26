import sys

N = int(sys.stdin.readline())
egg = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def back(depth, broken):
    global max_egg
    if depth == N:
        max_egg = max(max_egg, len(broken))
        return
    if egg[depth][0] <= 0 or len(broken) == N - 1:
        back(depth + 1, broken)
        return
    for i in range(N):
        if egg[i][0] > 0 and i != depth:
            tmp = broken.copy()
            egg[depth][0] -= egg[i][1]
            egg[i][0] -= egg[depth][1]
            if egg[depth][0] <= 0:
                tmp.add(depth)
            if egg[i][0] <= 0:
                tmp.add(i)
            back(depth + 1, tmp)
            egg[depth][0] += egg[i][1]
            egg[i][0] += egg[depth][1]

max_egg = 0
back(0, set())

print(max_egg)