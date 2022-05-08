N = int(input())
M = int(input())

room = [0]*(N+1)
for _ in range(M):
    s, e = map(int, input().split())
    for i in range(s,e):
        room[i] = 1

result = 0
for i in range(1, len(room)):
    if room[i] == 0:
        result += 1

print(result)


