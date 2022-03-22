from collections import deque

S, B = map(int, input().split())
visited = [0] * 100001
subin = deque([S])

while subin:
    v = subin.popleft()
    if v == B:
        print(visited[v])
        break
    
    for i in [1, -1, v]:
        ni = v + i
        if 100000 >= ni >= 0 and visited[ni] == 0:
            # BFS 1씩 증가시키는게 포인트!
            visited[ni] = visited[v] + 1
            subin.append(ni)

