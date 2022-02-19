# 인덱스 에러가 안나는게 중요
T = int(input())

for tc in range(1, T+1):
    arr = [list(map(str, input())) for _ in range(5)]

    max_len = 0
    for i in range(5):
        if max_len < len(arr[i]):
            max_len = len(arr[i])

    # max_len 길이만큼 다시 정사각형 행렬을 만들기
    new_arr = [[0]*max_len for i in range(5)]

    # 여기에 인풋값 넣어버리기
    for i in range(5):
        for j in range(len(arr[i])):
            new_arr[i][j] = arr[i][j]
    print(new_arr)

    result = ''
    # 0이 아닐때만 세로로 출력하기
    for i in range(max_len):
        for j in range(5):
            if new_arr[j][i] != 0:
                result += new_arr[j][i]

    print(f'#{tc} {result}')





