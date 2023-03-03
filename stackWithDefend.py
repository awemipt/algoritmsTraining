stack = []
with open('input.txt') as file:
    data = file.read()

for s in data.split('\n'):
    match s.split():
        case 'push', n:
            stack.append(int(n))
            print('ok')
        case 'back',:
            if stack:
                print(stack[-1])
            else:
                print('error')
        case 'exit', :
            print('bye')
            break
        case 'pop',:
            if stack:
                print(stack.pop())
            else:
                print('error')
        case 'clear',:
            print('ok')
            stack = []
        case 'size',:
            print(len(stack))