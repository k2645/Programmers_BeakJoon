def solution(food):
    answer = []
    flag = 0
    for i in range(1, len(food)):
        cnt = int(food[i] / 2)
        for j in range(cnt * 2):
            answer.insert(flag, i)
        flag += cnt
        
    answer.insert(flag, 0)    
        
    return "".join(map(str, answer))