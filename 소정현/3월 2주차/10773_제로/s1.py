# 파이썬
T = int(input())

lst = []
for _ in range(T):
    a = input()
    if a != '0':
        lst.append(a)
    else:
        lst.pop()
tot = sum(map(int, lst))
print(tot)

# pypy
T = int(input())

lst = []
for _ in range(T):
    a = int(input())
    if not a:
        lst.pop()
    else:
        lst.append(a)

print(sum(lst))