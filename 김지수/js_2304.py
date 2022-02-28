from pprint import pprint
import sys
sys.stdin = open('1.txt')
n = int(input()) # 기둥 갯수 7
lst = []
for i in range(n):
    lst.append(list(map(int,input().split())))
lst.sort()
width = 0
high = 0
for i in range(len(lst)):
    for j in range(len(lst)):
        if lst[i][0] > width:
            width = lst[i][0]
        if lst[i][1] > high:
            high = lst[i][1]
print(lst)
total = 0
height = [] # 4 6 3 10 4 6 8
for h in range(len(lst)):
    height.append(lst[h][1])
idx = 0
for i in range(idx, len(lst)-1):
    if lst[i][1] < lst[i+1][1]:
        total += lst[i][1] * (lst[i+1][0] - lst[i][0])
    if lst[i][1] > lst[i+1][1] and max(height) > lst[i][1] :
        tall_idx = 0
        for k1 in range(i+1, len(lst)):
            if lst[i][1] < lst[k1][1]:
                tall_idx = k1
                break
        total += lst[i][1] * (lst[tall_idx][0] - lst[i][0])
    if lst[i][1] == max(height):
        total += lst[i][1]
        middle_idx = 0
        for k2 in range(i+1, len(lst)):
            if lst[k2][1] > middle_idx:
                middle_idx = k2
        total += lst[middle_idx][1] * (lst[middle_idx][0] - lst[i][0])
print(total)
