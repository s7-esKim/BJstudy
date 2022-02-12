N = int(input())  # 번호판의 수
for nc in range(1, N+1):
    car = input()  # 자동차 번호판
    alphabet, number = car.split('-')  # 글자와 숫자 나누기

    count = 0  # 첫 번째 부분의 가치
    # 26**2 부터 값이 들어간다!
    # i = 0, 1, 2 / (2-i) = 2, 1, 0
    for i in range(3):
        count += (ord(alphabet[i]) - 65) * (26 ** (2-i))

    number_count = int(number)

    if abs(count - number_count) <= 100:
        print('nice')
    else:
        print('not nice')