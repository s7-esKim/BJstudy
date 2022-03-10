N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

houses = []
cnt = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global cnt
    if x < 0 or x >= N or y < 0 or y >= N:
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
            houses.append(cnt)
            cnt = 0

print(len(houses))
houses.sort()
for house in houses:
    print(house)
