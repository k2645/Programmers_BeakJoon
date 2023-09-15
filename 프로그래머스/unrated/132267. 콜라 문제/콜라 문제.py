def solution(a, b, n):
    answer = 0
    num = n
    while num >= a:
        q, r = divmod(num, a)
        answer += q * b
        num = q * b + r
        
    return answer