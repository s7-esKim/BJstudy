import sys
sys.stdin = open('1.txt.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input()) #항상 홀수 + 정사각형
    arr = [list(map(int, input())) for _ in range(N)]

    a = b = center = N // 2
    total = 0
    for i in range(N):
        for j in range(a, b + 1):
            total += arr[i][j]
        if i < center:
            a -= 1
            b += 1
        else:
            a += 1
            b -= 1
    print(total)



    #
    # start = center
    # end = center
    # for i in range(N):
    #     for j in range(start, end+1):
    #         total += arr[i][j]
    #     if i < center:
    #         start -= 1
    #         end += 1
    #     else:
    #         start += 1
    #         end -= 1
    # print(f'#{tc} {total}')
