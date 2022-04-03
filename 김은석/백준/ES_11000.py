import heapq

N = int(input())
time = [list(map(int,input().split())) for _ in range(N)]

time.sort()
classroom = []
heapq.heappush(classroom, time[0][1])
for i in range(1, len(time)):
    if time[i][0] < classroom[0]:
        heapq.heappush(classroom, time[i][1])
    else:
        heapq.heappop(classroom)
        heapq.heappush(classroom, time[i][1])

print(len(classroom))