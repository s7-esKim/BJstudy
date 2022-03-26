import sys

for tc in range(1, int(sys.stdin.readline().rstrip()) + 1):
    N = int(input())
    num_lst = []

    for i in range(N):
        num_lst.append((sys.stdin.readline().rstrip()))
    
    def check():
        for i in range(N - 1):
            if num_lst[i] == num_lst[i+1][:len(num_lst[i])]:
                print('NO')
                return
        else:
            print('YES')
            return

    num_lst.sort()
    check()

