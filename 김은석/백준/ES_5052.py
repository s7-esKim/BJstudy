T = int(input())

for tc in range(1,T+1):
    N = int(input())
    phone = []

    for i in range(N):
        phone.append(input())

    phone.sort(key=str)

    flag = True

    for i in range(len(phone) - 1):
        if phone[i] == phone[i+1][:len(phone[i])]:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")
