ans = []
heaplist = []
def append_heap(heaplist, value):
    heaplist.append(value)
    pos = len(heaplist) - 1
    while pos > 0 and heaplist[pos] <= heaplist[(pos - 1) // 2]:
        heaplist[pos], heaplist[(pos - 1) // 2] = heaplist[(pos - 1) // 2], heaplist[pos]
        pos = (pos - 1) // 2


def remove_heap(heaplist):
    ans.append(heaplist[0])
    pos = 0
    heaplist[0] = heaplist[-1]
    heaplist.pop()
    while 2 * pos + 1 < len(heaplist):
        max_son_index = 2 * pos + 1
        if 2 * pos + 2 < len(heaplist):
            if heaplist[2 * pos + 2] < heaplist[2 * pos + 1]:
                max_son_index = 2 * pos + 2
        if heaplist[max_son_index] <= heaplist[pos]:
            heaplist[max_son_index], heaplist[pos] = heaplist[pos], heaplist[max_son_index]
            pos = max_son_index
        else:
            break

with open('input.txt') as file:
    N = int(file.readline())
    data = list(map(int, file.readline().split()))

for num in data:
    append_heap(heaplist, num)

for _ in range(N):
    remove_heap(heaplist)

print(*ans)