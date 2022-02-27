import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    money = int(input())

    money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    answer_list = [0] * len(money_list)

    while money > 9:
        for i in range(len(money_list)):
            answer_list[i] = money // money_list[i]
            money = money % money_list[i]

    answer = ''
    for i in answer_list:
        answer += str(i)
        answer += ' '

    print(f'#{tc}\n{answer}')


