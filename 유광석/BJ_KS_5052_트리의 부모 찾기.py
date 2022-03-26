import sys

# 만들어진 tree를 1부터 DFS 돌리기
def DFS(s):
    stack = [1]
    
    # 스택 == DFS, 깊이 우선
    while stack:
        v = stack.pop()

        # 만약 방문하지 않았으면
        if visited[v] == 0:
            visited[v] += 1

            # 다음 행선지를 stack에 넣어주고 ans[다음 노드] = 현재노드 > 부모 로 설정해준다!
            for i in tree[v]:
                stack.append(i)
                if tree[v] and ans[i] == 0:
                    ans[i] = v


V = int(sys.stdin.readline().rstrip())
E = V - 1
tree = [[] for _ in range(V+1)]
visited = [0] * (V+1)
ans = [0] * (V+1)

# 방향은 쌍방!
for i in range(E):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    tree[x].append(y)
    tree[y].append(x)

DFS(1)

# 루트가 1이지만 1도 부모가 있기 때문에 슬라이싱으로 2부터 출력해준다.
for i in ans[2:]:
    print(i)
