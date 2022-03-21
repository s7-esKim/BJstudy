from collections import deque

N = int(input())
adj = [[] for _ in range(N+1)]
parent = [0] * (N+1)

for _ in range(N-1):
    v1, v2 = map(int, input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)

queue = deque()
queue.append(1)

def BFS():
    while queue:
        value = queue.popleft()
        for i in adj[value]:
            if parent[i] == 0:
                parent[i] = value
                queue.append(i)

BFS()
for i in parent[2:]:
    print(i)


