# 처음에는 주석의 코드대로 짰으나 런타임에러가 발생하여 수정
# while True:
#     string = list(input())
#     if string == '.':
#         break
#
#     stack = []
#     for i in string:
#         if i == '(' or i == '[' or i == '.':
#             stack.append(i)
#         elif stack and (i == ')' or i == ']'):
#             if i == ')' and stack[-1] == '(':
#                 stack.pop()
#             elif i == ']' and stack[-1] == '[':
#                 stack.pop()
#
#     if len(stack) == 1:
#         print('yes')
#     else:
#         print('no')



while True:                                 # 문자열 .이 나올때까지 반복
    string = input()
    if string == '.':
        break

    stack = []
    for i in string:
        if i == '(' or i == '[':            # 여는 소괄호나 여는 대괄호가 나오면 stack에 추가
            stack.append(i)
        elif i == ')':                      # 닫는 소괄호가 나왔을 때 짝이 이뤄지면 stack에서 제거
            if stack and stack[-1] == '(':
                stack.pop()
            else:                           # 시간을 줄이기 위해 짝이 안맞다면 바로 break
                stack.append(i)
                break
        elif i == ']':                      # 닫는 대괄호가 나왔을 때 짝이 이뤄지면 stack에서 제거
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
                break

    if len(stack) == 0:
        print('yes')
    else:
        print('no')
