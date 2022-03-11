R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
answer = 1


def BFS():
    global answer
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # set 으로 중복값 제거
    queue = {(0, 0, arr[0][0])}

    while queue:
        # 행, 열, 알파벳
        x, y, a = queue.pop()
        # a 안에 지나온 알파벳이 다 저장: a의 길이 = count
        answer = max(answer, len(a))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # index 범위를 벗어나지 않고, a안에 같은 알파벳이 없다면
            # queue.add((행값, 열값, 알파벳 누적))
            if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] not in a:
                queue.add((nx, ny, a + arr[nx][ny]))

BFS()
print(answer)