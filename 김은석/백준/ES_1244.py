N = int(input())                        # N : 스위치 개수
arr =list(map(int, input().split()))    # arr : 스위치 상태 0: off 1: on
std = int(input())                      # std : 학생수
for _ in range(std):
    A, B = map(int, input().split())    # A : 성별 남1 여2 B : 받은 스위치 개수
    if A == 1:
        for i in range(B-1,N,B):
            if arr[i] == 0:
                arr[i] = 1
            else:
                arr[i] = 0
    else:
        if arr[B-1] == 0:
            arr[B-1] = 1
        else:
            arr[B-1] = 0
        for j in range(N):
            if 0 <= B - 1 - j and B - 1 + j < N:
                if arr[B - 1 - j] == arr[B - 1 + j]:
                    if arr[B - 1 - j] == 0:
                        arr[B - 1 - j] = 1
                    elif arr[B - 1 - j] == 1:
                        arr[B - 1 - j] = 0
                    if arr[B - 1 + j] == 0:
                        arr[B - 1 + j] = 1
                    elif arr[B - 1 + j] == 1:
                        arr[B - 1 + j] = 0
                else:
                    break

# 20개씩 출력해야함
for k in range(0,N,20):
    print(*arr[k:20+k])
