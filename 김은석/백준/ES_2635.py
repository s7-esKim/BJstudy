N = int(input())
num_list = []
cnt = 0

for i in range(1, N+1):
    temp = [N]
    temp.append(i)

    while True:
        if temp[-2] - temp[-1] < 0:
            break
        else:
            temp.append(temp[-2] - temp[-1])

    if cnt < len(temp):
        cnt = len(temp)
        num_list = temp

print(cnt)
print(*num_list)