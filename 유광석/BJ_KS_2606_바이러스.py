def dfs(s):
    stack = []
    visited[s] += 1
    stack += arr[s]

    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] += 1
            stack += arr[v]

E = int(input())
V = int(input())
arr = [[] for _ in range(E + 1)]
visited = [0] * (E + 1)

for i in range(V):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

dfs(1)
ans = 0
for i in visited:
    if i:
        ans += 1
print(ans-1) if ans else print(0)

