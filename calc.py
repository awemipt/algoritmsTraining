with open('input.txt') as file:
    N = int(file.readline())


def argmin(sequence):
    return sequence.index(min(sequence))


dp = [0] * (N + 1)
data = [1]*N
for i in range(2, N + 1):
    tmp = dp[i - 1] + 1
    data[i-2] = i-1
    if i % 2 == 0:
        tmp = min(dp[i // 2] +1, tmp)
        data[i-2] = i//2
    if i % 3 == 0:
        tmp = min(dp[i // 3] +1, tmp)
        data[i-2] = i // 3
    dp[i] = tmp
path = []
i = N
while i > 1:
    if dp[i] == dp[i-1] + 1:
        path.append(i-1)
        i -= 1
        continue
    if i % 2 == 0 and dp[i] == dp[i//2] + 1:
        path.append(i//2)
        i //= 2
        continue
    path.append(i//3)
    i //= 3

print(dp[N])
print(*(list(reversed(path))+[N]))
