import sys

N = int(sys.stdin.readline())
potion = list(map(int,sys.stdin.readline().split()))
potion.append(0)
potion.sort()
if potion[0] >= 0: # 모두 산성
    print(potion[1], potion[2])
elif potion[-1] <= 0: # 모두 알칼리성
    print(potion[-3], potion[-2])
else:
    potion.remove(0)
    alkali = 0
    acid = N - 1
    ans = [potion[alkali], potion[acid]]
    while acid > alkali:
        sum_tmp = potion[alkali] + potion[acid]
        if sum_tmp == 0:
            ans = [potion[alkali], potion[acid]]
            break
        if abs(sum(ans)) > abs(sum_tmp):
            ans = [potion[alkali], potion[acid]]
        if sum_tmp < 0:
            alkali += 1
        else:
            acid -= 1
    print(ans[0], ans[1])