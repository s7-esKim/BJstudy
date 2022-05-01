N = int(input())

dp = [0] * (N + 1)

dp[0], dp[1] = 0, 1

for i in range(2, N+1):
    min_v = 50000
    for j in range(1, int(i**0.5)+1):
        min_v = min(min_v, dp[i-j**2])
    dp[i] = min_v + 1
print(dp[N])

