import sys
input = sys.stdin.readline
from collections import deque


def bfs():
    q = deque([[0, 0]])
    arr[0][0] = -1
    count = 0
    while q:
        j, i = q.popleft()
        if j % 2:
            dj = [0, 1, 0, -1, -1, 1]
            di = [1, 0, -1, 0, 1, 1]
        else:
            dj = [0, 1, 0, -1, -1, 1]
            di = [1, 0, -1, 0, -1, -1]
        for k in range(6):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= nj < H+2 and 0 <= ni < W+2:
                if arr[nj][ni] == 0:
                    q.append([nj, ni])
                    arr[nj][ni] = -1
                elif arr[nj][ni] == 1:
                    count += 1
    return count


W, H = map(int, input().split())
arr = [[0]*(W+2)] + [[0]+list(map(int, input().split()))+[0] for _ in range(H)] + [[0]*(W+2)]
print(bfs())
