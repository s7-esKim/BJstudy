import sys
sys.stdin = open('input (3).txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    farm = [list(input()) for _ in range(N)]    # 인풋 값을 받아준다
    c = N//2                                    # 중앙 값을 찾고
    value = []                                  # 농작물의 가치를 담을 리스트
    n = 0                                       # 증감 수치
    idx = 0                                     # 인덱스용
    if N > 1:                                   # 1*1의 농장은 제외하고
        flag = True                             # True일 경우에
        while True:
            if flag:
                value += (farm[idx][c-n:c+1+n]) # ex) N == 5, farm[0][2:3] > farm[1][1:4] ...
                n += 1                          # 모양에 맞게 증가
                idx += 1
                if n > c:                       # 가운데 까지 세면 다시 감소해야함으로
                    n = 1                       # 증감값 초기화
                    flag = False                # False 변경
            else:                               # 위와 동일하면서 양 옆으로 한칸 씩 줄어듬
                value += (farm[idx][n:N-n])
                n += 1
                idx += 1
                if n > c:
                    break                       # 맨 밑까지 도착하면 끝
        ans = 0
        for i in map(int, value):               # 아까 str로 받아서 int로 바꿔주고
            ans += i
        print(f'#{tc} {ans}')                   # 출력
    else:
        print(f'#{tc} {int(farm[0][0])}')       # 1*1이면 그냥 arr[0][0] 출력




