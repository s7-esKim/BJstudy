import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))


    max_num = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            total = 0
            for i2 in range(m):
                for j2 in range(m):
                    total += arr[i+i2][j+j2]
            if max_num < total:
                max_num = total

    print(f'#{tc} {max_num}')