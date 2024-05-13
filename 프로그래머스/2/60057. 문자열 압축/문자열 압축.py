'''
1개부터 차례로 잘라서 가장 작은 값 도출하기.
n개 단위로 자를때 나올 수 있는 가장 작은 길이는?
(len(s) // n) // 10 + n + len(s) % n

'''

def solution(s):
    answer = len(s)
    
    for n in range(1, 1 + len(s)):
        if answer < len(str(len(s) // n)) + n + (len(s) % n):
            continue
        
        compare = s[0:n]
        string = compare
        cnt = 1
        for i in range(n, len(s), n):
            new_str = s[i:i + n] if i + n <= len(s) else s[i:]
            if new_str == compare:
                cnt += 1
            else:
                if cnt > 1:
                    string += str(cnt)
                compare = new_str
                string += compare
                cnt = 1
        if cnt > 1:
            string += str(cnt)
        
        answer = min(answer, len(string))
        
    return answer