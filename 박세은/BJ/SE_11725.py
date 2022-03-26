from collections import deque

N = int(input())

tree = [[] for _ in range(N+1)]
p = [0] * (N+1)

for i in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)


def bfs(s, tree, p):
    q = deque([s])
    while q:
        x = q.popleft()
        for num in tree[x]:
            if p[num] == 0:
                p[num] = x
                q.append(num)


bfs(1, tree, p)

for i in range(2, N+1):
    print(p[i])
