'''
투입할 친구 순서 + 수, 점검 시작 위치 정하기

투입할 친구를 거리가 가장 먼 친구들 i명 뽑아 순열 만들기
ex) 친구 = [1,2,3,4]일 때, 1명 탐색의 경우 [4]로 해결이 되지 않는다면 [1],[2],[3] 모두 해결 불가능

i번 친구 투입
    남아있는 지점 중 첫 번째 지점 ~ 첫 번째 지점 + 친구 이동거리
    위 범위에 있는 취약 지점은 i번 친구가 해결
'''

from itertools import permutations

def solution(n, weak, dist):
    dist.sort(reverse=True) # 멀리갈 수 있는 친구 순서대로 정렬
    weak_num = len(weak)
    weak += [w + n for w in weak] # 취약 지점 일자로 펴기
    for i in range(1, len(dist) + 1):
        for perm in permutations(dist[:i]):
            for idx in range(weak_num): # idx는 점검 시작점
                friends = list(perm[:]) # i명 친구들 순열
                new_weak = weak[idx:idx + weak_num] # idx번째 부터 idx + len(weak)번째 까지 취약지점 리스트
                while friends and new_weak:
                    f = friends.pop(0)
                    w = new_weak.pop(0)
                    current = f + w # 취약지점 시작점 부터 친구가 움직일 수 있는 최대 거리
                    while new_weak and new_weak[0] <= current:
                        new_weak.pop(0)
                if len(new_weak) == 0: # 취약지점이 모두 사라지면 바로 i리턴
                    return i
    return -1