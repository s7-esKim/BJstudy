import sys; input = sys.stdin.readline

def divNConq(size, r, c):
    global answer
    if size == 1:
        answer += str(matrix[r][c])
        return
    if chk_arr(size, r, c, matrix[r][c]):
        answer += str(matrix[r][c])
        return
    half = size // 2
    # 좌상
    answer += "("
    divNConq(half, r, c)
    # 우상
    divNConq(half, r, c + half)
    # 좌하
    divNConq(half, r + half, c)
    # 우하
    divNConq(half, r + half, c + half)
    answer += ")"
    return


def chk_arr(size, r, c, sel):
    for i in range(r, r + size):
        for j in range(c, c + size):
            if matrix[i][j] != sel:
                return False
    return True

N = int(input())
matrix = [list(map(int, list(input().rstrip()))) for _ in range(N)]
answer = ''
divNConq(N, 0, 0)
print(answer)