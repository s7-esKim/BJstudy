import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, 1 + T):
    N, K = map(int, input().split())
    score = list(map(int, input().split()))

    for i in range(N-1, 0, -1):
        for j in range(i):
            if score[j] < score[j+1]:
                score[j], score[j+1] = score[j+1], score[j]

    ans = 0
    for i in range(K):
        ans += score[i]
    print(f'#{tc} {ans}')


