import sys
sys.stdin = open('1.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    sum_score = 0
    for i in range(K):
        sum_score += arr[i]
    print(f'#{tc} {sum_score}')
