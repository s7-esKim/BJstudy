# 1. 숫자든 알파벳이든 string으로 받기
# 2. 문자가 없을경우 FRULA 출력
# 3. 폭발 문자열은 같은 문자가 없다
text = list(input())
remove_text = list(input())
stack = []
# 시간 초과남.... 다른 방법을 찾아봐야 할듯...
# for문으로 2번비교해서 그런듯.. 한번에 폭발문자열을 비교할 수 있는 방법 생각하기
# for i in range(len(text)):
#     stack.append(text[i])
#     for j in remove_text:
#         try:
#             for k in stack:
#                 if k == j:
#                     stack.pop()
#         except IndexError:
#             pass

# 1. stack에 첫번째 글자 append
# 2. 폭발 문자랑 비교해서 같으면 pop
# 2-2 mirkovC4 << C4를 한번에 날려버리고 다시 append시작 mirkovnizCC44인 경우에는 C4날리고 C4한번더 날리고 결과출력
# 2-3 폭발문자 길이만큼 비교하기
# 2-4 폭발문자 길이만큼 없애기
for i in range(len(text)):
    stack.append(text[i])
    if stack[-len(remove_text):] == remove_text:
        for j in range(len(remove_text)):
            stack.pop()

if not stack:
    print('FRULA')
else:
    print("".join(stack))

