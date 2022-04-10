import sys
input = sys.stdin.readline
import heapq


def Dijkstra(start):
    dist = [E*10 + 1] * (V + 1)
    q = []
    heapq.heappush(q, [0, start])
    dist[start] = 0

    while q:
        w, e = heapq.heappop(q)
        if dist[e] < w:
            continue
        for i in arr[e]:
            total = w + i[1]
            if total < dist[i[0]]:
                dist[i[0]] = total
                heapq.heappush(q, [total, i[0]])
    return dist


V, E = map(int, input().split())  # V: 마지막 정점의번호, E 간선의 수
start = int(input())
arr = [[] * (V + 1) for _ in range(V + 1)]
for i in range(E):
    s, e, w = map(int, input().split())
    arr[s].append([e, w])

answer = Dijkstra(start)
for i in range(1, len(answer)):
    if answer[i] == E*10 + 1:
        print('INF')
    else:
        print(answer[i])
