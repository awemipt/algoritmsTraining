import math
from math import inf
with open('input.txt') as file:
    N, M = map(int, file.readline().split())
    data = file.read()

table = []
for row in data.split('\n'):
    tmp = list(map(int, row.split()))
    table.append(tmp)
dp = [[0]*(M) for _ in range(N+1)]
di = [0, -1]
dj = [-1, 0]
dp[0][0] = table[0][0]
for i in range(N):
    for j in range(M):
        a = []
        if i == 0 and j > 0:
            dp[i][j] = dp[i][j-1] + table[i][j]
        elif j ==0:
            dp[i][j] = dp[i-1][j] + table[i][j]
        else:
            for p in range(2):
                a.append(dp[i+di[p]][j+dj[p]])

            dp[i][j] = min(a)+table[i][j]

print(dp[N-1][M-1])
