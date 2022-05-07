def check(s, e):
    global cnt

    if s > e:
        return

    if s == e:
        cnt +=1
        return
    
    for i in nums:
        check(s+i, e)


nums = [1, 2, 3]
num = [i for i in range(1, 12)]

for i in range(len(num)):
    cnt = 0
    check(0 , num[i])
    num[i] = cnt

for i in range(int(input())):
    print(num[int(input())-1])