# def dijkstra(s):
#     D = [INF] * V
#     U = [0] * V
#     U[s] = 1
#     D[s] = 0

#     for v, w in L[s]:
#         D[v] = w

#     for i in range(1, V):
#         min_v = INF
#         t = 0

#         for j in range(V):
#             if U[j] == 0 and D[j] < min_v:
#                 min_v = D[j]
#                 t = j
#         U[t] = 1
#         for v, w in L[t]:
#             D[v] = min(D[v], D[t] + w)

#     return D                

import heapq
import sys


def dijkstra(s):
    D = [INF] * V
    q = []
    heapq.heappush(q, (0, s))
    D[s] = 0
    while q:
        dist, now = heapq.heappop(q)

        if D[now] < dist:
            continue

        for  i in L[now]:
            cost = dist + i[1]

            if cost < D[i[0]]:
                D[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
    return D


V, E = map(int, input().split())
start = int(input())
INF = 3000000
L = [[] for _ in range(V)]

for i in range(E):
    r, c, w = map(int, sys.stdin.readline().rstrip().split())
    L[r-1].append([c-1, w])

dist = dijkstra(start-1)
dist[start-1] = 0

for i in range(V):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])
