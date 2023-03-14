from math import  ceil, floor, modf
def myround(x):
    if modf(x)[0] >=0.5:
        return int(ceil(x))
    return int(floor(x))

class Mytime:
    def __init__(self, input):
        if type(input) is str:
            self.hours, self.minutes, self.seconds = map(int, input.split(':'))
            self.timestamp = self.hours * 3600 + self.minutes * 60 + self.seconds
        elif type(input) is int:
            self.timestamp = input
            self.seconds = input % 60
            input -= self.seconds
            self.minutes = input // 60 % 60
            input -= self.minutes * 60
            self.hours = input // 3600

    def __repr__(self):
        return ':'.join(map(lambda x: str(x).zfill(2), [self.hours, self.minutes, self.seconds]))

    def __sub__(self, other):
        return Mytime(self.timestamp - other.timestamp)

    def __add__(self, other):
        return Mytime(self.timestamp + other.timestamp)

    def __truediv__(self, other):
        return Mytime(myround(self.timestamp / other))

    def __lt__(self, other):
        return self.timestamp < other.timestamp

with open('input.txt') as file:
    A = Mytime(file.readline())
    B = Mytime(file.readline())
    C = Mytime(file.readline())
if C < A:
    C = Mytime(C.timestamp + 24*3600)
D = B + (C - A)/2
print(Mytime(D.timestamp % (24*3600)))

