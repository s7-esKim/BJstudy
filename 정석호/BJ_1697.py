from collections import deque

def bfs():
    queue = deque()
    queue.append(N)
    while queue:
        n = queue.popleft()
        if n == K:
            print(visited[n])
            break

        for i in [n-1, n+1, n*2]:
            # if not visited[i] and 0 <= i <= max_num:
            if 0 <= i <= max_num and not visited[i]:
                visited[i] = visited[n] + 1
                queue.append(i)

N, K = map(int, input().split())
max_num = 100000
visited = [0] * 100001
bfs()