# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    N, K = list(map(int, input().split()))
    good_std = list(map(int, input().split()))
    std = [i for i in range(1,N+1)]
    # 5명 이면 [1 2 3 4 5]
    # 2 5 3 베스트 [1 4]  <<< 2 5 3을 빼는방법이 필요
    # [1,4] 만 남길려면 새로운 리스트 변수 생성
    bad_std = []
    # [1,4]를 위에 넣어야 하는데
    for j in range(1,N+1):
        if j not in good_std:
            bad_std.append(str(j)) # join함수 쓰기 위해서 j를 숫자가 아닌 문자열로 바꿈
    result = ' '.join(bad_std)  # 리스트를 뽑는게 아니라 숫자를 뽑아야 하기 때문에 join함수 써서 공백있는 문자열로 변환
    print(f'#{tc} {result}')
