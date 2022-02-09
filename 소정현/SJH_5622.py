alphabet = input()

sec = 0

for i in alphabet:
    if i == 'Z':
        result = ord('Z') - ord('Q')
        sec += (result//3 + 7)
    elif ord(i) >= ord('S'):
        result = ord(i) - ord('Q')
        sec += (result//3 + 8)
    else:
        result = ord(i) - ord('A')
        sec += (result//3 + 3)

print(sec)
