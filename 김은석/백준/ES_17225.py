from collections import deque

A, B, N = map(int, input().split())
s_start = deque()
j_start = deque()
s_end, j_end = 0, 0

for _ in range(N):
    t, c, m = input().split()
    t = int(t)

    if c == 'B':
        t = max(t, s_end)

        for i in range(int(m)):
            s_start.append([t, 'B'])
            t += A
            s_end = t

    elif c == 'R':
        t = max(t, j_end)

        for i in range(int(m)):
            j_start.append([t, 'R'])
            t += B
            j_end = t

total_list = s_start + j_start
total_list = sorted(total_list, key=lambda x: [x[0], x[1]])

s_present, j_present = [], []

for idx, present in enumerate(total_list):
    if present[1] == 'B':
        s_present.append(idx + 1)
    else:
        j_present.append(idx + 1)

print(len(s_present))
print(*s_present)
print(len(j_present))
print(*j_present)