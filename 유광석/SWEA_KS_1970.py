money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]    # 돈의 종류를 리스트로 만들고

T = int(input())

for ts in range(T):
    don = int(input())
    ans = [0] * 8                                       # 결과를 담을 리스트를 생성
    for i in range(len(money)):                         # 위의 돈의 종류로 순회를 돌면서
        if don // money[i] >= 1:                        # 들어온 돈과 돈의 종류를 나눈 몫이 1보다 크면
            ans[i] += don // money[i]                   # 결과 리스트에 몫만큼 추가해주고
            don -= don  // money[i] * money[i]          # 그만큼 돈에서 빼준다
    
    print(f'#{ts + 1}')
    print(*ans)