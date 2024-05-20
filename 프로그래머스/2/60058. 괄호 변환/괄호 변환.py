'''
# 과정 4
new_u = ''
for i in range(1, len(u) - 1):
    if u[i] == (:
        new_u += ')'
    else:
        new_u += '('

( + v + ) + new_u
'''

from collections import deque

def isValid(p): # 올바른 괄호 문자열인지 확인하는 함수
    stack = []
    for c in p:
        if c == '(':
            stack.append(c)
        elif c == ')' and stack:
            stack.pop()
        else:
            return False
        
    if stack:
        return False
    else:
        return True
            
def correct(p): # 재귀함수
    u = ''
    queue = deque(p)
    while queue:
        u += queue.popleft()
        while u.count('(') != u.count(')'):
            u += queue.popleft()
        if isValid(u):
            return u + correct(''.join(queue))
        else:
            new_u = ''
            for i in range(1, len(u) - 1):
                if u[i] == '(':
                    new_u += ')'
                else:
                    new_u += '('
            return '(' + correct(''.join(queue)) + ')' + new_u
    return ''
    
def solution(p):
    
    if isValid(p):
        return p
            
    return correct(p)