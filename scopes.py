with open('input.txt') as file:
    line = file.read()
line = line.strip()
stack = []
flag = False
for x in line:
    match x:
        case '(':
            stack.append(x)
        case '{':
            stack.append(x)
        case '[':
            stack.append(x)
        case ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag = True
                break
        case ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                flag = True
                break
        case '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                flag = True
                break

if not stack and not flag:
    print('yes')
else:
    print('no')

