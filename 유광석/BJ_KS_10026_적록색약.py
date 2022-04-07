# 적록색약용 함수
def swich(t):
    if t == 'G':
        return 'R'
    else:
        return t

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

# 좌표와 배열, 패턴을 인자로받는 BFS 함수
def BFS(i, j, arr, p):

    # 방문 한 곳은 0으로 바꿔주고
    q = [(i, j)]
    arr[i][j] = 0

    # BFS 탐색
    while q:
        r, c = q.pop(0)

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            # 같은 패턴이면 0으로 만들기
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == p:
                arr[nr][nc] = 0
                q.append((nr, nc))


N = int(input())

# 일반인, 적록색약인 배열을 따로 만든다
arr = [list(input()) for _ in range(N)]
new_arr = [list(map(swich, i[:])) for i in arr]

# 범위를 저장할 값
P1 = 0
P2 = 0

# 2중 포문을 돌면서
for i in range(N):
    for j in range(N):

        # 0인 경우는 이미 방문 한 곳이므로 0이 아닌 좌표일 경우에 BFS 각각 실행
        if arr[i][j] != 0:
            p1 = arr[i][j]
            BFS(i, j, arr, p1)
            P1 += 1

        if new_arr[i][j] != 0:
            p2 = new_arr[i][j]
            BFS(i, j, new_arr, p2)
            P2 += 1

print(P1, P2)
