from collections import deque
import sys
input = sys.stdin.readline


def BFS(sr, sc, cnt, d):
    q = deque()
    q.append((sr, sc, cnt, d))

    while q:
        r, c, cnt, jump = q.popleft()

        if r == N - 1 and c == M - 1:
            return cnt

        for dr, dc in monkey:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == '0' and visited[nr][nc][jump] == 0:
                visited[nr][nc][jump] = 1
                q.append((nr, nc, cnt+1, jump))

        if jump < K:
            for dr, dc in horse:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == '0' and visited[nr][nc][jump+1] == 0:
                    visited[nr][nc][jump+1] = 1
                    q.append((nr, nc, cnt+1, jump+1))
        
    return -1

K = int(input())
M, N = map(int, input().split())

horse = [(-2, -1), (-1, -2), (1, -2), (2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1)]
monkey = [(0, 1), (0, -1), (1, 0), (-1, 0)]

arr = [list(input().split()) for _ in range(N)]
visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1
ans = BFS(0, 0, 0, 0)
print(ans)