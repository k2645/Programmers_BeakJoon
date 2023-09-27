def solution(num, total):
    
    n = (total - sum(range(num))) / num
    
    return [i + n for i in range(num)]