from itertools import combinations

def solution(numbers, target):
    result = 0
    numbers = sorted(numbers)
    graph = []
    for i in range(len(numbers) + 1):
        graph.append(list(combinations(numbers, i)))
    
    total = sum(numbers)
    for num in graph:
        for i in range(len(num)):
            minus = sum(num[i])
            if total - (2 * minus) == target:
                result += 1
                
    return result