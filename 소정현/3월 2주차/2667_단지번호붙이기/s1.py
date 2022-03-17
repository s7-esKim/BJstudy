# import sys
#
# T = int(sys.stdin.readline())
#
# apart_arr = [list(sys.stdin.readline().rstrip()) for _ in range(T)]
#
# visit = [[0]*T for _ in range(T)]
#
# def find_idx(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr[i])):
#             if arr[i][j] == '1':
#                 return i, j
#     else:
#         return -1, -1
#
#
# i, j = find_idx(apart_arr)
# di = [1,-1,0,0]
# dj = [0,0,1,-1]
# while i != -1:
#     for k in range(4):
#         if apart_arr[i+di[k]][j+dj[k]] != 0 and 0 <= i+di[k] < T and 0 <= j+dj[k] < T:
#             visit[i+di[k]][j+dj[k]] = 1
n = int(input())
graph = []
num = []

for i in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def DFS(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            DFS(nx, ny)
        return True
    return False


count = 0
result = 0

for i in range(n):
    for j in range(n):
        if DFS(i, j) == True:
            num.append(count)
            result += 1
            count = 0

num.sort()
print(result)
for i in range(len(num)):
    print(num[i])