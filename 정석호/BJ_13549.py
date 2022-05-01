from collections import deque

def bfs():
    queue = deque()
    queue.append(N)     # 시작점을 queue 에 추가
    visited[N] = 1      # 방문 체크
    while queue:
        n = queue.popleft()
        # 종료조건 : 시작점에서 종료점에 도착한다면
        if n == K:
            print(result[n])
            break

        # 2*X 순회
        for j in [n*2]:
            if 0 <= j <= max_num and not visited[j]:
                visited[j] = 1
                result[j] = result[n]   # 순간 이동 시 0초
                queue.append(j)

        # X-1, X+1 순회
        for i in [n-1, n+1]:
            if 0 <= i <= max_num and not visited[i]:
                visited[i] = 1
                result[i] = result[n] + 1   # 걸을 때는 1초
                queue.append(i)

N, K = map(int, input().split())
max_num = 100000
visited = [0] * 100001
result = [0] * 100001
bfs()