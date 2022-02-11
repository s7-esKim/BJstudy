n = int(input())

arr =[]

for i in range(n):
    a = input()
    arr.append(a)


for i in range(len(arr)):
    count = 0
    total = 0
    for j in arr[i]:
        if j == 'O':
            count += 1
            total += count
        else:
            count = 0
    print(total)