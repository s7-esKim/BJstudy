'''
5
1 3 2 -1
2 4 4 -1
3 1 2 4 3 -1
4 2 4 3 3 5 6 -1
5 4 6 -1
'''
# [[], [(3, 2)], [(4, 4)], [(1, 2), (4, 3)], [(2, 4), (3, 3), (5, 6)], [(4, 6)]]
# DFS는 시간초과가 나옴.... 가지치기 필요한듯....
# 아니면 BFS 방법을 찾아야 할듯...
from collections import deque

V = int(input())                                        # 트리 정점의 개수
                                                        # 간선 구하기
adj = [[] for _ in range(V+1)]                          # 서로 연결되어 있는 간선들 찾기위함
for i in range(V):
    temp = list(map(int, input().split()))
    for j in range(1, len(temp)-2, 2):
        adj[temp[0]].append((temp[j], temp[j+1]))

def BFS(s):
    visited = [-1] * (V+1)
    queue = deque()
    queue.append(s)
    visited[s] = 0
    _max = [0, 0]

    while queue:
        t = queue.popleft()
        for n, d in adj[t]:
            if visited[n] == -1:
                visited[n] = visited[t] + d
                queue.append(n)
                if _max[0] < visited[n]:
                    _max = visited[n], n

    return _max

dis, node = BFS(1)
dis, node = BFS(node)
print(dis)
