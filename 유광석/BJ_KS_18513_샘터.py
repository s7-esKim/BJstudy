import sys
from collections import deque
N, K = map(int, sys.stdin.readline().rstrip().split())
visited = set()
q = deque()
sam = list(map(int, sys.stdin.readline().rstrip().split()))
for i in range(N):
    visited.add(sam[i])
    q.append((sam[i], 0))

ans = 0
while q:
    
    v, d = q.popleft()
    d += 1
    for di in (-1, 1):
        ni = v + di

        if ni not in visited:
            visited.add(ni)
            K -= 1
            
            ans += d
            q.append((ni, d))

        if K == 0:
            print(ans)
            exit()
