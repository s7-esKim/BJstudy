'''
5
7 3 5 7 3 5
11 2 2 11
3 2 1 3 2 4 4 1
1 2 5 1 2 3 5 4 3 4
7 3 9 7 2 9 4 3 2 4
'''

from collections import deque

t = int(input())



for _ in range(t):
    car = list(map(int, input().split()))
    q = deque()
    for c in car:
        if not q or q[0] != c:
            q.append(c)
        else:
            q.popleft()
    if q:
        print('YES')
    else:
        print('NO')
