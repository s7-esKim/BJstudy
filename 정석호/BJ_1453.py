T = int(input())
attend_lst = list(map(int, input().split()))

boxes = [0] * 101
cnt = 0
for i in attend_lst:
    if boxes[i] == 0:
        boxes[i] += 1
    else:
        cnt += 1
print(cnt)




