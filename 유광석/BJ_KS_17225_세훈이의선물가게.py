from collections import deque

A, B, N = map(int, input().split())
gift = deque([i for i in range(1, 1000*100+1)])
order = deque()
sang = []
ji = []

for i in range(N):
    t, c, v = input().split()
    t = int(t)

    if c == 'B':
        if A == 1:
            if not sang:
                for i in range(int(v)):
                    sang.append((t + i, 'B'))
            else:
                if t - sang[-1][0] < A:
                    for i in range(int(v)):
                        sang.append((sang[-1][0] + 1, 'B'))

        elif not sang:
            for i in range(int(v)):
                sang.append((t + A * i, 'B'))
        else:
            if t - sang[-1][0] < A:
                for i in range(int(v)):
                    sang.append((sang[-1][0]  + A * 1, 'B'))
            else:
                for i in range(int(v)):
                    sang.append((t + A * i, 'B'))

    else:
        if B == 1:
            if not ji:
                for i in range(int(v)):
                    ji.append((t + i, 'R'))
            else:
                if t - ji[-1][0] < B:
                    for i in range(int(v)):
                        ji.append((ji[-1][0] + 1, 'R'))

        elif not ji:
            for i in range(int(v)):
                ji.append((t + B * i, 'R'))
        else:
            if t - ji[-1][0] < B:
                for i in range(int(v)):
                    ji.append((ji[-1][0]  + B * (i + 1), 'R'))
            else:
                for i in range(int(v)):
                    ji.append((t + B * i, 'R'))

lst = sang + ji
lst.sort()
ans1 = []
ans2 = []
for i in lst:
    if i[1] == 'B':
        ans1.append(gift.popleft())
    else:
        ans2.append(gift.popleft())

print(len(ans1))
print(*ans1)
print(len(ans2))
print(*ans2)