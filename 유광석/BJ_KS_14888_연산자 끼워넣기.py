def calc(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    else:
        if n1 >= 0 and n2 >= 0:
            return n1 // n2
        elif n1 < 0 or n2 < 0:
            return -(abs(n1)//abs(n2))
        else:
            return n1 // n2
    
# def nCr(n, r, s):
#     if r == 0:
#         print(a)
#     else:
#         for i in range(s, n-r+1):
#             a[r-1] = opr[i]
#             nCr(n, r-1, i+1)

def nPr(n, k):
    global min_num, max_num

    if n == k:

        ssum = nums[0]
        for i in range(1, len(nums)):
            ssum = calc(ssum, nums[i], a[i-1])
            # print(ssum, nums[i], a[i-1])
        if ssum < min_num:
            min_num = ssum
        if ssum > max_num:
            max_num = ssum
            print(a)

    else:
        for i in range(k):
            if used[i] == 0:
                used[i] = 1
                a[n] = opr[i]
                nPr(n+1, k)
                used[i] = 0

T = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))
max_num = -1000000000
min_num = 1000000000

opr = ['+' for _ in range(op[0])] + ['-' for _ in range(op[1])] + ['*' for _ in range(op[2])] + ['/' for _ in range(op[3])]
a = [0] * len(opr)
used = [0] * len(opr)
nPr(0, len(opr))

print(max_num)
print(min_num)
