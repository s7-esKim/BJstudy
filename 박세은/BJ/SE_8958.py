T = int(input())
for tc in range(1, T+1):
    arr = list(input())  # OX list

    score = 0  # 점수를 저장할 값
    sum_score = 0  # 점수의 합을 저장할 값
    for i in arr:
        # i가 'O' 라면 score 에 계속해서 저장
        # score 값을 sum_score 에 저장
        if i == 'O':
            score += 1
            sum_score += score
        # 중간에 'X' 가 나오면 score 값 초기화
        else:
            score = 0

    print(sum_score)