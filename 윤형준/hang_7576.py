import pprint
from collections import deque
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def BFS(queue):
    global sec
    Q = queue
    while Q:
        a = len(Q) # Q의 길이만큼 pop하기 위해? 동시 출발?
        for i in range(a):
            r, c = Q.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0<=nr<N and 0<=nc<M:
                    if arr[nr][nc] == 0:
                        Q.append([nr, nc])
                        arr[nr][nc] = 1
        # pprint.pprint(arr)
        # print(queue)

        sec += 1
    for i in range(N):
        if 0 in arr[i]:
            print('-1')
            break
    else:
        print(sec-1)

sec = 0
M, N = map(int,input().split())
# M, N = map(int, sys.stdin.readline().split())
arr = [list(map(int, input().split())) for _ in range(N)]  # N by M
# arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
queue = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            queue.append([i, j])
# print(queue)
BFS(queue)