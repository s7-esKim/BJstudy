import sys
sys.stdin = open('GNS_test_input.txt')

word = [_ for _ in range(0, 10)]
new_word = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

T = int(input())
for t in range(T):                                  # 인풋 형식이 이상해서 맞춰서 받기 위함
    tc, N = input().split()
    new_words = input().split()

    for i in range(10):                             # 받은 문자열 리스트와 만들어둔 리스트를 비교하여
        for j in range(int(N)):                     # 값이 같으면 같은 인덱스인 정수로 바꿔주는 과정
            if new_word[i] == new_words[j]:
                new_words[j] = word[i]

    for i in range(int(N) - 1, 0, -1):              # 정수로 만든 문자열 리스트를 버블 소트로 정렬
        for j in range(0, i):
            if new_words[j] > new_words[j+1]:
                new_words[j], new_words[j+1] = new_words[j+1], new_words[j]

    for i in range(10):                             # 위와 동일하게 정수를 다시 문자열로 인덱스에 맞게 바꿔서 넣어줌
        for j in range(int(N)):
            if word[i] == new_words[j]:
                new_words[j] = new_word[i]
    print(tc)                                       # 형식에 맞게 출력
    print(*new_words)


# for i in range(10
#   for j in number:
#       if num[i] == j:
#           result.append(j)