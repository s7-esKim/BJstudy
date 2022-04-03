N = int(input())
meeting = []
for i in range(N):
    start, end = map(int, input().split())
    meeting.append([start, end])

meeting = sorted(meeting)
meeting = sorted(meeting, key=lambda a: a[1])

last = 0
count = 0
for i, j in meeting:
    if i >= last:
        count += 1
        last = j
print(count)