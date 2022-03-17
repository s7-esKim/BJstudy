xy_lst = []
for i in range(100):
    xy_lst.append([0]*100)

def sum_array(array):
    tot = 0
    for lst in array:
        for i in lst:
            tot += i
    return tot

for i in range(4):
    x1,y1,x2,y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            xy_lst[y][x] = 1

print(sum_array(xy_lst))