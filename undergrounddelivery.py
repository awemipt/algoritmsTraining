class Train:
    def __init__(self):
        self.goods = {}
        self.trains = []

    def add(self, name, count):
        self.trains.append((name, count))
        if name not in self.goods:
            self.goods[name] = count
        else:
            self.goods[name] += count

    def get(self, name):
        return self.goods.get(name, 0)
    def delete(self, n):
        delete = n
        while delete > 0:
            name, amount = self.trains.pop()
            if delete > amount:
                delete -= amount
                self.goods[name] -= amount
            else:
                amount -= delete
                self.goods[name] -= delete
                self.trains.append((name, amount))
                delete = 0

train = Train()
with open('input.txt') as file:
    n = int(file.readline())
    for i in range(n):
        row = file.readline()
        match row.split():
            case 'add', amount, name:
                train.add(name, int(amount))
            case 'get', name:
                print(train.get(name))
            case 'delete', n:
                train.delete(int(n))
