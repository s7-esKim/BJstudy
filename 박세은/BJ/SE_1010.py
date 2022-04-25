def factorial(x):
    result = 1
    for i in range(1, x+1):
        result = result * i
    return result


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    answer = factorial(M) // (factorial(M-N) * factorial(N))
    print(answer)