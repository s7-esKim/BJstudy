M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0]*M for _ in range(N)]


def dfs(y, x):
    stack = [(y, x)]
    v[y][x] = 1
    cnt = 0
    while stack:
        y, x = stack.pop()
        if y % 2:
            di = [(-1, 0), (-1, -1), (0, -1), (0, 1), (1, 0), (1, -1)]
        else:
            di = [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, 0), (1, 1)]
        for i, j in di:
            if y + i >= 0 and y + i < N and x + j >= 0 and x + j < M and not v[y + i][x + j]:
                if arr[y + i][x + j]:
                    cnt += 1
                else:
                    v[y + i][x + j] = 1
                    stack.append((y + i, x + j))
    return cnt


# 가장 바깥쪽 칸들과 연결된 칸 탐색
total = 0
for y in [0, N - 1]:  # 맨 위, 맨 아래 줄 탐색
    for x in range(M):
        if arr[y][x]:
            total += 2
            if (y == 0 and x == M - 1) or (y == N - 1 and x == 0):
                total -= 1
        elif arr[y][x] == 0 and not v[y][x]:
            total += dfs(y, x)
for y in range(N):  # 맨 오른쪽, 맨 왼쪽 줄 탐색
    for x in [0, M - 1]:
        if arr[y][x]:
            if (x == 0 and y % 2) or (x == M - 1 and y % 2 == 0):
                total += 3
            else:
                total += 1
        elif arr[y][x] == 0 and not v[y][x]:
            total += dfs(y, x)

print(total)
