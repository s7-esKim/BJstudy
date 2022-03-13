string1 = list(input())
net = int(input())
str_len = len(string1)
string2 = []

for i in range(net):
    com = input().split()
    if com[0] == 'P':
        string1.append(com[1])
    elif com[0] == 'L' and string1 != []:
        string2.append(string1.pop())
    elif com[0] == 'D' and string2 != []:
        string1.append(string2.pop())
    elif com[0] == 'B' and string1 != []:
        string1.pop()

print(''.join(string1 + list(reversed(string2))))