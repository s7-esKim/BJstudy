lst = list(map(int, input().split()))
if lst[1]%2 == 0:
    repair_num = 0
    for i in range(lst[0]):
        chess = input().split('BW')
        for j in chess:
            if len(j) > 1:
                repair_num += len(j)//2
else:
    repair_num = 0
    for i in range(lst[0]):
        chess = input().split('BW')
        for j in chess:
            if len(j) > 1:
                if len(j)%2 ==0:
                    repair_num += (len(j)//2)
                else:
                    repair_num += (len(j)//2 + 1)
        print(repair_num)
print(repair_num)