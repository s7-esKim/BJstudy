# 수강생들 번호 1~N (제출하지 않은 사람 오름차순)
# 수강생 2 <= n <= 100

import sys
sys.stdin = open('1209.txt')

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split()) # n = 수강생수 m = 제출 수
    a = list(map(int, input().split())) # a = 제출 한 학생의 번호


    student_lst = []  #학생수 리스트
    for i in range(1, n+1):
        student_lst.append(i)

    no_submit = list(set(student_lst) - set(a))

    total = ' '.join(map(str, no_submit))

    print(f'#{tc} {total}')






