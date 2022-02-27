import sys
sys.stdin = open('input.txt')


def dice(arr, a):
    for i in range(6):
        # 아래 주사위와 같은 값 찾기
        if arr[i] == a:
            # index 값이 0 이면 arr[1] 이 다음 주사위와 같은 값
            # 옆면중에 가장 큰 값과 다음 값을 return
            if i == 0:
                return max(arr[2:]), arr[1]
            elif i == 1:
                return max(arr[2:]), arr[0]
            elif i == 2:
                return max(arr[0], arr[1], arr[4], arr[5]), arr[3]
            elif i == 3:
                return max(arr[0], arr[1], arr[4], arr[5]), arr[2]
            elif i == 4:
                return max(arr[:4]), arr[5]
            elif i == 5:
                return max(arr[:4]), arr[4]


# N : 주사위 개수
N = int(input())
# A:0, B:1, C;:2, D:3, E:4, F:5 -> A/F: 0/5, B/D: 1/3, C/E: 2/4
dice_list = []
for i in range(N):
    i = list(map(int, input().split()))
    # 마주보는 값끼리 정렬
    dice_list.append([i[0], i[5], i[1], i[3], i[2], i[4]])

my_max = 0
for i in range(1, 7):
    # 처음에 1부터 6까지 돌아보기!
    next = i
    ans = 0
    # 주사위의 개수 만큼 반복
    for j in range(N):
        num, next = dice(dice_list[j], next)
        ans += num
    if my_max < ans:
        my_max = ans
print(my_max)
