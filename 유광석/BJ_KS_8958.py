N = int(input())

for i in range(N):
    list = input()
    total = 0
    count = 0
    for j in range(len(list)):
        if list[j] == 'O':
            count = count + 1      
            total = count + total 
        else:
            count = 0
    print(total)            
