from collections import deque


def bfs(N, K):
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            return arr[x]

        for i in (x-1, x+1, x*2):
            if 0 <= i < 100001 and arr[i] == 0:
                arr[i] = arr[x] + 1
                q.append(i)


N, K = map(int, input().split())
arr = [0] * 100001

print(bfs(N, K))

