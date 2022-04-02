'''
첫째 줄에 N이 주어진다. N은 50보다 작거나 같은 자연수이다.
둘째 줄에는 각 크레인의 무게 제한이 주어진다. 이 값은 1,000,000보다 작거나 같다.
셋째 줄에는 박스의 수 M이 주어진다. M은 10,000보다 작거나 같은 자연수이다.
넷째 줄에는 각 박스의 무게가 주어진다. 이 값도 1,000,000보다 작거나 같은 자연수이다.
3
6 8 9
5
2 5 2 4 7
5 5 4
'''
import sys

input = sys.stdin.readline

N = int(input().strip())
crain_lst = sorted(list(map(int, input().split())))
M = int(input())
box_lst = sorted(list(map(int, input().split())))

def bfs():
    day = 0
    if crain_lst[-1] < box_lst[-1]:
        # print('-1')
        day -= 1
    while sum(box_lst) != 0 and box_lst[-1] <= crain_lst[-1]:
        start = N - 1 ; final = len(box_lst) - 1
        while start >= 0 and final >= 0:
            if crain_lst[start] >= box_lst[final] and box_lst[final]:
                box_lst[final] = 0
                start -= 1; final -= 1
            else:
                final -= 1
            if not box_lst:
                break
        day += 1
    print(day)

bfs()

'''
3
10 6 5
11
6 8 9 6 8 6 9 6 8 6 9
11 5 0
11 5 0
9 4 0
7 3 0 
5 2 0
3 1 0
1 0 0


7 8 9 10
6 7 8 9
6 6 7 8
6 6 6 7
6 6 6 6
5 5 5 5

'''