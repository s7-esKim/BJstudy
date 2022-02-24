S = int(input())
switch = list(map(int, input().split()))
students = int(input())

def female(num, swc): # 1
    if swc[num-1] == 1:
        swc[num-1] = 0
    else:
        swc[num-1] = 1

    for i in range(1, S + 1):
        if num - 1 - i < 0 or num -1 + i > S - 1:
            break
        if swc[num-1-i] + swc[num-1+i] == 2:
            swc[num-1-i] = swc[num-1+i] = 0
        elif swc[num-1-i] + swc[num-1+i] == 0:
            swc[num-1-i] = swc[num-1+i] = 1

        if swc[num-1-i] + swc[num-1+i] == 1 or num - 1 - i == 0 or num - 1 + i == S - 1:
            break
    return swc

for i in range(students):
    student, number = map(int, input().split())
    if student == 1:                                
        for i in range(1, S + 1):
            if i % number == 0:
                if switch[i-1] == 0:
                    switch[i-1] = 1
                else:
                    switch[i-1] = 0
    else: 
        switch = female(number, switch)

for b in range(1,S+1):
    print(switch[b-1],end=' ')
    if b%20==0:
        print()


