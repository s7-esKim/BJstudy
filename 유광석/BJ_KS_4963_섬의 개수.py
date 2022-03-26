while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        exit()

    arr = [list(map(int, input().split())) for _ in range(H)]
    cnt = 0

    dr = [-1, 1, 0, 0, -1, -1, 1, 1]
    dc = [0, 0, -1, 1, -1, 1, -1, 1]

    # def DFS(i, j):
    #     global cnt
    #     cnt += 1
    #     stack = [(i, j)]
    #     arr[i][j] = 0

    #     while stack:
    #         r, c = stack.pop()
    #         print((r, c))
    #         for k in range(8):
    #             nr = r + dr[k]
    #             nc = c + dc[k]

    #             if 0 <= nr < H and 0 <= nc < W and arr[nr][nc] == 1:
    #                 arr[nr][nc] = 0
    #                 stack.append((nr, nc))

    def DFS(r, c):
        for k in range(8):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nr < H and 0 <= nc < W and arr[nr][nc] == 1:
                arr[nr][nc] = 0
                DFS(nr, nc)


    # def BFS(i, j):
    #     global cnt
    #     cnt += 1
    #     queue = [(i, j)]
    #     arr[i][j] = 0

    #     while queue:
    #         r, c = queue.pop(0)
    #         print((r, c))

    #         for k in range(8):
    #             nr = r + dr[k]
    #             nc = c + dc[k]

    #             if 0 <= nr < H and 0 <= nc < W and arr[nr][nc] == 1:
    #                 arr[nr][nc] = 0
    #                 queue.append((nr, nc))

    for i in range(H):
        for j in range(W):
            if arr[i][j] == 1:
                arr[i][j] = 0 
                DFS(i, j)
                cnt += 1
                
    print(cnt)

'''
5 5
1 1 1 1 1
1 0 0 0 0
0 1 1 1 1
1 0 0 0 0
1 1 1 1 0
0 0
'''