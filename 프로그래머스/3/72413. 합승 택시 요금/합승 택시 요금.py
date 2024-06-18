'''
a, b, s, k(경유) 가 있다고 하자.
s -> k 최단 거리(k'), k -> a, k -> b 최단거리(각각 a', b')
k' + a' + b'의 최솟값을 구하자.
'''
import copy

def solution(n, s, a, b, fares):
    
    dist = [[10000000001] * (n + 1) for _ in range(n + 1)]
    for c, d, f in fares:
        dist[c][d] = f
        dist[d][c] = f
        
    for i in range(n + 1):
        dist[i][i] = 0
    
    for k in range(n + 1):
        for i in range(n + 1):
            for j in range(n + 1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    
    ans = float("inf")
    for k in range(n + 1):
        ans = min(ans, dist[s][k] + dist[k][a] + dist[k][b])
    
    return ans