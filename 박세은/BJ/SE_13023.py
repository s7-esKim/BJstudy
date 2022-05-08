import sys
input = sys.stdin.readline


def dfs(friend, x):
    global answer
    # 조건에 맞으면 1을 출력하기
    if friend == 5:
        answer = 1
        return
    # x와 친구인 애들 중 방문하지 않은 것으로 dfs
    for k in arr[x]:
        if visited[k] == 0:
            visited[k] = 1
            dfs(friend+1, k)
            visited[k] = 0


N, M = map(int, input().split())
arr = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
visited = [0] * N
answer = 0

for j in range(N):
    visited[j] = 1
    dfs(1, j)
    visited[j] = 0
    if answer == 1:
        break

print(answer)
