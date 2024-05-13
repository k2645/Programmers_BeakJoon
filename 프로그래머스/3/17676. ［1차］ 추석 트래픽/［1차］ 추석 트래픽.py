'''
초당 최대 처리량
끝난 시간 기점으로 오름차순
걸린 시간 S
'''
from collections import deque

def solution(lines):
    answer = 1
    times = deque()
    for t in lines:
        t = t.split()
        S, T = list(map(float, t[1].split(':'))), float(t[2].strip('s'))
        S = int((S[0] * 3600 * 1000) + (S[1] * 60 * 1000) + (S[2] * 1000))
        T = int(T * 1000)
        S_start = S - T + 1 if S - T + 1 >= 0 else 0
        times.append((S_start, S))
    print(times)
    
    while times:
        t = times.popleft()
        s, e = t[0], t[1]
        answer = max(answer, sum(x[0] < e + 1000 for x in times) + 1)
    
    return answer