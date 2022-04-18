'''
8
11110000
11110000
00011100
00011100
11110000
11110000
11110011
11110011
((110(0101))(0010)1(0001))
'''
# 왼쪽 위 오른쪽 위 왼쪽 아래 오른쪽 아래
import sys
input = sys.stdin.readline

def merge(lu, ru, ld, rd):
    lst = [*lu, *ru, *ld, *rd]
    if len(lst)==4 and (sum(lst) == 0 or sum(lst) == 4):
        return [lst[0]]
    else:
        return ['('] + lst + [')']
def partition(i, c, n): # 행시작 , 열시작, 나눈 개수
    global visit
    if n == 1:
        return [arr[i][c]]
    left_up = partition(i, c, n//2)
    right_up = partition(i, c + n // 2, n // 2)
    left_down = partition(i + n // 2 , c, n // 2)
    right_down = partition(i + n // 2, c + n // 2, n // 2)

    return merge(left_up, right_up, left_down, right_down)

N = int(input())
arr = [list(map(int, input().strip())) for _ in range(N)]

visit = []
partition_s = partition(0, 0, N)
print(''.join(list(map(str,partition_s))))

