with open('input.txt') as file:
    N = int(file.readline())
    letters = [int(file.readline()) for _ in range(N)]

ans = 0
for i in range(N-1):
    ans += min(letters[i], letters[i+1])

print(ans)