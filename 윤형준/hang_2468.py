import sys
sys.setrecursionlimit(100000)
di = [0,1,0,-1]
dj = [1,0,-1,0]
def dfs(ci,cj,h):
    for i in range(4):
        ni = ci +di[i]
        nj = cj +dj[i]
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] > h and not visited[ni][nj]:
            visited[ni][nj] = 1
            dfs(ni,nj,h)



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
max_cnt = 0

for k in range(max(map(max,arr))):
    cnt = 0
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] > k and not visited[i][j]:
                visited[i][j] = 1
                cnt+=1
                dfs(i, j, k)

    max_cnt = max(max_cnt,cnt)

print(max_cnt)