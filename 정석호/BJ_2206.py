from collections import deque

di, dj = ((-1, 1, 0, 0), (0, 0, -1, 1))

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(2)] # 벽을 만났을 때와 안 만났을 때의 3차원 배열 생성


queue = deque()
visited[0][0][0] = 1
queue.append([0, 0, 0])

# 시작점이 도착 지점일 때
if N == 1 and M == 1 and arr[0][0] == 0:
    print(1)
else:
    flag = 0
    while queue:
        x, y, z = queue.popleft()

        for i in range(4):
            ni = x + di[i]
            nj = y + dj[i]
            # 범위 내이고 방문하지 않았을 때
            if 0 <= ni < N and 0 <= nj < M and visited[z][ni][nj] == 0:
                # 벽을 만났을 때
                if arr[ni][nj] == 1 and z == 0:
                    visited[1][ni][nj] = visited[0][x][y] + 1
                    queue.append((ni, nj, 1))

                # 벽을 만나지 않았을 때
                elif arr[ni][nj] == 0:
                    visited[z][ni][nj] = visited[z][x][y] + 1
                    queue.append([ni, nj, z])

                # 도착했을 때
                if ni == N-1 and nj == M-1:
                    print(visited[z][ni][nj])
                    flag = 1
                    break
        # 도착했으면 while 문 종료
        if flag == 1:
            break

    # 도착지점을 가지 못했을 때
    if flag == 0:
        print(-1)