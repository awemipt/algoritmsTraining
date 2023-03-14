with open('input.txt') as file:
    N = int(file.readline())
    data = list(map(int, file.readline().split()))

data.sort()
dp = [0] * N
dp[1] = data[1] - data[0]
if N > 2:
    dp[2] = dp[1] + data[2] - data[1]
for i in range(3, N):
    dp[i] = min(dp[i-1], dp[i-2]) + data[i] - data[i-1]
# print(dp)
print(dp[N-1])