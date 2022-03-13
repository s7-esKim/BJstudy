R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, cnt):
    global result

    result = max(result, cnt)
    # 상 하 좌 우 순회
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        #행렬에서 벗어나지 않고 방문 기록 없으면 조건문, 재귀 실행
        if 0 <= nx < R and 0 <= ny < C and not alpha[ord(arr[nx][ny]) - 65]:
            alpha[ord(arr[nx][ny]) - 65] = 1
            dfs(nx, ny, cnt + 1)
            alpha[ord(arr[nx][ny]) - 65] = 0


alpha = [0] * 26                # 다른 알파벳 방문 기록
# 왼쪽 상단부터 시작
result = 1
alpha[ord(arr[0][0]) - 65] = 1
dfs(0, 0, 1)

print(result)