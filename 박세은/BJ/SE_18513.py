import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
water = list(map(int, input().split()))

q = deque()
visited = set()
for i in water:
    q.append((i, 1))
    visited.add(i)

answer = 0
while K > 0:
    if K <= 0:
        break
    while q:
        x, l = q.popleft()
        for i in [1, -1]:
            nx = x + i
            if nx not in visited and K > 0:
                visited.add(nx)
                answer += l
                K -= 1
                q.append((nx, l+1))
print(answer)