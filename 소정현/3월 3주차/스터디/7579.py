'''
첫 줄에는 상자의 크기를 나타내는 두 정수 M,N이 주어진다.
M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 단, 2 ≤ M,N ≤ 1,000 이다.
둘째 줄부터는 하나의 상자에 저장된 토마토들의 정보가 주어진다.
즉, 둘째 줄부터 N개의 줄에는 상자에 담긴 토마토의 정보가 주어진다.
하나의 줄에는 상자 가로줄에 들어있는 토마토의 상태가 M개의 정수로 주어진다.
정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.

토마토가 하나 이상 있는 경우만 입력으로 주어진다.
'''
from collections import deque
M, N = map(int, input().split()) # 세로, 가로

tomato = [list(map(int,input().split())) for _ in range(N)]
queue = deque()
apple_lst = list()
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def find_tomato(tomato):
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 1:
                apple_lst.append((i,j))


def bfs(graph, root):
    day = 0
    queue.append(root)
    while queue:
        lst = []
        i_j_lst = queue.popleft()
        for i, j in i_j_lst:
            for k in range(4):
                if 0 <= i+di[k] < N and 0 <= j+dj[k] < M:
                    if not graph[i+di[k]][j+dj[k]]:
                        lst.append((i+di[k], j+dj[k]))
                        graph[i+di[k]][j+dj[k]] = 1
        if lst:
            queue.append(lst)
        day += 1

    for i in graph: # 안익은토마토확인
        for j in i:
            if j == 0:
                day = 0
    return day-1

find_tomato(tomato)
day = bfs(tomato, apple_lst)
print(day)