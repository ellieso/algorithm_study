# 조건
# 1. 계단을 오를때는 1칸 또는 2칸까지 한번에 오를수있다.
# 2. 연속된 3칸은 오를 수 없다.
# 3. 마지막 계단은 무조건 밟아야한다.

# n 번째 계단에 올라오기 위해서는 두 가지 경우가 있습니다. n-1번째 계단으로 오는 경우와 n-2번째 계단으로 오는 경우입니다.
# 1.n-1번째 계단으로 오는 경우에는
# dp[n] = dp[n-3] + stairs[n-1] + stairs[n] 입니다
# 2.n-2번째 계단으로 오는 경우에는
# dp[n] = dp[n-2] + stairs[n] 입니다
# 이 중에서 더 큰 수가 dp[n]이 됩니다.

import sys

input = sys.stdin.readline

n = int(input())

# 계단의 숫자를 초기화 합니다. 1층은 1번째(not 0번째) 인덱스에 저장합니다.
stairs = [0] * 301
for i in range(1, n + 1):
    stairs[i] = int(input())

# dp 배열을 초기화합니다.
dp = [0] * 301
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

# 점화식을 계산합니다.
for i in range(4, n + 1):
    dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])

print(dp[n])