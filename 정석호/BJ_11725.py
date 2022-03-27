import sys
sys.setrecursionlimit(100000)           # 반복 횟수 제한

# dfs 구현
def dfs(s, t, p):
    for i in t[s]:
        if p[i] == 0:
            p[i] = s
            dfs(i, tree, par)

N = int(input())                        # 노드의 갯수
tree = [[] for _ in range(N+1)]         # 트리와 연결되어 있는 노드
par = [0] * (N+1)                       # 각 인덱스의 부모
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

dfs(1, tree, par)
for i in range(2, N+1):                 # 노드 번호 2부터 출력
    print(par[i])
