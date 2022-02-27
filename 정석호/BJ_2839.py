T = int(input())

bag1, bag2 = 5, 3
cnt = 0

while T >= 0: #18
    if T % bag1 == 0:
        cnt += T // bag1
        print(cnt)
        break
    T -= 3
    cnt += 1
else:
    print(-1)




