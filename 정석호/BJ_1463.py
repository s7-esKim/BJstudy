N = int(input())

dp = [0]*(N+1)
for i in range(2, N+1):
    dp[i] = dp[i-1] + 1     # 1을 뺏을 때

    # 2로 나누어질 때
    if i % 2 == 0 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2] + 1

    # 3으로 나누어 질때
    if i % 3 == 0 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1

print(dp[N])