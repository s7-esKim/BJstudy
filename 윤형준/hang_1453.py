N = int(input())

guests = list(map(int,input().split()))
lst = []
cnt = 0
for i in guests:
    if i not in lst:
        lst.append(i)
    else:
        cnt += 1
print(cnt)