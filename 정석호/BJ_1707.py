from collections import deque

def bfs(start):
    v[start] = 1
    q = deque()
    q.append(start)
    while q:
        a = q.popleft()
        for i in node[a]:
            if v[i] == 0:
                v[i] = -v[a]
                q.append(i)
            else:
                if v[i] == v[a]:
                    return False
    return True

T = int(input())
for _ in range(T):
    V, E = map(int, input().split())
    result = True
    node = [[] for _ in range(V + 1)]
    v = [0] * (V+1)
    for i in range(E):
        a, b = map(int, input().split())
        node[a].append(b)
        node[b].append(a)
    for i in range(1, V + 1):
        if v[i] == 0:
            if not bfs(i):
                result = False
                break
    if result:
        print('YES')
    else:
        print('NO')


