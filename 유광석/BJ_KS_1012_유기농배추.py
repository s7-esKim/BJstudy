from pprint import pprint

# 재귀 오류가 나서 재귀 제한 풀어줌!
import sys
sys.setrecursionlimit(10**6)
# 1인 좌표값을 받아서 사방으로 인접한 부분의 1에 num을 더해줌
def check(a, b, arr):
    da = [-1, 1, 0, 0]
    db = [0, 0, -1, 1]
    
    for i in range(4):
        na = a + da[i]
        nb = b + db[i]
        
        if 0 <= na < N and 0 <= nb < M and arr[na][nb] == 1:
            arr[na][nb] += num
            check(na,nb,arr) 
    else:
        return

# 좌표값이 1인 점을 찾고 위의 check 함수를 실행함
# 만약에 1인 점이 없으면 flag를 True로 바꿔주고 종료
def find(arr):
    global flag
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                arr[i][j] += num
                check(i, j, arr)
                return arr
    else:
        flag = True
        return arr

# 인풋값과 단지 구별을 위한 num 설정


T = int(input())
for tc in range(T):
    flag = False
    num = 0
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]

    for i in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1

    # 좌표값이 1이 없을 때 까지 (= 1이면 아직 방문하지 않은 곳)
    while True:
        num += 1
        find(arr)
        if flag:
            break

    print(num-1)