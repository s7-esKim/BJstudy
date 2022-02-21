import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    # N = 수강생의 수, K = 제출한 사람의 수
    N, K = map(int, input().split())
    # 제출한 학생의 번호 list
    arr = list(map(int, input().split()))

    # 학생들의 list
    student_list = [i for i in range(1, N+1)]
    # 제출하지 않는 학생들의 list
    no_homework = {i for i in range(1, N+1)}

    # 제출한 학생 목록에 없다면 no_homework 안에 값 추가
    for i in student_list:
        for j in arr:
            if i == j:
                no_homework.remove(i)

    # no_homework -> set 에서 str 으로 바꾸고 값들 사이에 공백을 추가하여 출력
    answer = ' '.join(map(str, no_homework))

    print(f'#{tc} {answer}')