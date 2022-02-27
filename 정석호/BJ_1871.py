N = int(input())

for i in range(N):
    alphabet, number = input().split('-')
    num = int(number)

    apl_total = 0
    alphabet = alphabet[::-1]
    for apl in range(len(alphabet)):
        apl_total += (ord(alphabet[apl])-65)*26**apl
    
    nice_value = apl_total - num
    if abs(nice_value) <= 100:
        print('nice')
    else:
        print('not nice')
