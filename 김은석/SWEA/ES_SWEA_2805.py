T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr= [list(map(int,input())) for _ in range(N)]

    # 처음 인덱스
    center = N // 2
    # 다음 인덱스도  양 옆으로 1 씩 증가
    left = N // 2
    right = N // 2
    # 그러다가 N // 2 지점을 지나면 다시 1씩 감소
    total = 0
    for i in range(N):  # 0 1 2 3 4
        if i == 0:
            left = N // 2
            right = N // 2
        elif i <= center:
            left -= 1
            right += 1
        else:
            left += 1
            right -= 1
        for j in range(left, right+1): # j 1 2 3
                total += arr[i][j]

    print(f'#{tc} {total}')