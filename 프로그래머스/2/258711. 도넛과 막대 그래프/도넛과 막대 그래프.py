'''
도넛 모양: n개의 정점, n개의 간선
막대 모양: n개의 정점, n-1개의 간선
8자 모양: 2n+1개의 정점, 2n+2개의 간선

정점이 되는 조건
1. 자신을 향하는 간선이 없을 것
2. 자신에게서 시작하는 간선이 2개 이상일 것

bfs 사용해서 그래프 모양 찾기 !
'''

from collections import deque

def bfs(vertex, start, graph):
    visited = set([start])
    edge_cnt = 0
    q = deque([start])
    while q:
        node = q.popleft()
        if node in graph:
            for new_node in graph[node]:
                edge_cnt += 1
                if new_node not in visited:
                    visited.add(new_node)
                    q.append(new_node)
            
    return (len(visited), edge_cnt)

def solution(edges):
    answer = [0, 0, 0, 0]
    
    edge = dict()
    re_edge = dict()
    vertexes = set()
    for a, b in edges:
        if a in edge:
            edge[a].append(b)
        else:
            edge[a] = [b]
            
        if b in re_edge:
            re_edge[b].append(a)
        else:
            re_edge[b] = [a]
        vertexes.add(a)
        vertexes.add(b)
    
    for i in vertexes:
        if i in edge and len(edge[i]) > 1 and i not in re_edge:
            answer[0] = i
            break
            
    for start in edge[answer[0]]:
        v, e = bfs(answer[0], start, edge)
        if v == e:
            answer[1] += 1
        elif v > e:
            answer[2] += 1
        else:
            answer[3] += 1
    
    return answer