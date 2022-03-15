from collections import deque
from pprint import pprint

# 인풋
N = int(input())
K = int(input())
arr = [[0] * N for _ in range(N)]

# 문제의 행열은 1, 1 부터 시작하니까 사과의 위치를 조정해준다.
for i in range(K):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 'A'

# 명령어 (초, 명령어) 형식으로 받아준다.
X = int(input())
order = deque()

for i in range(X):
    s, o = input().split()
    order.append((int(s), o))

# 방향을 찾아주는 함수 오른쪽, 왼쪽
def direction(dr, dc, order):
    if order == 'D':
        if dr == 0 and dc == 1:
            return 1, 0
        elif dr == 1 and dc == 0:
            return 0, -1
        elif dr == 0 and dc == -1:
            return -1, 0
        else:
            return 0, 1
    else:
        if dr == 0 and dc == 1:
            return -1, 0
        elif dr == -1 and dc == 0:
            return 0, -1
        elif dr == 0 and dc == -1:
            return 1, 0
        else:
            return 0, 1

# 뱀 길이
cm = 1

# 문제 로직 함수
def check(r, c):
    # cm를 전역변수로 두고 값을 바꾸면서 활용하기 위함
    global cm

    # 시간을 0으로 초기화, q는 덱설정 (몸통 넣어줄 값), dr, dc는 오른쪽 시작이므로 0, 1 기본값으로
    time = 0
    q = deque()
    q.append((r, c))
    dr = 0
    dc = 1
    
    # 꼬리에 닿거나 index를 벗어나기 전까지 반복
    while True:

        # 만약에 명령이 있고 그 명령 초가 현재 time이랑 같으면
        if order:
            if time == order[0][0]:
                v = order.popleft()

                # dr, dc를 바꿔준다.
                dr, dc = direction(dr, dc, v[1])

        # 한 칸 이동 할 때마다 시간 +1
        time += 1

        # q에 넣은 마지막 값이 현재 머리 위치
        r, c = q[-1]

        # 방향을 더해주고
        nr = r + dr
        nc = c + dc
        print(nr, nc)
        # 만약에 가는 곳이 인덱스 안이면서 사과가 있으면
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 'A':
            
            # 사과를 0으로 만들고 cm 증가
            arr[nr][nc] = 0
            cm += 1

        # 만약에 인덱스 안이면서 q 즉 몸통이 아니면 몸통에 넣어주고
        if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in q:
            q.append((nr, nc)) 

            # 만약 몸통의 길이가 cm보다 크다면 가장 왼쪽 값을 빼줌 > 꼬리
            if len(q) > cm:
                while len(q) != cm:
                    q.popleft()
        
        # while 종료 조건
        else:
            return time

# 뱀은 항상 0, 0 시작
t = check(0, 0)
pprint(arr)
print(t)



