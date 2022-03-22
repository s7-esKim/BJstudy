from collections import deque

A, B, N = map(int, input().split())  # A:상민이 포장시간, B:지수 포장시간, C: 손님수
queue1 = deque()  # 상민 포장시작 시간 리스트
queue2 = deque()  # 지수 포장시작 시간 시간 리스트
s_end, j_end = 0, 0  # 상민, 지수 포장 끝난 시간

for _ in range(N):
    start, color, cnt = input().rstrip().split()  # 주문시각, 색깔, 개수
    start = int(start)

    if color == 'B':  # 상민
        start = max(start, s_end)
        for i in range(int(cnt)):
            queue1.append([start, 'B'])
            start += A
            s_end = start

    elif color == 'R':  # 지수
        start = max(start, j_end)
        for i in range(int(cnt)):
            queue2.append([start, 'R'])
            start += B
            j_end = start

total_list = queue1 + queue2
total_list = sorted(total_list, key=lambda x: [x[0], x[1]])

s_present, j_present = [], []  # 상민, 지수가 포장한 선물리스트

for idx, present in enumerate(total_list):
    if present[1] == 'B':
        s_present.append(idx + 1)
    else:
        j_present.append(idx + 1)

print(len(s_present))
print(*s_present)
print(len(j_present))
print(*j_present)
