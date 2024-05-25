'''
완전탐색
1. 코스 개수에 해당하는 모든 조합을 돈다.
2. order별로 가능한 조합들을 돈다.
'''
from itertools import combinations

def solution(orders, course):
    orders = sorted(orders, key = lambda x: -len(x))
    answer = []
    for n in course:
        while orders and len(orders[-1]) < n:
            orders.pop()
        if len(orders) < 2:
            break
        combs = set()
        for order in orders:
            combs.update(set(map(lambda x: ''.join(sorted(list(x))), list(combinations(order, n)))))
        max_cnt = 0
        n_course = []
        for comb in combs:
            cnt = 0
            for order in orders:
                if set(order) & set(comb) == set(comb):
                    cnt += 1
            if cnt > 1 and cnt > max_cnt:
                max_cnt = cnt
                n_course = [''.join(sorted(list(comb)))]
            elif cnt > 1 and cnt == max_cnt:
                n_course.append(''.join(sorted(list(comb))))
        answer += n_course
    answer.sort()
    return answer