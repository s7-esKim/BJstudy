def DFS(s, cnt):
    global ans
    if cnt == 4:
        ans = True
        print(1)
        exit()

    for j in lst[s]:
        if not visited[j]:
            visited[j] += 1
            DFS(j, cnt+1)
            visited[j] = 0

N, M = map(int, input().split())
ans = False
lst = [[] for _ in range(N)]


for i in range(M):
    x, y = map(int, input().split())
    lst[x].append(y)
    lst[y].append(x)

for i in range(N):
    visited = [0] * N
    visited[i] += 1
    DFS(i, 0)
else:
    print(0)

