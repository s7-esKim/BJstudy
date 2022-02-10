x = input().lower()
cnt = 0
for i in x:
    if i == 'a' or i == 'b' or i == 'c':
        cnt += 3
    elif i == 'd' or i == 'e' or i == 'f':
        cnt += 4
    elif i == 'g' or i == 'h' or i == 'i':
        cnt += 5
    elif i == i == 'j' or i == 'k' or i =='l':
        cnt += 6
    elif i == i =='m' or i =='n' or i =='o':
        cnt += 7
    elif i == 'p' or i =='q' or i =='r' or i =='s':
        cnt += 8
    elif i == 't' or i =='u' or i =='v':
        cnt += 9
    elif i == 'w' or i =='x' or i =='y' or i =='z':
        cnt += 10
    else:
        cnt += 0
print(cnt)