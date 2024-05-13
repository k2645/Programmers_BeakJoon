'''
enter, leave, change 
user id
nickname

key: user id 와 value: nickname 딕셔너리로 묶기
enter, leave 를 담을 list만들기
'''

def solution(record):
    
    user_nickname = dict()
    enter_leave = []
    for r in record:
        r = r.split()
        if r[0] == 'Leave':
            enter_leave.append((0, r[1]))
        elif r[0] == 'Enter':
            user_nickname[r[1]] = r[2]
            enter_leave.append((1, r[1]))
        else:
            user_nickname[r[1]] = r[2]
    
    answer = []
    for el in enter_leave:
        t, uid = el
        if t == 0:
            answer.append("%s님이 나갔습니다." %(user_nickname[uid]))
        else:
            answer.append("%s님이 들어왔습니다." %(user_nickname[uid]))
    
    return answer