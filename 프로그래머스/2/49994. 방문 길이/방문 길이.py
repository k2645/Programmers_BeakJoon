def solution(dirs):
    answer = 0
    
    prev = [0, 0]
    char = [0, 0]
    loc = []
    
    for i in dirs:
        if i == 'U':
            if char[0] == 5:
                continue
            char[0] += 1
        elif i == 'D':
            if char[0] == -5:
                continue
            char[0] -= 1
        elif i == 'L':
            if char[1] == -5:
                continue
            char[1] -= 1
        elif i == 'R':
            if char[1] == 5:
                continue
            char[1] += 1
        
        
        if [tuple(prev), tuple(char)] not in loc and [tuple(char), tuple(prev)] not in loc:
            loc.append([tuple(prev), tuple(char)])
            answer += 1

        prev = char[:]
    
    return answer