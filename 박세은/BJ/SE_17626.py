def search():
    global answer
    for i in range(l):
        if arr[i] == N:
            answer = 1
            return

    for i in range(l):
        for j in range(l):
            if arr[i] + arr[j] == N:
                answer = 2
                return

    for i in range(l):
        for j in range(l):
            for k in range(l):
                if arr[i] + arr[j] + arr[k] == N:
                    answer = 3
                    return

    if answer == 0:
        answer = 4
        return


N = int(input())
answer = 0

arr = []
for i in range(1, 224):
    arr.append(i**2)
l = len(arr)

search()
print(answer)