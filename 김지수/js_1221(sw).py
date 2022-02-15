import sys
sys. stdin = open('GNS_test_input.txt')

T = int(input())
for tc in range(1,T+1):
    num_dict = {'ZRO': 0, 'ONE':0, 'TWO': 0, 'THR':0, 'FOR':0, 'FIV':0, 'SIX':0, 'SVN':0, 'EGT':0, 'NIN':0}
    N = input().split()
    arr = list(input().split())

    for i in arr:
        num_dict[i] += 1

    result = []
    for key, value in num_dict.items():
        for j in range(value):
            result.append(key)
    last = ' '.join(result)

    print(f'#{tc} {last}')

