import sys

N, d, k, c = map(int, sys.stdin.readline().split())
belt = [int(sys.stdin.readline()) for _ in range(N)]

sushi = [0] * (d + 1) # 스시 종류별 개수
sushi[c] = 1
cnt = 1 # 쿠폰때문에 기본 1개임
for i in belt[:k]: # 처음 0 - k개 스시 종류 세기
    if sushi[i] == 0:
        cnt += 1 # 종류 개수 세기
    sushi[i] += 1

max_count = cnt
for i in range(N):
    left, right = belt[i], belt[(i + k) % N] # 왼쪽꺼 뺴고, 오른쪽꺼 더하면서 포인터 이동
    if left != right:
        sushi[left] -= 1
        sushi[right] += 1
        if sushi[left] == 0:
            cnt -= 1
        if sushi[right] == 1:
            cnt += 1
        max_count = max(max_count, cnt)
    if max_count == k + 1:
        break

print(max_count)