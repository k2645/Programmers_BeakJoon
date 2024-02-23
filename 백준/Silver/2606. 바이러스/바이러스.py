import sys
from collections import deque

def virusComputerCount(networkGraph, visitedComputer):
    computerQueue = deque([0])
    visitedComputer[0] = True
    virusComputerNum = 0
    while computerQueue:
        nowComputer = computerQueue.popleft()
        for computer in networkGraph[nowComputer]:
            if visitedComputer[computer] == False:
                computerQueue.append(computer)
                visitedComputer[computer] = True
                virusComputerNum += 1
    return virusComputerNum

computerNum = int(sys.stdin.readline())
networkNum = int(sys.stdin.readline())
network = [list(map(int, sys.stdin.readline().split())) for _ in range(networkNum)]
networkGraph = {i: [] for i in range(computerNum)}
for computer in network:
    networkGraph[computer[0]-1].append(computer[1]-1)
    networkGraph[computer[1]-1].append(computer[0]-1)

print(virusComputerCount(networkGraph, [False] * computerNum))

