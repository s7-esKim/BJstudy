import sys
sys.setrecursionlimit(10**9)

num = []
while True:
    try:
        num.append(int(input()))
    except:
        break


def postorder(s, e):
    if s > e:
        return
    else:
        mid = e + 1
        for i in range(s+1, e+1):
            if num[s] < num[i]:
                mid = i
                break
        postorder(s+1, mid-1)
        postorder(mid, e)
        print(num[s])


postorder(0, len(num) - 1)