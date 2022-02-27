T = int(input())

for tc in range(1, T+1):
    arr = input()
    # 레이저 다른 모양으로 바꾸기
    Laser = arr.replace('()', 'L')
    # L만나면 반으로 자르기
    # '(' 만나면 막대기 갯수 1개씩 증가
    # 도중에 L 만나면 막대기들 반으로 갈라짐
    # ')' 만나면 막대기 더이상 끝
    bar = 0
    result = 0
    for i in range(len(Laser)):
        if Laser[i] == '(':
            bar += 1
        elif Laser[i] == 'L':
            result += bar
        else:
            bar -= 1
            result += 1

    print(f'#{tc} {result}')




