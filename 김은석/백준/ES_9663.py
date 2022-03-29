# 1. 행 체크 >> 행에다 무조건 한번씩만 넣는 방식으로 구현
# 2. 열 체크 >> 현재 행과 이전행 비교해서 같은 열이면 False
# 3. 대각선 체크 >> 행과 행 뺀값이 열과 열 뺀값과 같으면 대각선에 있음 (위치가 어디에 있는지 모르니 절대값으로 비교하기)
# 시간초과 코드.... 가지치기 하나가 더 필요한듯...
import sys
# def check(idx):
#     for i in range(idx):
#         if queen[idx] == queen[i] or abs(queen[idx] - queen[i]) == abs(idx - i):
#             return False
#     return True

def DFS(idx):
    global cnt

    if idx == N:                        # N 까지 도달한 경우는 조건에 만족
        cnt += 1                        # 경우의 수 추가
        return
    # else:
    #     for i in range(N):  # i = 0 i = 1
    #         queen[idx] = i  #  [0] 행을 인덱스 열을 값으로 (0,0) >>> (1,0) (1,1)
    #                         #  [1] (0,1)
    #         if check(idx):
    #             DFS(idx+1)
    for i in range(N):
        flag = True
        for j in range(idx):
            if queen[j] == i or abs(i - queen[j]) == abs(idx-j):
                flag = False
                break
        if flag:
            queen[idx] = i
            DFS(idx + 1)

N = int(sys.stdin.readline())
cnt = 0                                 # 경우의 수
queen = [0] * N                         # 퀸이 놓여진 위치 (행을 인덱스 열을 값으로)
DFS(0)
print(cnt)