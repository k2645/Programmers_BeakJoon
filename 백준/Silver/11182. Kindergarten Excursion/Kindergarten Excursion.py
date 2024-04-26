import sys

'''
자신보다 앞에 있는 숫자 중 자기보다 큰 값 의 갯수 함
'''

children = list(map(int, list(sys.stdin.readline().strip())))
lake_cnt = 0
science_cnt = 0
ans = 0
for i in range(len(children)):
    if children[i] == 0:
        ans += lake_cnt + science_cnt
    elif children[i] == 1:
        ans += science_cnt
        lake_cnt += 1
    else:
        science_cnt += 1
print(ans)