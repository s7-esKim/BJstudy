from collections import deque

s_time, j_time, N = map(int,input().split())
s_end, j_end = 0, 0 # 상민,지수 포장 끝난 시간
s_lst = deque()
j_lst = deque()
for _ in range(N):
    t, color, m = map(str,input().split())  # 주문 시각, 색, 개수
    t = int(t)
    m = int(m)

    if color == 'B':
        t = max(s_end, t)
        for i in range(m): # 개수만큼 반복하면서 포장 시각 저장
            s_lst.append([t, 'B'])
            t += s_time
            s_end = t

    elif color =='R':
        t = max(j_end, t)
        for i in range(m):
            j_lst.append([t, 'R'])
            t += j_time
            j_end = t

total_lst = sorted(s_lst+j_lst)
s_num = []
j_num = []
for i in range(len(total_lst)):
    if total_lst[i][1] == 'B':
        s_num.append(i+1)
    else:
        j_num.append(i+1)
print(len(s_num))
print(*s_num)
print(len(j_num))
print(*j_num)
