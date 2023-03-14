with open('input.txt') as file:
    N = int(file.readline())

dp = [0] * 3
dp[0] = 2
dp[1] = 4
dp[2] = 7
for i in range(3, N):
    dp.append(dp[i-1] + dp[i-2] + dp[i-3])
print(dp[N-1])
