word = input().lower()
dial = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
second = 0
for i in word:
    cnt = 3
    for j in dial:
        if i in j:
            second += cnt
            break
        else:
            cnt += 1

print(second)