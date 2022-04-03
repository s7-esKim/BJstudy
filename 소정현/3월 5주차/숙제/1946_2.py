import sys

T = int(input())  # 테스트케이스

for i in range(0, T):
    cnt = 1
    people = []

    N = int(input())
    for i in range(N):
        paper, interview = map(int, sys.stdin.readline().split())
        people.append([paper, interview])

    people.sort()  # 서류 기준 오름차순 정렬
    max = people[0][1]

    for i in range(1, N):
        if max > people[i][1]:
            cnt += 1
            max = people[i][1]

    print(cnt)