import sys

T = int(input())

for i in range(1, T+1):
    cnt = 1
    people = []

    N = int(input())
    for i in range(N):
        paper, interview = map(int, sys.stdin.readline().split())
        people.append([paper, interview])

    people.sort()
    max_value = people[0][1]

    for i in range(1, N):
        if max_value > people[i][1]:
            cnt += 1
            max_value = people[i][1]

    print(cnt)