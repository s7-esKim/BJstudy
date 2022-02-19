import sys
sys.stdin = open('s_input.txt')

def check(n):
    n = str(n)
    for k in range(len(n)-1):
        if n[k] > n[k+1]:
            return False
    return True

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_num = -999
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            num = arr[i] * arr[j]
            if max_num < num and check(num):
                max_num = num
    print(f'#{tc} {max_num}')