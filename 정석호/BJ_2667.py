N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

result = []
cnt = 0
dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]


def dfs(x, y):
    global cnt
    if x < 0 or x >= N or y < 0 or y >= N:  # 범위
        return False

    if arr[x][y] == 1:
        cnt += 1
        arr[x][y] = 0
        for i in range(4):
            dfs(x + dx[i], y + dy[i])
        return True


for i in range(N):
    for j in range(N):
        if dfs(i, j) == True:
            result.append(cnt)
            cnt = 0

print(len(result))
result.sort()
for i in result:
    print(i)
