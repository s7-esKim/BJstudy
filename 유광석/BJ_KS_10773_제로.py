T = int(input())
lst = []
for tc in range(T):
    N = int(input())
    if N:
        lst.append(N)
    else:
        lst.pop()

print(sum(lst))