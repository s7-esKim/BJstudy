import sys
sys.stdin = open('s_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))        # 인풋값을 받음
    x_nums = []                                   # 곱한수를 넣어줄 리스트를 만들어준다!
    for i in range(N - 1):                        # (N-1), (1+i, N) 이라는 범위로 자기 자신을 빼고 곱해서 리스트에 넣음
        for j in range(1 + i, N):
            x_nums.append(nums[i] * nums[j])

    increase = []                                 # 단조증가하는 수를 담아줄 리스트
    for k in map(str, x_nums):                    # 곱해준수들을 str로 바꾸고 map객체는 순회가능하니까 for문을 돌림
        if len(k) == 1:                           # 한자리수이면 그냥 리스트에 추가
            increase.append(k)
        else:
            for l in range(1, len(k)):            # 반복문에서 앞 숫자가 뒤 숫자보다 크면 break
                if int(k[l - 1]) > int(k[l]):     # 아니면  for - else 구문으로 단조증가 수를 리스트에 넣어줌
                    break
            else:
                increase.append(k)
    if increase == []:                            # 만약 빈리스트라면 증가하는 수가 없으므로 -1 출력
        print(f'#{tc} {-1}')
    else:
        ans = 0
        for mv in map(int, increase):             # 있으면 다시 int로 바꾸고 ans에 최댓값을 저장해서 출력
            if mv >= ans:
                ans = mv
        print(f'#{tc} {ans}')
