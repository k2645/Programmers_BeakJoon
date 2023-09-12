def solution(n, m):
    answer = []
    if n <= m:
        answer.append(gcd(n, m))
        answer.append(lcm(n, m))
    else:
        answer.append(gcd(m, n))
        answer.append(lcm(m, n))
    return answer

def gcd(a, b):
    if b % a != 0:
        return gcd(b % a, a)
    return a

def lcm(a, b):
    return a * b // gcd(a, b)
    