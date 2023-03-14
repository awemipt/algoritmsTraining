with open('input.txt') as file:
    N, M = map(int, file.readline().split())

di = [-1, -2]
dj = [-2, -1]

dp = [[0] * M for _ in range(N)]
dp[0][0] = 1
for i in range(N):
    for j in range(M):
        for p in range(2):
            if i + di[p] >= 0 and j + dj[p] >= 0:
                dp[i][j] += dp[i + di[p]][j + dj[p]]

print(dp[-1][-1])
