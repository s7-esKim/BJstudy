N, M = map(int, input().split())
adjlst = [[] for _ in range(N+1)]
max_cnt = 0
max_idx = []
for i in range(M):
    x, y = map(int, input().split())
    adjlst[y].append(x)

for i in range(1, N+1):
    cnt = 0
    visited = set()
    visited.add(i)
    stack = []
    stack += adjlst[i]
    
    while stack:
        v = stack.pop()

        if v not in visited:
            visited.add(v)
            stack += adjlst[v]
            cnt += 1
    
    if cnt == max_cnt:
        max_idx.append(i)
    elif cnt > max_cnt:
        max_cnt = cnt
        max_idx.clear()
        max_idx.append(i)

print(*max_idx)