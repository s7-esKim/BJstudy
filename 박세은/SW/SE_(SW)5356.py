import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(str, input())) for _ in range(5)]  # 문자열 list -> 문자열마다 길이가 다름
    # arr 중에 가장 긴 문자열의 길이 찾기
    max_len = 0
    for i in arr:
        if len(i) > max_len:
            max_len = len(i)

    answer = ''
    for i in range(max_len):         # 문자열이 가장 긴 것을 기준
        for j in range(5):           # 행의 값 : 5
            try:
                answer += arr[j][i]  # 행 우선 순회
            except IndexError:       # 값이 없는 경우에는 공백 넣기
                pass
    print(f'#{tc} {answer}')