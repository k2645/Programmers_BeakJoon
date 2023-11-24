import heapq

def solution(n, paths, gates, summits):
    
    graph = {}
    
    set_gates = set(gates)
    set_summits = set(summits)
    
    for path in paths:
        if path[0] not in set_summits:
            if path[0] not in graph:
                graph[path[0]] = {}
            if path[1] not in set_gates:
                graph[path[0]][path[1]] = path[2]
        if path[1] not in set_summits:
            if path[1] not in graph:
                graph[path[1]] = {}
            if path[0] not in set_gates:
                graph[path[1]][path[0]] = path[2]
    
    intensities = {node: float("inf") for node in range(1, n + 1)}
    queue = []
    
    for gate in gates:
        intensities[gate] = 0
        heapq.heappush(queue, [intensities[gate], gate])
    
    while queue:
        now_intensity, now_location = heapq.heappop(queue)
        
        if now_location in set_summits or now_intensity > intensities[now_location]:
            continue
        
        for new_location, new_intensity in graph[now_location].items():
            intensity = max(new_intensity, intensities[now_location])
            if intensities[new_location] > intensity:
                intensities[new_location] = intensity
                heapq.heappush(queue, [intensity, new_location])
                # if new_location not in set_summits:
                #     heapq.heappush(queue, [intensity, new_location])
    
    answer = [1, 10000001]
    summits.sort()
    for summit in summits:
        if intensities[summit] < answer[1]:
            answer = [summit, intensities[summit]]
    
    return answer