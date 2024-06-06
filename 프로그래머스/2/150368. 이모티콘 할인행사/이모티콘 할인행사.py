'''
할인율 40, 30, 20, 10
users = 사용자 구매 기준
emoticons = 이모티콘 정가
할인율 40 -> users[0] 40 이하 (전부 해당)
할인율 30 -> users[0] 30 이하
할인율 20 -> users[0] 20 이하
할인율 10 -> users[0] 10 이하
이모티콘 할인율 ....어떻게 돌 것인가...최대 4^7...
'''

# emoticon_sale: [10% 이상 세일 가격, 20% 이상, 30% 이상, 40% 이상]
def back(emoticon_sale, n, m, answer, user_dict, emoticons):
    if n == m:
        plus_cnt = 0
        total_price = 0
        for x in user_dict.keys():
            price = emoticon_sale[(x // 10) - 1]
            emoticon_plus = len(list(filter(lambda x: x <= price, user_dict[x])))
            total_price += (len(user_dict[x]) - emoticon_plus) * price
            plus_cnt += emoticon_plus
        answer.append([plus_cnt, total_price])      
        return
    
    for x in range(4):
        price = [emoticons[n] * (6 + x) // 10] * (4 - x) + [0] * x
        emoticon_sale = [x + y for x, y in zip(emoticon_sale, price)]
        back(emoticon_sale, n + 1, m, answer, user_dict, emoticons)
        emoticon_sale = [x - y for x, y in zip(emoticon_sale, price)]

def solution(users, emoticons):

    user_dict = {x * 10: [] for x in range(1, 5)}
    for user in users:
        if user[0] <= 10:
            user_dict[10].append(user[1])
        elif user[0] <= 20:
            user_dict[20].append(user[1])
        elif user[0] <= 30:
            user_dict[30].append(user[1])
        else:
            user_dict[40].append(user[1])
    
    emoticons.sort(reverse=True)
    answer = []
    back([0, 0, 0, 0], 0, len(emoticons), answer, user_dict, emoticons)
    answer.sort(key=lambda x: (-x[0], -x[1]))
    return answer[0]