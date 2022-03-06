lst = [i for i in range(1, int(input())+1)]
front = -1
rear = len(lst)
while front < rear - 2:
    front += 2
    v = lst[front]
    lst += [v]
    rear += 1

print(lst[front])


    