N = int(input())
rooms = [1] * (2*N+1)
for i in range(len(rooms)):
    if i % 2:
        rooms[i] = 0

M = int(input())

for i in range(M):
    x, y = map(int, input().split())
    x = x*2-1
    y = y*2-1
    for j in range(x+1, y):
        if rooms[j] == 1:
            rooms[j] = 0

ans = rooms[1:-2].count(1) + 1
print(ans)
