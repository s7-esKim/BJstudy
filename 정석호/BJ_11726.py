n = int(input())
lst = [0] * (n+1)

# n이 3일 때까지의 값
if n == 1:
    print('1')
elif n == 2:
    print('2')
elif n == 3:
    print('3')

# n이 4이상일 때의 값
else:
    lst[1] = 1
    lst[2] = 2
    lst[3] = 3
    for i in range(4, n+1):
        lst[i] = lst[i-1] + lst[i-2]
    print(lst[n] % 10007)   # n의 값에 10007을 나눈 나머지를 출력한다.