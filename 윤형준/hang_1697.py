from collections import deque
def bfs(n):
    global result, flag
    queue.append(n)
    while queue:
        for i in range(len(queue)):
            a = queue.popleft()
            if arr[a] == arr[K]:
                result = 0
                flag = 0
                break
            left = a-1
            right = a+1
            jump = a*2
            if 0<=left<=100000:
                if arr[left]==0:
                    arr[left] = arr[a]+1
                    queue.append(left)
                elif arr[left]==-1:
                    result = arr[a]+1
                    flag = 0
                    break

            if 0<=right<=100000:
                if arr[right]==0:
                    arr[right] = arr[a]+1
                    queue.append(right)
                elif arr[right]==-1:
                    result = arr[a]+1
                    flag = 0
                    break
            if 0<=jump<=100000:
                if arr[jump]==0:
                    arr[jump] = arr[a]+1
                    queue.append(jump)
                elif arr[jump]==-1:
                    result = arr[a]+1
                    flag = 0
                    break
        if flag == 0:
            break
    return result
result = 0
flag = 1
N, K = map(int, input().split()) # 수빈이, 동생 위치
queue = deque()
arr = [0] * 100001
arr[N] = 0 # 수빈이
arr[K] = -1 # 동생
print(bfs(N))