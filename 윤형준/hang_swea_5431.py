import sys
sys.stdin = open('input 5431.txt')

T = int(input())

for tc in range(1,T+1):
    N, K = map(int, input().split())
    student_lst = set(x for x in range(1,N+1))
    submit_lst = set(list(map(int, input().split())))

    unsubmit_lst = list(student_lst - submit_lst)

    print(f'#{tc}', end=' ')
    for unsub in unsubmit_lst:
        print(unsub, end = ' ')
    print()
