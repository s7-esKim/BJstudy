N = int(input())  # N*N 행렬
n_apple = int(input())
apple = [list(map(int, input().split())) for _ in range(n_apple)]
n_change = int(input())
change = [list(map(str, input().split())) for _ in range(n_change)]
# print(N, n_apple, n_change, apple, change)

# 사과가 있는 곳 : 1
arr = [[0]*N for _ in range(N)]
for i in apple:
    arr[i[0]-1][i[1]-1] = 1

# 방향
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x = y = 0
time = 0
a = 0
t = 0
visited = [[0, 0]]
while True:
    x += dx[a]
    y += dy[a]
    # 범위 지정, 뱀이 있는 곳이 아닐 때
    if 0 <= x < N and 0 <= y < N and arr[x][y] != 2:
        # 사과가 없으면 방문했던 곳의 값을 빼서 0으로 바꾸기
        if arr[x][y] != 1:
            x1, y1 = visited.pop(0)
            arr[x1][y1] = 0
        # 사과가 있으면 길이가 늘어남
        arr[x][y] = 2
        visited.append([x, y])
        # 시간 추가
        time += 1
        # 시간 값이 change 에 있으면 방향 바꾸기
        if change and str(time) == change[0][0]:
            if change[0][1] == 'D':
                a = (a + 1) % 4
            else:
                a = (a - 1) % 4
            change.pop(0)
    else:
        print(time + 1)
        break
