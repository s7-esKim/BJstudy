# import sys
# C, R = map(int, sys.stdin.readline().rstrip().split())

# arr = [sys.stdin.readline().rstrip() for i in range(C)] 
# visited = set()
# m_v = 0
# dr = [-1, 1, 0, 0]
# dc = [0, 0, 1, -1]

# def check(c, r, cnt):
#     global m_v, visited

#     if cnt == 26:
#         m_v = 26
#         return
#     else:
#         m_v = max(cnt, m_v)
    
#     for k in range(4):
#         nr = r + dr[k]
#         nc = c + dc[k]

#         if 0 <= nr < R and 0 <= nc < C and not arr[nc][nr] in visited:
#             visited.add(arr[nc][nr])
#             check(nc, nr, cnt+1)
#             visited.remove(arr[nc][nr])
#     return

# visited.add(arr[0][0])
# check(0, 0, 1)
# print(m_v)

import sys

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def BFS(x, y):
    global answer
    q = set([(x, y, board[x][y])])

    while q:
        x, y, ans = q.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if ((0 <= nx < R) and (0 <= ny < C)) and (board[nx][ny] not in ans):
                q.add((nx,ny,ans + board[nx][ny]))
                answer = max(answer, len(ans)+1)


R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(R)]

answer = 1
BFS(0, 0)
print(answer)