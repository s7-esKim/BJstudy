import sys
sys.stdin = open('sample_input.txt')

def bubble(n):
    for i in range(len(n)-1, 0, -1):
        for j in range(i):
            if n[j] > n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]
    return n

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    score = list(map(int, input().split()))
    bubble_score = bubble(score) # 40 80 100

    total = 0
    for i in range(K):
        total += (bubble_score[::-1])[i]

    print(f'#{tc} {total}')



