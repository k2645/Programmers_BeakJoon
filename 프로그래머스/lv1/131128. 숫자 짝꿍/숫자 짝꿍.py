def solution(X, Y):
    result = []
    
    for i in range(9, -1, -1):
        result.extend([str(i) for k in range(min(X.count(str(i)), Y.count(str(i))))])
    
    if not result:
        result = "-1"
    else:
        if result[0] == "0":
            result = "0"
        else:
            result = "".join(result)
        
    return result