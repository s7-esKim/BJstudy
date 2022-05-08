from collections import deque


def bfs(n):
    q = deque([n])
    while q:
        x = q.popleft()
        if x == K:
            return arr[x]
        for nx in (x-1, x+1, x*2):
            if 0 <= nx < a and arr[nx] == 0:
                if nx == x*2 and x != 0:
                    arr[nx] = arr[x]
                    q.appendleft(nx)
                else:
                    arr[nx] = arr[x] + 1
                    q.append(nx)


a = 100001
N, K = map(int, input().split())
arr = [0] * a
print(bfs(N))