def f(x, y, N):
    a = arr[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if a != arr[i][j]:
                print('(', end='')
                f(x, y, N//2)
                f(x, y+N//2, N//2)
                f(x+N//2, y, N//2)
                f(x+N//2, y+N//2, N//2)
                print(')', end='')
                return
    if a == 0:
        print('0', end='')
        return
    else:
        print('1', end='')
        return


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
f(0, 0, N)