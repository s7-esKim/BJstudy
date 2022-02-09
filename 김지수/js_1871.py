# # 좋은 자동차 번호판

N = int(input())

for i in range(N):
    abc_part, num_part = input().split('-')
    cba_part = abc_part[::-1]
    num_part_value = int(num_part)
    cba_part_value = 0
    for i in range(len(cba_part)):
       cba_part_value += (ord(cba_part[i]) - 65) * (26**i) 
    if abs(cba_part_value - num_part_value) <= 100:
        print('nice')
    else:
        print('not nice')
        
# 2
# ABC-0123
# AAA-9999
