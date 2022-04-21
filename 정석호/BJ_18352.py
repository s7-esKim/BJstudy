from collections import deque

N, M, K, X = map(int, input().split())  # 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호

city = [[] for _ in range(N+1)]         # 각 도시마다 연결된 도시
for i in range(M):
    a, b = map(int, input().split())
    city[a].append(b)

dist = [0]*(N+1)        # 각 도시의 거리값
visited = [0]*(N+1)     # 각 도시 방문 체크

result = []             # 결과 값
q = deque([X])          # 출발 도시
visited[X] = 1

while q:
    start = q.popleft()
    # 연결된 도시 중 방문한 적이 없으면
    for i in city[start]:
        if not visited[i]:
            q.append(i)     # 도시 추가
            visited[i] = 1  # 방문 체크
            dist[i] = dist[start] + 1
            if dist[i] == K:        # 거리의 값이 거리 정보랑 같을 때 result에 추가
                result.append(i)

# 거리 정보와 맞는 도시가 없을 때
if len(result) == 0:
    print('-1')
# 있을 때 오름차순 정렬 후 한 줄씩 출력
else:
    result.sort()
    for i in result:
        print(i)

