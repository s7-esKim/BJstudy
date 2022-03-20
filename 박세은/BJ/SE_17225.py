# pypy 만 통과

# A : 상민포장시간, B : 지수포장시간, N : 손님수
A, B, N = map(int, input().split())
a = []
b = []
a_end, b_end = 0, 0

# T : 주문시각, C : 포장지색깔, M : 선물개수
for i in range(N):
    T, C, M = map(str, input().split())
    T = int(T)
    M = int(M)

    if C == 'B':
        T = max(T, a_end)
        for j in range(M):
            a.append(T)
            T += A
            a_end = T

    elif C == 'R':
        T = max(T, b_end)
        for j in range(M):
            b.append(T)
            T += B
            b_end = T

answer1 = []
answer2 = []
total = sorted(a + b)
for i in range(len(total)):
    if total[i] in a:
        answer1.append(i + 1)
        a.pop(0)
    else:
        answer2.append(i + 1)
print(len(answer1))
print(*answer1)
print(len(answer2))
print(*answer2)
