import sys
sys.setrecursionlimit(100000)

def dfs(s, t, p):
    for i in t[s]:
        if p[i] == 0:
            p[i] = s
            dfs(i, tree, par)

N = int(input())
tree = [[] for _ in range(N+1)]
par = [0] * (N+1)
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

dfs(1, tree, par)
for i in range(2, N+1):
    print(par[i])