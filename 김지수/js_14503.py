import sys
sys.stdin = open('1.txt')
from collections import deque
'''
북쪽의 왼쪽 = 서 
동쪽의 왼쪽 = 북 
남쪽의 왼쪽 = 동 
서쪽의 왼쪽 = 남
'''


dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
dir = [2, 3, 0, 1]


def find(di):
    if di == 0:
        di = 3
        return di
    if di == 1:
        di = 0
        return di
    if di == 2:
        di = 1
        return di
    if di == 3:
        di = 2
        return di

def bfs(i, j, d):
    global cnt
    q = deque()
    q.append([i, j, d])
    room[i][j] = -1
    cnt += 1

    while q:
        i, j, d = q.popleft()
        a = 0
        while a < 4:
            if room[i + dx[d]][j + dy[d]] == 0:
                room[i + dx[d]][j + dy[d]] = -1
                a += 1
                bfs(i + dx[d], j + dy[d], dir[d])

            else:
                d = find(d)
                bfs(i, j, d)

        if room[i-dx[d]][i-dy[d]] == 0:
            bfs(i-dx[d], j[dy[d]], dir[d])
        else:
            return







t = int(input())
for tc in range(t+1):
    n, m = map(int, input().split())
    r, c, direction = map(int, input().split())
    room = [list(map(int, input().split())) for _ in range(n)]

    cnt = 0
    bfs(r, c, direction)

    print(cnt)