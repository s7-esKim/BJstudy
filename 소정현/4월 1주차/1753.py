'''
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
'''
import heapq
import sys
input = sys.stdin.readline

V, E = map(int,input().split())
start = int(input())
connect_lst = [[] for _ in range(V+1)]
visit = [100000000] * V
visit[start-1] = 0

for _ in range(E):
    n1, n2, w = map(int, input().split())
    connect_lst[n1].append((n2,w))

def bfs(s):
    q = []
    q.append(s)

    while q:
        n = heapq.heappop(q)

        for i, d in connect_lst[n]:
            if visit[i-1] > visit[n-1] + d:
                visit[i-1] = visit[n-1] + d
                heapq.heappush(q, i)

    for i in range(len(visit)):
        if visit[i] != 100000000:
            print(visit[i])
        else:
            print('INF')

bfs(start)