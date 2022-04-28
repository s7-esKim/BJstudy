from collections import deque

N, M = map(int, input().split())

# visited를 사용 x, str로 받아줌
arr = [list(input().split()) for _ in range(N)]

# 배열을 탐색하면서 '2'를 발견하면 바로 BFS 시작
for i in range(N):
    for j in range(M):

        # '2'일 경우
        if arr[i][j] == '2':

            # int 0 으로 바꿔주고 BFS
            arr[i][j] = 0
            q = deque()
            q.append((i, j))

            while q:
                r, c = q.popleft()

                # 4방향 탐색하면서 만약에 '1'이면 갈 수 있는 통로니까 q에 추가해줌
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == '1':
                        arr[nr][nc] = arr[r][c] + 1
                        q.append((nr, nc))

            # BFS가 끝나면 갈 수 있는 곳은 전부 int로 바뀜
            # 남아있는 str이 있다면 갈 수 없는 길이므로 -1로 바꿔주고 출력해줌
            for i in range(N):
                if '1' in arr[i]:
                    for j in range(M):
                        if arr[i][j] == '1':
                            arr[i][j] = -1
                print(*arr[i])

            exit()