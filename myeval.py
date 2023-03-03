def toPoland(s: str):
    stack = []
    ans = []
    operations = {'+': 1, '-': 1, '*': 2, '/': 2}
    while ' ' in s:
        s = s.replace(' ', '')
    num = 0
    # print(s)
    flag = False
    for x in s:
        if x.isdigit():
            flag = True
            num *= 10
            num += int(x)
            if s[-1] == x:
                ans.append(num)
        elif x in operations or x == ')':
            if flag:
                ans.append(num)
                num = 0
                flag = False
            if x in operations:
                while stack and stack[-1] in operations and operations[stack[-1]] >= operations[x]:
                    ans.append(stack.pop())
                stack.append(x)
            elif x == ')':
                while stack[-1] != '(':
                    ans.append(stack.pop())
                stack.pop()
        elif x == '(':
            stack.append(x)

    while stack:
        ans.append(stack.pop())
    return ans


def myeval(s: str):
    polandstack = toPoland(s)
    operations = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = []
    for x in polandstack:
        if type(x) in (int, float):
            stack.append(x)
        elif x in operations:
            a = stack.pop()
            b = stack.pop()
            if x == '*':
                stack.append(a * b)
            if x == '+':
                stack.append(a + b)
            if x == '-':
                stack.append(b - a)
            if x == '/':
                stack.append(b / a)
    return stack.pop()


s = input()

print(myeval(s))
