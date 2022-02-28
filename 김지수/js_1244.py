import sys
sys.stdin = open('1.txt')
n = int(input())
switch = ['x'] + list(map(int, input().split())) + ['x']
student_cnt = int(input())

for _ in range(student_cnt):
    genre, card = map(int, input().split())
    if genre == 1: # 남자 조건 수행
        for i in range(1, len(switch)-1):
            if i % card == 0:
                if switch[i] == 0:
                    switch[i] = 1
                else:
                    switch[i] = 0
    elif genre == 2:
        cnt = 0
        for i in range(1, card+1):
            if i == card:
                if switch[i] == 0:
                    switch[i] = 1
                else:
                    switch[i] = 0
                    while True:
                        if switch[i - 1 - cnt] == switch[i + 1 + cnt]:
                            try:
                                if switch[i - 1 - cnt] == 0:
                                    switch[i - 1 - cnt] = 1
                                    switch[i + 1 + cnt] = 1
                                else:
                                    switch[i + 1 + cnt] = 0
                                    switch[i - 1 + cnt] = 0
                                cnt += 1
                            except IndexError:
                                pass
                        else:
                            break

switch.pop()
for i in range(1, n + 1):
    print(switch[i], end=' ')
    if i % 20 == 0:
        print()




    # elif genre == 2:
    #     cnt = 0
    #     for i in range(1, len(switch)-1):
    #         if i == card:
    #             if switch[i] == 0:
    #                 switch[i] = 1
    #             else:
    #                 switch[i] = 0
    #             while True:
    #                 if switch[i - 1 - cnt] == switch[i + 1 + cnt]:
    #                     try:
    #                         if switch[i - 1 - cnt] == 0:
    #                             switch[i - 1 - cnt] = 1
    #                             switch[i + 1 + cnt] = 1
    #                         else:
    #                             switch[i + 1 + cnt] = 0
    #                             switch[i - 1 + cnt] = 0
    #                         cnt += 1
    #                     except IndexError:
    #                         pass
    #                 else:
    #                     break
switch.pop()
for i in range(1, n+1):
    print(switch[i], end = ' ')
    if i % 20 == 0:
        print()