import sys
sys.stdin = open('2.txt')
T = 2
for tc in range(T):
    string = input() # mirkovC4nizCC44
    bomb = input() # c4

    bomb_last = bomb[-1]  # 폭발물의 마지막 문자 C4 = 4
    stack = [] # 스택 하나 만들고 string 순회 하면서 하나씩 넣을거임
    bomb_len = len(bomb) # 폭발물 문자열의 길이 2

    for i in string:
        stack.append(i) # stack = mirkovC4nizCC44
        if i == bomb_last and ''.join(stack[-bomb_len:]) == bomb: # 음수 슬라이싱 < 처음알았음
            del stack[-bomb_len:] # bomb이랑 같으면 지워버리기

    result = ''.join(stack) # 스택에 있는거 문자만 뺴서 result에 저장
    if result == '': # 비어있으면 FRULA
        print("FRULA")
    else:
        print(result)


