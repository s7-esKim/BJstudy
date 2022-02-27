import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    pipe = input()
    cut = pipe.replace('()', '!')           # 레이저 부분을 느낌표로 바꿔준다!
    c_len = len(cut)                        # 바꿔주면 2문자가 1개가 됨으로 길이를 계산해줌

    idx = 0                                 # while문에서 쓰일 idx
    v = 0                                   # 파이프 갯수를 담을 value 값
    now_pipe = 0                            # 현재 파이프 갯수
    print(cut)
    while idx < c_len:                      # idx가 cut보다 작을때
        if cut[idx] == '(':                 # 여는괄호면 파이프 + 1
            now_pipe += 1
        elif cut[idx] == '!':               # 레이저를 만나면 지금까지 있던 파이프를 v 추가
            v += now_pipe
        else:
            now_pipe -= 1                   # 닫는 괄호면 현재 파이프 -1 해주고 v에 하나 추가
            v += 1
        idx += 1
    print(f'#{tc} {v}')                     # 출력!