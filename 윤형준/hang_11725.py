from collections import deque

N = int(input())
G = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
queue = deque()
queue.append(1)

ans = [0] * (N+1)
visited = [0] * (N+1)
def bfs():
    while queue:
        now = queue.popleft()
        for j in G[now]:
            if ans[j] == 0:
                ans[j] = now
                if visited[j] == 0:
                    queue.append(j)
        visited[now] = 1

bfs()
for x in range(2,len(ans)):
    print(ans[x])
