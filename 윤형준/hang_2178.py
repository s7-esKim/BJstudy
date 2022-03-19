from collections import deque
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
queue = deque()
dr = [0, 1, 0, -1]
dc = [1, 0 ,-1, 0]
queue.append([0,0])
while queue:
    i,j = queue.popleft()
    for k in range(4):
        ni = i+dr[k]
        nj = j+dc[k]
        if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 1:
            arr[ni][nj] = arr[i][j] + 1
            queue.append([ni, nj])

print(arr[N-1][M-1])


