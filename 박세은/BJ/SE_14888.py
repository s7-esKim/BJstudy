def result(count, total):
    global max_answer, min_answer
    if count == N:
        max_answer = max(max_answer, total)
        min_answer = min(min_answer, total)
        return
    if operator[0]:
        operator[0] -= 1
        result(count+1, total + arr[count])
        operator[0] += 1
    if operator[1]:
        operator[1] -= 1
        result(count+1, total - arr[count])
        operator[1] += 1
    if operator[2]:
        operator[2] -= 1
        result(count+1, total * arr[count])
        operator[2] += 1
    if operator[3]:
        operator[3] -= 1
        result(count+1, total // arr[count] if total >= 0 else -(-total // arr[count]))
        operator[3] += 1


N = int(input())
arr = list(map(int, input().split()))
operator = list(map(int, input().split()))

max_answer = -1000000000
min_answer = 1000000000
result(1, arr[0])
print(max_answer)
print(min_answer)
