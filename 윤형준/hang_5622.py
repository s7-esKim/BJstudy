word = input()

lst = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
cnt = 0
for i in word:
    for j in range(len(lst)):
        if i in lst[j]:
            cnt += j+3

print(cnt)