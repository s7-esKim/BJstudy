def result():
    for i in range(len(phone_num)-1):
        if phone_num[i] == phone_num[i+1][0:len(phone_num[i])]:
            print('NO')
            return
    print('YES')

T = int(input())
for tc in range(T):
    N = int(input())
    phone_num = []
    for _ in range(N):
        phone_num.append(input())
    phone_num.sort()
    result()
