from collections import deque

di, dj = ((0,-1,1,0,0,-1,-1,1,1), (0,0,0,-1,1,-1,1,-1,1))

def bfs():
    q = deque()
    q.append([7,0])

    while q:
        v = [[0]*8 for _ in range(8)]
        for _ in range(len(q)):
            ci, cj = q.popleft()
            if ci == 0 and cj == 7:
                return 1

            if chess[ci][cj] == '#':
                continue

            for i in range(9):
                ni, nj = ci+di[i], cj+dj[i]
                if 0<=ni<8 and 0<=nj<8 and chess[ni][nj] != '#' and not v[ni][nj]:
                    v[ni][nj] = 1
                    q.append([ni, nj])

        chess.pop()
        chess.insert(0, ['.', '.', '.', '.', '.', '.', '.', '.'])

    return 0

chess = [list(input()) for _ in range(8)]
v = [[0]*8 for _ in range(8)]

print(bfs())