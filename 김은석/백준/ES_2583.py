from collections import deque

def bfs(si,sj):
    queue = deque()
    queue.append((si,sj))
    arr[si][sj] = 1
    cnt = 1

    while queue:
        ci, cj = queue.popleft()

        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni = ci + di
            nj = cj + dj
            if 0 <= ni < M and 0 <= nj < N and arr[ni][nj] == 0:
                arr[ni][nj] = 1
                queue.append((ni,nj))
                cnt += 1

    return cnt

M, N, K = map(int, input().split())

area = []                               # 각각의 영역의 넓이 , len 써서 개수 구하기

arr = [[0] * N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            arr[i][j] = 1

arr = arr[::-1]                         # 모눈종이 좌표가 밑에서부터 위로 올라감


for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            area.append(bfs(i,j))

print(len(area))
print(*sorted(area))