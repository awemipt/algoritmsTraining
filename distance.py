import heapq

import math

with open('input.txt') as file:
    n, k = map(int, file.readline().split())
    a = list(map(int, file.readline().split()))

m = [0] * n

for i in range(len(a)):
    s  =[]
    for j in range(len(a)):
        if i != j:
            s.append(abs(a[i]-a[j]))
    m[i] = sum(heapq.nsmallest(k,s))
print(*m)
