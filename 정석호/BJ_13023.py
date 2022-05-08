def dfs(ci, cnt):
    if cnt == 4:
        print(1)
        exit()

    for i in lst[ci]:
        if not v[i]:
            v[i] = 1
            dfs(i, cnt+1)
            v[i] = 0

N, M = map(int, input().split())
lst = [[] for _ in range(N)]
v = [0]*N
for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

for i in range(N):
    v[i] = 1
    dfs(i, 0)
    v[i] = 0

print(0)