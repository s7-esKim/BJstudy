import sys
sys.setrecursionlimit(10000)

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)
def DFS(r, c):

    if r == tr and c == tc:
        return 1
    
    if dp[r][c] == -1:
        dp[r][c] = 0

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] < arr[r][c]:
                    dp[r][c] += DFS(nr,nc)
    
    return dp[r][c]

                

N, M = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
dp = [[-1] * M for _ in range(N)]
sr = sc = 0
tr, tc = N-1, M-1

print(DFS(sr, sc))