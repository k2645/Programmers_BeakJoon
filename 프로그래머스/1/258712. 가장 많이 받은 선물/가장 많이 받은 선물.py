'''
선물은 많이 받은 애 -> 적게 받은 애 한테 준다.
선물지수 = 이번 달 준 선물 수 - 받은 선물 수

이차원 배열 주고받은 선물
선물 지수 표

Friends별 index
'''

def solution(friends, gifts):
    friends = {name: idx for idx, name in enumerate(friends)}
    gift_num = {i: 0 for i in range(len(friends))}
    give_and_take = [[0] * len(friends) for _ in range(len(friends))]
    
    for gift in gifts:
        give, take = map(lambda x: friends[x], gift.split())
        gift_num[give] += 1
        gift_num[take] -= 1
        give_and_take[give][take] += 1

    # 사람 별 선물 받는 개수 count
    gift_list = [0] * len(friends)
    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            if give_and_take[i][j] > give_and_take[j][i]:
                gift_list[i] += 1
            elif give_and_take[i][j] < give_and_take[j][i]:
                gift_list[j] += 1
            else:
                if gift_num[i] > gift_num[j]:
                    gift_list[i] += 1
                elif gift_num[i] < gift_num[j]:
                    gift_list[j] += 1
        
    return max(gift_list)