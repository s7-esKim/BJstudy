import sys

for tc in range(int(sys.stdin.readline().rstrip())):
    N = int(sys.stdin.readline().rstrip())
    lst = []
    cnt = 0
    for i in range(N):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        lst.append((x, y))

    lst.sort()
    min_y = lst[0][1]
    cnt = 1
    for i in range(1, N):
        if lst[i][1] < min_y:
            cnt += 1
            min_y = lst[i][1]
    
    print(cnt)

