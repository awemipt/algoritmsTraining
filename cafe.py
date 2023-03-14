from math import inf

with open('input.txt') as file:
    N = int(file.readline())
    prices = [int(file.readline()) for _ in range(N)]
dp = [[0] * (N) for _ in range(N + 1)]
dp[0] = [0] + [inf] * (N - 1)

for i in range(1, N + 1):
    for j in range(N):
        if prices[i - 1] > 100:
            tmp = dp[i - 1][j - 1] + prices[i - 1]
        else:
            tmp = dp[i - 1][j] + prices[i - 1]
        if j + 1 < N:
            dp[i][j] = min(dp[i - 1][j + 1], tmp)
        else:
            dp[i][j] = tmp

m = inf
lasts_coupons = 0
max_coupons = -1
for row in dp:
    print(*row)
for i, x in enumerate(dp[-1]):

    if x <= m:
        m = x
        lasts_coupons = i
    if x != inf:
        max_coupons += 1

i = N
j = lasts_coupons

days = []
if i == 1:
    if dp[1][0] > 100:
        lasts_coupons += 1
else:
    while i > 0:
        if j + 1 < N and dp[i][j] == dp[i - 1][j + 1]:
            days.append(i)
            i -= 1
            j += 1
        elif prices[i - 1] > 100:
            j -= 1
            i -= 1
        else:
            i -= 1
print(m)
print(lasts_coupons, len(days))
for day in reversed(days):
    print(day)
