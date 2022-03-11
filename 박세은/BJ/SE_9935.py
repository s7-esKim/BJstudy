S = input()  # 문자열
B = input()  # 폭발 문자열
stack = []

i = 0
while i < len(S):
    # stack 에 문자열 추가
    stack.append(S[i])
    # 만약 추가한 문자열 부터 B의 길이까지 문자열이 B와 같다면 추가한 값 pop
    # index 번호는 B랑 똑같은 문자열이 끝난 다음 지점 부터
    if S[i:i+len(B)] == B:
        stack.pop()
        i += len(B)
    # stack 을 돌아보며 stack 의 마지막 값에서 B의 길이만큼 뺀것이 B를 뒤집은 것과 같다면
    # B의 길이만큼 빼주고 i값 증가
    elif ''.join(stack[-1:-len(B)-1:-1]) == B[::-1]:
        for j in range(len(B)):
            stack.pop()
        i += 1
    # 아무것도 아닐 시 i값 증가
    else:
        i += 1

# stack 이 비어있으면 'FRULA' 출력, 그렇지 않으면 stack 의 문자열 출력
if len(stack) == 0:
    print('FRULA')
else:
    print(''.join(stack))
