def change(num):
    if switch[num] == 0:
        switch[num] = 1
    else:
        switch[num] = 0
    return

N = int(input())
switch = ['X'] + list(map(int, input().split()))
student = int(input())
for _ in range(student):
    genre, idx = map(int, input().split())

    if genre == 1:
        for i in range(idx, N+1, idx):
            change(i)
    else:
        change(idx)
        for k in range(1, N//2):
            if idx-k < 1 or idx+k > N:
                break
            if switch[idx-k] == switch[idx+k]:
                change(idx-k)
                change(idx+k)
            else:
                break
for i in range(1, N+1):
    print(switch[i], end=' ')
    if i % 20 == 0:
        print()
