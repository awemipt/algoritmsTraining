from collections import Counter

with open('input.txt') as file:
    text = file.read()

text = text.replace(' ', '')
text = text.replace('\n', '')

syms = list(set(text))
syms.sort(key=ord)
# print(syms)
c = Counter(text)
l = max(c.values())

ans = {k: '#' * c[k] + ' ' * (l - c[k]) for k in syms}
for i in range(l):
    for k in sorted(ans, key=ord):
        print(ans[k][-1 - i], end='', sep='')
    print()
print(''.join(syms))
