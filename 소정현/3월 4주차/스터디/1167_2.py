from collections import deque
V = int(input())

tree_lst = [list(map(int, input().split())) for _ in range(V)]

connect_lst = [[] for _ in range(V+1)]
dist_lst = [[0]*(V+1) for _ in range(V+1)]

for i in range(V):
    j = 1
    while tree_lst[i][j] != -1:
        connect_lst[i+1].append(tree_lst[i][j])
        dist_lst[i+1][tree_lst[i][j]]  = tree_lst[i][j+1]
        j += 2

def pre_order(T):
    if connect_lst[T]:
        visit.append(T)
        for node in connect_lst[T]:
            if node not in visit:
                pre_order(node)

max_length = 0

def max_dist():
    global max_length
    q = deque()
    q.append(visit.popleft())
    dist = 0
    while visit:
        a = visit.popleft()
        if dist_lst[q[-1]][a]:
            dist += dist_lst[q[-1]][a]
            q.append(a)
        else:
            while not dist_lst[q[-1]][a] and len(q) != 1:
                dist -= dist_lst[q[-2]][q[-1]]
                q.pop()
            dist += dist_lst[q[-1]][a]
            q.append(a)
        if dist > max_length:
            max_length = dist
    return max_length

for v in range(1, V+1):
    visit = deque()
    pre_order(v)
    max_dist()

print(max_length)