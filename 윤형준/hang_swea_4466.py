import sys
sys.stdin = open('input 4466.txt')

def selection_sort(lst):
    for i in range(len(lst)-1):
        for j in range(i+1,len(lst)):
            if lst[i] < lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())

    score_lst = list(map(int, input().split()))
    selection_sort(score_lst)
    max_score = 0
    for k in range(K):
        max_score += score_lst[k]

    print(f'#{tc} {max_score}')





