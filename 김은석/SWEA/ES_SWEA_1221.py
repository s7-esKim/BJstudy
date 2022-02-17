T = int(input())

for tc in range(1, T+1):
    # #1 7041 인풋
    N, length = input().split()
    number = list(map(str, input().split()))

    # 숫자체계
    num = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

    result = []
    for i in range(10):
        for j in number:
            if num[i] == j:
                result.append(j)

    print(N)
    print(*result)