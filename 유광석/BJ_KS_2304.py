def max_n(li):
    max_v = 0
    for i in li:
        if i > max_v:
            max_v = i
    return max_v


space = [0] * 1001
T = int(input())
for ts in range(T):
    x, y = map(int, input().split())
    space[x] = y
flag = 0
ans = 0
h = 0

for i in range(1001):
    if flag == 0:
        if space[i] < max_n(space):
            if space[i] >= h:
                h = space[i]
                ans += h
            else:
                ans += h
        else:
            if max_n(space) == max_n(space[i+1:]):
                h = space[i]
                ans += h
            else:
                flag = 1
                ans += space[i]
    else:
        ans += max_n(space[i:])

    if max_n(space[i+1:]) == False:
        break

print(ans)
# 2 4 4 6 5 3 8 10