A = input()
# dial list
second = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
answer = 0
for i in A:  # A
    for j in second:  # j = 'ABC', 'DEF', ..., 'WXYZ'
        if i in j:  # A in 'ABC'
            answer += second.index(j) + 3  # 'ABC' -> second[0] : 3초
print(answer)
