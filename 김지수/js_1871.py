# # 좋은 자동차 번호판

N = int(input())

# 번호판 수 만큼 순회
for i in range(N):
    # 글자 부분, 숫자부분 -를 중심으로 나누기 = 'ABC' '0123'
    abc_part, num_part = input().split('-')
    # 글자 부분을 reverse
    cba_part = abc_part[::-1]
    # 숫자 부분 정수변환
    num_part_value = int(num_part)
    # reverse된 글자의 value를 0으로 지정 -> 26진수 쓸꺼라서
    cba_part_value = 0
    # 글자의 길이만큼 순회
    for i in range(len(cba_part)):
        # 0에다가 26진수 변환한거 더하기
        # reverse한 이유 : abc=28 : (0×26**2 + 1×26**1 + 2×26**0)
        # ord('a') = 65 , ord('b') = 66, ord('c') = 67
        # i가 0부터 1만큼 증가하니까 계산하기 편함
        cba_part_value += (ord(cba_part[i]) - 65) * (26**i)
    # abs = 절대값
    if abs(cba_part_value - num_part_value) <= 100:
        print('nice')
    else:
        print('not nice')
        
# 2
# ABC-0123
# AAA-9999
