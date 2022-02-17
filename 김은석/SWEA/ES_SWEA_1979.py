T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 자리의 수
    result = 0
    # 행
    for i in range(N):
        cnt1 = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt1 += 1
            else:
                if cnt1 == K:
                    result += 1
                cnt1 = 0
        if cnt1 == K:
            result += 1
    # 열
    for k in range(N):
        cnt2 = 0
        for l in range(N):
            if arr[l][k] == 1:
                cnt2 += 1
            else:
                if cnt2 == K:
                    result += 1
                cnt2 = 0
        if cnt2 == K:
            result += 1

    print(f'#{tc} {result}')