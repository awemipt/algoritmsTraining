with open('input.txt')  as file:
    N = int(file.readline())
    sequence1 = list(map(int, file.readline().split()))
    M = int(file.readline())
    sequence2 = list(map(int, file.readline().split()))

dp = [[0] * (M + 1) for _ in range(N+1)]
# dp[1][1] = 0 if sequence1[0] != sequence2[0] else 1

for i in range(1, N+1):
    for j in range(1, M+1):
        if sequence1[i-1] == sequence2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])


# for row in dp:
#     print(*row)
j = M
i = N
ans = []
while j > 0 and i > 0:
    if dp[i][j] == dp[i-1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j-1]:
        j -= 1
    elif dp[i][j] == dp[i-1][j-1] +1:
        j -= 1
        i -= 1
        ans.append(sequence1[i])
print(dp[-1][-1])
print(*reversed(ans))