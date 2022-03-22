from collections import deque
N, M = map(int, input().split())
start = (0,0)
graph = [list(map(int, input())) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
visit[0][0] = 1
def bfs(graph, root):
    queue = deque()
    queue.append(root)
    di = [1,-1,0,0]
    dj = [0,0,1,-1]

    while queue:
        i, j = queue.popleft()
        if i == N-1 and j == M-1:
            print(visit[N-1][M-1])
            return
        for k in range(4):
            if 0 <= i + di[k] < N and 0 <= j + dj[k] < M:
                if not visit[i+di[k]][j+dj[k]] and graph[i+di[k]][j+dj[k]]:
                    queue.append((i+di[k], j+dj[k]))
                    visit[i+di[k]][j+dj[k]] = visit[i][j] + 1

bfs(graph, start)