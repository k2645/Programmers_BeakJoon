'''
combination 조합..
1개짜리 찾기 -> set으로 묶었을 떄 list의 길이와 동일하면 후보키
1개짜리 column 삭제
2개짜리 찾기
2개짜리 column 삭제
...
n번 반복
'''

from itertools import combinations

def isCandidateKey(relation, keys):
    values = []
    for v in relation:
        values.append(tuple([i for idx, i in enumerate(v) if idx in keys]))
    
    if len(values) == len(set(values)):
        return True
    else:
        return False

def solution(relation):
    answer = 0
    
    rows = len(relation)
    columns = [i for i in range(len(relation[0]))]
    keys = set()
    i = 1
    while True:
        for j in combinations(columns, i):
            if all(set(key) & set(j) != set(key) for key in keys) and isCandidateKey(relation, j):
                keys.add(j)
                answer += 1
        i += 1
        if i > len(columns):
            break
    
    return answer