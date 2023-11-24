from collections import deque

def solution(queue1, queue2):
    
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    if (sum1 + sum2) % 2 != 0:
        return -1
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    origin1 = deque(queue1)
    origin2 = deque(queue2)
    limit = len(queue1) * 4
    answer = 0
    
    while sum1 != sum2:
        if sum1 > sum2:
            num = q1.popleft()
            sum1 -= num
            sum2 += num
            q2.append(num)
        else:
            num = q2.popleft()
            sum1 += num
            sum2 -= num
            q1.append(num)
        answer += 1
        
        if answer == limit:
            return -1
    
    return answer