def solution(t, p):
    answer = 0
    length_p = len(p)
    length_t = len(t)
    list_t = list(t)

    for i in range(length_t - length_p + 1):
        num = int("".join(list_t[i:i+length_p]))
        if num <= int(p):
            answer += 1

    return answer