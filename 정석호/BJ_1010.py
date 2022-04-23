import math

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    bridge = [0] * M
    print(math.comb(M, N))
