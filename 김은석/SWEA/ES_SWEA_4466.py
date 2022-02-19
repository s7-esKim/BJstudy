def bubblesort(a):
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    a = bubblesort(arr)
    b = a[::-1]
    total = 0
    for i in range(K):
        total += b[i]

    print(f'#{tc} {total}')