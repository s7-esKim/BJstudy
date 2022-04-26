def f(a, b):
    count = 0
    x = a
    y = b
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            # 땅 주위에 바다가 있으면 count += 1
            if arr[nx][ny] == '.':
                count += 1
    # 땅 주위에 바다가 3개 이상이면 섬이 잠김
    if count >= 3:
        arr[x][y] = 'O'
    # 그렇지 않은 경우 잠기지 않으므로 땅의 index 값을 추가
    else:
        arr_x.append(x)
        arr_y.append(y)


R, C = map(int, input().split())
N = R+2
M = C+2
# 위, 아래, 오른쪽, 왼쪽에 한줄씩 바다 추가
arr = [['.'] * (M)] + [['.']+list(map(str, input()))+['.'] for _ in range(R)] + [['.'] * (M)]

arr_x = []  # 섬들의 행 index
arr_y = []  # 섬들의 열 index
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'X':
            f(i, j)

# 최소한의 지도 출력
for i in range(min(arr_x), max(arr_x)+1):
    for j in range(min(arr_y), max(arr_y)+1):
        # 'O'도 바다에 잠긴것으로 바꿔주기
        if arr[i][j] == 'O':
            print('.', end='')
        else:
            print(arr[i][j], end='')
    print()