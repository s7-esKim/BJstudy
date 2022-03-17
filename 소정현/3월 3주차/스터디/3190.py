'''
뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 뱀은 처음에 오른쪽을 향한다.
뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.
매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.

먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라
'''
from collections import deque
# 뱀의 초기 위치 0,0 X초 후 L은 왼쪽으로 90도 D는 오른쪽으로 90도 회전
N = int(input()) # 보드 크기
K = int(input()) # 사과 개수

apple = [list(map(int,input().split())) for _ in range(K)]

L = int(input()) # 움직임 횟수
move_dict = {}
for _ in range(L):
    key, value = input().split()
    move_dict[int(key)] = value
# L이면 k에 -1 D면 k에 + 1 # 4로나눠서 나머지로 계산
dj = [1, 0, -1, 0]
di = [0, 1, 0, -1]

location = deque([[1,1]])


time = 0

def dummy_game():
    global time
    k = 0
    while True:
        if time in move_dict.keys():
            if move_dict[time] == 'D':
                k += 1
            elif move_dict[time] == 'L':
                k -= 1
                if k < 0:
                    k = 4 + k
            k %= 4

        i, j = location[-1] # 머리 늘리기
        i += di[k]; j += dj[k]
        time += 1

        if i > N or i < 1 or j < 1 or j > N or [i, j] in location:
            break
        if [i,j] not in apple: # 길이는 그대로 늘어난 머리는 그대로 유지
            location.append([i,j])
            location.popleft() # 꼬리 줄이기
        else: # 사과 먹기
            location.append([i,j])
            apple.remove([i, j])

dummy_game()

print(time)