import sys
from collections import deque

def checkWins(array, start):
    for dx, dy in directions:
        queue = deque([array[start]])
        minimum = array[start]
        count = 1
        while queue:
            x, y = queue.popleft()
            nx, ny = x + dx, y + dy
            if (nx, ny) in array:
                queue.append((nx, ny))
                count += 1
            else:
                break
        queue.append(array[start])
        while queue:
            x, y = queue.popleft()
            nx, ny = x - dx, y - dy
            if (nx, ny) in array:
                minimum = (nx, ny)
                queue.append((nx, ny))
                count += 1
            else:
                break
        if count == 5:
            return minimum
    return (0, 0)

black = []
white = []
for i in range(1, 20):
    l = [0]
    l += (list(map(int, sys.stdin.readline().split())))
    black += list(map(lambda x: (i, x), list(filter(lambda x: l[x] == 1, range(1, 20)))))
    white += list(map(lambda x: (i, x), list(filter(lambda x: l[x] == 2, range(1, 20)))))

directions = [(-1, 1), (0, 1), (1, 1), (1, 0)]
blackResult = (0, 0)
whiteResult = (0, 0)
for i in range(len(black)):
    blackResult = checkWins(black, i)
    if blackResult != (0, 0):
        print("1")
        print("%d %d" % (blackResult[0], blackResult[1]))
        break

if blackResult == (0, 0):
    for i in range(len(white)):
        whiteResult = checkWins(white, i)
        if whiteResult != (0, 0):
            print("2")
            print("%d %d" % (whiteResult[0], whiteResult[1]))
            break

if blackResult == (0, 0) and whiteResult == (0, 0):
    print("0")