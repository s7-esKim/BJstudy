from collections import deque

N, M = map(int, input().split())                    # N은 행, M은 열
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]                 # 방문기록 체크 동시에 방문 횟수

def bfs(x, y):
    # 상 하 좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))

    while queue:    # 큐가 비어있을 때까지 반복
        x, y = queue.popleft()
        for i in range(4):      # 상하좌우 순회
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]: # 행렬에 벗어나지 않고 방문기록 없을 때
                if arr[nx][ny] != 0:    # 벽이 아니면(이동할 수 있으면)
                    visited[nx][ny] = visited[x][y] + 1     # 방문기록 체크 동시에 방문 횟수 기록
                    queue.append((nx, ny))

bfs(0, 0)   # 문제에서 첫번째 행렬 시작
print(visited[N-1][M-1] + 1)    # 마지막 행렬 인덱스의 최소 방문기록 출력

