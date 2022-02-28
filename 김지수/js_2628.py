row, column = map(int, input().split())
n = int(input())

rlst = [0, row] #  10 4
clst = [0, column] #  8 3 2
for i in range(n):
    start , end = map(int, input().split())
    if start == 0 :
        clst.append(end)
    elif start == 1:
        rlst.append(end)

rlst.sort()
clst.sort()
r_max = 0
for i in range(len(rlst)):
    a = 0
    try:
        a += rlst[i+1] - rlst[i]
    except IndexError:
        pass
    if a > r_max:
        r_max = a

c_max = 0
for i in range(len(clst)):
    a = 0
    try:
        a += clst[i+1] - clst[i]
    except IndexError:
        pass
    if a > c_max:
        c_max = a

print(r_max * c_max)