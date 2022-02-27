T = input()

a = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

total = 0
for i in range(len(a)): # 0
    for j in T: # W, A
        if j in a[i]:
            total += i + 3
print(total)


