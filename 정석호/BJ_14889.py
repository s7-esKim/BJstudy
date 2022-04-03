def team_top(team1, team2):
    team1_sum = 0
    team2_sum = 0

    for i in range(len(team1)):
        for j in range(len(team1)):
            team1_sum += arr[team1[i]][team1[j]]
            team2_sum += arr[team2[i]][team2[j]]
    return abs(team1_sum - team2_sum)

def choice(team1, s, cnt, N):
    global result

    if cnt == N//2:
        team2 = []
        for i in range(1, N+1):
            if i not in team1:
                team2.append(i)

        result = min(result, team_top(team1, team2))
        return

    for i in range(s, N+1):
        if i not in team1:
            team1.append(i)
            choice(team1, i+1, cnt+1, N)
            team1.remove(i)


N = int(input())
arr = [[0]*(N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

result = 10000
choice([], 1, 0, N)
print(result)