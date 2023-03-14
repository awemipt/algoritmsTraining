with open('input.txt') as file:
    row = file.read()

row = row.strip()
data = row.split()
stack = []
for x in data:
    if x.isdigit():
        stack.append(int(x))
    else:
        b = stack.pop()
        a = stack.pop()
        match x:
            case "*":
                stack.append(a * b)
            case '+':
                stack.append(a + b)
            case '-':
                stack.append(a - b)
            case '/':
                stack.append(a / b)
print(stack.pop())

