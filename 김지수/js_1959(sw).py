import sys
sys.stdin = open('새 텍스트 문서.txt')

def check(long, short):
    max_value = -99999999
    for i in range(len(long)-len(short)+1):
        result = 0
        for j in range(len(short)):
            result += long[i+j] * short[j]

        if max_value < result:
            max_value = result

    return max_value

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N > M:
        ans = check(A, B)

    else:
        ans = check(B, A)
    print("#{} {}".format(tc, ans))