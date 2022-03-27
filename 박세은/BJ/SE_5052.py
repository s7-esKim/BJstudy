import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N = int(input())
    phone = list(input().strip() for _ in range(N))
    phone.sort()

    for i in range(N-1):
        if phone[i] == phone[i+1][:len(phone[i])]:
            print('NO')
            break
    else:
        print('YES')
