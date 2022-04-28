N = int(input())	
arr = [0]

for _ in range(N):
    arr.append(int(input()))
ans = set()			


def dfs(li1, li2, num):
    li1.add(num)			
    li2.add(arr[num])		

    if arr[num] in li1:		
        if li1 == li2:	
            ans.update(li1)	
            return
    return dfs(li1, li2, arr[num])

for i in range(1, N+1):
    if i not in ans:
        dfs(set(), set(), i)

print(len(ans))

ans = list(ans)
ans.sort()

for i in ans:
    print(i)