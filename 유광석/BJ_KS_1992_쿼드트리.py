N = int(input())
arr = [list(input()) for _ in range(N)]
ans = ''
def recur(r, c, n):
    global ans
    
    color = arr[r][c]

    for i in range(r, r+n):
        for j in range(c, c+n):
            if arr[i][j] != color:
                ans += '('
                recur(r, c, n//2)
                recur(r, c+n//2, n//2)
                recur(r+n//2, c, n//2)
                recur(r+n//2, c+n//2, n//2)
                ans += ')'
                return
    ans += color
recur(0, 0, N)
print(ans)

'''
8
11110000
11110000
00011100
00011100
11110000
11110000
11110011
11110011
'''