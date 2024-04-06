import sys

N = int(sys.stdin.readline())

min_dp = list(map(int, sys.stdin.readline().split()))
max_dp = min_dp.copy()

for i in range(N - 1):
    new_list = list(map(int, sys.stdin.readline().split()))
    temp_min = min_dp.copy()
    temp_max = max_dp.copy()
    for j in range(3):
        if j == 0:
            min_dp[j] = min(temp_min[j], temp_min[j + 1]) + new_list[j]
            max_dp[j] = max(temp_max[j], temp_max[j + 1]) + new_list[j]
        elif j == 1:
            min_dp[j] = min(temp_min) + new_list[j]
            max_dp[j] = max(temp_max) + new_list[j]
        elif j == 2:
            min_dp[j] = min(temp_min[j], temp_min[j - 1]) + new_list[j]
            max_dp[j] = max(temp_max[j], temp_max[j - 1]) + new_list[j]

print(max(max_dp), end = ' ')
print(min(min_dp))