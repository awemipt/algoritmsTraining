with open('input.txt') as file:
    N, M = map(int, file.readline().split())
    data = file.read()

table = []
for row in data.split('\n'):
    tmp = list(map(int, row.split()))
    table.append(tmp)

dp = [[0]*M for _ in range(N)]
dp[0][0] = table[0][0]
for i in range(1, M):
    dp[0][i] = dp[0][i-1] + table[0][i]

for i in range(1, N):
    dp[i][0] = dp[i-1][0] + table[i][0]
for i in range(1, N):
    for j in range(1, M):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + table[i][j]


i = N -1
j = M - 1
ans = []
while i > 0 or j > 0:
    if i == 0 or j == 0:
        break
    if dp[i-1][j] > dp[i][j-1]:
        ans.append('D')
        i -= 1
    else:
        j -= 1
        ans.append('R')
while i > 0:
    ans.append('D')
    i -= 1
while j > 0:
    ans.append('R')
    j-=1
print(dp[-1][-1])
print(*reversed(ans))