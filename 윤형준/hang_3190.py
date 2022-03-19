import pprint
from collections import deque
N = int(input())
K = int(input()) # 사과
arr = [[0]*(N+1) for _ in range(N+1)] # N+1 by N+1 행렬

queue = [[1,1]] # 초기 뱀의 위치
for i in range(K):
    r, c = map(int, input().split())
    arr[r][c] = 1 # 사과 위치한 곳 1
arr[1][1] = 2 # 뱀 몸통은 2

direction = [[0,1], [1,0], [0,-1], [-1,0]] # 우하좌상
mode = 0 # 초기 방향 오른쪽
L = int(input()) # 방향 변환 횟수

second = 0
flag = 1
temp = [0]
sec_list = deque()
for k in range(L):
    s = input().split()
    sec_list.append(int(s[0]))

for j in range(L):
    X, C = input().split()
    X = int(X)
    if j == L-1:
        temp[0] = -100
    for x in range(X-temp[0]): #
        temp.append(X)
        temp.pop(0)
        ni = queue[-1][0] + direction[mode][0]
        nj = queue[-1][1] + direction[mode][1]
        if 1<=ni<N+1 and 1<=nj<N+1 and arr[ni][nj] != 2: # 벽도 아니고 몸통도 아니면
            queue.append([ni, nj]) # 이동한 칸 큐에 append
            second += 1
            if arr[ni][nj] == 0: # 사과가 없으면
                arr[queue[0][0]][queue[0][1]] = 0 # 꼬리를 0으로 초기화 시키고
                queue.pop(0) # 꼬리자르기
            arr[ni][nj] = 2 # 한칸 이동
            pprint.pprint(arr)
        else:
            flag = 0
            break
    if flag == 0:
        break
    if C == 'D':
        mode = (mode+1)%4
    elif C == 'L':
        mode = (mode+3)%4

print(second+1)
