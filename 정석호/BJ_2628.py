L, C = map(int, input().split())
low = [0]
column = [0]
N = int(input())
for i in range(N):
    line, inx = map(int, input().split())
    if line == 0:
        column.append(inx)
    elif line == 1:
        low.append(inx)
low.append(L)
column.append(C)
low.sort()
column.sort()

max_low = 0
for i in range(1, len(low)):
    low_gap = abs(low[i] - low[i - 1])
    if max_low < low_gap:
        max_low = low_gap

max_column = 0
for i in range(1, len(column)):
    column_gap = abs(column[i] - column[i - 1])
    if max_column < column_gap:
        max_column = column_gap

print(max_low * max_column)