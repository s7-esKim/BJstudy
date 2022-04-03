def nCr(n, r, s):
    global answer

    if r == 0:
        team2 = []
        for i in A:
            if i not in team1:
                team2.append(i)

        team1_total = 0
        team2_total = 0
        for i in range(R):
            for j in range(R):
                team1_total += arr[team1[i]][team1[j]]
                team2_total += arr[team2[i]][team2[j]]

        result = abs(team1_total - team2_total)
        if result < answer:
            answer = result

    else:
        for i in range(s, n-r+1):
            team1[len(team1)-r] = A[i]
            nCr(n, r-1, i+1)


N = int(input())
R = N//2
arr = [list(map(int, input().split())) for _ in range(N)]

team1 = [0] * R
A = [i for i in range(N)]
answer = 2000
nCr(N, R, 0)
print(answer)