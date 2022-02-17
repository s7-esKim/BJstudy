#테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # N = N * N 배열 안의 파리 숫자들
    # M = M * M 크기의 파리채
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for i in range(N)] #list comprehension
    # 리스트 안에 리스트 형식필요
    # [[1, 3, 3, 6, 7], [8, 13, 9, 12, 8], [4, 16, 11, 12, 6], [2, 4, 1, 23, 2], [9, 13, 4, 7, 3]] # 5개씩 한줄
    # 2*2 일경우 인덱스 이중포문 필요할듯
    max_fly = 0 # 최댓값 찾기
    for j in range(N-M+1):              #오늘풀었던 구간합이랑 비슷
        for k in range(N-M+1):
            fly = 0 #임시 죽은파리의총합
            for a in range(M):             #파리채의 범위만큼
                for b in range(M):
                    fly += arr[j+a][k+b]
                    if fly > max_fly:
                        max_fly = fly

    print(f'#{tc} {max_fly}')

