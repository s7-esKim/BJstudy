import heapq

def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0

    while q:
        dist, now = heapq.heappop(q)    # 가중치 초기값, 현재위치
        # 노드의 거리가 최소가 아니면 건너뛰기
        if distance[now] < dist:
            continue

        for w, nn in arr[now]:
            value = w + dist
            if value < distance[nn]:
                distance[nn] = value
                heapq.heappush(q, (value, nn))

V, E = map(int, input().split())
start = int(input())
arr = [[] for _ in range(V+1)]
INF = 30000000
distance = [INF] * (V+1)

# 간선 정보 입력
for _ in range(E):
    s, e, w = map(int, input().split())
    arr[s].append((w, e))

dijkstra(start)

for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])