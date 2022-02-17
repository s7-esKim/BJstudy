import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, 2):                      # 인풋 받는 부분
    word = [input() for _ in range(5)]          # 줄은 5줄 고정이니 5만큼 받고
    max_len = 0                                 # 공백 문자가 포함 되어있으니 최대 길이 재줌
    for i in word:                              # text의 최대 길이를 구하는 부분
        if len(i) > max_len:
            max_len = len(i)

    for i in range(5):                          # 최대 길이 보다 작은 부분은 공백
        if max_len - len(word[i]) != 0:         # 단어의 길이가 최대 길이가 아니면
            a = word[i] + ' ' * (max_len - len(word[i]))  # 공백을 더해준다!
            word[i] = a                         # 그리고 다시 i에 넣어줌
    # print(word)
    c_list = []                                 # 전치행렬 만드는 부분
    for i in range(max_len):
        c_word = ''
        for j in range(5):
            c_word += word[j][i]
        c_list.append(c_word)
    # print(c_list)
    ans = ''.join(c_list)                       # 출력과 동일하게 리스트를 풀어주고
    real_ans = ans.replace(' ', '')             # 공백을 제거한 후
    print(f'#{tc} {real_ans}')                  # 알맞게 출력