# 1번 12345 12345 12345 순서대로
# 2번 21232425 21232425 2가 항상 홀수번째
# 3번 3311224455 3311224455

def check_answer(numbers):
    ans_lst = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    cnt_1 = 0;
    cnt_2 = 0;
    cnt_3 = 0
    for i in range(len(numbers)):
        if ans_lst[0][i % len(ans_lst[0])] == numbers[i]:
            cnt_1 += 1
        if ans_lst[1][i % len(ans_lst[1])] == numbers[i]:
            cnt_2 += 1
        if ans_lst[2][i % len(ans_lst[2])] == numbers[i]:
            cnt_3 += 1

    max_cnt = cnt_1;
    max_key_visit = [1]
    if max_cnt < cnt_2:
        max_key_visit = [2]
        max_cnt = cnt_2
    elif max_cnt = cnt_2:
        max_key_visit.append(2)
    if max_cnt < cnt_3:
        max_key_visit = [3]
        max_cnt = cnt_3
    elif max_cnt = cnt_3:
        max_key_visit.append(3)
    return max_key_visit


def solution(answers):
    answer = check_answer(answers)
    return answer
ans = solution([1,3,2,4,2])
print(ans)