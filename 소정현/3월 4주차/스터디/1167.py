V = int(input())

tree_lst = [list(map(int, input().split())) for _ in range(V)]

connect_lst = [[] for _ in range(V+1)]


for i in range(V):
    j = 1
    while tree_lst[i][j] != -1:
        connect_lst[i+1].append((tree_lst[i][j], tree_lst[i][j+1]))
        j += 2
def pre_order(N, distance):
    global max_distance
    cnt = 0

    if connect_lst[N]:
        for node, dist in connect_lst[N]:
            if not visit[node]:
                visit[node] = 1
                pre_order(node, distance + dist)
                visit[node] = 0
            else:
                cnt += 1
        if cnt == len(connect_lst[N]):
            if distance > max_distance:
                max_distance = distance
            return
max_distance = 0

for v in range(1, V+1):
    visit = [0]*(V+1)
    visit[v] = 1
    pre_order(v,0)

print(max_distance)