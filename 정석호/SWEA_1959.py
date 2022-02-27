import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split()) # 1번째 줄, 2번째 줄
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    min_len = 0 #최소 길이를 구하고
    if len(A) <= len(B):
        min_len = len(A)
        small = A
        big = B
    else:
        min_len = len(B)
        big = A
        small = B

    max_total = 0
    for i in range(len(big) - len(small) + 1):
        case_total = 0
        for j in range(len(small)):
            case_total += small[j] * big[i+j]
        if max_total < case_total:
            max_total = case_total

    print(f'#{tc} {max_total}')

