class Queue:
    def __init__(self):
        self.stackAdd = []
        self.stackRemove = []

    def push(self, value):
        self.stackAdd.append(value)
        print('ok')

    def gostack(self):
        while self.stackAdd:
            self.stackRemove.append(self.stackAdd.pop())

    def pop(self):
        if not self.stackRemove:
            self.gostack()
        if self.stackRemove:
            print(self.stackRemove.pop())
        else:
            print('error')

    def front(self):
        if not self.stackRemove:
            self.gostack()
        if self.stackRemove:
            print(self.stackRemove[-1])
        else:
            print('error')

    def size(self):
        print(len(self.stackRemove) + len(self.stackAdd))

    def clear(self):
        self.stackAdd = []
        self.stackRemove = []
        print('ok')

    def exit(self):
        # self.clear()
        print('bye')

with open('input.txt') as file:
    data = file.read().strip()

queue = Queue()
for line in data.split('\n'):

    match line.split():
        case 'push', n:

            queue.push(int(n))
        case 'pop', :
            queue.pop()
        case 'front', :
            queue.front()
        case 'size', :
            queue.size()
        case 'clear', :
            queue.clear()
        case 'exit', :
            queue.exit()
            break
