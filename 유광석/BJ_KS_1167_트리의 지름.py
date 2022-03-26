import sys

# 트리 지름 공식 == 임의의 정점에서 가장 먼 정점을 구한다
# 그 정점에서 가장 먼 정점까지의 거리가 트리의 지름
# DFS로 임의의 정점 하나에서 가장 먼 정점을 구한 뒤
# DFS로 그 정점에서 가장 먼 정점의 길이를 구함

def DFS(s, d):
    global max_v, max_s

    if d > max_v:
        max_v = d
        max_s = s
        
    for i in range(len(tree[s])):
        if tree[s][i] not in visited:

            visited.add(tree[s][i])
            
            DFS(tree[s][i], d + dist[s][i])


V = int(sys.stdin.readline().rstrip())
E = V - 1
tree = [[] for _ in range(V + 1)]
dist = [[] for _ in range(V + 1)]
max_v = 0
max_s = 0

for i in range(V):
    inp = list(map(int, sys.stdin.readline().rstrip().split()))

    for i in range(1, len(inp)-1):
        if i % 2:
            tree[inp[0]].append(inp[i])
        else:
            dist[inp[0]].append(inp[i])


for i in range(V + 1):
    if tree[i]:
        visited = set()
        visited.add(i)
        DFS(i, 0)
        break


print(visited)
visited = set()
visited.add(max_s)
max_v = 0
DFS(max_s, 0)
print(max_v)

