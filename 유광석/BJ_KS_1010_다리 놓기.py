for _ in range(int(input())):
    N, M = map(int, input().split())
    if N > M: N, M = M, N
    memo = [0] * (M+1)
    memo[0] = 1
    memo[1] = 1
    for i in range(2, M+1):
        memo[i] = i * memo[i-1]

# nPr = n! // r! * (n-r)!
    print(memo[M]//(memo[M-N]*memo[N]))
