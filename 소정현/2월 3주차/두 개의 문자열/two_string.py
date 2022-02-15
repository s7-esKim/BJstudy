import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for ts in range(T):
    A_n, B_n = map(int, input().split())
    A = list(map(int,input().split()))
    B = list(map(int, input().split()))
    if A_n > B_n:
        A, B = B, A
    dist = abs(A_n - B_n)
    if dist > 0:
        max_tot = 0
        for i in range(dist+1):
            tot = 0
            for j in range(len(A)):
                tot += (A[j]*B[j+i])
            if tot > max_tot:
                max_tot = tot
    else:
        tot = 0
        for i in range(len(A)):
            tot += A[i]*B[j]
        max_tot = tot
    print(f'#{ts+1} {max_tot}')