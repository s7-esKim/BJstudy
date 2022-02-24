# 줄마다 빙고인지 확인하기, 빙고면 b에다가 추가해서 리턴
def check(li):
    b = 0
    # 가로
    for i in li:
        xb = 0
        for j in i:
            xb += j
        if xb == 0:
            b += 1
    # 세로
    for i in range(5):
        yb = 0
        for j in range(5):
            yb += li[j][i]
        if yb == 0:
            b += 1
    # 대각선
    c_x = 0
    c_y = 0
    for i in range(5):
        c_x += li[i][i]
        c_y += li[i][-i-1]      # 인덱스 -순회로 뒤부터
    if c_x == 0: b += 1
    if c_y == 0: b += 1
    
    return b
    
# 철수꺼 사회자꺼 비교
def check_bingo(li1, li2):
    cnt = 0                     # 정답용 카운트
    for i in range(5):
        for j in range(5):
            cnt += 1
            for k in range(5):
                for l in range(5):
                    if li2[i][j] == li1[k][l]:  # 사회자꺼가 철수꺼에 있으면 0으로 바꿈
                        li1[k][l] = 0
            clear = check(li1)                  # 0으로 바꾸고 빙고가 몇개 있는지 확인
            if clear >= 3:
                
                return cnt

# input
bingo = [list(map(int, input().split())) for _ in range(5)] # 철수
bingo_x = [list(map(int, input().split())) for _ in range(5)] # 사회자
print(check_bingo(bingo, bingo_x))



                

