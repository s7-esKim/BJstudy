import sys
import heapq

N = int(sys.stdin.readline().rstrip())
time_lst = []
h = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    time_lst.append((x, y))

time_lst.sort()
heapq.heappush(h, time_lst[0][1])

for i in range(1, N):
    if h[0] <= time_lst[i][0]:
        heapq.heappop(h)
        heapq.heappush(h, time_lst[i][1])
    else:
        heapq.heappush(h, time_lst[i][1])

print(len(h))
    
