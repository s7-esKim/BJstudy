from collections import deque
import sys
input = sys.stdin.readline

def check(r, c):
    
    for i in range(r, r + H):
        if 0 <= i < N and 0 <= c < M and 0 <= c+W-1 < M:
            if arr[i][c] == 1 or arr[i][c+W-1] == 1:
                return False
        else:
            return False


    for j in range(c, c + W):
        if 0 <= r < N and 0 <= j < M and 0 <= r+H-1 < N:
            if arr[r][j] == 1 or arr[r+H-1][j] == 1:
                return False
        else:
            return False
    return True

def BFS(sr, sc):
    q = deque()
    q.append((sr, sc))

    while q:
        r, c = q.popleft()

        if r == er - 1 and c == ec - 1:
            print(visited[r][c]-1)
            return

        # 하 상 우 좌
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr = r + dr
            nc = c + dc

            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and arr[nr][nc] != 1 and check(nr, nc):
                visited[nr][nc] = visited[r][c] + 1
                
                q.append((nr, nc))

            # if d == 0 or d == 1:
            #     if visited[nr][nc] == 0:
            #         for i in range(W):
            #             if d and 0 <= nr < N and 0 <= nc+i < M and arr[nr][nc+i] == 0:
            #                 pass
            #             elif d == 0 and 0 <= nr+H-1 < N and 0 <= nc+i < M and arr[nr+H-1][nc+i] == 0:
            #                 pass
            #             else:
            #                 break
            #         else:
            #             visited[nr][nc] = visited[r][c] + 1
            #             q.append((nr, nc))

            # if d == 2 or d == 3:
            #     for i in range(H):
            #         if d == 2 and 0 <= nc < M and 0 <= nr+i < N and arr[nr+i][nc] == 0:
            #             pass
            #         elif d == 3 and 0 <= nc+W-1 < N and 0 <= nr+i < N and arr[nr+i][nc+W-1] == 0:
            #             pass
            #         else:
            #             break
            #     else:
            #         visited[nr][nc] = visited[r][c] + 1
            #         q.append((nr, nc))
    
    print(-1)
    return

N, M = map(int, input().split())
arr = [list(map(int , input().split())) for _ in range(N)]
H, W, sr, sc, er, ec = map(int, input().split())
visited = [[0] * M for _ in range(N)]
visited[sr-1][sc-1] = 1
BFS(sr-1,sc-1)


'''
6 7
0 0 0 1 0 0 0
0 0 0 1 1 1 1
0 0 0 0 0 0 0
0 0 0 0 0 0 0
1 1 1 1 0 0 0
0 0 1 1 0 0 0
2 3 1 1 5 5
'''