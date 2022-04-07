def quadtree(n,x,y):
    temp = arr[x][y]

    for i in range(x,x+n):
        for j in range(y,y+n):
            if temp != arr[i][j]:
                print('(', end='')
                quadtree(n//2,x,y)
                quadtree(n//2,x,y+n//2)
                quadtree(n//2,x+n//2,y)
                quadtree(n//2,x+n//2,y+n//2)
                print(')', end='')
                return

    if temp == 0:
        print('0', end='')
        return
    else:
        print('1', end='')
        return

N = int(input())

arr = [list(map(int, input())) for _ in range(N)]
quadtree(N,0,0)