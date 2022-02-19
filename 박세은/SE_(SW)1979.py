import sys
sys.stdin = open('input.txt')


def count_word(arr):
    answer = 0
    for i in range(N):
        count = 0
        for j in range(N):
            # 1이 나오면 몇글자 까지 들어갈 수 있는지 세기
            if arr[i][j] == 1:
                count += 1
            # 만약 중간에 0 이 나오면 이제까지의 count 들어갈 단어의 길이와 같은지 판별
            else:
                if count == K:
                    answer += 1
                    count = 0
                else:
                    count = 0
        # for 문이 끝나고 이제까지의 count 들어갈 단어의 길이와 같은지 판별
        if count == K:
            answer += 1
    return answer


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())  # N*N 배열, 숫자길이
    arr = [list(map(int, input().split())) for _ in range(N)]

    col_arr = []
    for i in range(N):
        a = [arr[j][i] for j in range(N)]
        col_arr.append(a)

    result = count_word(arr) + count_word(col_arr)
    print(f'#{tc} {result}')