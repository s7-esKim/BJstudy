import sys
sys.stdin = open('7576.txt')
from collections import deque

T = int(input())
for tc in range(1, T+1):
    M, N = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(N)]

    q = deque()

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                x, y = i, j
                q.append([x, y])
    day = -1
    while q:
        day += 1
        for _ in range(len(q)):
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                try:
                    if 0 <= nx and 0 <= ny and arr[nx][ny] == 0:
                        q.append([nx, ny])
                        arr[nx][ny] = arr[x][y] + 1
                except IndexError:
                    continue


    for i in arr:
        if 0 in i:
            print(-1)
            break
    else:
        print(day)