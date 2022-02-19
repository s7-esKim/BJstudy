import sys
sys.stdin = open('GNS_test_input.txt')

T = int(input())
for tc in range(1, T+1):
    test = input().split()
    test_num = test[0]  # 테스트 케이스의 번호
    N = int(test[1])  # 테스트 케이스의 길이
    arr = list(input().split())  # 어느 행성의 숫자들

    # 숫자들의 개수를 셀 dictionary
    my_dic = {'ZRO':  0, 'ONE': 0, 'TWO': 0, 'THR': 0, 'FOR': 0, 'FIV': 0, 'SIX': 0, 'SVN': 0, 'EGT': 0, 'NIN': 0}

    # 숫자와 my_dic 의 key 값이 같다면 value 에 1씩 추가
    for i in arr:
        my_dic[i] += 1

    # ZRO 부터 value 값 만큼 list 에 추가
    my_list = []
    for key, values in my_dic.items():
        for j in range(values):
            my_list.append(key)

    print(f'{test_num}')
    print(' '.join(my_list))