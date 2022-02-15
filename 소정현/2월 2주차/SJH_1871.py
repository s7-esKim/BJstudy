n = int(input())

for i in range(n):
    car_number = input().split('-')
    first_number = 0
    k = 2
    for j in car_number[0]:
        number = ord(j)-ord('A')
        first_number += number * (26**k)
        k -= 1
    if abs(first_number-int(car_number[1]))>100:
        print("not nice")
    else:
        print("nice")