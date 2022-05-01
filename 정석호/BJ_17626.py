N = int(input())
dp = [0]*(N+1)
dp[1] = 1
for i in range(2, N+1):
    min_value = 10000
    for j in range(1, int(i**(1/2))+1):
        min_value = min(min_value, dp[i-(j**2)])
    dp[i] = min_value + 1

print(dp[N])

