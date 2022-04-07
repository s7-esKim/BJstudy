# from collections import deque

N, M, K = map(int, input().split())
arr = [[0]*M for _ in range(N)]

for _ in range(K):
    y1, x1, y2, x2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[j][i] = 1

cnt_lst = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            arr[i][j] = 1
            cnt = 1
            q = []
            q.append((i,j))

            while q:
                r, c = q.pop(0)
                
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nr = r + dr
                    nc = c + dc
                    
                    if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
                        cnt += 1
                        arr[nr][nc] = 1
                        q.append((nr, nc))

            cnt_lst.append(cnt)

print(len(cnt_lst))
print(*sorted(cnt_lst))
