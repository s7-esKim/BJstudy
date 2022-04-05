# '''
# dfs(x)
# 0,0부터 시작해서 0,7까지 퀸을 놓는다
# -> 조건 만족하는지 검사
# -> 만족하면 bfs(x+1)
# -> 실패하면 백트래킹(?)
# -> 1,0부터 시작해서 1,7까지 퀸을 놓는다
# -> 조건 만족하는지 검사..반복
# '''
#
# def dfs(x): # x부터 시작해서 N-1까지
#     global ans
#     if x == N: # N-1까지 만족했으면 경우의 수 +1
#         ans +=1
#         return
#
#     # 조건 # 인덱스 범위 -> 항상 만족 // 상하대각선 퀸 유무 확인 필요
#     for i in range(N): # 0부터 N까지
#         visited[x] = i # x번 행 i번 열에 퀸?
#         if #상하좌우대각선에 퀸이 없으면:
#             dfs(x+1)
#
# N = int(input()) # N by N
# visited = [0 for _ in range(N)] # 각 행당 퀸은 1개
# ans = 0 # 경우의 수
# dfs(0)

def DFS_1(n):
    global ans
    if n == N:
        ans += 1
        return

    for j in range(N):
        if v1[j]==v2[n+j]==v3[n-j]==0:
            v1[j]=v2[n+j]=v3[n-j]=1
            DFS_1(n+1)
            v1[j]=v2[n+j]=v3[n-j]=0

N = int(input())
# v = [[0]*N for _ in range(N)]
ans = 0
v1, v2, v3 = [0]*30, [0]*30, [0]*30
DFS_1(0)
# DFS(0)
print(ans)