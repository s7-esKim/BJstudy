import sys
sys.stdin = open('input (1).txt')

T = int(input())

for tc in range(1, 1 + T):
    N, K = map(int, input().split())
    arr = [''.join(input().split()) for i in range(N)]  # 문자열로 한줄씩 받아 준다.

    c_arr = []                                          # 전치를 이요해서 세로 문자열을 만든다
    for i in range(N):
        c_t = ''
        for j in range(N):
            c_t += arr[j][i]
        c_arr.append(c_t)

    total_arr = arr + c_arr                             # 가로, 세로 문자열을 더해서 하나의 리스트로
    word = '1' * K                                      # 단어의 길이를 1*K로만들고

    ans = 0
    for i in range(N * 2):                              # 리스트에서 순회를 돌면서 한줄 씩 비교
        for j in range(N - K + 1):
            if total_arr[i][j:j+K] == word:             # 그 부분이 단어랑 같다면
                if j + K == N:                          # 앞 뒤 '1'이 아니고, 인덱스 시작과 끝을 제한
                    if total_arr[i][j-1] != '1':
                        ans += 1
                elif j == 0:
                    if total_arr[i][j+K] != '1':
                        ans += 1
                else:
                    if total_arr[i][j-1] != '1' and total_arr[i][j+K] != '1':
                        ans += 1
    print(f'#{tc} {ans}')                               # 결과에 담아 출력








