import sys
from collections import deque
from pprint import pprint

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(M)]

# 안 익은 토마토가 있는지 확인하는 함수
def check_Arr(arr):
    for i in range(M):
        for j in range(N):
            if arr[i][j] == 0:
                return False
    return True

# 처음 토마토 위치를 리스트로 반환하는 함수
def find_tomato(arr):
    lst = []
    for i in range(M):
        for j in range(N):
            if arr[i][j] == 1:
                lst.append((i, j))
    return lst

# bfs로 익을 때마다 주위의 토마토에 +1을 추가하면서 증가
def fresh(r, c):

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        
        # 인덱스 범위 안에서 0이면 계속 진행
        if 0 <= nr < M and 0 <= nc < N and arr[nr][nc] == 0:
            arr[nr][nc] = arr[r][c] + 1
            tomato.append((nr, nc))

tomato = deque(find_tomato(arr))

# 더이상 갈 곳이 없으면 종료
while tomato:
    v = tomato.popleft()
    x, y = v
    fresh(x, y)

# 결과 값은 arr의 가장 큰 값 - 1 만큼
max_v = 0

# 만약 0이 없으면 최대값
if check_Arr(arr):
    for i in range(M):
        for j in range(N):
            if max_v < arr[i][j]:
                max_v = arr[i][j]
    print(max_v - 1)

# 있으면 - 1
else:
    print(-1)

pprint(arr)

# 시간초과
# import sys

# N, M = map(int, sys.stdin.readline().rstrip().split())

# arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(M)]

# def check_Arr(arr):
#     for i in range(M):
#         for j in range(N):            
#             if arr[i][j] == 0:
#                 return False
#     return True

# def find_tomato(arr):
#     lst = []

#     for i in range(M):
#         for j in range(N):
#             if arr[i][j] == 1:
#                 lst.append((i, j))
#     return lst

# def fresh(r, c):

#     dr = [1, -1, 0, 0]
#     dc = [0, 0, 1, -1]

#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]

#         if 0 <= nr < M and 0 <= nc < N and arr[nr][nc] == 0:
#             arr[nr][nc] += 1
# t = 0

# while not check_Arr(arr):
#     tomato = find_tomato(arr)
#     t += 1
#     for i in range(len(tomato)):
#         x, y = tomato[i]
#         fresh(x, y)
#         arr[x][y] = 2
    
#     if t > N * M:
#         t = -1
#         break

# print(t)
