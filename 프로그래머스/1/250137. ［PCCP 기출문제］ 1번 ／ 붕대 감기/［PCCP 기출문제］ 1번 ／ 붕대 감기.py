def solution(bandage, health, attacks):
    
    t, x, y = bandage
    answer = health
    last_time = 0
    for attack in attacks:
        time, damage = attack
        bandage_time = (time - 1) - last_time
        heal = x * bandage_time + y * (bandage_time // t)
        if answer + heal > health:
            answer = health
        else:
            answer += heal
        answer -= damage
        last_time = time
        if answer <= 0:
            answer = -1
            break
        
    return answer