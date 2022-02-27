import sys
sys.stdin = open('s_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 정수의 개수
    N_list = list(map(int, input().split()))

    new_list = []  # 각 숫자의 곱이 들어갈 list
    for i in range(len(N_list) - 1):
        for j in range(i+1, len(N_list)):
            new_list.append(N_list[i] * N_list[j])

    my_max = 0
    for i in new_list:
        str_i = str(i)  # 숫자형을 문자형으로 바꿔서 비교하기
        for j in range(len(str_i)-1):
            if int(str_i[j]) > int(str_i[j+1]):  # 앞의 숫자가 뒤의 숫자보다 크다면 for 문 종료
                break
        else:  # 그렇지 않다면 단조 증가하는 수 : max 값 찾기
            if i > my_max:
                my_max = i

    if my_max == 0:
        print(f'#{tc} {-1}')
    else:
        print(f'#{tc} {my_max}')
