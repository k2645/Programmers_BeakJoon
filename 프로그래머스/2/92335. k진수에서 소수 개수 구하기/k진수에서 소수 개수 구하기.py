import math

def changeDecimal(n, k):
    if k == 10:
        return str(n)
    
    num = []
    while n > 0:
        num.append(str(n % k))
        n = n // k
    num.reverse()
    return ''.join(num)

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
                
def solution(n, k):
    
    n_arr = changeDecimal(n, k).split('0')
    answer = 0
    for num in n_arr:
        if num and isPrime(int(num)):
            answer += 1
            
    return answer