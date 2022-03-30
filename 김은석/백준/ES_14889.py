from itertools import combinations

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
members = [i for i in range(N)]
possible_team = []


for team in list(combinations(members, N // 2)):
    possible_team.append(team)

result = 99999999999
for i in range(len(possible_team) // 2):
    teamA = possible_team[i]
    start = 0
    for j in range(N // 2):
        member = teamA[j]
        for k in teamA:
            start += arr[member][k]


    teamB = possible_team[-i - 1]
    link = 0
    for j in range(N // 2):
        member = teamB[j]
        for k in teamB:
            link += arr[member][k]

    result = min(result, abs(start - link))

print(result)