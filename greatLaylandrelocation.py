with open('input.txt') as file:
    N = int(file.readline())
    relocate = map(int, file.readline().split())
stack = []
ans = [-1] * N
for i, r in enumerate(relocate):
    while stack and stack[-1][1] > r:
        ans[stack[-1][0]] = i
        stack.pop()
    stack.append((i, r))

print(*ans)