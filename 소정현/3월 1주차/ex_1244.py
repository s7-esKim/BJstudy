n = int(input())

switch = list(map(int, input().split()))
# switch = list(map(int, input()))

student = int(input())

def change_switch(x):
    if x == 0:
        x = 1
    elif x == 1:
        x = 0
    return x

def man_switch(number, switch):
    for i in range(1, len(switch)+1):
        if i % number == 0:
            switch[i-1] = change_switch(switch[i-1])
    return switch

def woman_switch(number, switch):
    i = 0
    number = number-1
    while True:
        if i == 0:
            switch[number] = change_switch(switch[number])
        else:
            if switch[(number-i)] == switch[(number+i)]:
                switch[number-i] = change_switch(switch[number-i])
                switch[number+i] = change_switch(switch[number+i])
            else:
                break
        i += 1

        if (number-i) < 0 or (number+i) >= len(switch):
            break
        
    return switch



for i in range(student):
    sex, num = map(int, input().split())
    if sex == 1:
        switch = man_switch(num, switch)
    elif sex == 2:
        switch = woman_switch(num, switch)


if n <= 20:
    result = " ".join(list(map(str, switch)))
    print(result)
else:
    i = 0
    while True:
        if  n >= i + 20:
            result = " ".join(list(map(str, switch[i:i+20])))
            print(result)
            if i + 20 == n:
                break
        else:
            result = " ".join(list(map(str, switch[i:])))
            print(result)
            break
        i += 20
