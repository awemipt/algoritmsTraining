class Node:
    def __init__(self, value, next=None, prev=None):
        self.next = next
        self.prev = prev
        self.value = value


class Dequeue:
    def __init__(self):
        self.front = None
        self.back = None
        self.length = 0

    def push_front(self, val):
        if self.front is None:
            self.front = self.back = Node(val)
        else:
            self.front.prev = Node(val, next=self.front)
            self.front = self.front.prev
        self.length += 1
        print('ok')

    def push_back(self, val):
        if self.back is None:
            self.back = self.front = Node(val)
        else:
            self.back.next = Node(val, prev=self.back)
            self.back = self.back.next
        self.length += 1
        print('ok')

    def pop_front(self):
        if self.front is None:
            print('error')
        elif self.front is self.back:
            print(self.front.value)
            self.front = self.back = None
            self.length -= 1
        else:
            print(self.front.value)
            tmp = self.front.next
            self.front.next = None
            self.front = tmp
            self.length -= 1

    def pop_back(self):
        if self.back is None:
            print('error')
        elif self.front is self.back:
            print(self.back.value)
            self.back = self.front = None
            self.length -= 1
        else:
            print(self.back.value)
            tmp = self.back.prev
            self.back.prev = None
            self.back = tmp
            self.length -= 1

    def _front(self):
        if self.front:
            print(self.front.value)
        else:
            print('error')

    def _back(self):
        if self.back:
            print(self.back.value)
        else:
            print('error')

    def size(self):
        print(self.length)

    def clear(self):
        self.front = self.back = None
        self.length = 0
        print('ok')

    def exit(self):
        print('bye')


with open('input.txt') as file:
    data = file.read()

q = Dequeue()
for line in data.split('\n'):
    match line.split():
        case 'push_front', n:
            q.push_front(int(n))
        case 'push_back', n:
            q.push_back(int(n))
        case 'pop_back',:
            q.pop_back()
        case 'pop_front',:
            q.pop_front()
        case 'front',:
            q._front()
        case 'back',:
            q._back()
        case 'size',:
            q.size()
        case 'clear',:
            q.clear()
        case 'exit',:
            q.exit()
            break
