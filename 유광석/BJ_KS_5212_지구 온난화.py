N, M = map(int, input().split())
arr = [['.'] * (M+2)] +  [['.'] + list(input()) + ['.'] for _ in range(N)] + [['.'] * (M+2)]
sea = []
for i in range(N+2):
    for j in range(M+2):
        if arr[i][j] == 'X':
            cnt = 0
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ni = i + di
                nj = j + dj
                if arr[ni][nj] == '.':
                    cnt += 1
                if cnt >= 3:
                    sea.append((i, j))

for r, c in sea:
    arr[r][c] = '.'

i = 0
while True:
    if arr[i].count('X') == 0:
        arr.pop(i)
    else:
        break

j = len(arr) - 1
while True:
    if arr[j].count('X') == 0:
        arr.pop()
        j -= 1
    else:
        break

minj = 11
maxj = 0
for i in range(len(arr)):
    for j in range(M+2):
        if arr[i][j] == 'X':
            if j < minj:
                minj = j
            if j > maxj:
                maxj = j

if arr:
    for i in arr:
        print(''.join(i[minj:maxj+1]))
else:
    print('X')
            