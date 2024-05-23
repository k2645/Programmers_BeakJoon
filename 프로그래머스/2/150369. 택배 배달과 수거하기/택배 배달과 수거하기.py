'''
배달 / 수거
가장 먼 거리부터 배달 및 수거를 모두 마치는 것이 좋다.
우선순위
가장 먼 거리의 배달, 가장 먼 거리의 수거

'''

def solution(cap, n, deliveries, pickups):
    
    while deliveries and deliveries[-1] == 0:
        deliveries.pop()
    
    while pickups and pickups[-1] == 0:
        pickups.pop()
    
    ans = 0
    while deliveries or pickups:
        ans += max(len(deliveries), len(pickups))
        delivery = 0
        while delivery <= cap and deliveries:
            delivery += deliveries.pop()
        if delivery > cap:
            deliveries.append(delivery - cap)
        pick = 0
        while pick <= cap and pickups:
            pick += pickups.pop()
        if pick > cap:
            pickups.append(pick - cap)
            
    return ans * 2