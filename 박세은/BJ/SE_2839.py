N = int(input())
answer = 0
# 설탕이 0이 될 때까지 반복
while N >= 0:
    # 만약 설탕을 5kg 봉지로 담을 수 있다면 그 몫을 출력하고 반복문 종료
    if N % 5 == 0:
        answer += (N // 5)
        print(answer)
        break
    # 5kg 봉지로 나누어 떨어지지 않으면 3kg 봉지 하나 사용
    else:
        N -= 3
        answer += 1
# 정확하게 나누어 담을 수 없다면 -1 출력
else:
    print(-1)