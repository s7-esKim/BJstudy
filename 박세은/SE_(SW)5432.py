import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    A = str(input())

    list_A = []                            # input 값 -> list
    i = 0
    while i < len(A):
        if A[i] == '(' and A[i+1] == ')':  # '(' 바로 뒤에 ')' 나오면 laser
            list_A.append('laser')
            i += 2                         # '()' 다음 값으로
        elif A[i] == '(':                  # '(' 하나 있을 때는 1
            list_A.append(1)
            i += 1
        elif A[i] == ')':                  # ')' 하나 있을 때는 -1
            list_A.append(-1)
            i += 1

    plus = 0
    answer = 0
    for j in list_A:
        if j == 'laser':       # laser 를 만나면
            answer += plus     # plus 에 담아뒀던 값을 answer 에 더하기
        elif j == 1:
            plus += 1          # 1을 만나면 쇠막대기 하나 시작
        else:
            plus -= 1          # -1을 만나면 쇠막대기 하나 끝남
            answer += 1        # 끝난 쇠막대기 하나 추가
    print(f'#{tc} {answer}')