with open('input.txt') as file:
    n, k = map(int, file.readline().split())

dp = [1]*k
for i in range(1,k):
    dp[i] = sum(dp[:i])

for i in range(k, n):
    dp.append(sum(dp[i-k:i]))
print(dp[n-1])