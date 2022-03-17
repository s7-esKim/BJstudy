def f(i,n):
    if i == n:
        print(bit, end =' ')
        for j in range(n):
            if bit[j]:
                print(a[j], end = '')
        print()
    else:
        bit[i] = 1
        f(i+1, n)
        bit[i] = 0
        f(i+1, n)
    return

a = [1,2,3]
bit = [0,0,0]
f(0, 3)