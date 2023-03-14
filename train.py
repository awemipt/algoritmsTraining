with open('input.txt') as file:
    N = int(file.readline())
    data = list(map(int, file.readline().split()))

ans = 1
stack = []
for x in data:
    stack.append(x)
    while stack and stack[-1] == ans:
        ans += 1
        stack.pop()
if not stack:
    print('YES')
else:
    print('NO')

