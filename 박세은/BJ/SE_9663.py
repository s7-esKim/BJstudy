import sys
input = sys.stdin.readline

def chess(row):
    global count
    if row == N:
        count += 1
        return

    for j in range(N):
        for i in range(row):
            if arr[i] == j or row-i == abs(j-arr[i]):
               break
        else:
            arr[row] = j
            chess(row+1)


N = int(input())
count = 0
arr = [N] * N
chess(0)
print(count)



