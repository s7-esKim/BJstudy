import sys
input = sys.stdin.readline
import heapq

N = int(input())
arr = []
for i in range(N):
    s, e = map(int, input().split())
    arr.append([s, e])
arr = sorted(arr)

heap = []
for j in arr:
    if heap and heap[0] <= j[0]:
        heapq.heappop(heap)
    heapq.heappush(heap, j[1])

print(len(heap))