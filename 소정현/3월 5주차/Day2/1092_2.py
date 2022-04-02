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
box_lst = sorted(list(map(int, input().split())), reverse=True)

def bfs():
    day = 0
    if crain_lst[-1] < box_lst[-1]:
        day -= 1
        print(day)
        return
    for i in crain_lst:
        if i < box_lst[-1]:
            crain_lst.pop(0)
        else:
            break
    while box_lst:
        for i in range(len(crain_lst)-1, -1, -1):
            for box in box_lst:
                if crain_lst[i] >= box:
                    box_lst.remove(box)
                    break
            else:
                crain_lst.pop(i)
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